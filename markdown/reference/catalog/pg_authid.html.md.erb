---
title: pg_authid
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

The `pg_authid` table contains information about database authorization identifiers (roles). A role subsumes the concepts of users and groups. A user is a role with the `rolcanlogin` flag set. Any role (with or without `rolcanlogin`) may have other roles as members. See [pg\_auth\_members](pg_auth_members.html#topic1).

Since this catalog contains passwords, it must not be publicly readable. [pg\_roles](pg_roles.html#topic1) is a publicly readable view on `pg_authid` that blanks out the password field.

Because user identities are system-wide, `pg_authid` is shared across all databases in a HAWQ system: there is only one copy of `pg_authid` per system, not one per database.

<a id="topic1__gd143898"></a>
<span class="tablecap">Table 1. pg\_catalog.pg\_authid</span>

| column              | type        | references | description                                                                                                           |
|---------------------|-------------|------------|-----------------------------------------------------------------------------------------------------------------------|
| `rolname`           | name        |            | Role name                                                                                                             |
| `rolsuper`          | boolean     |            | Role has superuser privileges                                                                                         |
| `rolinherit`        | boolean     |            | Role automatically inherits privileges of roles it is a member of                                                     |
| `rolcreaterole`     | boolean     |            | Role may create more roles                                                                                            |
| `rolcreatedb`       | boolean     |            | Role may create databases                                                                                             |
| `rolcatupdate`      | boolean     |            | Role may update system catalogs directly. (Even a superuser may not do this unless this column is true)               |
| `rolcanlogin`       | boolean     |            | Role may log in. That is, this role can be given as the initial session authorization identifier                      |
| `rolconnlimit`      | int4        |            | For roles that can log in, this sets maximum number of concurrent connections this role can make. `-1` means no limit |
| `rolpassword`       | text        |            | Password (possibly encrypted); NULL if none                                                                           |
| `rolvaliduntil`     | timestamptz |            | Password expiry time (only used for password authentication); NULL if no expiration                                   |
| `rolconfig`         | text\[\]    |            | Session defaults for server configuration parameters                                                                  |
| `relresqueue`       | oid         |            | Object ID of the associated resource queue ID in `pg_resqueue`                                                       |
| `rolcreaterextgpfd` | boolean     |            | Privilege to create read external tables with the `gpfdist` or `gpfdists` protocol                                    |
| `rolcreaterexhttp`  | boolean     |            | Privilege to create read external tables with the `http` protocol                                                     |
| `rolcreatewextgpfd` | boolean     |            | Privilege to create write external tables with the `gpfdist` or `gpfdists` protocol                                   |
| `rolcreaterexthdfs` | boolean     |            | Privilege to create read external tables with the `gphdfs` protocol. (`gphdfs` is deprecated.)                        |
| `rolcreatewexthdfs` | boolean     |            | Privilege to create write external tables with the `gphdfs` protocol. (`gphdfs` is deprecated.)                       |




