---
title: HAWQ Administration Basics
---

Your HAWQ cluster can be managed from either the command line or the Ambari Web UI.

In this tutorial section, you will be introduced to basic HAWQ and database administration tasks.  You will manage aspects of your HAWQ cluster from both the command line and Ambari.

## <a id="tut_adminprereq"></a> Prerequisites
You must have a running HAWQ installation.

## <a id="tut_adminsetupenv"></a> HAWQ Environment

The `/usr/local/hawq/greenplum_path.sh` script sets up access to the HAWQ components on your system.  This script sets your `$PATH` and other environment variables to find HAWQ files.  Most importantly, it sets the `$GPHOME` environment variable to point to the root of the HAWQ installation.  The HAWQ root is `/usr/local/hawq` in the sandbox VM.

Source `greenplum_path.sh` before invoking any HAWQ commands.

``` shell
$ . /usr/local/hawq/greenplum_path.sh
```
  
## <a id="tut_adminclustermgmt"></a>HAWQ Management - Command Line

The following table identifies a subset of HAWQ management commands that are applicable to the tutorial exercises.  For detailed information on HAWQ management commands, refer to the [HAWQ Management Tools Reference](../../reference/cli/management_tools.html).

<caption><span class="tablecap">Table 1. Common HAWQ Management Commands</span></caption>

<a id="topic_table_clustmgmtcmd"></a>

| Action                                                    | Command                                                                                                                                                                                            |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| get HAWQ cluster status | `$ hawq state` |
| start/stop/restart HAWQ cluster | `$ hawq start cluster` <p> `$ hawq stop cluster` <p> `$ hawq restart cluster` |
| reload HAWQ configuration files               | `$ hawq stop --reload`                                                                                         |
| restart PXF service               | `$ sudo service pxf-service restart`                                                                                         |
| copy or run command on all hosts in cluster               | `$ hawq ssh ...` <p> `$ hawq scp ...`                                                                                        |
| ?? OTHERS ??              | ??                                                                                        |


To obtain the state of your HAWQ cluster:

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

## <a id="tut_adminclustermgmt"></a>HAWQ Management - Ambari Web UI

You can also use the Ambari Web UI to manage your HAWQ deployment.

?????

?? CHANGE RUNTIME CONFIG PARAM AND STOP --reload AND DISCUSS ??


## <a id="tut_admindbaccess"></a>HAWQ Database Access

?? DESCRIBE HAWQ DATABASES/TABLES CREATED AT INSTALL TIME ??


HAWQ databases and roles can be created and deleted via the command line.

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
| read SQL script     | `\i scriptname`                                                                                         |
| quit    | `\q`                                                                                         |

For detailed information on `psql` commands, refer to the [psql](../../reference/cli/client_utilities/psql.html) reference page.


