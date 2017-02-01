---
title: ALTER ROLE
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

Changes a database role (user or group).

## <a id="alterrole__section2"></a>Synopsis

```pre
ALTER ROLE <name> RENAME TO <newname>

ALTER ROLE <name> RESOURCE QUEUE {<queue_name> | NONE}

ALTER ROLE <name> [ [WITH] <option> [ ... ] ]
```

where \<option\> can be:

```pre
      SUPERUSER | NOSUPERUSER
    | CREATEDB | NOCREATEDB
    | CREATEROLE | NOCREATEROLE
    | CREATEEXTTABLE | NOCREATEEXTTABLE
    [ ( <attribute>='<value>'[, ...] ) ]
           where attribute and value are:
           type='readable'|'writable'
           protocol='gpfdist'|'http'
    
    | INHERIT | NOINHERIT
    | LOGIN | NOLOGIN
    | CONNECTION LIMIT <connlimit>
    | [ENCRYPTED | UNENCRYPTED] PASSWORD '<password>'
    | VALID UNTIL '<timestamp>'
    | [ DENY <deny_point> ]
    | [ DENY BETWEEN <deny_point> AND <deny_point>]
    | [ DROP DENY FOR <deny_point> ]
```

## <a id="desc"></a>Description

`ALTER ROLE` changes the attributes of a HAWQ role. There are several variants of this command:

-   **RENAME** — Changes the name of the role. Database superusers can rename any role. Roles having `CREATEROLE` privilege can rename non-superuser roles. The current session user cannot be renamed (connect as a different user to rename a role). Because MD5-encrypted passwords use the role name as cryptographic salt, renaming a role clears its password if the password is MD5-encrypted.
-   **RESOURCE QUEUE** — Assigns the role to a workload management resource queue. The role would then be subject to the limits assigned to the resource queue when issuing queries. Specify `NONE` to assign the role to the default resource queue. A role can only belong to one resource queue. For a role without `LOGIN` privilege, resource queues have no effect. See [CREATE RESOURCE QUEUE](CREATE-RESOURCE-QUEUE.html#topic1) for more information.
-   **WITH** \<option\> — Changes many of the role attributes that can be specified in [CREATE ROLE](CREATE-ROLE.html). Attributes not mentioned in the command retain their previous settings. Database superusers can change any of these settings for any role. Roles having `CREATEROLE` privilege can change any of these settings, but only for non-superuser roles. Ordinary roles can only change their own password.

**Note:** SET and RESET commands are currently not supported in connection with ALTER ROLE and will result in an error. See [SET](SET.html) and [About Server Configuration Parameters](../guc/guc_config.html#topic1) for information about user-settable configuration parameters.

## <a id="alterrole__section4"></a>Parameters

<dt> \<name\>  </dt>
<dd>The name of the role whose attributes are to be altered.</dd>

<dt> \<newname\>  </dt>
<dd>The new name of the role.</dd>

<dt> \<queue\_name\>  </dt>
<dd>The name of the resource queue to which the user-level role is to be assigned. Only roles with `LOGIN` privilege can be assigned to a resource queue. To unassign a role from a resource queue and put it in the default resource queue, specify `NONE`. A role can only belong to one resource queue.</dd>

<dt>SUPERUSER | NOSUPERUSER  
CREATEDB | NOCREATEDB  
CREATEROLE | NOCREATEROLE  
CREATEEXTTABLE | NOCREATEEXTTABLE \[(\<attribute\>='\<value\>')\]  </dt>
<dd>If `CREATEEXTTABLE` is specified, the role being defined is allowed to create external tables. The default `type` is `readable` and the default `protocol` is `gpfdist` if not specified. `NOCREATEEXTTABLE` (the default) denies the role the ability to create external tables. Using the `file` protocol when creating external tables is not supported. This is because HAWQ cannot guarantee scheduling executors on a specific host. Likewise, you cannot use the `execute` command with `ON ALL` and `ON HOST` for the same reason. Use the `ON MASTER/<number>/SEGMENT <segment_id>` to specify which segment instances are to execute the command.</dd>

<dt>INHERIT | NOINHERIT  
LOGIN | NOLOGIN  
CONNECTION LIMIT \<connlimit\>  
PASSWORD '\<password\>'  
ENCRYPTED | UNENCRYPTED  
VALID UNTIL '\<timestamp\>'  </dt>
<dd>These clauses alter role attributes originally set by [CREATE ROLE](CREATE-ROLE.html).</dd>

<dt>DENY \<deny\_point\>  
DENY BETWEEN \<deny\_point\> AND \<deny\_point\>   </dt>
<dd>The `DENY` and `DENY BETWEEN` keywords set time-based constraints that are enforced at login. `DENY`sets a day or a day and time to deny access. `DENY BETWEEN` sets an interval during which access is denied. Both use the parameter \<deny\_point\> that has following format:

```pre
DAY <day> [ TIME '<time>' ]
```

The two parts of the \<deny_point\> parameter use the following formats:

For \<day\>:

``` pre
{'Sunday' | 'Monday' | 'Tuesday' |'Wednesday' | 'Thursday' | 'Friday' |
'Saturday' | 0-6 }
```

For \<time\>:

``` pre
{ 00-23 : 00-59 | 01-12 : 00-59 { AM | PM }}
```

The `DENY BETWEEN` clause uses two \<deny\_point\> parameters.

```pre
DENY BETWEEN <deny_point> AND <deny_point>

```
</dd>

<dt>DROP DENY FOR \<deny\_point\>  </dt>
<dd>The `DROP DENY FOR` clause removes a time-based constraint from the role. It uses the \<deny\_point\> parameter described above.</dd>

## Notes

Use `GRANT` and `REVOKE` for adding and removing role memberships.

Caution must be exercised when specifying an unencrypted password with this command. The password will be transmitted to the server in clear text, and it might also be logged in the client’s command history or the server log. The `psql` command-line client contains a meta-command `\password` that can be used to safely change a role’s password.

It is also possible to tie a session default to a specific database rather than to a role. Role-specific settings override database-specific ones if there is a conflict.

## Examples

Change the password for a role:

```pre
ALTER ROLE daria WITH PASSWORD 'passwd123';
```

Change a password expiration date:

```pre
ALTER ROLE scott VALID UNTIL 'May 4 12:00:00 2015 +1';
```

Make a password valid forever:

```pre
ALTER ROLE luke VALID UNTIL 'infinity';
```

Give a role the ability to create other roles and new databases:

```pre
ALTER ROLE joelle CREATEROLE CREATEDB;
```

Give a role a non-default setting of the `maintenance_work_mem` parameter:

```pre
ALTER ROLE admin SET maintenance_work_mem = 100000;
```

Assign a role to a resource queue:

```pre
ALTER ROLE sammy RESOURCE QUEUE poweruser;
```

Give a role permission to create writable external tables:

```pre
ALTER ROLE load CREATEEXTTABLE (type='writable');
```

Alter a role so it does not allow login access on Sundays:

```pre
ALTER ROLE user3 DENY DAY 'Sunday';
```

Alter a role to remove the constraint that does not allow login access on Sundays:

```pre
ALTER ROLE user3 DROP DENY FOR DAY 'Sunday';
```

## <a id="compat"></a>Compatibility

The `ALTER ROLE` statement is a HAWQ extension.

## <a id="see"></a>See Also

[CREATE ROLE](CREATE-ROLE.html), [DROP ROLE](DROP-ROLE.html), [SET](SET.html), [CREATE RESOURCE QUEUE](CREATE-RESOURCE-QUEUE.html), [GRANT](GRANT.html), [REVOKE](REVOKE.html) 
