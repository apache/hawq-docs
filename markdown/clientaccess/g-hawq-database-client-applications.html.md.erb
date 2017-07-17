---
title: HAWQ Client Applications
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

HAWQ is pre-installed with a number of client utility applications. You can also run client applications in your HAWQ deployment that were created using standard ODBC/JDBC Application Interfaces.

Alternatively, you may want to provide access to your HAWQ master node from a Linux client outside of your HAWQ cluster. One option to enable this access is to install the full HAWQ binary on the client node. A second option is to create a minimal `psql` client package from an existing HAWQ installation which you could then install on a non-HAWQ client. Refer to [HAWQ psql Client Package](#hawqclient_pkg) for instructions on creating, installing, and running such a package.

## <a id="hawqclient_installed"></a>HAWQ-Installed Client Applications

HAWQ is installed with a number of client utility applications. These applications are located in the `$GPHOME/bin` directory of your HAWQ master host installation. The following client utility applications are the most commonly used:

|Name|Usage|
|----|-----|
|`createdb`|create a new database|
|`createlang`|define a new procedural language|
|`createuser`|define a new database role|
|`dropdb`|remove a database|
|`droplang`|remove a procedural language|
|`dropuser`|remove a role|
|`psql`|PostgreSQL interactive terminal|
|`reindexdb`|reindex a database|
|`vacuumdb`|garbage-collect and analyze a database|

When using these client applications, you must connect to a database through the HAWQ master instance. You will need to know the name of your target database, the host name and port number of the master, and what database user name to connect as. This information can be provided on the command-line using the options `-d`, `-h`, `-p`, and `-U` respectively. If an argument is found that does not belong to any option, it will be interpreted as the database name first.

All of these options have default values which will be used if the option is not specified. The default host is the local host. The default port number is 5432. The default user name is your OS system user name, as is the default database name. Note that OS user names and HAWQ user names are not necessarily the same.

If the default values are not correct, you can set the environment variables `PGDATABASE`, `PGHOST`, `PGPORT`, and `PGUSER` to the appropriate values, or use a `psql``~/.pgpass` file to contain frequently-used passwords.

## <a id="hawqclient_pkg"></a>HAWQ psql Client Package

You may choose to provide `psql` access to your HAWQ master node from a non-HAWQ Linux client. This section describes the procedures for creating, installing, and running a minimal HAWQ `psql` client package.

### <a id="hawqpsqlclient_pkg_create"></a>Creating the HAWQ psql Client Package

Perform the following steps to create a HAWQ Linux `psql` client package:

1. Log in to a HAWQ node and set up your HAWQ environment:

    ``` shell
    $ ssh gpadmin@<hawq-node>
    gpadmin@hawq-node$ . /usr/local/hawq/greenplum_path.sh
    ```

    **Note**: You can create the client package on any node on which HAWQ is installed.

2. Create working directories:

    ``` shell
    gpadmin@hawq-node$ mkdir hawqclient
    gpadmin@hawq-node$ cd hawqclient
    gpadmin@hawq-node$ export HAWQCLIENTWORKDIR=`pwd`
    gpadmin@hawq-node$ mkdir bin
    gpadmin@hawq-node$ mkdir lib
    ```

3. Copy the HAWQ `psql` client binary and libraries to the appropriate work directories:

    ``` shell
    gpadmin@hawq-node$ cp $GPHOME/bin/psql $HAWQCLIENTWORKDIR/bin/
    gpadmin@hawq-node$ cp -d $GPHOME/lib/libpq.* $HAWQCLIENTWORKDIR/lib/
    ```

4. Generate a runtime environment file for the HAWQ client package:

    ``` shell
    gpadmin@hawq-node$ echo 'HAWQ_CLIENT=`pwd`
    export PATH=$HAWQ_CLIENT/bin:$PATH
    export LD_LIBRARY_PATH=$HAWQ_CLIENT/lib:$LD_LIBRARY_PATH' > ./hawq_client_env.sh
    ```

    The `hawq_client_env.sh` file sets `$PATH` and `$LD_LIBRARY_PATH` appropriately for a HAWQ client runtime environment.

5. Tar and compress the HAWQ client package:

    ``` shell
    gpadmin@hawq-node$ cd $HAWQCLIENTWORKDIR/../
    gpadmin@hawq-node$ tar czvf hawqclient.tar.gz ./hawqclient
    ```

    These commands create a `hawqclient.tar.gz` file in the current directory.

### <a id="hawqclient_pkg_install"></a>Installing the HAWQ psql Client Package

Perform the following procedure to install the HAWQ `psql` client package you created in the previous section on a like Linux-based system:

1. Log in to the client system and create or navigate to the directory in which you want to install the HAWQ client:

    ``` shell
    $ ssh <user>@<client>
    user@client$ cd <install-dir>
    user@client$ export HAWQCLIENTINSTDIR=`pwd`
    ```

    Make note of the base HAWQ client install directory, you will need this path to run the client.

2. Add the HAWQ client install directory setting to your `.bash_profile` or similar shell login script:

    ``` shell
    export HAWQCLIENTINSTDIR=<install-dir>
    ```
    
    Substitute the full path to your HAWQ client install directory for <install-dir>.

3. Copy the HAWQ client package you created previously to the client system:

    ``` shell
    user@client$ scp gpadmin@hawq-node:/<dir>/hawqclient.tar.gz .
    ```

4. Extract the package:

    ``` shell
    user@client$ tar xzf hawqclient.tar.gz
    ```

    This command extracts the HAWQ client to `./hawqclient`.

5. Clean up:

    ``` shell
    user@client$ rm hawqclient.tar.gz
    ```

### <a id="hawqclient_pkg_run"></a>Running the HAWQ psql Client

Perform the following procedure to run a previously-installed HAWQ `psql` client package.

**Note**: If you have enabled Kerberos user authentication for HAWQ, refer to [Kerberos Considerations for Non-HAWQ Clients](kerberos.html#client_considerations) for additional client configuration requirements.

1. Source the HAWQ client environment file (recall the HAWQ client install directory you noted in the previous section):

    ``` shell
    user@client$ . $HAWQCLIENTINSTDIR/hawqclient/hawq_client_env.sh
    ```

    `hawq_client_env.sh` sets up the HAWQ client runtime environment, including setting your `$PATH` and `$LD_LIBRARY_PATH` to locate the `psql` client binaries and libraries.

2. Edit your `.bash_profile` or other shell initialization file to source `hawq_client_env.sh` on login. For example, add:

    ``` shell
    . $HAWQCLIENTINSTDIR/hawqclient/hawq_client_env.sh
    ```

3. Start the `psql` client. Since the HAWQ master is running on another node, you must identify the HAWQ master hostname. You may also be required to provide the HAWQ master port number if the process is not running on the HAWQ default port. Provide these values via environment variables or on the command line:

    ``` shell
    user@client$ PGHOST=<master-host> PGPORT=<master-port> psql -d <database-name>
    ```

    Or:

    ``` shell
    user@client$ psql -d <database-name> -h <master-host> -p <master-port>
    ```
