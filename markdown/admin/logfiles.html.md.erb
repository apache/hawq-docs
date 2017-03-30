---
title: HAWQ Administrative Log Files
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

Log files are files that include messages and other information about your HAWQ deployment, including the database and utilities. HAWQ administrative log files reside in pre-defined or configured locations on the local file system of the HAWQ node.  These log files are distinctly located, formatted, configured, and managed.

Every database instance in HAWQ \(master, standby, and segments\) runs a PostgreSQL database server with its own server log file. You generate log files when you invoke HAWQ management utilities directly, or indirectly via Ambari management operations. Additionally, other components in your HAWQ cluster (PXF, HDFS) generate log files of their own.

Configurable logging parameters may affect what, when, and where messages are logged. You configure HAWQ administrative logging options via HAWQ server configuration parameters or command line options.

Log files may be created and/or rotated at pre-defined or configured intervals.   Note that administrative log files are not automatically truncated or deleted. The administrator must implement and periodically run scripts to clean up these log files.

## <a id="topic28"></a>HAWQ Database Server Log Files


### <a id="logfile_locate_db"></a>Locating HAWQ Log Files 

Each HAWQ master, standby, and segment database instance has its own server log file. Daily log files are created in the `pg_log` subdirectory of the master and segment data directory on the respective HAWQ node. You can obtain the master data directory location from the `hawq_master_directory` property value set in the `$GPHOME/etc/`[`hawq-site.xml`](../reference/HAWQSampleSiteConfig.html) configuration file. Similarly, you can obtain the segment data directory location from the `hawq_segment_directory` property value from `hawq-site.xml`.

The naming convention for HAWQ database server log files is `hawq-<date>_<time>.[csv|log]`. For example, `hawq-2017-01-02_061611.csv` or `hawq-2017-01-03_001704.log`. The number and size of log files present for a given \<date\> is dependent upon the values of certain HAWQ server configuration parameters (discussed later in this document).

### <a id="logfile_format_db"></a>HAWQ Log Format

The HAWQ server log files are written in text or comma-separated values \(CSV\) format.

HAWQ log entries may include the following fields:

<table>
  <tr><th>#</th><th>Field Name</th><th>Data Type</th><th>Description</th></tr>
  <tr><td>1</td><td>event_time</td><td>timestamp with time zone</td><td>Th time that the log entry was written to the log</td></tr>
  <tr><td>2</td><td>user_name</td><td>varchar(100)</td><td>The database user name</td></tr>
  <tr><td>3</td><td>database_name</td><td>varchar(100)</td><td>The database name</td></tr>
  <tr><td>4</td><td>process_id</td><td>varchar(10)</td><td>The system process ID (prefixed with "p")</td></tr>
  <tr><td>5</td><td>thread_id</td><td>varchar(50)</td><td>The thread count (prefixed with "th-")</td></tr>
  <tr><td>6</td><td>remote_host</td><td>varchar(100)</td><td>The hostname/address of the client machine (if on master node). The hostname/address of the master (if on segment node).</td></tr>
  <tr><td>7</td><td>remote_port</td><td>varchar(10)</td><td>The segment or master port number</td></tr>
  <tr><td>8</td><td>session_start_time</td><td>timestamp with time zone</td><td>The time the session connection was opened</td></tr>
  <tr><td>9</td><td>transaction_id</td><td>int</td><td>The top-level transaction ID on the master; this ID is the parent of any subtransactions.</td></tr>
  <tr><td>10</td><td>gp_session_id</td><td>text</td><td>The session identifier number (prefixed with "con")</td></tr>
  <tr><td>11</td><td>gp_command_count</td><td>text</td><td>The command number within a session (prefixed with "cmd")</td></tr>
  <tr><td>12</td><td>gp_segment</td><td>text</td><td>The segment content identifier. The master always has a content ID of -1.</td></tr>
  <tr><td>13</td><td>slice_id</td><td>text</td><td>The slice ID (portion of the query plan being executed)</td></tr>
  <tr><td>14</td><td>distr_tranx_id</td><td>text</td><td>The distributed transaction identifier</td></tr>
  <tr><td>15</td><td>local_tranx_id</td><td>text</td><td>The local transaction identifier</td></tr>
  <tr><td>16</td><td>sub_tranx_id</td><td>text</td><td>The subtransaction identifier</td></tr>
  <tr><td>17</td><td>event_severity</td><td>varchar(10)</td><td>The event severity; values include: LOG, ERROR, FATAL, PANIC, DEBUG1, DEBUG2</td></tr>
  <tr><td>18</td><td>sql_state_code</td><td>varchar(10)</td><td>The SQL state code associated with the log message</td></tr>
  <tr><td>19</td><td>event_message</td><td>text</td><td>The log or error message text</td></tr>
  <tr><td>20</td><td>event_detail</td><td>text</td><td>The detail message text associated with an error or warning message</td></tr>
  <tr><td>21</td><td>event_hint</td><td>text</td><td>The hint message text associated with an error or warning message</td></tr>
  <tr><td>22</td><td>internal_query</td><td>text</td><td>The internally-generated query text</td></tr>
  <tr><td>23</td><td>internal_query_pos</td><td>int</td><td>The cursor index into the internally-generated query text</td></tr>
  <tr><td>24</td><td>event_context</td><td>text</td><td>The context in which this message is generated</td></tr>
  <tr><td>25</td><td>debug_query_string</td><td>text</td><td>User-supplied query string with full detail for debugging. This string can be modified for internal use.</td></tr>
  <tr><td>26</td><td>error_cursor_pos</td><td>int</td><td>The cursor index into the query string</td></tr>
  <tr><td>27</td><td>func_name</td><td>text</td><td>The function in which this message is generated</td></tr>
  <tr><td>28</td><td>file_name</td><td>text</td><td>The name of the source file in which the message originated</td></tr>
  <tr><td>29</td><td>file_line</td><td>int</td><td>The line number of the source file in which the message originated</td></tr>
  <tr><td>30</td><td>stack_trace</td><td>text</td><td>The stack trace text associated with this message</td></tr>
</table>

**Note**: Log entries may not include values for all log fields. For example, the `slice_id` field is populated only for log entries associated with a query worker process.

Example HAWQ server log file entries in a `.csv` file:

``` pre
2017-01-02 01:19:55.293050 PST,"gpadmin","testdb",p381034,th-1259067104,"[local]",,2017-01-02 01:19:21 PST,28083,con3595,cmd7,seg-1,,,x28083,sx1,"LOG","00000","ConnID 207. Acquired resource from resource manager, (256 MB, 0.062500 CORE) x 1.",,,,,,"INSERT INTO extblwstrings VALUES ('my string');",0,,"rmcomm_QD2RM.c",868,
2017-01-02 06:16:06.383827 PST,,,p360256,th-1259067104,,,,0,,,seg-10000,,,,,"LOG","00000","database system is shut down",,,,,,,0,,"xlog.c",7882,
```

Example HAWQ server log file entries in a `.log` file:

``` pre
2017-01-03 00:17:04.848268 PST|||706424|startup||:-LOG:  database system was shut down at 2017-01-03 00:16:58 PST
2017-01-03 00:17:04.988778 PST|gpadmin|template1|706437|cmd1|x31410|:-LOG:  statement: SELECT oid,rolname,rolsuper,rolresqueue FROM pg_authid
2017-01-03 00:17:04.990520 PST|||706432|master resource manager||:-LOG:  Resource manager successfully loaded role specifications.
```

### <a id="logfile_examine_db"></a>Examining HAWQ Log Files 

You will examine the HAWQ log files to obtain information about your HAWQ deployment, as well as diagnose problems.

Identify log entries of related transactions using the `transaction_id`. You can identify related log entries of a particular query by the query's session identifier \(`gp_session_id`\) and command identifier \(`gp_command_count`\).

Alternatively, you can use the [*hawq_toolkit*](../reference/toolkit/hawq_toolkit.html#topic16) administrative schema to query HAWQ log files when the [`gp_log_format`](../reference/guc/parameter_definitions.html#gp_log_format) server configuration parameter value specifies `csv` format log files.

For example, the following `hawq_toolkit` query displays the time and message for all `ERROR` logs related to the database named `testdb`:

``` sql
=# SELECT logtime, logmessage FROM hawq_toolkit.hawq_log_master_concise 
     WHERE logdatabase='testdb' AND logseverity='ERROR';
```

### <a id="topic30"></a>Searching HAWQ Log Files 

Use the [`gplogfilter`](../reference/cli/admin_utilities/gplogfilter.html) HAWQ utility to search through a HAWQ log file for entries matching specific criteria. By default, this utility searches through the HAWQ master log file in the default location.

For example, to display the entries logged to the master log file after 2:00pm on January 18, 2016:

``` shell
$ gplogfilter -b '2016-01-18 14:00'
```

Run `gplogfilter` using the [`hawq ssh`](../reference/cli/admin_utilities/hawqssh.html) utility to search through all segment log files simultaneously. For example, create a \<seg\_hosts\> file that includes all segment hosts of interest, then invoke `gplogfilter` to display the last three lines of each segment log file on each segment host. (Note: enter the commands after the `=>` prompt, do not include the `=>`.):

``` shell
$ hawq ssh -f <seg_hosts>
=> source /usr/local/hawq/greenplum_path.sh
=> gplogfilter -n 3 /data/hawq/segment/pg_log/hawq*.csv
```

### <a id="logging_config"></a>Configuring HAWQ Logging 

You can configure the logging characteristics of HAWQ server operations using HAWQ server configuration [Logging Parameters](../reference/guc/guc_category-list.html#topic29). These configuration parameters work in conjunction with each other to determine what information is logged to the HAWQ server log file, and when.

HAWQ server logging-related configuration parameters include:

| Server Configuration Parameter     | Description     |
|-----------------------------------|------------------------|
| [`client_min_messages`](../reference/guc/parameter_definitions.html#client_min_messages) | Identify log level for client messages |
| [`debug_pretty_print`](../reference/guc/parameter_definitions.html#debug_pretty_print) |  Indent/format debug output to make it more readable |
| [`gp_log_format`](../reference/guc/parameter_definitions.html#gp_log_format) | Identify format of server log files |
| [`gp_max_csv_line_length`](../reference/guc/parameter_definitions.html#gp_max_csv_line_length) |  Set the maximum line length of csv-formatted file |
| [`log_autostats`](../reference/guc/parameter_definitions.html#log_autostats) |  Log information about automatic statistics generation |
| [`log_connections`](../reference/guc/parameter_definitions.html#log_connections) |  Log each client connection |
| [`log_disconnections`](../reference/guc/parameter_definitions.html#log_disconnections) |  Log each client connection termination |
| [`log_dispatch_stats`](../reference/guc/parameter_definitions.html#log_dispatch_stats) |  Log information related to statement dispatch |
|  [`log_duration`](../reference/guc/parameter_definitions.html#log_duration) |  Log the duration of completed statements satisfying  `log_statement` |
| [`log_error_verbosity`](../reference/guc/parameter_definitions.html#log_error_verbosity) |  Govern how much detail is written to the log |
| [`log_hostname`](../reference/guc/parameter_definitions.html#log_hostname) |  Log the hostname of the connecting host |
| [`log_min_duration_statement`](../reference/guc/parameter_definitions.html#log_min_duration_statement) |  Configure runtime duration at which a statement should be logged |
| [`log_min_error_statement`](../reference/guc/parameter_definitions.html#log_min_error_statement) |  Write sql statement causing the error condition |
| [`log_min_messages`](../reference/guc/parameter_definitions.html#log_min_messages) |  Identify log level for writing to log file |
| [`log_statement`](../reference/guc/parameter_definitions.html#log_statement)| Control which SQL statements are logged |
| [`log_timezone`](../reference/guc/parameter_definitions.html#log_timezone)|  Set the timezone used in log file timestamps |


#### <a id="logging_config_query"></a>Configuring Log Rotation

When log file rotation is enabled, you can control the rotation options with these HAWQ server configuration parameters:

| Server Configuration Parameter     | Description     |
|-----------------------------------|------------------------|
| [`log_rotation_age`](../reference/guc/parameter_definitions.html#log_rotation_age) |  Configure the lifetime of log file |
| [`log_rotation_size`](../reference/guc/parameter_definitions.html#log_rotation_size) |  Configure the maximum size of log file |
| [`log_truncate_on_rotation`](../reference/guc/parameter_definitions.html#log_truncate_on_rotation) |  Identify whether to truncate or append to the log file |

#### <a id="logging_config_query"></a>Configuring Query Logging

HAWQ exposes a set of server configuration parameters dealing exclusively with GPORCA query executor and optimizer logging.  These include:

| Server Configuration Parameter     | Description     |
|-----------------------------------|------------------------|
|  [`debug_print_parse`](../reference/guc/parameter_definitions.html#debug_print_parse) |  Log the query parse tree |
|  [`debug_print_plan`](../reference/guc/parameter_definitions.html#debug_print_plan) |  Log the query plan |
|  [`debug_print_prelim_plan`](../reference/guc/parameter_definitions.html#debug_print_prelim_plan) |  Log the preliminary query plan |
|  [`debug_print_rewritten`](../reference/guc/parameter_definitions.html#debug_print_rewritten) |  Log the query rewriter output |
|  [`debug_print_slice_table`](../reference/guc/parameter_definitions.html#debug_print_slice_table) |  Log the query slice plan |
|  [`log_executor_stats`](../reference/guc/parameter_definitions.html#log_executor_stats) |  Log query executor performance statistics |
|  [`log_parser_stats`](../reference/guc/parameter_definitions.html#log_parser_stats) |  Log query parser performance statistics |
|  [`log_planner_status`](../reference/guc/parameter_definitions.html#log_planner_stats) |  Log the performance statistics of the legacy query optimizer (planner) |
|  [`log_statement_stats`](../reference/guc/parameter_definitions.html#log_statement_stats) |  Log the total performance statistics of the query parser, planner, and executor |

[Query Minidump Log Files](#query_log) identifies configuration options and additional information related to generating query optimizer minidump log files.

### <a id="logfile_manage_db"></a>Managing HAWQ Log Files 

HAWQ log output tends to be voluminous, especially at higher debug levels. You should not need to save this information indefinitely. HAWQ administrators typically configure HAWQ to rotate the log files periodically so new log files are created.

Daily log files are created in the `pg_log` subdirectory of the master and each segment data directory. Although log files are rolled over daily, they are not automatically truncated or deleted. Administrators must implement and run scripts to periodically clean up old log files in the `pg_log` directory of the master, standby, and every segment instance.


## <a id="mgmtutil_log"></a>Management Utility Log Files 
You invoke HAWQ management utilities both from the command line and when you perform cluster management activities using the Ambari user interface. Regardless of source, these utilities log information about command execution status and results. The messages are logged to both `stdout` and a log file.

Each management utility, when invoked, creates/manages a daily log file.  The logs for a particular execution of a utility are added or appended to its daily log file each time that utility is run that day.

**Note**: Some management utilities are aliases for invoking one or more other management utilities. For example, `hawq restart` invokes `hawq stop` and `hawq start`. Logs are written to the daily log files associated with the two invoked utilities.

### <a id="logfile_locate_mu"></a>Locating Management Utility Log Files

The default location of HAWQ management utility log files is `/home/gpadmin/hawqAdminLogs/`. You may choose to specify an alternate log file directory.

The naming convention for HAWQ management utility log files is  `<cmdname>_<date>.log`. For example, `hawq_state_20170102.log` or `hawq_start_20161228.log`.

### <a id="logfile_format_mu"></a>Management Utility Log Format

HAWQ management utility log files are written in text format.

Management utility commands' log entries are formed as follows:

&nbsp;&nbsp;&nbsp;&nbsp;`<date>:<time>:<pid> <cmdname>:<host>:<user>-[<loglevel>]:-<message>`

Log entry fields are described in the table below.

| Log Entry Field      | Description     |
|----------------------|------------------------|
| date | The date (month, day, year) the entry was logged |
| time | The time the entry was logged |
| pid | The process id associated with the command invocation |
| cmdname | The name of the HAWQ management utility command |
| host | The name of the host on which the command was executed |
| user | The name of the user invoking the command |
| loglevel | The log level, one of `DEBUG`, `INFO`, `WARN`, or `FATAL`. The default logging level will log `INFO` and more severe messages. |
| message | The log message |


Example management utility log entries:

&nbsp;&nbsp;&nbsp;&nbsp;`20170102:06:16:06:451225 hawq_stop:hmast1:gpadmin-[INFO]:-Master host=hmast1`

&nbsp;&nbsp;&nbsp;&nbsp;`20170102:06:16:15:451826 hawq_start:hmast1:gpadmin-[INFO]:-Start hawq with args: ['start', 'segment']`


**Note**: The log files for certain management utility commands, for example `hawq init`, diverge from these conventions.


### <a id="logfile_examine_mu"></a>Examining Management Utility Log Entries

You will examine the HAWQ management utility log files to get more detailed information about the execution of the command. Additionally, the most recent log file for a particular command provides date/time and status information about the last time you invoked the command.


### <a id="logging_config_mu"></a>Configuring Management Utility Logging

Most management utilities support options for verbose logging and identifying  alternate log file directories.

Management utility logging-related configuration command options include:

| Option         | Description     |
|----------------------|------------------------|
| -l  &#124;   &#45;&#45;logdir \<dir\>  | Use alternate log file directory \<dir\> for this command invocation. |
| -v  &#124;   &#45;&#45;verbose  | Include `DEBUG` log messages in output. The default logging level will log `INFO` and more severe messages. |

Invoke the management utility command with the `--help` option to determine support for changing the log directory and/or enabling verbose output.

### <a id="logfile_manage_mu"></a>Managing Management Utility Log Files

Although Management Utility log files are rolled over daily, they are not automatically truncated or deleted. Administrators should implement and run scripts or programs to periodically clean up old Management Utility log files.


## <a id="query_log"></a>Query Minidump Log Files 

You can configure the HAWQ GPORCA query optimizer to generate output minidump files describing the optimization context for a given query. (The information in a minidump file is not in a format that you can easily understand. Rather, you would generate and provide the minidump file to the HAWQ development team or support.)

GPORCA minidump files include the following query-related information:

- Catalog objects including data types, tables, operators, and statistics required by GPORCA.
- An internal representation (DXL) of the query.
- An internal representation (DXL) of the query plan produced by GPORCA.
- System configuration information passed to GPORCA, including server configuration parameters, cost and statistics configuration, and number of segments.
- A stack trace of errors generated while optimizing the query.

Query minidump files are generated in a `minidumps/` subdirectory in the HAWQ master data directory. The minidump file naming convention is `Minidump_<date>_<time>_<gp_session_id>_<gp_command_count>.mdp`, for example `Minidump_20170102_213701_904_12.mdp`.

Use the [optimizer_minidump](../reference/guc/parameter_definitions.html#optimizer_minidump) HAWQ server configuration parameter to configure minidump generation. The default setting generates minidump files only on error.


## <a id="logging_pxf"></a>PXF Log Files

PXF provides both service- and database-level logging. Refer to [PXF Logging](../pxf/TroubleshootingPXF.html#pxflogging) for specific PXF logging configuration and management information.

## <a id="logging_ambari"></a>Ambari Log Files

Ambari log files may be useful in helping diagnose general cluster problems. The Ambari server log files are located in the `/var/log/ambari-server/` directory. Ambari agent log files are located in `/var/log/ambari-agent/`. Refer to [Reviewing Ambari Log Files](https://docs.hortonworks.com/HDPDocuments/Ambari-2.2.1.1/bk_ambari_troubleshooting/content/_reviewing_ambari_log_files.html) for additional information.

## <a id="rangerlogs"></a> Ranger Log Files

The HAWQ Ranger Plug-in Service log files may be useful in helping diagnose Ranger connectivity and authorization problems. You will find these log files in the `$GPHOME/ranger/plugin-service/logs/` directory. In addition to HAWQ Ranger Plug-in service-related logs, this directory includes the `log4j` provider `audit.log` file. (Refer to [Auditing Authorization Events](../ranger/ranger-auditing.html) for information on configuring HAWQ Ranger audit logging.)

Ranger log files are located in the `/var/log/ranger/admin/` directory.


## <a id="logging_other"></a>Hadoop Log Files

Hadoop log files are managed by your Hadoop distribution. If you built Hadoop from source, your log file locations and configuration may be governed by the build and/or install options you specified during the build process.
