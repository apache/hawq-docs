---
title: Overview of HAWQ Authorization
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

Native HAWQ authorization provides SQL standard authorization at the database and table level for specific users/roles using the `GRANT` and `REVOKE` SQL commands. HAWQ integration with Ranger provides policy-based authorization, enabling you to identify the conditions under which a user and/or group can access individual HAWQ resources, including the operations permitted on those resources.

Native HAWQ and Ranger authorization are mutually exclusive.

Native HAWQ and Ranger authorization share `pg_hba.conf`-based user authentication. Native HAWQ authorization is used for certain database operations, even when Ranger is enabled. Additionally, HAWQ always verifies superuser privileges.


## <a id="pghbaconf"></a> pg_hba.conf
The `pg_hba.conf` file on the HAWQ master node identifies the users you permit to access the HAWQ cluster, and the hosts from which the access may be initiated. This authentication is the first line of defense for both HAWQ-Native and HAWQ-Ranger authorization.


## <a id="alwaysnative"></a> HAWQ Native Authorization
HAWQ *always* employs its native authorization for operations on its catalog. HAWQ also uses only native authorization for the following HAWQ operations, *even when Ranger is enabled*. These operations are available to superusers and may be available those non-admin users to which access was specifically configured:

- operations on HAWQ catalog
- `CREATE CAST` command when function is NULL
- `CREATE DATABASE`, `DROP DATABASE`, `createdb`, `dropdb`
- `hawq filespace` management tool
- `CREATE`, `DROP`, or `ALTER` commands for resource queues
- `CREATE ROLE`, `DROP ROLE`, `SET ROLE`, `createuser`, `dropuser`
- `CREATE TABLESPACE`, `DROP TABLESPACE` (Ranger does manage authorization for creating tables and indexes _within_ an existing tablespace.)
- HAWQ catalog-related built-in functions such as pg\_logdir\_ls, pg\_ls\_dir, pg\_read\_file, pg\_reload\_conf, pg\_rotate\_logfile, pg\_signal\_backend, pg\_start\_backup,  pg\_stat\_file, pg\_stat\_get\_activity, pg\_stat\_get\_backend\_activity\_start, pg\_stat\_get\_backend\_activity, pg\_stat\_get\_backend\_client\_addr, pg\_stat\_get\_backend\_client\_port, pg\_stat\_get\_backend\_start, pg\_stat\_get\_backend\_waiting, pg\_stop\_backup, pg\_switch\_xlog, and pg\_stat\_reset.


The following SQL operations do not require any authorization checks:

- `DEALLOCATE`
- `SET`, `RESET`


## <a id="rangersuperuser"></a> Ranger Authorization
When Ranger authorization is enabled, HAWQ uses Ranger policies to determine access to all user database objects, apart from the operations listed above. HAWQ denies a user operation if no policy exists to provide the necessary permissions for the requesting user to access the specific resource(s). 

In cases where an operation requires super-user privileges, HAWQ first performs a super-user check, and then requests the Ranger policy check. Operations that require super-user checks include:

- `CREATE`, `DROP`, or `ALTER` commands that involve a foreign-data wrapper
- `CREATE LANGUAGE` and `DROP LANGUAGE` for non-built-in languages
- `CREATE FUNCTION` command for untrusted languages
- `CREATE EXTERNAL TABLE` commands that include the `EXECUTE` clause
- `CREATE OPERATOR CLASS` command
- `COPY` command. Using `COPY` is always limited to the super-user. When Ranger policy management is enabled, the super-user must have `SELECT` or `INSERT` privileges on a table in order to `COPY` from or to that table.


## <a id="authalgorithm"></a> Access Check Summary

When determining if a database operation is supported for a specific user, HAWQ:

1. Confirms user access allowed by pg_hba.conf file.
2. Determines if the operation requires superuser access, and if so, verifies the requesting user has such privileges.
3. Determines if the operation requires native HAWQ authorization.
4. Determines if Ranger authorization for HAWQ is enabled.
4. Performs a HAWQ Native authorization check if required or if Ranger is not enabled  **OR**  Performs a HAWQ Ranger policy check.
