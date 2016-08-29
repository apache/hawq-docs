#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

__all__ = ["copy_tarballs_to_hdfs", ]
import os
import glob
import re
import tempfile
from resource_management.libraries.functions.default import default
from resource_management.libraries.functions.format import format
from resource_management.libraries.resources.copy_from_local import CopyFromLocal
from resource_management.libraries.resources.execute_hadoop import ExecuteHadoop
from resource_management.core.resources.system import Execute
from resource_management.core.exceptions import Fail
from resource_management.core.logger import Logger
from resource_management.core import shell

"""
This file provides helper methods needed for the versioning of RPMs. Specifically, it does dynamic variable
interpretation to replace strings like {{ hdp_stack_version }}  where the value of the
variables cannot be determined ahead of time, but rather, depends on what files are found.

It assumes that {{ hdp_stack_version }} is constructed as ${major.minor.patch.rev}-${build_number}
E.g., 998.2.2.1.0-998
Please note that "-${build_number}" is optional.
"""

# These values must be the suffix of the properties in cluster-env.xml
TAR_SOURCE_SUFFIX = "_tar_source"
TAR_DESTINATION_FOLDER_SUFFIX = "_tar_destination_folder"


def _get_tar_source_and_dest_folder(tarball_prefix):
  """
  :param tarball_prefix: Prefix of the tarball must be one of tez, hive, mr, pig
  :return: Returns a tuple of (x, y) after verifying the properties
  """
  component_tar_source_file = default("/configurations/cluster-env/%s%s" % (tarball_prefix.lower(), TAR_SOURCE_SUFFIX), None)
  # E.g., /usr/hdp/current/hadoop-client/tez-{{ hdp_stack_version }}.tar.gz

  component_tar_destination_folder = default("/configurations/cluster-env/%s%s" % (tarball_prefix.lower(), TAR_DESTINATION_FOLDER_SUFFIX), None)
  # E.g., hdfs:///hdp/apps/{{ hdp_stack_version }}/mapreduce/

  if not component_tar_source_file or not component_tar_destination_folder:
    Logger.warning("Did not find %s tar source file and destination folder properties in cluster-env.xml" %
                   tarball_prefix)
    return None, None

  if component_tar_source_file.find("/") == -1:
    Logger.warning("The tar file path %s is not valid" % str(component_tar_source_file))
    return None, None

  if not component_tar_destination_folder.endswith("/"):
    component_tar_destination_folder = component_tar_destination_folder + "/"

  if not component_tar_destination_folder.startswith("hdfs://"):
    return None, None

  return component_tar_source_file, component_tar_destination_folder


def _copy_files(source_and_dest_pairs, file_owner, group_owner, kinit_if_needed):
  """
  :param source_and_dest_pairs: List of tuples (x, y), where x is the source file in the local file system,
  and y is the destination file path in HDFS
  :param file_owner: Owner to set for the file copied to HDFS (typically hdfs account)
  :param group_owner: Owning group to set for the file copied to HDFS (typically hadoop group)
  :param kinit_if_needed: kinit command if it is needed, otherwise an empty string
  :return: Returns 0 if at least one file was copied and no exceptions occurred, and 1 otherwise.

  Must kinit before calling this function.
  """
  import params

  return_value = 1
  if source_and_dest_pairs and len(source_and_dest_pairs) > 0:
    return_value = 0
    for (source, destination) in source_and_dest_pairs:
      try:
        destination_dir = os.path.dirname(destination)

        params.HdfsDirectory(destination_dir,
                             action="create",
                             owner=file_owner,
                             mode=0555
        )

        CopyFromLocal(source,
                      mode=0444,
                      owner=file_owner,
                      group=group_owner,
                      dest_dir=destination_dir,
                      kinnit_if_needed=kinit_if_needed,
                      hdfs_user=params.hdfs_user,
                      hadoop_bin_dir=params.hadoop_bin_dir,
                      hadoop_conf_dir=params.hadoop_conf_dir
        )
      except:
        return_value = 1
  return return_value


def copy_tarballs_to_hdfs(tarball_prefix, component_user, file_owner, group_owner):
  """
  :param tarball_prefix: Prefix of the tarball must be one of tez, hive, mr, pig
  :param component_user: User that will execute the Hadoop commands
  :param file_owner: Owner of the files copied to HDFS (typically hdfs account)
  :param group_owner: Group owner of the files copied to HDFS (typically hadoop group)
  :return: Returns 0 on success, 1 if no files were copied, and in some cases may raise an exception.

  In order to call this function, params.py must have all of the following,
  hdp_stack_version, kinit_path_local, security_enabled, hdfs_user, hdfs_principal_name, hdfs_user_keytab,
  hadoop_bin_dir, hadoop_conf_dir, and HdfsDirectory as a partial function.
  """
  import params

  if not hasattr(params, "hdp_stack_version") or params.hdp_stack_version is None:
    Logger.warning("Could not find hdp_stack_version")
    return 1

  component_tar_source_file, component_tar_destination_folder = _get_tar_source_and_dest_folder(tarball_prefix)
  if not component_tar_source_file or not component_tar_destination_folder:
    Logger.warning("Could not retrieve properties for tarball with prefix: %s" % str(tarball_prefix))
    return 1

  if not os.path.exists(component_tar_source_file):
    Logger.warning("Could not find file: %s" % str(component_tar_source_file))
    return 1

  # Ubuntu returns: "stdin: is not a tty", as subprocess output.
  tmpfile = tempfile.NamedTemporaryFile()
  with open(tmpfile.name, 'r+') as file:
    get_hdp_version_cmd = '/usr/bin/hdp-select versions > %s' % tmpfile.name
    code, stdoutdata = shell.call(get_hdp_version_cmd)
    out = file.read()
  pass
  if code != 0 or out is None:
    Logger.warning("Could not verify HDP version by calling '%s'. Return Code: %s, Output: %s." %
                   (get_hdp_version_cmd, str(code), str(out)))
    return 1

  hdp_version = out.strip() # this should include the build number

  file_name = os.path.basename(component_tar_source_file)
  destination_file = os.path.join(component_tar_destination_folder, file_name)
  destination_file = destination_file.replace("{{ hdp_stack_version }}", hdp_version)

  does_hdfs_file_exist_cmd = "fs -ls %s" % destination_file

  kinit_if_needed = ""
  if params.security_enabled:
    kinit_if_needed = format("{kinit_path_local} -kt {hdfs_user_keytab} {hdfs_principal_name};")

  if kinit_if_needed:
    Execute(kinit_if_needed,
            user=component_user,
            path='/bin'
    )

  does_hdfs_file_exist = False
  try:
    ExecuteHadoop(does_hdfs_file_exist_cmd,
                  user=component_user,
                  logoutput=True,
                  conf_dir=params.hadoop_conf_dir,
                  bin_dir=params.hadoop_bin_dir
    )
    does_hdfs_file_exist = True
  except Fail:
    pass

  if not does_hdfs_file_exist:
    source_and_dest_pairs = [(component_tar_source_file, destination_file), ]
    return _copy_files(source_and_dest_pairs, file_owner, group_owner, kinit_if_needed)
  return 1
