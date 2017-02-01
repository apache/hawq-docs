---
title: Introducing the HAWQ Operating Environment
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

Before invoking operations on a HAWQ cluster, you must set up your HAWQ environment. This set up is required for both administrative and non-administrative HAWQ users.

## <a id="hawq_setupenv"></a>Procedure: Setting Up Your HAWQ Operating Environment

HAWQ installs a script that you can use to set up your HAWQ cluster environment. The `greenplum_path.sh` script, located in your HAWQ root install directory, sets `$PATH` and other environment variables to find HAWQ files.  Most importantly, `greenplum_path.sh` sets the `$GPHOME` environment variable to point to the root directory of the HAWQ installation.  If you installed HAWQ from a product distribution, the HAWQ root is typically `/usr/local/hawq`. If you built HAWQ from source or downloaded the tarball, you will have selected an install root directory on your own.

Perform the following steps to set up your HAWQ operating environment:

1. Log in to the HAWQ node as the desired user.  For example:

    ``` shell
    $ ssh gpadmin@<master>
    gpadmin@master$ 
    ```

    Or, if you are already logged in to \<node\-type\> as a different user, switch to the desired user. For example:
    
    ``` shell
    gpadmin@master$ su - <hawq-user>
    Password:
    hawq-user@master$ 
    ```

2. Set up your HAWQ operating environment by sourcing the `greenplum_path.sh` file. If you built HAWQ from source or downloaded the tarball, substitute the path to the installed or extracted `greenplum_path.sh` file \(for example `/opt/hawq-2.1.0.0/greenplum_path.sh`\):

    ``` shell
    hawq-node$ source /usr/local/hawq/greenplum_path.sh
    ```
    
    `source`ing `greenplum_path.sh` sets `PATH` to include the HAWQ `$GPHOME/bin/` directory. It also sets `LD_LIBRARY_PATH` to include the HAWQ libraries in `$GPHOME/lib/`.


3. Edit your `.bash_profile` or other shell initialization file to source `greenplum_path.sh` on login.  For example, add:

    ``` shell
    source /usr/local/hawq/greenplum_path.sh
    ```
    
4. Set HAWQ-specific environment variables relevant to your deployment in your shell initialization file. These include `PGAPPNAME`, `PGDATABASE`, `PGHOST`, `PGPORT`, and `PGUSER.` For example:

    1.  If you use a custom HAWQ master port number, make this port number the default by setting the `PGPORT` environment variable in your shell initialization file; add:

        ``` shell
        export PGPORT=10432
        ```
    
        Setting `PGPORT` simplifies `psql` invocation by providing a default for the `-p` (port) option.

    1.  If you will routinely operate on a specific database, make this database the default by setting the `PGDATABASE` environment variable in your shell initialization file:

        ``` shell
        export PGDATABASE=<database-name>
        ```
    
        Setting `PGDATABASE` simplifies `psql` invocation by providing a default for the `-d` (database) option.

    You may choose to set additional HAWQ deployment-specific environment variables. See [Environment Variables](../reference/HAWQEnvironmentVariables.html#optionalenvironmentvariables).

## <a id="hawq_env_files_and_dirs"></a>HAWQ Files and Directories

The following table identifies some files and directories of interest in a default HAWQ installation.  Unless otherwise specified, the table entries are relative to `$GPHOME`.

|File/Directory                   | Contents           |
|---------------------------------|---------------------|
| $HOME/hawqAdminLogs/            | Default HAWQ management utility log file directory |
| greenplum_path.sh      | HAWQ environment set-up script |
| bin/      | HAWQ admin, client, database, and administration utilities |
| etc/              | HAWQ configuration files, including `hawq-site.xml` |
| include/          | HDFS, PostgreSQL, `libpq` header files  |
| lib/              | HAWQ libraries |
| lib/postgresql/   | PostgreSQL shared libraries and JAR files |
| share/postgresql/ | PostgreSQL and procedural languages samples and scripts    |
| /data/hawq/[master&#124;segment]/ | Default location of HAWQ master and segment data directories |
| /data/hawq/[master&#124;segment]/pg_log/ | Default location of HAWQ master and segment log file directories |
| /etc/pxf/conf/               | PXF service and configuration files |
| /usr/lib/pxf/                | PXF service and plug-in shared libraries  |
| /var/log/pxf/                | PXF log file directory  |
| /usr/hdp/current/            | HDP runtime and configuration files |
