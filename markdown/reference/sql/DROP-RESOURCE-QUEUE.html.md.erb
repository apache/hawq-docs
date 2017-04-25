---
title: DROP RESOURCE QUEUE
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

Removes a resource queue.

## <a id="topic1__section2"></a>Synopsis

``` pre
DROP RESOURCE QUEUE <queue_name>
         
```

## <a id="topic1__section3"></a>Description

This command removes a resource queue from HAWQ. To drop a resource queue, the queue cannot have any roles assigned to it, nor can it have any statements waiting in the queue or have any children resource queues. Only a superuser can drop a resource queue.

**Note:** The `pg_root` and `pg_default` resource queues cannot be dropped.

## <a id="topic1__section4"></a>Parameters

<dt> \<queue\_name\>   </dt>
<dd>The name of a resource queue to remove.</dd>

## <a id="topic1__section5"></a>Notes

Use [ALTER ROLE](ALTER-ROLE.html) to remove a user from a resource queue.

To see all the currently active queries for all resource queues, perform the following query of the `pg_locks` table joined with the `pg_roles` and `pg_resqueue` tables:

``` pre
SELECT rolname, rsqname, locktype, objid, transaction, pid, 
mode, granted FROM pg_roles, pg_resqueue, pg_locks WHERE 
pg_roles.rolresqueue=pg_locks.objid AND 
pg_locks.objid=pg_resqueue.oid;
```

To see the roles assigned to a resource queue, perform the following query of the `pg_roles` and `pg_resqueue` system catalog tables:

``` pre
SELECT rolname, rsqname FROM pg_roles, pg_resqueue WHERE 
pg_roles.rolresqueue=pg_resqueue.oid;
```

## <a id="topic1__section6"></a>Examples

Remove a role from a resource queue (and move the role to the default resource queue, `pg_default`):

``` pre
ALTER ROLE bob RESOURCE QUEUE NONE;
```

Remove the resource queue named `adhoc`:

``` pre
DROP RESOURCE QUEUE adhoc;
```

## <a id="topic1__section7"></a>Compatibility

The `DROP RESOURCE QUEUE` statement is a HAWQ extension.

## <a id="topic1__section8"></a>See Also

[CREATE RESOURCE QUEUE](CREATE-RESOURCE-QUEUE.html), [ALTER ROLE](ALTER-ROLE.html), [ALTER RESOURCE QUEUE](ALTER-RESOURCE-QUEUE.html)
