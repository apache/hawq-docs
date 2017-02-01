---
title: ALTER DATABASE
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

Changes the attributes of a database.

## <a id="alterrole__section2"></a>Synopsis

```pre
ALTER DATABASE <name> SET <parameter> { TO | = } { <value> | DEFAULT } 

ALTER DATABASE <name> RESET <parameter>
```

## <a id="desc"></a>Description

`ALTER DATABASE` changes the attributes of a HAWQ database.

`SET` and `RESET` \<parameter\> changes the session default for a configuration parameter for a HAWQ database. Whenever a new session is subsequently started in that database, the specified value becomes the session default value. The database-specific default overrides whatever setting is present in the server configuration file (`hawq-site.xml`). Only the database owner or a superuser can change the session defaults for a database. Certain parameters cannot be set this way, or can only be set by a superuser.

## <a id="alterrole__section4"></a>Parameters

<dt> \<name\>   </dt>
<dd>The name of the database whose attributes are to be altered.

**Note:** HAWQ reserves the database "hcatalog" for system use. You cannot connect to or alter the system "hcatalog" database.</dd>

<dt> \<parameter\>   </dt>
<dd>Set this database's session default for the specified configuration parameter to the given value. If value is `DEFAULT` or if `RESET` is used, the database-specific setting is removed, so the system-wide default setting will be inherited in new sessions. Use `RESET ALL` to clear all database-specific settings. See [About Server Configuration Parameters](../guc/guc_config.html#topic1) for information about user-settable configuration parameters.</dd>

## <a id="notes"></a>Notes

It is also possible to set a configuration parameter session default for a specific role (user) rather than to a database. Role-specific settings override database-specific ones if there is a conflict. See [ALTER ROLE](ALTER-ROLE.html).

## <a id="examples"></a>Examples

To set the default schema search path for the `mydatabase` database:

```pre
ALTER DATABASE mydatabase SET search_path TO myschema, 
public, pg_catalog;
```

## <a id="compat"></a>Compatibility

The `ALTER DATABASE` statement is a HAWQ extension.

## <a id="see"></a>See Also

[CREATE DATABASE](CREATE-DATABASE.html#topic1), [DROP DATABASE](DROP-DATABASE.html#topic1), [SET](SET.html)


