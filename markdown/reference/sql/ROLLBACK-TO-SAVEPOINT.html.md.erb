---
title: ROLLBACK TO SAVEPOINT
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

Rolls back the current transaction to a savepoint.

## <a id="topic1__section2"></a>Synopsis

``` pre
ROLLBACK [WORK | TRANSACTION] TO [SAVEPOINT] <savepoint_name>

```

## <a id="topic1__section3"></a>Description

This command will roll back all commands that were executed after the savepoint was established. The savepoint remains valid and can be rolled back to again later, if needed.

`ROLLBACK TO SAVEPOINT` implicitly destroys all savepoints that were established after the named savepoint.

## <a id="topic1__section4"></a>Parameters

<dt>WORK  
TRANSACTION  </dt>
<dd>Optional key words. They have no effect.</dd>

<dt> \<savepoint\_name\>  </dt>
<dd>The name of a savepoint to roll back to.</dd>

## <a id="topic1__section5"></a>Notes

Use `RELEASE SAVEPOINT` to destroy a savepoint without discarding the effects of commands executed after it was established.

Specifying a savepoint name that has not been established is an error.

Cursors have somewhat non-transactional behavior with respect to savepoints. Any cursor that is opened inside a savepoint will be closed when the savepoint is rolled back. If a previously opened cursor is affected by a `FETCH` command inside a savepoint that is later rolled back, the cursor position remains at the position that `FETCH` left it pointing to (that is, `FETCH` is not rolled back). Closing a cursor is not undone by rolling back, either. A cursor whose execution causes a transaction to abort is put in a can't-execute state, so while the transaction can be restored using `ROLLBACK TO SAVEPOINT`, the cursor can no longer be used.

## <a id="topic1__section6"></a>Examples

To undo the effects of the commands executed after `my_savepoint` was established:

``` sql
ROLLBACK TO SAVEPOINT my_savepoint;
```

Cursor positions are not affected by a savepoint rollback:

``` sql
BEGIN;
DECLARE foo CURSOR FOR SELECT 1 UNION SELECT 2;
SAVEPOINT foo;
FETCH 1 FROM foo;
```
``` pre
column
----------
        1
```
``` sql
ROLLBACK TO SAVEPOINT foo;
FETCH 1 FROM foo;
```
``` pre
column
----------
        2
```
``` sql
COMMIT;
```

## <a id="topic1__section7"></a>Compatibility

The SQL standard specifies that the key word `SAVEPOINT` is mandatory, but HAWQ (and Oracle) allow it to be omitted. SQL allows only `WORK`, not `TRANSACTION`, as a stopword after `ROLLBACK`. Also, SQL has an optional clause `AND [NO] CHAIN` which is not currently supported by HAWQ. Otherwise, this command conforms to the SQL standard.

## <a id="topic1__section8"></a>See Also

[BEGIN](BEGIN.html), [COMMIT](COMMIT.html), [SAVEPOINT](SAVEPOINT.html), [RELEASE SAVEPOINT](RELEASE-SAVEPOINT.html), [ROLLBACK](ROLLBACK.html)
