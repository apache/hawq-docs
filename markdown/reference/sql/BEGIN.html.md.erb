---
title: BEGIN
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

Starts a transaction block.

## <a id="topic1__section2"></a>Synopsis

``` pre
BEGIN [WORK | TRANSACTION] [SERIALIZABLE | REPEATABLE READ | READ COMMITTED | READ UNCOMMITTED]
      [READ WRITE | READ ONLY]
```

## <a id="topic1__section3"></a>Description

`BEGIN` initiates a transaction block, that is, all statements after a `BEGIN` command will be executed in a single transaction until an explicit `COMMIT` or `ROLLBACK` is given. By default (without `BEGIN`), HAWQ executes transactions in autocommit mode, that is, each statement is executed in its own transaction and a commit is implicitly performed at the end of the statement (if execution was successful, otherwise a rollback is done).

Statements are executed more quickly in a transaction block, because transaction start/commit requires significant CPU and disk activity. Execution of multiple statements inside a transaction is also useful to ensure consistency when making several related changes: other sessions will be unable to see the intermediate states wherein not all the related updates have been done.

## <a id="topic1__section4"></a>Parameters

<dt>WORK  
TRANSACTION  </dt>
<dd>Optional key words. They have no effect.</dd>

<dt>SERIALIZABLE  
REPEATABLE READ  
READ COMMITTED  
READ UNCOMMITTED  </dt>
<dd>The SQL standard defines four transaction isolation levels: `READ COMMITTED`, `READ UNCOMMITTED`, `SERIALIZABLE`, and `REPEATABLE READ`. The default behavior is that a statement can only see rows committed before it began (`READ COMMITTED`). In HAWQ, `READ UNCOMMITTED` is treated the same as `READ COMMITTED`. `SERIALIZABLE` is supported the same as `REPEATABLE                      READ` wherein all statements of the current transaction can only see rows committed before the first statement was executed in the transaction. `SERIALIZABLE` is the strictest transaction isolation. This level emulates serial transaction execution, as if transactions had been executed one after another, serially, rather than concurrently. Applications using this level must be prepared to retry transactions due to serialization failures.</dd>

<dt>READ WRITE  
READ ONLY  </dt>
<dd>Determines whether the transaction is read/write or read-only. Read/write is the default. When a transaction is read-only, the following SQL commands are disallowed: `INSERT` and `COPY FROM` if the table they would write to is not a temporary table; all `CREATE`, `ALTER`, and `DROP` commands; `GRANT`, `REVOKE`, `TRUNCATE`; and `EXPLAIN ANALYZE` and `EXECUTE` if the command they would execute is among those listed.</dd>

## <a id="topic1__section5"></a>Notes

Use [COMMIT](COMMIT.html) or [ROLLBACK](ROLLBACK.html) to terminate a transaction block.

Issuing `BEGIN` when already inside a transaction block will provoke a warning message. The state of the transaction is not affected. To nest transactions within a transaction block, use savepoints (see [SAVEPOINT](SAVEPOINT.html)).

## <a id="topic1__section6"></a>Examples

To begin a transaction block:

``` pre
BEGIN;
```

## <a id="topic1__section7"></a>Compatibility

`BEGIN` is a HAWQ language extension. It is equivalent to the SQL-standard command `START TRANSACTION lang="EN"`.

Incidentally, the `BEGIN` key word is used for a different purpose in embedded SQL. You are advised to be careful about the transaction semantics when porting database applications.

## <a id="topic1__section8"></a>See Also

[COMMIT](COMMIT.html), [ROLLBACK](ROLLBACK.html), [SAVEPOINT](SAVEPOINT.html)
