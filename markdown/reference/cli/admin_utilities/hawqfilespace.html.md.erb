---
title: hawq filespace
---

<!--
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
-->

Creates a filespace using a configuration file that defines a file system location. Filespaces describe the physical file system resources to be used by a tablespace.

## <a id="topic1__section2"></a>Synopsis

``` pre
hawq filespace [<connection_options>] 
  -o <output_directory_name> | --output <output_directory_name>
  [-l <logfile_directory> | --logdir <logfile_directory>] 

hawq filespace [<connection_options]  
  -c <fs_config_file> | --config <fs_config_file> 
  [-l <logfile_directory> | --logdir <logfile_directory>] 

hawq filespace [<connection_options>]
  --movefilespace <filespace> --location <dfslocation>
  [-l <logfile_directory> | --logdir <logfile_directory>] 

hawq filespace -v | --version 

hawq filespace -? | --help
```
where:

``` pre
<connection_options> =
  [-h <host> | --host <host>] 
  [-p <port> | -- port <port>] 
  [-U <username> | --username <username>] 
  [-W | --password] 
```

## <a id="topic1__section3"></a>Description

A tablespace requires a file system location to store its database files. This file system location for all components in a HAWQ system is referred to as a *filespace*. Once a filespace is defined, it can be used by one or more tablespaces.

The `--movefilespace` option allows you to relocate a filespace and its components within a dfs file system.

When used with the `-o` option, the `hawq filespace` utility looks up your system configuration information in the system catalog tables and prompts you for the appropriate file system location needed to create the filespace. It then outputs a configuration file that can be used to create a filespace. If a file name is not specified, a `hawqfilespace_config_`*\#* file will be created in the current directory by default.

Once you have a configuration file, you can run `hawq filespace` with the `-c` option to create the filespace in HAWQ system.

**Note:** If segments are down due to a power or nic failure, you may see inconsistencies during filespace creation. You may not be able to bring up the cluster.

## <a id="topic1__section4"></a>Options

<dt>-o, -\\\-output &lt;output\_directory\_name&gt;  </dt>
<dd>The directory location and file name to output the generated filespace configuration file. You will be prompted to enter a name for the filespace and file system location. The file system locations must exist on all hosts in your system prior to running the `hawq filespace` command. You will specify the number of replicas to create. The default is 3 replicas. After the utility creates the configuration file, you can manually edit the file to make any required changes to the filespace layout before creating the filespace in HAWQ.</dd>

<dt>-c, -\\\-config &lt;fs\_config\_file&gt;  </dt>
<dd>A configuration file containing:

-   An initial line denoting the new filespace name. For example:

    filespace:&lt;myfs&gt;
</dd>

<dt>-\\\-movefilespace &lt;filespace&gt;  </dt>
<dd>Create the filespace in a new location on a distributed file system. Updates the dfs url in the HAWQ database, so that data in the original location can be moved or deleted. Data in the original location is not affected by this command.</dd>

<dt>-\\\-location &lt;dfslocation&gt;  </dt>
<dd>Specifies the new URL location to which a dfs file system should be moved.</dd>

<dt>-l, -\\\-logdir &lt;logfile\_directory&gt;  </dt>
<dd>The directory to write the log file. Defaults to `~/hawqAdminLogs`.</dd>

<dt>-v, -\\\-version (show utility version)  </dt>
<dd>Displays the version of this utility.</dd>

<dt>-?, -\\\-help (help)  </dt>
<dd>Displays the command usage and syntax.</dd>

**&lt;connection_options&gt;**

<dt>-h, -\\\-host &lt;hostname&gt;  </dt>
<dd>The host name of the machine on which the HAWQ master database server is running. If not specified, reads from the environment variable `PGHOST` or defaults to localhost.</dd>

<dt>-p, -\\\-port &lt;port&gt;  </dt>
<dd>The TCP port on which the HAWQ master database server is listening for connections. If not specified, reads from the environment variable `PGPORT` or defaults to 5432.</dd>

<dt>-U, -\\\-username &lt;superuser\_name&gt;  </dt>
<dd>The database superuser role name to connect as. If not specified, reads from the environment variable `PGUSER` or defaults to the current system user name. Only database superusers are allowed to create filespaces.</dd>

<dt>-W, -\\\-password  </dt>
<dd>Force a password prompt.</dd>

## <a id="topic1__section6"></a>Example 1

Create a filespace configuration file. Depending on your system setup, you may need to specify the host and port. You will be prompted to enter a name for the filespace and a replica number. You will then be asked for the DFS location. The file system locations must exist on all hosts in your system prior to running the `hawq filespace` command:

``` shell
$ hawq filespace -o .
```

``` pre
Enter a name for this filespace
> fastdisk
Enter replica num for filespace. If 0, default replica num is used (default=3)
0
Please specify the DFS location for the filespace (for example: localhost:9000/fs)
location> localhost:9000/hawqfs

20160203:11:35:42:272716 hawqfilespace:localhost:gpadmin-[INFO]:-[created]
20160203:11:35:42:272716 hawqfilespace:localhost:gpadmin-[INFO]:-
To add this filespace to the database please run the command:
   hawqfilespace --config ./hawqfilespace_config_20160203_112711
Checking your configuration: 

Your system has 1 hosts with 2 primary segments 
per host.

Configuring hosts: [sdw1, sdw2] 

Enter a file system location for the master:
master location> /hawq_master_filespc
```

Example filespace configuration file:

``` pre
filespace:fastdisk
mdw:1:/hawq_master_filespc/gp-1
sdw1:2:/hawq_pri_filespc/gp0
sdw2:3:/hawq_pri_filespc/gp1
```

Execute the configuration file to create the filespace:

``` shell
$ hawq filespace --config hawq_filespace_config_1
```

## Example 2

Create the filespace at `cdbfast_fs_a` and move an hdfs filesystem to it:

``` shell
$ hawq filespace --movefilespace=cdbfast_fs_a
      --location=hdfs://gphd-cluster/cdbfast_fs_a/
```

## <a id="topic1__section7"></a>See Also

[CREATE TABLESPACE](../../sql/CREATE-TABLESPACE.html)
