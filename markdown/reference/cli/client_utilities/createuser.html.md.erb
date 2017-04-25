---
title: createuser
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

Creates a new database role.

## <a id="topic1__section2"></a>Synopsis

``` pre
createuser [<connection_options>] [<role_attribute_options>] [-e | --echo] <role_name>

createuser --help 

createuser --version
```
where:

``` pre
<connection_options> =
	[-h <host> | --host <host>] 
	[-p <port> | -- port <port>] 
	[-U <username> | --username <username>] 
    [-W | --password]
    
<role_attribute_options> = 
    [-c <number> | --connection-limit <number>]
    [(-D | --no-createdb) | (-d | --createdb)]
    [(-E | --encrypted) | (-N | --unencrypted)]
    [(-i | --inherit) | (-I | --no-inherit)]
    [(-l | --login) | (-L | --no-login)]
    [-P | --pwprompt]
    [(-r | --createrole) | (-R | --no-createrole)]
    [(-s | --superuser) | -S | --no-superuser]
    
```

## <a id="topic1__section3"></a>Description

`createuser` creates a new HAWQ role. You must be a superuser or have the `CREATEROLE` privilege to create new roles. You must connect to the database as a superuser to create new superusers.

Superusers can bypass all access permission checks within the database, so superuser privileges should not be granted lightly.

`createuser` is a wrapper around the SQL command `CREATE ROLE`.

## <a id="args"></a>Arguments

<dt>**\<role\_name\>**</dt>
<dd>The name of the role to be created. This name must be different from all existing roles in this HAWQ installation.</dd>

## <a id="topic1__section4"></a>Options

<dt>-e, -\\\-echo  </dt>
<dd>Echo the commands that `createuser` generates and sends to the server.</dd>

**\<role\_attribute\_options\>**

<dt>-c, -\\\-connection-limit \<number\>  </dt>
<dd>Set a maximum number of connections for the new role. The default is to set no limit.</dd>


<dt>-D, -\\\-no-createdb  </dt>
<dd>The new role will not be allowed to create databases. This is the default.</dd>

<dt>-d, -\\\-createdb  </dt>
<dd>The new role will be allowed to create databases.</dd>


<dt>-E, -\\\-encrypted  </dt>
<dd>Encrypts the role's password stored in the database. If not specified, the default password behavior is used.</dd>

<dt>-i, -\\\-inherit  </dt>
<dd>The new role will automatically inherit privileges of roles it is a member of. This is the default.</dd>

<dt>-I, -\\\-no-inherit  </dt>
<dd>The new role will not automatically inherit privileges of roles it is a member of.</dd>

<dt>-l, -\\\-login  </dt>
<dd>The new role will be allowed to log in to HAWQ. This is the default.</dd>

<dt>-L, -\\\-no-login  </dt>
<dd>The new role will not be allowed to log in (a group-level role).</dd>

<dt>-N, -\\\-unencrypted  </dt>
<dd>Does not encrypt the role's password stored in the database. If not specified, the default password behavior is used.</dd>

<dt>-P, -\\\-pwprompt  </dt>
<dd>If given, `createuser` will issue a prompt for the password of the new role. This is not necessary if you do not plan on using password authentication.</dd>

<dt>-r, -\\\-createrole  </dt>
<dd>The new role will be allowed to create new roles (`CREATEROLE` privilege).</dd>

<dt>-R, -\\\-no-createrole  </dt>
<dd>The new role will not be allowed to create new roles. This is the default.</dd>

<dt>-s, -\\\-superuser  </dt>
<dd>The new role will be a superuser.</dd>

<dt>-S, -\\\-no-superuser  </dt>
<dd>The new role will not be a superuser. This is the default.</dd>

**\<connection\_options\>**

<dt>-h, -\\\-host \<host\> </dt>
<dd>The host name of the machine on which the HAWQ master database server is running. If not specified, reads from the environment variable `PGHOST` or defaults to localhost.</dd>

<dt>-p, -\\\-port \<port\>  </dt>
<dd>The TCP port on which the HAWQ master database server is listening for connections. If not specified, reads from the environment variable `PGPORT` or defaults to 5432.</dd>

<dt>-U, -\\\-username \<username\>  </dt>
<dd>The database role name to connect as. If not specified, reads from the environment variable `PGUSER` or defaults to the current system role name.</dd>

<dt>-w, -\\\-no-password  </dt>
<dd>Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a `.pgpass` file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.</dd>

<dt>-W, -\\\-password  </dt>
<dd>Force a password prompt.</dd>

**Other Options**

<dt>-\\\-help  </dt>
<dd>Displays the online help.</dd>

<dt>-\\\-version  </dt>
<dd>Displays the version of this utility.</dd>

## <a id="topic1__section6"></a>Examples

Create a role named `joe` using the default options:

``` shell
$ createuser joe
Shall the new role be a superuser? (y/n) n
Shall the new role be allowed to create databases? (y/n) n
Shall the new role be allowed to create more new roles? (y/n) n
CREATE ROLE
```

To create the same role `joe` using connection options and avoiding the prompts and taking a look at the underlying command:

``` shell
$ createuser -h masterhost -p 54321 -S -D -R -e joe
CREATE ROLE joe NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT 
LOGIN;
CREATE ROLE
```

To create the role `joe` as a superuser, and assign password `admin123` immediately:

``` shell
$ createuser -P -s -e joe
Enter password for new role: admin123
Enter it again: admin123
CREATE ROLE joe PASSWORD 'admin123' SUPERUSER CREATEDB 
CREATEROLE INHERIT LOGIN;
CREATE ROLE
```

In the above example, the new password is not actually echoed when typed, but we show what was typed for clarity. However the password will appear in the echoed command, as illustrated if the `-e` option is used.
