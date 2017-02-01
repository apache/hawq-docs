---
title: Defining a Command-Based Writable External Web Table
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

You can define writable external web tables to send output rows to an application or script. The application must accept an input stream, reside in the same location on all of the HAWQ segment hosts, and be executable by the `gpadmin` user. All segments in the HAWQ system run the application or script, whether or not a segment has output rows to process.

Use `CREATE WRITABLE EXTERNAL WEB TABLE` to define the external table and specify the application or script to run on the segment hosts. Commands execute from within the database and cannot access environment variables (such as `$PATH`). Set environment variables in the `EXECUTE` clause of your writable external table definition. For example:

``` sql
=# CREATE WRITABLE EXTERNAL WEB TABLE output (output text) 
    EXECUTE 'export PATH=$PATH:/home/gpadmin/programs; myprogram.sh' 
    ON 6
    FORMAT 'TEXT'
    DISTRIBUTED RANDOMLY;
```

The following HAWQ variables are available for use in OS commands executed by a web or writable external table. Set these variables as environment variables in the shell that executes the command(s). They can be used to identify a set of requests made by an external table statement across the HAWQ array of hosts and segment instances.

<caption><span class="tablecap">Table 1. External Table EXECUTE Variables</span></caption>

<a id="topic71__du224024"></a>

| Variable            | Description                                                                                                                |
|---------------------|----------------------------------------------------------------------------------------------------------------------------|
| $GP\_CID            | Command count of the transaction executing the external table statement.                                                   |
| $GP\_DATABASE       | The database in which the external table definition resides.                                                               |
| $GP\_DATE           | The date on which the external table command ran.                                                                          |
| $GP\_MASTER\_HOST   | The host name of the HAWQ master host from which the external table statement was dispatched.                              |
| $GP\_MASTER\_PORT   | The port number of the HAWQ master instance from which the external table statement was dispatched.                        |
| $GP\_SEG\_DATADIR   | The location of the data directory of the segment instance executing the external table command.                           |
| $GP\_SEG\_PG\_CONF  | The location of the `hawq-site.xml` file of the segment instance executing the external table command.                     |
| $GP\_SEG\_PORT      | The port number of the segment instance executing the external table command.                                              |
| $GP\_SEGMENT\_COUNT | The total number of segment instances in the HAWQ system.                                                                  |
| $GP\_SEGMENT\_ID    | The ID number of the segment instance executing the external table command (same as `dbid` in `gp_segment_configuration`). |
| $GP\_SESSION\_ID    | The database session identifier number associated with the external table statement.                                       |
| $GP\_SN             | Serial number of the external table scan node in the query plan of the external table statement.                           |
| $GP\_TIME           | The time the external table command was executed.                                                                          |
| $GP\_USER           | The database user executing the external table statement.                                                                  |
| $GP\_XID            | The transaction ID of the external table statement.                                                                        |

-   **[Disabling EXECUTE for Web or Writable External Tables](../../datamgmt/load/g-disabling-execute-for-web-or-writable-external-tables.html)**


