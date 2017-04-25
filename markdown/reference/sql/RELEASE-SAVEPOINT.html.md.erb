---
title: RELEASE SAVEPOINT
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

Destroys a previously defined savepoint.

## <a id="topic1__section2"></a>Synopsis

``` pre
RELEASE [SAVEPOINT] <savepoint_name>
         
```

## <a id="topic1__section3"></a>Description

`RELEASE SAVEPOINT` destroys a savepoint previously defined in the current transaction.

Destroying a savepoint makes it unavailable as a rollback point, but it has no other user visible behavior. It does not undo the effects of commands executed after the savepoint was established. (To do that, see [ROLLBACK TO SAVEPOINT](ROLLBACK-TO-SAVEPOINT.html).) Destroying a savepoint when it is no longer needed may allow the system to reclaim some resources earlier than transaction end.

`RELEASE SAVEPOINT` also destroys all savepoints that were established *after* the named savepoint was established.

## <a id="topic1__section4"></a>Parameters

<dt> \<savepoint\_name\>   </dt>
<dd>The name of the savepoint to destroy.</dd>

## <a id="topic1__section5"></a>Examples

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

## <a id="topic1__section6"></a>Compatibility

This command conforms to the SQL standard. The standard specifies that the key word `SAVEPOINT` is mandatory, but HAWQ allows it to be omitted.

## <a id="topic1__section7"></a>See Also

[BEGIN](BEGIN.html), [SAVEPOINT](SAVEPOINT.html), [ROLLBACK TO SAVEPOINT](ROLLBACK-TO-SAVEPOINT.html), [COMMIT](COMMIT.html)
