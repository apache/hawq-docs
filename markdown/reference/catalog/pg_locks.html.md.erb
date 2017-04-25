---
title: pg_locks
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

The `pg_locks` view provides access to information about the locks held by open transactions within HAWQ.

`pg_locks` contains one row per active lockable object, requested lock mode, and relevant transaction. Thus, the same lockable object may appear many times, if multiple transactions are holding or waiting for locks on it. However, an object that currently has no locks on it will not appear at all.

There are several distinct types of lockable objects: whole relations (such as tables), individual pages of relations, individual tuples of relations, transaction IDs, and general database objects. Also, the right to extend a relation is represented as a separate lockable object.

<a id="topic1__gv141982"></a>
<span class="tablecap">Table 1. pg\_catalog.pg\_locks</span>

| column           | type     | references       | description                                                                                                                                                                                           |
|------------------|----------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `locktype`       | text     |                  | Type of the lockable object: `relation`, `extend`, `page`, `tuple`, `transactionid`, `object`, `userlock`, `resource queue`, or `advisory`                                                            |
| `database`       | oid      | pg\_database.oid | OID of the database in which the object exists, zero if the object is a shared object, or NULL if the object is a transaction ID                                                                      |
| `relation`       | oid      | pg\_class.oid    | OID of the relation, or NULL if the object is not a relation or part of a relation                                                                                                                    |
| `page `          | integer  |                  | Page number within the relation, or NULL if the object is not a tuple or relation page                                                                                                                |
| `tuple `         | smallint |                  | Tuple number within the page, or NULL if the object is not a tuple                                                                                                                                    |
| `transactionid ` | xid      |                  | ID of a transaction, or NULL if the object is not a transaction ID                                                                                                                                    |
| `classid`        | oid      | pg\_class.oid    | OID of the system catalog containing the object, or NULL if the object is not a general database object                                                                                               |
| `objid `         | oid      | any OID column   | OID of the object within its system catalog, or NULL if the object is not a general database object                                                                                                   |
| `objsubid `      | smallint |                  | For a table column, this is the column number (the `classid` and `objid` refer to the table itself). For all other object types, this column is zero. NULL if the object is not a general database object |
| `transaction`    | xid      |                  | ID of the transaction that is holding or awaiting this lock                                                                                                                                           |
| `pid`            | integer  |                  | Process ID of the server process holding or awaiting this lock. NULL if the lock is held by a prepared transaction                                                                                    |
| `mode`           | text     |                  | Name of the lock mode held or desired by this process                                                                                                                                                 |
| `granted`        | boolean  |                  | True if lock is held, false if lock is awaited.                                                                                                                                                       |
| `mppsessionid`   | integer  |                  | The id of the client session associated with this lock.                                                                                                                                               |
| `mppiswriter`    | boolean  |                  | Specifies whether the lock is held by a writer process.                                                                                                                                               |
| `gp_segment_id`  | integer  |                  | The HAWQ segment id (`dbid`) where the lock is held.                                                                                                                                                  |




