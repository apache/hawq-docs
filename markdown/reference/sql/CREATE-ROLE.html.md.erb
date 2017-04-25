---
title: CREATE ROLE
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

Defines a new database role (user or group).

## <a id="topic1__section2"></a>Synopsis

``` pre
CREATE ROLE <name> [[WITH] <option> [ ... ]]
```

where \<option\> can be:

``` pre
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
    | [ ENCRYPTED | UNENCRYPTED ] PASSWORD '<password>'
    | VALID UNTIL '<timestamp>'
    | IN ROLE <rolename> [, ...]
    | ROLE <rolename> [, ...]
    | ADMIN <rolename> [, ...]
    | RESOURCE QUEUE <queue_name>
    | [ DENY <deny_point> ]
    | [ DENY BETWEEN <deny_point> AND <deny_point>]
```

## <a id="topic1__section3"></a>Description

`CREATE ROLE` adds a new role to a HAWQ system. A role is an entity that can own database objects and have database privileges. A role can be considered a user, a group, or both depending on how it is used. You must have `CREATEROLE` privilege or be a database superuser to use this command.

Note that roles are defined at the system-level and are valid for all databases in your HAWQ system.

## <a id="topic1__section4"></a>Parameters

<dt> \<name\>  </dt>
<dd>The name of the new role.</dd>

<dt>SUPERUSER,  
NOSUPERUSER  </dt>
<dd>If `SUPERUSER` is specified, the role being defined will be a superuser, who can override all access restrictions within the database. Superuser status is dangerous and should be used only when really needed. You must yourself be a superuser to create a new superuser. `NOSUPERUSER` is the default.</dd>

<dt>CREATEDB,  
NOCREATEDB  </dt>
<dd>If `CREATEDB` is specified, the role being defined will be allowed to create new databases. `NOCREATEDB` (the default) will deny a role the ability to create databases.</dd>

<dt>CREATEROLE,  
NOCREATEROLE  </dt>
<dd>If `CREATEDB` is specified, the role being defined will be allowed to create new roles, alter other roles, and drop other roles. `NOCREATEROLE` (the default) will deny a role the ability to create roles or modify roles other than their own.</dd>

<dt>CREATEEXTTABLE,  
NOCREATEEXTTABLE  </dt>
<dd>If `CREATEEXTTABLE` is specified, the role being defined is allowed to create external tables. The default \<type\> is `readable` and the default `protocol` is `gpfdist` if not specified. `NOCREATEEXTTABLE` (the default) denies the role the ability to create external tables. Using the `file` protocol when creating external tables is not supported. This is because HAWQ cannot guarantee scheduling executors on a specific host. Likewise, you cannot use the `EXECUTE` command with `ON                      ALL` and `ON HOST` for the same reason. Use the `ON MASTER/number/SEGMENT segment_id` to specify which segment instances are to execute the command.</dd>

<dt>INHERIT,  
NOINHERIT  </dt>
<dd>If specified, `INHERIT` (the default) allows the role to use whatever database privileges have been granted to all roles it is directly or indirectly a member of. With `NOINHERIT`, membership in another role only grants the ability to `SET ROLE` to that other role.</dd>

<dt>LOGIN,  
NOLOGIN  </dt>
<dd>If specified, `LOGIN` allows a role to log in to a database. A role having the `LOGIN` attribute can be thought of as a user. Roles with `NOLOGIN` (the default) are useful for managing database privileges, and can be thought of as groups.</dd>

<dt>CONNECTION LIMIT \<connlimit\>  </dt>
<dd>The number maximum of concurrent connections this role can make. The default of -1 means there is no limitation.</dd>

<!-- -->

<dt>PASSWORD \<password\>  </dt>
<dd>Sets the user password for roles with the `LOGIN` attribute. If you do not plan to use password authentication you can omit this option. If no \<password\> is specified, the password will be set to null and password authentication will always fail for that user. A null \<password\> can optionally be written explicitly as `PASSWORD NULL`.</dd>

<dt>ENCRYPTED,  
UNENCRYPTED  </dt>
<dd>These key words control whether the password is stored encrypted in the system catalogs. (If neither is specified, the default behavior is determined by the configuration parameter `password_encryption`.) If the presented password string is already in MD5-encrypted format, then it is stored encrypted as-is, regardless of whether `ENCRYPTED` or `UNENCRYPTED` is specified (since the system cannot decrypt the specified encrypted password string). This allows reloading of encrypted passwords during dump/restore.

Note that older clients may lack support for the MD5 authentication mechanism that is needed to work with passwords that are stored encrypted.</dd>

<dt>VALID UNTIL '\<timestamp\>'  </dt>
<dd>The VALID UNTIL clause sets a date and time after which the role's password is no longer valid. If this clause is omitted the password will never expire.</dd>

<dt>IN ROLE \<rolename\>  </dt>
<dd>Adds the new role as a member of the named roles. Note that there is no option to add the new role as an administrator; use a separate `GRANT` command to do that.</dd>

<dt>ROLE \<rolename\>  </dt>
<dd>Adds the named roles as members of this role, making this new role a group.</dd>

<dt>ADMIN \<rolename\>  </dt>
<dd>The `ADMIN` clause is like `ROLE`, but the named roles are added to the new role `WITH ADMIN OPTION`, giving them the right to grant membership in this role to others.</dd>

<dt>RESOURCE QUEUE \<queue\_name\>  </dt>
<dd>The name of the resource queue to which the new user-level role is to be assigned. Only roles with `LOGIN` privilege can be assigned to a resource queue. The special keyword `NONE` means that the role is assigned to the default resource queue. A role can only belong to one resource queue.</dd>

<dt>DENY \<deny\_point\>,  
DENY BETWEEN \<deny\_point\> AND \<deny\_point\>   </dt>
<dd>The `DENY` and `DENY BETWEEN` keywords set time-based constraints that are enforced at login. `DENY` sets a day or a day and time to deny access. `DENY BETWEEN` sets an interval during which access is denied. Both use the parameter \<deny\_point\> that has the following format:

``` pre
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

The `DENY BETWEEN` clause uses two \<deny\_point\> parameters:

``` pre
DENY BETWEEN deny_point AND deny_point

```
</dd>

## <a id="topic1__section5"></a>Notes

The preferred way to add and remove role members (manage groups) is to use [GRANT](GRANT.html) and [REVOKE](REVOKE.html).

The `VALID UNTIL` clause defines an expiration time for a password only, not for the role. The expiration time is not enforced when logging in using a non-password-based authentication method.

The `INHERIT` attribute governs inheritance of grantable privileges (access privileges for database objects and role memberships). It does not apply to the special role attributes set by `CREATE ROLE` and `ALTER                ROLE`. For example, being a member of a role with `CREATEDB` privilege does not immediately grant the ability to create databases, even if `INHERIT` is set.

The `INHERIT` attribute is the default for reasons of backwards compatibility. In prior releases of HAWQ, users always had access to all privileges of groups they were members of. However, `NOINHERIT` provides a closer match to the semantics specified in the SQL standard.

Be careful with the `CREATEROLE` privilege. There is no concept of inheritance for the privileges of a `CREATEROLE`-role. That means that even if a role does not have a certain privilege but is allowed to create other roles, it can easily create another role with different privileges than its own (except for creating roles with superuser privileges). For example, if a role has the `CREATEROLE` privilege but not the `CREATEDB` privilege, it can create a new role with the `CREATEDB` privilege. Therefore, regard roles that have the `CREATEROLE` privilege as almost-superuser-roles.

The `CONNECTION LIMIT` option is never enforced for superusers.

Caution must be exercised when specifying an unencrypted password with this command. The password will be transmitted to the server in clear-text, and it might also be logged in the client's command history or the server log. The client program `createuser`, however, transmits the password encrypted. Also, psql contains a command `\password` that can be used to safely change the password later.

## <a id="topic1__section6"></a>Examples

Create a role that can log in, but don't give it a password:

``` pre
CREATE ROLE jonathan LOGIN;
```

Create a role that belongs to a resource queue:

``` pre
CREATE ROLE jonathan LOGIN RESOURCE QUEUE poweruser;
```

Create a role with a password that is valid until the end of 2009 (`CREATE                USER` is the same as `CREATE ROLE` except that it implies `LOGIN`):

``` pre
CREATE USER joelle WITH PASSWORD 'jw8s0F4' VALID UNTIL '2010-01-01';
```

Create a role that can create databases and manage other roles:

``` pre
CREATE ROLE admin WITH CREATEDB CREATEROLE;
```

Create a role that does not allow login access on Sundays:

``` pre
CREATE ROLE user3 DENY DAY 'Sunday';
```

## <a id="topic1__section7"></a>Compatibility

The SQL standard defines the concepts of users and roles, but it regards them as distinct concepts and leaves all commands defining users to be specified by the database implementation. In HAWQ, users and roles are unified into a single type of object. Roles therefore have many more optional attributes than they do in the standard.

`CREATE ROLE` is in the SQL standard, but the standard only requires the syntax:

``` pre
CREATE ROLE <name> [WITH ADMIN <rolename>]
```

Allowing multiple initial administrators, and all the other options of `CREATE ROLE`, are HAWQ extensions.

The behavior specified by the SQL standard is most closely approximated by giving users the `NOINHERIT` attribute, while roles are given the `INHERIT` attribute.

## <a id="topic1__section8"></a>See Also

[SET ROLE](SET-ROLE.html), [ALTER ROLE](ALTER-ROLE.html), [DROP ROLE](DROP-ROLE.html), [GRANT](GRANT.html), [REVOKE](REVOKE.html), [CREATE RESOURCE QUEUE](CREATE-RESOURCE-QUEUE.html)
