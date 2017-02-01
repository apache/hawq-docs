---
title: Concurrency Control
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

This topic discusses the mechanisms used in HAWQ to provide concurrency control.

HAWQ and PostgreSQL do not use locks for concurrency control. They maintain data consistency using a multiversion model, Multiversion Concurrency Control (MVCC). MVCC achieves transaction isolation for each database session, and each query transaction sees a snapshot of data. This ensures the transaction sees consistent data that is not affected by other concurrent transactions.

Because MVCC does not use explicit locks for concurrency control, lock contention is minimized and HAWQ maintains reasonable performance in multiuser environments. Locks acquired for querying (reading) data do not conflict with locks acquired for writing data.

HAWQ provides multiple lock modes to control concurrent access to data in tables. Most HAWQ SQL commands automatically acquire the appropriate locks to ensure that referenced tables are not dropped or modified in incompatible ways while a command executes. For applications that cannot adapt easily to MVCC behavior, you can use the `LOCK` command to acquire explicit locks. However, proper use of MVCC generally provides better performance.

<caption><span class="tablecap">Table 1. Lock Modes in HAWQ</span></caption>

<a id="topic_f5l_qnh_kr__ix140861"></a>

| Lock Mode              | Associated SQL Commands                                                             | Conflicts With                                                                                                          |
|------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| ACCESS SHARE           | `SELECT`                                                                            | ACCESS EXCLUSIVE                                                                                                        |
| ROW EXCLUSIVE          | `INSERT`, `COPY`                                                                    | SHARE, SHARE ROW EXCLUSIVE, EXCLUSIVE, ACCESS EXCLUSIVE                                                                 |
| SHARE UPDATE EXCLUSIVE | `VACUUM` (without `FULL`), `ANALYZE`                                                | SHARE UPDATE EXCLUSIVE, SHARE, SHARE ROW EXCLUSIVE, EXCLUSIVE, ACCESS EXCLUSIVE                                         |
| SHARE                  | `CREATE INDEX`                                                                      | ROW EXCLUSIVE, SHARE UPDATE EXCLUSIVE, SHARE ROW EXCLUSIVE, EXCLUSIVE, ACCESS EXCLUSIVE                                 |
| SHARE ROW EXCLUSIVE    |                                                                                     | ROW EXCLUSIVE, SHARE UPDATE EXCLUSIVE, SHARE, SHARE ROW EXCLUSIVE, EXCLUSIVE, ACCESS EXCLUSIVE                          |
| ACCESS EXCLUSIVE       | `ALTER TABLE`, `DROP TABLE`, `TRUNCATE`, `REINDEX`, `CLUSTER`, `VACUUM FULL`        | ACCESS SHARE, ROW SHARE, ROW EXCLUSIVE, SHARE UPDATE EXCLUSIVE, SHARE, SHARE ROW EXCLUSIVE, EXCLUSIVE, ACCESS EXCLUSIVE |
