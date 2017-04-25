---
title: DROP ROLE
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

Removes a database role.

## <a id="topic1__section2"></a>Synopsis

``` pre
DROP ROLE [IF EXISTS] <name> [, ...]
```

## <a id="topic1__section3"></a>Description

`DROP ROLE` removes the specified role(s). To drop a superuser role, you must be a superuser yourself. To drop non-superuser roles, you must have `CREATEROLE` privilege.

A role cannot be removed if it is still referenced in any database; an error will be raised if so. Before dropping the role, you must drop all the objects it owns (or reassign their ownership) and revoke any privileges the role has been granted. The `REASSIGN           OWNED` and `DROP OWNED` commands can be useful for this purpose.

However, it is not necessary to remove role memberships involving the role; `DROP ROLE` automatically revokes any memberships of the target role in other roles, and of other roles in the target role. The other roles are not dropped nor otherwise affected.

## <a id="topic1__section4"></a>Parameters

<dt>IF EXISTS  </dt>
<dd>Do not throw an error if the role does not exist. A notice is issued in this case.</dd>

<dt>\<name\>   </dt>
<dd>The name of the role to remove.</dd>

## <a id="topic1__section5"></a>Examples

Remove the roles named `sally` and `bob`:

``` pre
DROP ROLE sally, bob;
```

## <a id="topic1__section6"></a>Compatibility

The SQL standard defines `DROP ROLE`, but it allows only one role to be dropped at a time, and it specifies different privilege requirements than HAWQ uses.

## <a id="topic1__section7"></a>See Also

[ALTER ROLE](ALTER-ROLE.html), [CREATE ROLE](CREATE-ROLE.html), [DROP OWNED](DROP-OWNED.html), [REASSIGN OWNED](REASSIGN-OWNED.html), [SET ROLE](SET-ROLE.html)
