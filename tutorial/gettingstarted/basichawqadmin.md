---
title: HAWQ Administration Basics
---

You can manage your HAWQ cluster from either the command line or the Ambari web console.

In this tutorial section, you will be introduced to basic HAWQ and database administration tasks.  You will manage aspects of your HAWQ cluster from both the command line and Ambari.

## <a id="tut_adminprereq"></a> Prerequisites
You must have a running HAWQ installation.

## <a id="tut_adminsetupenv"></a> HAWQ Environment

The `/usr/local/hawq/greenplum_path.sh` script sets up access to the HAWQ components on your system.  This script sets your `$PATH` and other environment variables to find HAWQ files.  Most importantly, it sets the `$GPHOME` environment variable to point to the root of the HAWQ installation.  The HAWQ root directory is `/usr/local/hawq` in the sandbox VM.

Source `greenplum_path.sh` before invoking any HAWQ commands.

``` shell
$ . /usr/local/hawq/greenplum_path.sh
```

Add the command above to your `.bash_profile` to set up your HAWQ environment on every log in.

## <a id="tut_adminsetupenv"></a> HAWQ Administrator

`gpadmin` is the HAWQ administrator user name.  The `gpadmin` user has super-user capabilities on all HAWQ databases and HAWQ cluster management commands.
  
## <a id="tut_adminclustermgmt"></a>HAWQ Management - Command Line

The following table identifies a subset of HAWQ management commands that are applicable to the tutorial exercises.  For detailed information on HAWQ management commands, refer to the [HAWQ Management Tools Reference](../../reference/cli/management_tools.html).

<caption><span class="tablecap">Table 1. Common HAWQ Management Commands</span></caption>

<a id="topic_table_clustmgmtcmd"></a>

| Action                                                    | Command                                                                                                                                                                                            |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| get HAWQ cluster status | `$ hawq state` |
| start/stop/restart HAWQ object (cluster, master, segment, standby, allsegments) | `$ hawq start object` <p> `$ hawq stop object` <p> `$ hawq restart object` |
| list HAWQ configuration parameters and values               | `$ hawq config --list`                                                                                         |
| change value of HAWQ configuration parameter   | `$ hawq config -c parameter_name -v new_value`                                                                                         |
| reload HAWQ configuration files               | `$ hawq stop --reload`                                                                                         |
| restart PXF service               | `$ sudo service pxf-service restart`                                                                                         |
| extract/dump database             | `$ pg_dump -f output_file dbname`                                                                                         |

### <a id="tut_adminclustermgmthstate"></a>HAWQ State 

Use the `hawq state` command to obtain the state of your HAWQ cluster:

``` shell
$ hawq state
DATETIME hawq_state:sandbox:gpadmin-[INFO]:--HAWQ instance status summary
DATETIME hawq_state:sandbox:gpadmin-[INFO]:------------------------------------------------------
DATETIME hawq_state:sandbox:gpadmin-[INFO]:--   Master instance                                = Active
DATETIME hawq_state:sandbox:gpadmin-[INFO]:--   No Standby master defined                           
DATETIME hawq_state:sandbox:gpadmin-[INFO]:--   Total segment instance count from config file  = 1
DATETIME hawq_state:sandbox:gpadmin-[INFO]:------------------------------------------------------ 
DATETIME hawq_state:sandbox:gpadmin-[INFO]:--   Segment Status                                    
DATETIME hawq_state:sandbox:gpadmin-[INFO]:------------------------------------------------------ 
DATETIME hawq_state:sandbox:gpadmin-[INFO]:--   Total segments count from catalog      = 1
DATETIME hawq_state:sandbox:gpadmin-[INFO]:--   Total segment valid (at master)        = 1
DATETIME hawq_state:sandbox:gpadmin-[INFO]:--   Total segment failures (at master)     = 0
DATETIME hawq_state:sandbox:gpadmin-[INFO]:--   Total number of postmaster.pid files missing   = 0
DATETIME hawq_state:sandbox:gpadmin-[INFO]:--   Total number of postmaster.pid files found     = 1
```

State information returned includes the status of the master node, standby master, number of segment instances, and for each segment, number valid and failed.

### <a id="tut_adminclustermgmthcfgparam"></a>HAWQ Configuration Parameters

HAWQ configuration parameters affect the behaviour of the HAWQ system.  The collection of HAWQ configuration parameters and values are stored in the `$GPHOME/etc/hawq-site.xml` file.  Use the `hawq config` command to view and set the values of HAWQ configuration parameters from the command line.

Display the value of the segment temporary directory:

``` shell
$ hawq config --show hawq_segment_temp_directory
GUC	   : hawq_segment_temp_directory
Value  : /tmp/hawq/segment
```

Set the PL/Java classpath configuration parameter value:

``` shell
$ hawq config -c pljava_classpath -v \'examples.jar\'
GUC pljava_classpath does not exist in hawq-site.xml
Try to add it with value: examples.jar
GUC	    : pljava_classpath
Value   : examples.jar
```

As the message indicates, `pljava_classpath` was not previously set.

HAWQ configuration must be reloaded after setting a configuration parameter. 

``` shell
$ hawq stop --reload
```

`hawq config` will propagate the configuration parameter value changes across the cluster.  Never modify the `hawq-site.xml` file directly.


## <a id="tut_adminclustermgmt"></a>HAWQ Management - Ambari Web UI

You can also use the Ambari Web UI to manage your HAWQ deployment.

?? CHANGE RUNTIME CONFIG PARAM AND STOP --reload AND DISCUSS ??

1. Start the Ambari web UI by entering the the IP address of your sandbox VM followed by `:8080` in the URL of a browser window.  If you do not remember, view the `/etc/hosts` file to get your VM IP address: 

    ``` shell
    vm_ipaddr:8080
    ```
    
    Ambari runs on port 8080.

2. Log in to Ambari; Ambari user credentials in the sandbox VM are `admin`/`admin`.

    After logging in, you are presented with the Ambari dashboard. The dashboard provides an at-a-glance status of the health of your HAWQ cluster. A list of running services and their status is displayed in the left panel. The main display area includes a set of configurable tiles providing specific information about your cluster, including HDFS disk usage and resource manager metrics.

3. Select the *HAWQ* service from the service list.

    The HAWQ service page *Summary* tab is displayed.  This page includes a *Summary* pane identifying the HAWQ master and all HAWQ segment nodes in your cluster. The *Metrics* pane includes a set of HAWQ-specific metrics tiles.
    
4. View HAWQ-specific configuration settings by selecting the *Configs* tab.

    HAWQ general settings displayed include master and segment data and temp directories, and specific resource management parameters.
    
5. Select the *Advanced* tab to view additional HAWQ parameter settings.

    The *General* drop down pane is opened. In addition to displaying master and segment port information, this pane is where the HAWQ administrator would (re)set the `gpadmin` password.
    
    *Advanced* and *Custom* drop down panes provide access to advanced configuration settings for HAWQ, HDFS, and YARN components.
    
6.  Select the *Advanced hawq-site* drop down.

   Specific configuration parameters and values are displayed in the pane.  Hover the mouse cursor over the value field to display a tooltip description of a specific configuration parameter.


## <a id="tut_admindbaccess"></a>HAWQ Database

The HAWQ PostgreSQL database XXXX

??DESCRIBE HOW IT DOES/DOES NOT CONFORM TO STANDARD??

?? DESCRIBE HAWQ DATABASES/TABLES CREATED AT INSTALL TIME ??

### <a id="tut_admindbaccesscmds"></a>Database Commands

HAWQ databases and roles can be created and deleted by authorized users via the command line.

<caption><span class="tablecap">Table 2. Common HAWQ Database Commands</span></caption>

<a id="topic_table_dbcmd"></a>

| Action                                                    | Command                                                                                                                                                                                            |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| create database | `createdb` |
| created database role   | `createuser`                                                                                         |
| remove database    | `dropdb`                                                                                         |
| remove database role     | `dropuser`                                                                                         |
| interactive HAWQ database front-end     | `psql`                                                                                         |

### <a id="tut_admindbaccesspsql"></a>psql

You can also manage and access HAWQ databases via the `psql` utility, an interactive front-end to the HAWQ PostgreSQL database.  Commonly-used `psql` meta commands include:

| Action                                                    | Command                                                                                                                                                                                            |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| list databases | `\l` |
| list tables in current database   | `\dt`                                                                                         |
| get schema info for specific table   | `\d tablename`                                                                                         |
| read SQL script     | `\i scriptname`                                                                                         |
| quit    | `\q`                                                                                         |

For detailed information on `psql` commands, refer to the [psql](../../reference/cli/client_utilities/psql.html) reference page.

### <a id="tut_admindbsql"></a>SQL

For specific information on SQL command support in HAWQ databases, refer to the [SQL Command Reference](../../reference/SQLCommandReference.html).
