---
title: Client-Based HAWQ Load Tools
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
HAWQ supports data loading from Red Hat Enterprise Linux 5, 6, and 7 and Windows XP client systems. HAWQ Load Tools include both a loader program and a parallel file distribution program.

This topic presents the instructions to install the HAWQ Load Tools on your client machine. It also includes the information necessary to configure HAWQ databases to accept remote client connections.

## <a id="installloadrunrhel"></a>RHEL Load Tools

The RHEL Load Tools are provided in a HAWQ distribution. 


### <a id="installloadrunux"></a>Installing the RHEL Loader

1. Download a HAWQ installer package or build HAWQ from source.
 
2. Refer to the HAWQ command line install instructions to set up your package repositories and install the HAWQ binary.

3. Install the `libevent` and `libyaml` packages. These libraries are required by the HAWQ file server. You must have superuser privileges on the system.

    ``` shell
    $ sudo yum install -y libevent libyaml
    ```

### <a id="installrhelloadabout"></a>About the RHEL Loader Installation

The files/directories of interest in a HAWQ RHEL Load Tools installation include:

`bin/` — data loading command-line tools ([gpfdist](../../reference/cli/admin_utilities/gpfdist.html) and [hawq load](../../reference/cli/admin_utilities/hawqload.html))   
`greenplum_path.sh` — environment set up file

### <a id="installloadrhelcfgenv"></a>Configuring the RHEL Load Environment

A `greenplum_path.sh` file is located in the HAWQ base install directory following installation. Source `greenplum_path.sh` before running the HAWQ RHEL Load Tools to set up your HAWQ environment:

``` shell
$ . /usr/local/hawq/greenplum_path.sh
```

Continue to [Using the HAWQ File Server (gpfdist)](g-using-the-hawq-file-server--gpfdist-.html) for specific information about using the HAWQ load tools.

## <a id="installloadrunwin"></a>Windows Load Tools

### <a id="installpythonwin"></a>Installing Python 2.5
The HAWQ Load Tools for Windows requires that the 32-bit version of Python 2.5 be installed on your system. 

**Note**: The 64-bit version of Python is **not** compatible with the HAWQ Load Tools for Windows.

1. Download the [Python 2.5 installer for Windows](https://www.python.org/downloads/).  Make note of the directory to which it was downloaded.

2. Double-click on the `python Load Tools for Windows-2.5.x.msi` package to launch the installer.
3. Select **Install for all users** and click **Next**.
4. The default Python install location is `C:\Pythonxx`. Click **Up** or **New** to choose another location. Click **Next**.
5. Click **Next** to install the selected Python components.
6. Click **Finish** to complete the Python installation.


### <a id="installloadrunwin"></a>Running the Windows Installer

1. Download the `greenplum-loaders-4.3.x.x-build-n-WinXP-x86_32.msi` installer package from [Pivotal Network](https://network.pivotal.io/products/pivotal-gpdb). Make note of the directory to which it was downloaded.
 
2. Double-click the `greenplum-loaders-4.3.x.x-build-n-WinXP-x86_32.msi` file to launch the installer.
3. Click **Next** on the **Welcome** screen.
4. Click **I Agree** on the **License Agreement** screen.
5. The default install location for HAWQ Loader Tools for Windows is `C:\"Program Files (x86)"\Greenplum\greenplum-loaders-4.3.8.1-build-1`. Click **Browse** to choose another location.
6. Click **Next**.
7. Click **Install** to begin the installation.
8. Click **Finish** to exit the installer.

    
### <a id="installloadabout"></a>About the Windows Loader Installation
Your HAWQ Windows Load Tools installation includes the following files and directories:

`bin/` — data loading command-line tools ([gpfdist](http://gpdb.docs.pivotal.io/4380/client_tool_guides/load/unix/gpfdist.html) and [gpload](http://gpdb.docs.pivotal.io/4380/client_tool_guides/load/unix/gpload.html))  
`lib/` — data loading library files  
`greenplum_loaders_path.bat` — environment set up file


### <a id="installloadcfgenv"></a>Configuring the Windows Load Environment

A `greenplum_loaders_path.bat` file is provided in your load tools base install directory following installation. This file sets the following environment variables:

- `GPHOME_LOADERS` - base directory of loader installation
- `PATH` - adds the loader and component program directories
- `PYTHONPATH` - adds component library directories

Execute `greenplum_loaders_path.bat` to set up your HAWQ environment before running the HAWQ Windows Load Tools.
 

## <a id="installloadenableclientconn"></a>Enabling Remote Client Connections
The HAWQ master database must be configured to accept remote client connections.  Specifically, you need to identify the client hosts and database users that will be connecting to the HAWQ database.

1. Ensure that the HAWQ database master `pg_hba.conf` file is correctly configured to allow connections from the desired users operating on the desired database from the desired hosts, using the authentication method you choose. For details, see [Configuring Client Access](../../clientaccess/client_auth.html#topic2).

    Make sure the authentication method you choose is supported by the client tool you are using.
    
2. If you edited the `pg_hba.conf` file, reload the server configuration. If you have any active database connections, you must include the `-M fast` option in the `hawq stop` command:

    ``` shell
    $ hawq stop cluster -u [-M fast]
    ```
   

3. Verify and/or configure the databases and roles you are using to connect, and that the roles have the correct privileges to the database objects.