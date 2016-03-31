---
title: Routine System Maintenance Tasks
---

## Overview<a id="overview-topic"></a>

To keep a HAWQ system running efficiently, the database must be regularly cleared of expired data and the table statistics must be updated so that the query optimizer has accurate information.

HAWQ requires that certain tasks be performed regularly to achieve optimal performance. The tasks discussed here are required, but database administrators can automate them using standard UNIX tools such as `cron` scripts. An administrator sets up the appropriate scripts and checks that they execute successfully. See [Recommended Monitoring and Maintenance Tasks](RecommendedMonitoringTasks.html) for additional suggested maintenance activities you can implement to keep your HAWQ system running optimally.

## Database Server Log Files <a id="topic10"></a>

HAWQ log output tends to be voluminous, especially at higher debug levels, and you do not need to save it indefinitely. Administrators rotate the log files periodically so new log files are started and old ones are removed.

HAWQ has log file rotation enabled on the master and all segment instances. Daily log files are created in the `pg_log` subdirectory of the master and each segment data directory using the following naming convention: <code>hawq-<i>YYYY-MM-DD\_hhmmss</i>.csv</code>. Although log files are rolled over daily, they are not automatically truncated or deleted. Administrators need to implement scripts or programs to periodically clean up old log files in the `pg_log` directory of the master and of every segment instance.

For information about viewing the database server log files, see [Viewing the Database Server Log Files](monitor.html).

## Management Utility Log Files <a id="topic11"></a>

Log files for the HAWQ management utilities are written to `~/hawqAdminLogs` by default. The naming convention for management log files is:

<pre><code><i>script_name_date</i>.log
</code></pre>

The log entry format is:

<pre><code><i>timestamp:utility:host:user</i>:[INFO|WARN|FATAL]:<i>message</i>
</code></pre>

The log file for a particular utility execution is appended to its daily log file each time that utility is run.
