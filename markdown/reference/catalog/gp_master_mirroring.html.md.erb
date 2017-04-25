---
title: gp_master_mirroring
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

The `gp_master_mirroring` table contains state information about the standby master host and its associated write-ahead log (WAL) replication process. If this synchronization process (`gpsyncagent`) fails on the standby master, it may not always be noticeable to users of the system. This catalog is a place where HAWQ administrators can check to see if the standby master is current and fully synchronized.

<a id="topic1__op164584"></a>
<span class="tablecap">Table 1. pg\_catalog.gp\_master\_mirroring</span>

| column          | type                     | references | description                                                                                                                                                                                                                                                                                                   |
|-----------------|--------------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `summary_state` | text                     |            | The current state of the log replication process between the master and standby master - logs are either ‘Synchronized’ or ‘Not Synchronized’                                                                                                                                                                 |
| `detail_state`  | text                     |            | If not synchronized, this column will have information about the cause of the error.                                                                                                                                                                                                                          |
| `log_time`      | timestamp with time zone |            | This contains the timestamp of the last time a master mirroring change occurred. For example, the timestamp when the value of `summary_state` changed from "Synchronized" to "Not Synchronized". If no changes occur with regards to the standby master (it stays synchronized), the timestamp is not updated. |
| `error_message` | text                     |            | If not synchronized, this column will have the error message from the failed synchronization attempt.                                                                                                                                                                                                         |




