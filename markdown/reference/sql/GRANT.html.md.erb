---
title: GRANT
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

Defines access privileges.

## <a id="topic1__section2"></a>Synopsis

``` pre
GRANT { {SELECT | INSERT | UPDATE | DELETE | REFERENCES }
[,...] | ALL [PRIVILEGES] }
    ON [TABLE] <tablename> [, ...]
    TO {<rolename> | PUBLIC} [, ...] [WITH GRANT OPTION]

GRANT { {USAGE | SELECT | UPDATE} [,...] | ALL [PRIVILEGES] }
    ON SEQUENCE <sequencename> [, ...]
    TO { <rolename> | PUBLIC } [, ...] [WITH GRANT OPTION]

GRANT { {CREATE | CONNECT | TEMPORARY | TEMP} [,...] | ALL
[PRIVILEGES] }
    ON DATABASE <dbname> [, ...]
    TO {<rolename> | PUBLIC} [, ...] [WITH GRANT OPTION]

GRANT { EXECUTE | ALL [PRIVILEGES] }
    ON FUNCTION <funcname> ( [ [<argmode>] [<argname>] <argtype> [, ...]
    ] ) [, ...]
    TO {<rolename> | PUBLIC} [, ...] [WITH GRANT OPTION]

GRANT { USAGE | ALL [PRIVILEGES] }
    ON LANGUAGE <langname> [, ...]
    TO {<rolename> | PUBLIC} [, ...] [WITH GRANT OPTION]

GRANT { {CREATE | USAGE} [,...] | ALL [PRIVILEGES] }
    ON SCHEMA <schemaname> [, ...]
    TO {<rolename> | PUBLIC} [, ...] [WITH GRANT OPTION]

GRANT { CREATE | ALL [PRIVILEGES] }
    ON TABLESPACE <tablespacename> [, ...]
    TO {<rolename> | PUBLIC} [, ...] [WITH GRANT OPTION]

GRANT <parent_role> [, ...]
    TO <member_role> [, ...] [WITH ADMIN OPTION]

GRANT { SELECT | INSERT | ALL [PRIVILEGES] }
    ON PROTOCOL <protocolname>
    TO <username>

```

## <a id="topic1__section3"></a>Description

The `GRANT` command has two basic variants: one that grants privileges on a database object (table, view, sequence, database, function, procedural language, schema, or tablespace), and one that grants membership in a role.

**GRANT on Database Objects**

This variant of the `GRANT` command gives specific privileges on a database object to one or more roles. These privileges are added to those already granted, if any.

The key word `PUBLIC` indicates that the privileges are to be granted to all roles, including those that may be created later. `PUBLIC` may be thought of as an implicitly defined group-level role that always includes all roles. Any particular role will have the sum of privileges granted directly to it, privileges granted to any role it is presently a member of, and privileges granted to `PUBLIC`.

If `WITH GRANT OPTION` is specified, the recipient of the privilege may in turn grant it to others. Without a grant option, the recipient cannot do that. Grant options cannot be granted to `PUBLIC`.

There is no need to grant privileges to the owner of an object (usually the role that created it), as the owner has all privileges by default. The right to drop an object, or to alter its definition in any way is not described by a grantable privilege; it is inherent in the owner, and cannot be granted or revoked. The owner implicitly has all grant options for the object, too.

Depending on the type of object, the initial default privileges may include granting some privileges to `PUBLIC`. The default is no public access for tables, schemas, and tablespaces; `CONNECT` privilege and `TEMP` table creation privilege for databases; `EXECUTE` privilege for functions; and `USAGE` privilege for languages. The object owner may of course revoke these privileges.

**GRANT on Roles**

This variant of the `GRANT` command grants membership in a role to one or more other roles. Membership in a role is significant because it conveys the privileges granted to a role to each of its members.

If `WITH ADMIN OPTION` is specified, the member may in turn grant membership in the role to others, and revoke membership in the role as well. Database superusers can grant or revoke membership in any role to anyone. Roles having `CREATEROLE` privilege can grant or revoke membership in any role that is not a superuser.

Unlike the case with privileges, membership in a role cannot be granted to `PUBLIC`.

## <a id="topic1__section7"></a>Parameters

<dt>SELECT  </dt>
<dd>Allows `SELECT` from any column of the specified table, view, or sequence. Also allows the use of `COPY TO`. For sequences, this privilege also allows the use of the `currval` function.</dd>

<dt>INSERT  </dt>
<dd>Allows `INSERT` of a new row into the specified table. Also allows `COPY FROM`.</dd>

<dt>UPDATE  </dt>
<dd>Allows `UPDATE` of any column of the specified table. `SELECT               ... FOR UPDATE` and `SELECT ... FOR SHARE` also require this privilege (as well as the `SELECT` privilege). For sequences, this privilege allows the use of the `nextval` and `setval` functions.</dd>

<dt>DELETE  </dt>
<dd>Allows `DELETE` of a row from the specified table.</dd>

<dt>REFERENCES  </dt>
<dd>This keyword is accepted, although foreign key constraints are currently not supported in HAWQ. To create a foreign key constraint, it is necessary to have this privilege on both the referencing and referenced tables.</dd>

<dt>TRIGGER  </dt>
<dd>Allows the creation of a trigger on the specified table.

**Note:** HAWQ does not support triggers.</dd>

<dt>CREATE  </dt>
<dd>For databases, allows new schemas to be created within the database.

For schemas, allows new objects to be created within the schema. To rename an existing object, you must own the object and have this privilege for the containing schema.

For tablespaces, allows tables and indexes to be created within the tablespace, and allows databases to be created that have the tablespace as their default tablespace. (Note that revoking this privilege will not alter the placement of existing objects.)</dd>

<dt>CONNECT  </dt>
<dd>Allows the user to connect to the specified database. This privilege is checked at connection startup (in addition to checking any restrictions imposed by `pg_hba.conf`).</dd>

<dt>TEMPORARY  
TEMP  </dt>
<dd>Allows temporary tables to be created while using the database.</dd>

<dt>EXECUTE  </dt>
<dd>Allows the use of the specified function and the use of any operators that are implemented on top of the function. This is the only type of privilege that is applicable to functions. (This syntax works for aggregate functions, as well.)</dd>

<dt>USAGE  </dt>
<dd>For procedural languages, allows the use of the specified language for the creation of functions in that language. This is the only type of privilege that is applicable to procedural languages.

For schemas, allows access to objects contained in the specified schema (assuming that the objects' own privilege requirements are also met). Essentially this allows the grantee to look up objects within the schema.

For sequences, this privilege allows the use of the `currval` and `nextval` functions.</dd>

<dt>ALL PRIVILEGES  </dt>
<dd>Grant all of the available privileges at once. The `PRIVILEGES` key word is optional in HAWQ, though it is required by strict SQL.</dd>

<dt>PUBLIC  </dt>
<dd>A special group-level role that denotes that the privileges are to be granted to all roles, including those that may be created later.</dd>

<dt>WITH GRANT OPTION  </dt>
<dd>The recipient of the privilege may in turn grant it to others.</dd>

<dt>WITH ADMIN OPTION  </dt>
<dd>The member of a role may in turn grant membership in the role to others.</dd>

## <a id="topic1__section8"></a>Notes

Database superusers can access all objects regardless of object privilege settings. One exception to this rule is view objects. Access to tables referenced in the view is determined by permissions of the view owner not the current user (even if the current user is a superuser).

If a superuser chooses to issue a `GRANT` or `REVOKE` command, the command is performed as though it were issued by the owner of the affected object. In particular, privileges granted via such a command will appear to have been granted by the object owner. For role membership, the membership appears to have been granted by the containing role itself.

`GRANT` and `REVOKE` can also be done by a role that is not the owner of the affected object, but is a member of the role that owns the object, or is a member of a role that holds privileges `WITH GRANT OPTION` on the object. In this case the privileges will be recorded as having been granted by the role that actually owns the object or holds the privileges `WITH GRANT OPTION`.

Granting permission on a table does not automatically extend permissions to any sequences used by the table, including sequences tied to `SERIAL` columns. Permissions on a sequence must be set separately.

HAWQ does not support granting or revoking privileges for individual columns of a table. One possible workaround is to create a view having just the desired columns and then grant privileges to that view.

Use psql's `\z` meta-command to obtain information about existing privileges for an object.

## <a id="topic1__section9"></a>Examples

Grant insert privilege to all roles on table `mytable`:

``` pre
GRANT INSERT ON mytable TO PUBLIC;
```

Grant all available privileges to role `sally` on the view `topten`. Note that while the above will indeed grant all privileges if executed by a superuser or the owner of `topten`, when executed by someone else it will only grant those permissions for which the granting role has grant options.

``` pre
GRANT ALL PRIVILEGES ON topten TO sally;
```

Grant membership in role `admins` to user `joe`:

``` pre
GRANT admins TO joe;
```

## <a id="topic1__section10"></a>Compatibility

The `PRIVILEGES` key word in is required in the SQL standard, but optional in HAWQ. The SQL standard does not support setting the privileges on more than one object per command.

HAWQ allows an object owner to revoke his own ordinary privileges: for example, a table owner can make the table read-only to himself by revoking his own `INSERT` privileges. This is not possible according to the SQL standard. HAWQ treats the owner's privileges as having been granted by the owner to himself; therefore he can revoke them too. In the SQL standard, the owner's privileges are granted by an assumed *system* entity.

The SQL standard allows setting privileges for individual columns within a table.

The SQL standard provides for a `USAGE` privilege on other kinds of objects: character sets, collations, translations, domains.

Privileges on databases, tablespaces, schemas, and languages are HAWQ extensions.

## <a id="topic1__section11"></a>See Also

[REVOKE](REVOKE.html)
