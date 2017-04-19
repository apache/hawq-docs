---
title: Installing PXF Plug-ins
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

This topic describes how to install the built-in PXF service plug-ins that are required to connect PXF to HDFS, Hive, HBase, JDBC, and JSON. 

**Note:** PXF requires that you run Tomcat on the host machine. Tomcat reserves ports 8005, 8080, and 8009. If you have configured Oozie JXM reporting on a host that will run PXF, make sure that the reporting service uses a port other than 8005. This helps to prevent port conflict errors from occurring when you start the PXF service.

## <a id="directories_and_logs"></a>PXF Installation and Log File Directories

Installing PXF plug-ins, regardless of method, creates directories and log files on each node receiving the plug-in installation:

| Directory                      | Description                                                                                                                                                                                                                                |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `/usr/lib/pxf`                 | PXF library location                                                                                                                                                                                                                       |
| `/etc/pxf/conf`                | PXF configuration directory. This directory contains the `pxf-public.classpath` and `pxf-private.classpath` configuration files. See [Setting up the Java Classpath](ConfigurePXF.html#settingupthejavaclasspath). |
| `/var/pxf/pxf-service`         | PXF service instance location                                                                                                                                                                                                              |
| `/var/log/pxf` | This directory includes `pxf-service.log` and all Tomcat-related logs including `catalina.out`. Logs are owned by user:group `pxf`:`pxf`. Other users have read access.                                                                          |
| `/var/run/pxf/catalina.pid`    | PXF Tomcat container PID location                                                                                                                                                                                                          |


## <a id="install_pxf_plug_ambari"></a>Installing PXF Using Ambari

If you are using Ambari to install and manage your HAWQ cluster, you do *not* need to follow the manual installation steps in this topic. Installing using the Ambari web interface installs all of the necessary PXF plug-in components.

## <a id="install_pxf_plug_cmdline"></a>Installing PXF from the Command Line

Each PXF service plug-in resides in its own RPM.  You may have built these RPMs in the Apache HAWQ open source project repository (see [PXF Build Instructions](https://github.com/apache/incubator-hawq/blob/master/pxf/README.md)), or these RPMs may have been included in a commercial product download package.

Perform the following steps on **_each_** node in your cluster to install PXF:

1. Install the PXF software, including Apache, the PXF service, and all PXF plug-ins: HDFS, HBase, Hive, JDBC, JSON:

    ```shell
    $ sudo yum install -y pxf
    ```

    Installing PXF in this manner:
    * installs the required version of `apache-tomcat`
    * creates a `/etc/pxf/pxf-n.n.n` directory, adding a softlink from `/etc/pxf` to this directory
    * sets up the PXF service configuration files in `/etc/pxf`
    * creates a `/usr/lib/pxf-n.n.n` directory, adding a softlink from `/usr/lib/pxf` to this directory
    * copies the PXF service JAR file `pxf-service-n.n.n.jar` to `/usr/lib/pxf-n.n.n/`
    * copies JAR files for each of the PXF plugs-ins to `/usr/lib/pxf-n.n.n/`
    * creates softlinks from `pxf-xxx.jar` in `/usr/lib/pxf-n.n.n/`

2. Initialize the PXF service:

    ```shell
    $ sudo service pxf-service init
    ```

2. Start the PXF service:

    ```shell
    $ sudo service pxf-service start
    ```
    
    Additional `pxf-service` command options include `stop`, `restart`, and `status`.

2. If you choose to use the HBase plug-in, perform the following configuration:

    1. Add the PXF HBase plug-in JAR file to the HBase `CLASSPATH` by updating the `HBASE_CLASSPATH` environment variable setting in the HBase environment file `/etc/hbase/conf/hbase-env.sh`:

        ``` shell
        export HBASE_CLASSPATH=${HBASE_CLASSPATH}:/usr/lib/pxf/pxf-hbase.jar
        ```

    3. Restart the HBase service after making this update to HBase configuration.

        On the HBase Master node:

        ``` shell
        $ su -l hbase -c "/usr/hdp/current/hbase-master/bin/hbase-daemon.sh restart master; sleep 25"
       ```

        On an HBase Region Server node:

        ```shell
        $ su -l hbase -c "/usr/hdp/current/hbase-regionserver/bin/hbase-daemon.sh restart regionserver"
        ```
