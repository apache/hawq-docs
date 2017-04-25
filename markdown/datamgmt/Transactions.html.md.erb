---
title: Working with Transactions
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

This topic describes transaction support in HAWQ.

Transactions allow you to bundle multiple SQL statements in one all-or-nothing operation.

The following are the HAWQ SQL transaction commands:

-   `BEGIN` or `START TRANSACTION `starts a transaction block.
-   `END` or `COMMIT` commits the results of a transaction.
-   `ROLLBACK` abandons a transaction without making any changes.
-   `SAVEPOINT` marks a place in a transaction and enables partial rollback. You can roll back commands executed after a savepoint while maintaining commands executed before the savepoint.
-   `ROLLBACK TO SAVEPOINT `rolls back a transaction to a savepoint.
-   `RELEASE SAVEPOINT `destroys a savepoint within a transaction.

## <a id="topic8"></a>Transaction Isolation Levels

HAWQ accepts the standard SQL transaction levels as follows:

-   *read uncommitted* and *read committed* behave like the standard *read committed*
-   serializable and repeatable read behave like the standard serializable

The following information describes the behavior of the HAWQ transaction levels:

-   **read committed/read uncommitted** — Provides fast, simple, partial transaction isolation. With read committed and read uncommitted transaction isolation, `SELECT` transactions operate on a snapshot of the database taken when the query started.

A `SELECT` query:

-   Sees data committed before the query starts.
-   Sees updates executed within the transaction.
-   Does not see uncommitted data outside the transaction.
-   Can possibly see changes that concurrent transactions made if the concurrent transaction is committed after the initial read in its own transaction.

Successive `SELECT` queries in the same transaction can see different data if other concurrent transactions commit changes before the queries start.

Read committed or read uncommitted transaction isolation may be inadequate for applications that perform complex queries and require a consistent view of the database.

-   **serializable/repeatable read** — Provides strict transaction isolation in which transactions execute as if they run one after another rather than concurrently. Applications on the serializable or repeatable read level must be designed to retry transactions in case of serialization failures.

A `SELECT` query:

-   Sees a snapshot of the data as of the start of the transaction (not as of the start of the current query within the transaction).
-   Sees only data committed before the query starts.
-   Sees updates executed within the transaction.
-   Does not see uncommitted data outside the transaction.
-   Does not see changes that concurrent transactions made.

    Successive `SELECT` commands within a single transaction always see the same data.

The default transaction isolation level in HAWQ is *read committed*. To change the isolation level for a transaction, declare the isolation level when you `BEGIN` the transaction or use the `SET TRANSACTION` command after the transaction starts.


