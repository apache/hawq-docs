---
title: SAVEPOINT
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

Defines a new savepoint within the current transaction.

## <a id="topic1__section2"></a>Synopsis

``` pre
SAVEPOINT <savepoint_name>
         
```

## <a id="topic1__section3"></a>Description

`SAVEPOINT` establishes a new savepoint within the current transaction.

A savepoint is a special mark inside a transaction that allows all commands that are executed after it was established to be rolled back, restoring the transaction state to what it was at the time of the savepoint.

## <a id="topic1__section4"></a>Parameters

<dt> \<savepoint\_name\>   </dt>
<dd>The name of the new savepoint.</dd>

## <a id="topic1__section5"></a>Notes

Use [ROLLBACK TO SAVEPOINT](ROLLBACK-TO-SAVEPOINT.html) to rollback to a savepoint. Use [RELEASE SAVEPOINT](RELEASE-SAVEPOINT.html) to destroy a savepoint, keeping the effects of commands executed after it was established.

Savepoints can only be established when inside a transaction block. There can be multiple savepoints defined within a transaction.

## <a id="topic1__section6"></a>Examples

To establish a savepoint and later undo the effects of all commands executed after it was established:

``` pre
BEGIN;
    INSERT INTO table1 VALUES (1);
    SAVEPOINT my_savepoint;
    INSERT INTO table1 VALUES (2);
    ROLLBACK TO SAVEPOINT my_savepoint;
    INSERT INTO table1 VALUES (3);
COMMIT;
```

The above transaction will insert the values 1 and 3, but not 2.

To establish and later destroy a savepoint:

``` pre
BEGIN;
    INSERT INTO table1 VALUES (3);
    SAVEPOINT my_savepoint;
    INSERT INTO table1 VALUES (4);
    RELEASE SAVEPOINT my_savepoint;
COMMIT;
```

The above transaction will insert both 3 and 4.

## <a id="topic1__section7"></a>Compatibility

SQL requires a savepoint to be destroyed automatically when another savepoint with the same name is established. In HAWQ, the old savepoint is kept, though only the more recent one will be used when rolling back or releasing. (Releasing the newer savepoint will cause the older one to again become accessible to [ROLLBACK TO SAVEPOINT](ROLLBACK-TO-SAVEPOINT.html) and [RELEASE SAVEPOINT](RELEASE-SAVEPOINT.html).) Otherwise, `SAVEPOINT` is fully SQL conforming.

## <a id="topic1__section8"></a>See Also

[BEGIN](BEGIN.html), [COMMIT](COMMIT.html), [ROLLBACK](ROLLBACK.html), [RELEASE SAVEPOINT](RELEASE-SAVEPOINT.html), [ROLLBACK TO SAVEPOINT](ROLLBACK-TO-SAVEPOINT.html)
