---
title: REVOKE
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

Removes access privileges.

## <a id="topic1__section2"></a>Synopsis

``` pre
REVOKE [GRANT OPTION FOR] { {SELECT | INSERT | UPDATE | DELETE 
       | REFERENCES | TRUNCATE } [,...] | ALL [PRIVILEGES] }
       ON [TABLE] <tablename> [, ...]
       FROM {<rolename> | PUBLIC} [, ...]
       [CASCADE | RESTRICT]

REVOKE [GRANT OPTION FOR] { {USAGE | SELECT | UPDATE} [,...] 
       | ALL [PRIVILEGES] }
       ON SEQUENCE <sequencename> [, ...]
       FROM { <rolename> | PUBLIC } [, ...]
       [CASCADE | RESTRICT]

REVOKE [GRANT OPTION FOR] { {CREATE | CONNECT 
       | TEMPORARY | TEMP} [,...] | ALL [PRIVILEGES] }
       ON DATABASE <dbname> [, ...]
       FROM {<rolename> | PUBLIC} [, ...]
       [CASCADE | RESTRICT]

REVOKE [GRANT OPTION FOR] {EXECUTE | ALL [PRIVILEGES]}
       ON FUNCTION <funcname> ( [[<argmode>] [<argname>] <argtype>
                              [, ...]] ) [, ...]
       FROM {<rolename> | PUBLIC} [, ...]
       [CASCADE | RESTRICT]

REVOKE [GRANT OPTION FOR] {USAGE | ALL [PRIVILEGES]}
       ON LANGUAGE <langname> [, ...]
       FROM {<rolename> | PUBLIC} [, ...]
       [ CASCADE | RESTRICT ]

REVOKE [GRANT OPTION FOR] { {CREATE | USAGE} [,...] 
       | ALL [PRIVILEGES] }
       ON SCHEMA <schemaname> [, ...]
       FROM {<rolename> | PUBLIC} [, ...]
       [CASCADE | RESTRICT]

REVOKE [GRANT OPTION FOR] { CREATE | ALL [PRIVILEGES] }
       ON TABLESPACE <tablespacename> [, ...]
       FROM { <rolename> | PUBLIC } [, ...]
       [CASCADE | RESTRICT]

REVOKE [ADMIN OPTION FOR] <parent_role> [, ...] 
       FROM <member_role> [, ...]
       [CASCADE | RESTRICT]
```

## <a id="topic1__section3"></a>Description

`REVOKE` command revokes previously granted privileges from one or more roles. The key word `PUBLIC` refers to the implicitly defined group of all roles.

See the description of the [GRANT](GRANT.html) command for the meaning of the privilege types.

Note that any particular role will have the sum of privileges granted directly to it, privileges granted to any role it is presently a member of, and privileges granted to `PUBLIC`. Thus, for example, revoking `SELECT` privilege from `PUBLIC` does not necessarily mean that all roles have lost `SELECT` privilege on the object: those who have it granted directly or via another role will still have it.

If `GRANT OPTION FOR` is specified, only the grant option for the privilege is revoked, not the privilege itself. Otherwise, both the privilege and the grant option are revoked.

If a role holds a privilege with grant option and has granted it to other roles then the privileges held by those other roles are called dependent privileges. If the privilege or the grant option held by the first role is being revoked and dependent privileges exist, those dependent privileges are also revoked if `CASCADE` is specified, else the revoke action will fail. This recursive revocation only affects privileges that were granted through a chain of roles that is traceable to the role that is the subject of this `REVOKE` command. Thus, the affected roles may effectively keep the privilege if it was also granted through other roles.

When revoking membership in a role, `GRANT OPTION` is instead called `ADMIN OPTION`, but the behavior is similar.

## <a id="topic1__section4"></a>Parameters

See [GRANT](GRANT.html).

## <a id="topic1__section5"></a>Examples

Revoke insert privilege for the public on table `films`:

``` sql
REVOKE INSERT ON films FROM PUBLIC;
```

Revoke all privileges from role `sally` on view `topten`. Note that this actually means revoke all privileges that the current role granted (if not a superuser).

``` sql
REVOKE ALL PRIVILEGES ON topten FROM sally;
```

Revoke membership in role `admins` from user `joe`:

``` sql
REVOKE admins FROM joe;
```

## <a id="topic1__section6"></a>Compatibility

The compatibility notes of the [GRANT](GRANT.html) command also apply to `REVOKE`.

Either `RESTRICT` or `CASCADE` is required according to the standard, but HAWQ assumes `RESTRICT` by default.

## <a id="topic1__section7"></a>See Also

[GRANT](GRANT.html)
