---
title: Lesson 1 - Runtime Environment
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

This section introduces you to the HAWQ runtime environment. You will examine your HAWQ installation, set up your HAWQ environment, and execute HAWQ management commands. If installed in your environment, you will also explore the Ambari management console.

## <a id="tut_runtime_usercred"></a>Prerequisites

- Install a HAWQ commercial product distribution or HAWQ sandbox virtual machine or docker environment, or build and install HAWQ from source. Ensure that your HAWQ installation is configured appropriately.

- Make note of the HAWQ master node hostname or IP address.

- The HAWQ administrative user is named `gpadmin`. This is the user account from which you will administer your HAWQ cluster. To perform the exercises in this tutorial, you must:

    - Obtain the `gpadmin` user credentials.

    - Ensure that your HAWQ runtime environment is configured such that the HAWQ admin user `gpadmin` can run commands to access the HDFS Hadoop system accounts (`hdfs`, `hadoop`) via `sudo` without having to provide a password.

    - Obtain the Ambari UI user name and password (optional, if Ambari is installed in your HAWQ deployment). The default Ambari user name and password are both `admin`.

## <a id="tut_runtime_setup"></a> Exercise: Set Up your HAWQ Runtime Environment

HAWQ installs a script that you can use to set up your HAWQ cluster environment. The `greenplum_path.sh` script, located in your HAWQ root install directory, sets `$PATH` and other environment variables to find HAWQ files.  Most importantly, `greenplum_path.sh` sets the `$GPHOME` environment variable to point to the root directory of the HAWQ installation.  If you installed HAWQ from a product distribution or are running a HAWQ sandbox environment, the HAWQ root is typically `/usr/local/hawq`. If you built HAWQ from source or downloaded the tarball, your `$GPHOME` may differ.

Perform the following steps to set up your HAWQ runtime environment:

4.	Log in to the HAWQ master node using the `gpadmin` user credentials; you may not need to provide a password:

    ``` shell
    $ ssh gpadmin@<master>
    Password:
    gpadmin@master$ 
    ```

5. Set up your HAWQ operating environment by sourcing the `greenplum_path.sh` file. If you built HAWQ from source or downloaded the tarball, substitute the path to the installed or extracted `greenplum_path.sh` file \(for example `/opt/hawq-2.1.0.0/greenplum_path.sh`\):

    ``` shell
    gpadmin@master$ source /usr/local/hawq/greenplum_path.sh
    ```
    
    `source`ing `greenplum_path.sh` sets:
    - `$GPHOME`
    - `$PATH` to include the HAWQ `$GPHOME/bin/` directory 
    - `$LD_LIBRARY_PATH` to include the HAWQ libraries in `$GPHOME/lib/`
    
    
    ``` shell
    gpadmin@master$ echo $GPHOME
    /usr/local/hawq/.
    gpadmin@master$ echo $PATH
    /usr/local/hawq/./bin:/usr/lib64/qt-3.3/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/gpadmin/bin
    gpadmin@master$ echo $LD_LIBRARY_PATH
    /usr/local/hawq/./lib
    ```
    
    **Note**: You must source `greenplum_path.sh` before invoking any HAWQ commands. 

3. Edit your (`gpadmin`) `.bash_profile` or other shell initialization file to source `greenplum_path.sh` on login.  For example, add:

    ``` shell
    source /usr/local/hawq/greenplum_path.sh
    ```
    
4. Set the HAWQ-specific environment variables relevant to your deployment in your shell initialization file. These include `PGDATABASE`, `PGHOST`, `PGOPTIONS`, `PGPORT`, and `PGUSER.` You may not need to set any of these environment variables. For example, if you use a custom HAWQ master port number, make this port number the default by setting the `PGPORT` environment variable in your shell initialization file; add:

    ``` shell
    export PGPORT=5432
    ```
    
    Setting `PGPORT` simplifies `psql` invocation by providing a default for the port option value.
    
    Similarly, setting `PGDATABASE` simplifies `psql` invocation by providing a default for the database option value.


6. Examine your HAWQ installation:

    ``` shell
    gpadmin@master$ ls $GPHOME
    bin  docs  etc  greenplum_path.sh  include  lib  sbin  share
    ```
    
    The HAWQ command line utilities are located in `$GPHOME/bin`. `$GPHOME/lib` includes HAWQ and PostgreSQL libraries.
  
6. View the current state of your HAWQ cluster, and if it is not already running, start the cluster. In practice, you will perform different procedures depending upon whether you manage your cluster from the command line or use Ambari. While you are introduced to both in this tutorial, lessons will focus on command line instructions, as not every HAWQ deployment will utilize Ambari.<p>

    *Command Line*:

    ``` shell
    gpadmin@master$ hawq state
    Failed to connect to database, this script can only be run when the database is up.
    ```
    
    If your cluster is not running, start it:
    
    ``` shell
    gpadmin@master$ hawq start cluster
    20170411:15:54:47:357122 hawq_start:master:gpadmin-[INFO]:-Prepare to do 'hawq start'
    20170411:15:54:47:357122 hawq_start:master:gpadmin-[INFO]:-You can find log in:
    20170411:15:54:47:357122 hawq_start:master:gpadmin-[INFO]:-/home/gpadmin/hawqAdminLogs/hawq_start_20170411.log
    20170411:15:54:47:357122 hawq_start:master:gpadmin-[INFO]:-GPHOME is set to:
    20170411:15:54:47:357122 hawq_start:master:gpadmin-[INFO]:-/usr/local/hawq/.
    20170411:15:54:47:357122 hawq_start:master:gpadmin-[INFO]:-Start hawq with args: ['start', 'cluster']
    20170411:15:54:47:357122 hawq_start:master:gpadmin-[INFO]:-Gathering information and validating the environment...
    20170411:15:54:47:357122 hawq_start:master:gpadmin-[INFO]:-No standby host configured
    20170411:15:54:47:357122 hawq_start:master:gpadmin-[INFO]:-Start all the nodes in hawq cluster
    20170411:15:54:47:357122 hawq_start:master:gpadmin-[INFO]:-Starting master node 'master'
    20170411:15:54:47:357122 hawq_start:master:gpadmin-[INFO]:-Start master service
    20170411:15:54:48:357122 hawq_start:master:gpadmin-[INFO]:-Master started successfully
    20170411:15:54:48:357122 hawq_start:master:gpadmin-[INFO]:-Start all the segments in hawq cluster
    20170411:15:54:48:357122 hawq_start:master:gpadmin-[INFO]:-Start segments in list: ['segment']
    20170411:15:54:48:357122 hawq_start:master:gpadmin-[INFO]:-Start segment service
    20170411:15:54:48:357122 hawq_start:master:gpadmin-[INFO]:-Total segment number is: 1
    .....
    20170411:15:54:53:357122 hawq_start:master:gpadmin-[INFO]:-1 of 1 segments start successfully
    20170411:15:54:53:357122 hawq_start:master:gpadmin-[INFO]:-Segments started successfully
    20170411:15:54:53:357122 hawq_start:master:gpadmin-[INFO]:-HAWQ cluster started successfully
    ```
    
    Get the status of your cluster:
    
    ``` shell
    gpadmin@master$ hawq state
    20170411:16:39:18:370305 hawq_state:master:gpadmin-[INFO]:-- HAWQ instance status summary
    20170411:16:39:18:370305 hawq_state:master:gpadmin-[INFO]:------------------------------------------------------
    20170411:16:39:18:370305 hawq_state:master:gpadmin-[INFO]:--   Master instance                                = Active
    20170411:16:39:18:370305 hawq_state:master:gpadmin-[INFO]:--   No Standby master defined                           
    20170411:16:39:18:370305 hawq_state:master:gpadmin-[INFO]:--   Total segment instance count from config file  = 1
    20170411:16:39:18:370305 hawq_state:master:gpadmin-[INFO]:------------------------------------------------------ 
    20170411:16:39:18:370305 hawq_state:master:gpadmin-[INFO]:--   Segment Status                                    
    20170411:16:39:18:370305 hawq_state:master:gpadmin-[INFO]:------------------------------------------------------ 
    20170411:16:39:18:370305 hawq_state:master:gpadmin-[INFO]:--   Total segments count from catalog      = 1
    20170411:16:39:18:370305 hawq_state:master:gpadmin-[INFO]:--   Total segment valid (at master)        = 1
    20170411:16:39:18:370305 hawq_state:master:gpadmin-[INFO]:--   Total segment failures (at master)     = 0
    20170411:16:39:18:370305 hawq_state:master:gpadmin-[INFO]:--   Total number of postmaster.pid files missing   = 0
    20170411:16:39:18:370305 hawq_state:master:gpadmin-[INFO]:--   Total number of postmaster.pid files found     = 1
    ```
    
    State information returned includes the status of the master node, standby master, number of segment instances, and for each segment, the number valid and failed.<p>

    *Ambari*:
    
    If your deployment includes an Ambari server, perform the following steps to start and view the current state of your HAWQ cluster. 
    
    1. Start the Ambari management console by entering the following URL in your favorite (supported) browser window:

        ``` shell
        <ambari-server-node>:8080
        ```

    2. Log in with the Ambari credentials (default `admin`:`admin`) and view the Ambari dashboard:

        ![Ambari Dashboard](imgs/ambariconsole.png)
 
        The Ambari dashboard provides an at-a-glance status of the health of your HAWQ cluster. A list of each running service and its status is provided in the left panel. The main display area includes a set of configurable tiles providing specific information about your cluster, including HAWQ segment status, HDFS disk usage, and resource manager metrics. 
        
    3. Navigate to the **HAWQ** service listed in the left pane. If the service is not running (i.e. no green checkmark to the left of the service name), start your HAWQ cluster by clicking the **HAWQ** service name, and then selecting the **Start** operation from the **Service Actions** menu button.

    4. Log out of the Ambari console by clicking the **admin** button and selecting the **Sign out** drop down menu item.

## <a id="tut_runtime_sumary"></a>Summary
Your HAWQ cluster is now running. For additional information:

- [HAWQ Files and Directories](../../admin/setuphawqopenv.html#hawq_env_files_and_dirs) identifies HAWQ files and directories and their install locations.
- [Environment Variables](../../reference/HAWQEnvironmentVariables.html#optionalenvironmentvariables) includes a complete list of HAWQ deployment-specific environment variables.
- [Running a HAWQ Cluster](../../admin/RunningHAWQ.html) provides an overview of the components comprising a HAWQ cluster, including the users (administrative and operating), deployment systems (HAWQ master, standby, and segments), databases, and data sources.

Lesson 2 introduces basic HAWQ cluster administration activities and commands.
 
**Lesson 2**: [Cluster Administration](basichawqadmin.html)
