---
title: Routine System Maintenance Tasks
---

To keep a HAWQ system running efficiently, the database must be regularly cleared of expired data and the table statistics must be updated so that the query optimizer has accurate information.

HAWQ requires that certain tasks be performed regularly to achieve optimal performance. The tasks discussed here are required, but database administrators can automate them using standard UNIX tools such as `cron` scripts. An administrator sets up the appropriate scripts and checks that they execute successfully. See [Recommended Monitoring and Maintenance Tasks](RecommendedMonitoringTasks.html) for additional suggested maintenance activities you can implement to keep your HAWQ system running optimally.

## Managing HAWQ Log Files <a name="topic9"></a>

-   [Database Server Log Files](#topic10)
-   [Management Utility Log Files](#topic11)

### Database Server Log Files <a name="topic10"></a>

HAWQ log output tends to be voluminous, especially at higher debug levels, and you do not need to save it indefinitely. Administrators rotate the log files periodically so new log files are started and old ones are removed.

HAWQ has log file rotation enabled on the master and all segment instances. Daily log files are created in the `pg_log` subdirectory of the master and each segment data directory using the following naming convention: `hawq-*YYYY*-*MM*-*DD\_hhmmss*.csv`. Although log files are rolled over daily, they are not automatically truncated or deleted. Administrators need to implement scripts or programs to periodically clean up old log files in the `pg_log` directory of the master and of every segment instance.

For information about viewing the database server log files, see [Viewing the Database Server Log Files](monitor.html).

### Management Utility Log Files <a name="topic11"></a>

Log files for the HAWQ management utilities are written to `~/hawqAdminLogs` by default. The naming convention for management log files is:

```
script_name_date.log
```

The log entry format is:

```
timestamp:utility:host:user:[INFO|WARN|FATAL]:message
```

The log file for a particular utility execution is appended to its daily log file each time that utility is run.
