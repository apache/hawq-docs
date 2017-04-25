---
title: Using HAWQ Native Authorization
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

The HAWQ authorization mechanism stores roles and permissions to access database objects in the database and is administered using SQL statements or command-line utilities.

HAWQ manages database access permissions using *roles*. The concept of roles subsumes the concepts of *users* and *groups*. A role can be a database user, a group, or both. Roles can own database objects \(for example, tables\) and can assign privileges on those objects to other roles to control access to the objects. Roles can be members of other roles, thus a member role can inherit the object privileges of its parent role.

Every HAWQ system contains a set of database roles \(users and groups\). Those roles are separate from the users and groups managed by the operating system on which the server runs. However, for convenience you may want to maintain a relationship between operating system user names and HAWQ role names, since many of the client applications use the current operating system user name as the default.

In HAWQ, users log in and connect through the master instance, which then verifies their role and access privileges. The master then issues commands to the segment instances behind the scenes as the currently logged in role.

Roles are defined at the system level, meaning they are valid for all databases in the system.

In order to bootstrap the HAWQ system, a freshly initialized system always contains one predefined *superuser* role \(also referred to as the system user\). This role will have the same name as the operating system user that initialized the HAWQ system. Customarily, this role is named `gpadmin`. In order to create more roles you first have to connect as this initial role.

## <a id="topic2"></a>Security Best Practices for Roles and Privileges 

-   **Secure the gpadmin system user.** HAWQ requires a UNIX user id to install and initialize the HAWQ system. This system user is referred to as `gpadmin` in the HAWQ documentation. This `gpadmin` user is the default database superuser in HAWQ, as well as the file system owner of the HAWQ installation and its underlying data files. This default administrator account is fundamental to the design of HAWQ. The system cannot run without it, and there is no way to limit the access of this gpadmin user id. Use roles to manage who has access to the database for specific purposes. You should only use the `gpadmin` account for system maintenance tasks such as expansion and upgrade. Anyone who logs on to a HAWQ host as this user id can read, alter or delete any data; specifically system catalog data and database access rights. Therefore, it is very important to secure the gpadmin user id and only provide access to essential system administrators. Administrators should only log in to HAWQ as `gpadmin` when performing certain system maintenance tasks \(such as upgrade or expansion\). Database users should never log on as `gpadmin`, and ETL or production workloads should never run as `gpadmin`.
-   **Assign a distinct role to each user that logs in.** For logging and auditing purposes, each user that is allowed to log in to HAWQ should be given their own database role. For applications or web services, consider creating a distinct role for each application or service. See [Creating New Roles \(Users\)](#topic3).
-   **Use groups to manage access privileges.** See [Role Membership](#topic5).
-   **Limit users who have the SUPERUSER role attribute.** Roles that are superusers bypass all access privilege checks in HAWQ, as well as resource queuing. Only system administrators should be given superuser rights. See [Altering Role Attributes](#topic4).

## <a id="topic3"></a>Creating New Roles \(Users\) 

A user-level role is considered to be a database role that can log in to the database and initiate a database session. Therefore, when you create a new user-level role using the `CREATE ROLE` command, you must specify the `LOGIN` privilege. For example:

``` sql
=# CREATE ROLE jsmith WITH LOGIN;
```

A database role may have a number of attributes that define what sort of tasks that role can perform in the database. You can set these attributes when you create the role, or later using the `ALTER ROLE` command. See [Table 1](#iq139556) for a description of the role attributes you can set.

### <a id="topic4"></a>Altering Role Attributes 

A database role may have a number of attributes that define what sort of tasks that role can perform in the database.

<a id="iq139556"></a>

|Attributes|Description|
|----------|-----------|
|SUPERUSER &#124; NOSUPERUSER|Determines if the role is a superuser. You must yourself be a superuser to create a new superuser. NOSUPERUSER is the default.|
|CREATEDB &#124; NOCREATEDB|Determines if the role is allowed to create databases. NOCREATEDB is the default.|
|CREATEROLE &#124; NOCREATEROLE|Determines if the role is allowed to create and manage other roles. NOCREATEROLE is the default.|
|INHERIT &#124; NOINHERIT|Determines whether a role inherits the privileges of roles it is a member of. A role with the INHERIT attribute can automatically use whatever database privileges have been granted to all roles it is directly or indirectly a member of. INHERIT is the default.|
|LOGIN &#124; NOLOGIN|Determines whether a role is allowed to log in. A role having the LOGIN attribute can be thought of as a user. Roles without this attribute are useful for managing database privileges \(groups\). NOLOGIN is the default.|
|CONNECTION LIMIT *connlimit*|If role can log in, this specifies how many concurrent connections the role can make. -1 \(the default\) means no limit.|
|PASSWORD '*password*'|Sets the role's password. If you do not plan to use password authentication you can omit this option. If no password is specified, the password will be set to null and password authentication will always fail for that user. A null password can optionally be written explicitly as PASSWORD NULL.|
|ENCRYPTED &#124; UNENCRYPTED|Controls whether the password is stored encrypted in the system catalogs. The default behavior is determined by the configuration parameter `password_encryption` \(currently set to md5, for SHA-256 encryption, change this setting to password\). If the presented password string is already in encrypted format, then it is stored encrypted as-is, regardless of whether ENCRYPTED or UNENCRYPTED is specified \(since the system cannot decrypt the specified encrypted password string\). This allows reloading of encrypted passwords during dump/restore.|
|VALID UNTIL '*timestamp*'|Sets a date and time after which the role's password is no longer valid. If omitted the password will be valid for all time.|
|RESOURCE QUEUE *queue\_name*|Assigns the role to the named resource queue for workload management. Any statement that role issues is then subject to the resource queue's limits. Note that the RESOURCE QUEUE attribute is not inherited; it must be set on each user-level \(LOGIN\) role.|
|DENY \{deny\_interval &#124; deny\_point\}|Restricts access during an interval, specified by day or day and time. For more information see [Time-based Authentication](#topic13).|

You can set these attributes when you create the role, or later using the `ALTER ROLE` command. For example:

``` sql
=# ALTER ROLE jsmith WITH PASSWORD 'passwd123';
=# ALTER ROLE admin VALID UNTIL 'infinity';
=# ALTER ROLE jsmith LOGIN;
=# ALTER ROLE jsmith RESOURCE QUEUE adhoc;
=# ALTER ROLE jsmith DENY DAY 'Sunday';
```

## <a id="topic5"></a>Role Membership 

It is frequently convenient to group users together to ease management of object privileges: that way, privileges can be granted to, or revoked from, a group as a whole. In HAWQ this is done by creating a role that represents the group, and then granting membership in the group role to individual user roles.

Use the `CREATE ROLE` SQL command to create a new group role. For example:

``` sql
=# CREATE ROLE admin CREATEROLE CREATEDB;
```

Once the group role exists, you can add and remove members \(user roles\) using the `GRANT` and `REVOKE` commands. For example:

``` sql
=# GRANT admin TO john, sally;
=# REVOKE admin FROM bob;
```

For managing object privileges, you would then grant the appropriate permissions to the group-level role only \(see [Table 2](#iq139925)\). The member user roles then inherit the object privileges of the group role. For example:

``` sql
=# GRANT ALL ON TABLE mytable TO admin;
=# GRANT ALL ON SCHEMA myschema TO admin;
=# GRANT ALL ON DATABASE mydb TO admin;
```

The role attributes `LOGIN`, `SUPERUSER`, `CREATEDB`, and `CREATEROLE` are never inherited as ordinary privileges on database objects are. User members must actually `SET ROLE` to a specific role having one of these attributes in order to make use of the attribute. In the above example, we gave `CREATEDB` and `CREATEROLE` to the `admin` role. If `sally` is a member of `admin`, she could issue the following command to assume the role attributes of the parent role:

``` sql
=> SET ROLE admin;
```

## <a id="topic6"></a>Managing Object Privileges 

When an object \(table, view, sequence, database, function, language, schema, or tablespace\) is created, it is assigned an owner. The owner is normally the role that executed the creation statement. For most kinds of objects, the initial state is that only the owner \(or a superuser\) can do anything with the object. To allow other roles to use it, privileges must be granted. HAWQ supports the following privileges for each object type:

<a id="iq139925"></a>

|Object Type|Privileges|
|-----------|----------|
|Tables, Views, Sequences|SELECT <br/> INSERT <br/> RULE <br/> ALL|
|External Tables|SELECT <br/> RULE <br/> ALL|
|Databases|CONNECT<br/>CREATE<br/>TEMPORARY &#124; TEMP <br/> ALL|
|Functions|EXECUTE|
|Procedural Languages|USAGE|
|Schemas|CREATE <br/> USAGE <br/> ALL|
|Custom Protocol|SELECT <br/> INSERT <br/> RULE </br> ALL|

**Note:** Privileges must be granted for each object individually. For example, granting ALL on a database does not grant full access to the objects within that database. It only grants all of the database-level privileges \(CONNECT, CREATE, TEMPORARY\) to the database itself.

Use the `GRANT` SQL command to give a specified role privileges on an object. For example:

``` sql
=# GRANT INSERT ON mytable TO jsmith;
```

To revoke privileges, use the `REVOKE` command. For example:

``` sql
=# REVOKE ALL PRIVILEGES ON mytable FROM jsmith;
```

You can also use the `DROP OWNED` and `REASSIGN OWNED` commands for managing objects owned by deprecated roles \(Note: only an object's owner or a superuser can drop an object or reassign ownership\). For example:

``` sql
=# REASSIGN OWNED BY sally TO bob;
=# DROP OWNED BY visitor;
```

### <a id="topic7"></a>Simulating Row and Column Level Access Control 

Row-level or column-level access is not supported, nor is labeled security. Row-level and column-level access can be simulated using views to restrict the columns and/or rows that are selected. Row-level labels can be simulated by adding an extra column to the table to store sensitivity information, and then using views to control row-level access based on this column. Roles can then be granted access to the views rather than the base table.

## <a id="topic8"></a>Encrypting Data 

PostgreSQL provides an optional package of encryption/decryption functions called `pgcrypto`, which you can enable in HAWQ.

If you are building HAWQ from source, then you should enable `pgcrypto` support as an option when compiling HAWQ.

The `pgcrypto` functions allow database administrators to store certain columns of data in encrypted form. This adds an extra layer of protection for sensitive data, as data stored in HAWQ in encrypted form cannot be read by users who do not have the encryption key, nor be read directly from the disks.

**Note:** The `pgcrypto` functions run inside the database server, which means that all the data and passwords move between `pgcrypto` and the client application in clear-text. For optimal security, consider also using SSL connections between the client and the HAWQ master server.

## <a id="topic9"></a>Encrypting Passwords 

This technical note outlines how to use a server parameter to implement SHA-256 encrypted password storage. Note that in order to use SHA-256 encryption for storage, the client authentication method must be set to `password` rather than the default, `MD5`. \(See [Encrypting Client/Server Connections](client_auth.html) for more details.\) This means that the password is transmitted in clear text over the network; to avoid this, set up SSL to encrypt the client server communication channel.

### <a id="topic10"></a>Enabling SHA-256 Encryption 

You can set your chosen encryption method system-wide or on a per-session basis. There are three encryption methods available: `SHA-256`, `SHA-256-FIPS`, and `MD5` \(for backward compatibility\). The `SHA-256-FIPS` method requires that FIPS compliant libraries are used.

#### <a id="topic11"></a>System-wide 

You will perform different procedures to set the encryption method (`password_hash_algorithm` server parameter) system-wide depending upon whether you manage your cluster from the command line or use Ambari. If you use Ambari to manage your HAWQ cluster, you must ensure that you update encryption method configuration parameters only via the Ambari Web UI. If you manage your HAWQ cluster from the command line, you will use the `hawq config` command line utility to set encryption method configuration parameters.

If you use Ambari to manage your HAWQ cluster:

1. Set the `password_hash_algorithm` configuration property via the HAWQ service **Configs > Advanced > Custom hawq-site** drop down. Valid values include `SHA-256` \(or `SHA-256-FIPS` to use the FIPS-compliant libraries for SHA-256\).
2. Select **Service Actions > Restart All** to load the updated configuration.

If you manage your HAWQ cluster from the command line:

1.  Log in to the HAWQ master host as a HAWQ administrator and source the file `/usr/local/hawq/greenplum_path.sh`.

    ``` shell
    $ source /usr/local/hawq/greenplum_path.sh
    ```

1. Use the `hawq config` utility to set `password_hash_algorithm` to `SHA-256` \(or `SHA-256-FIPS` to use the FIPS-compliant libraries for SHA-256\):

    ``` shell
    $ hawq config -c password_hash_algorithm -v 'SHA-256'
    ```
        
    Or:
        
    ``` shell
    $ hawq config -c password_hash_algorithm -v 'SHA-256-FIPS'
    ```

2. Reload the HAWQ configuration:

    ``` shell
    $ hawq stop cluster -u
    ```

3.  Verify the setting:

    ``` bash
    $ hawq config -s password_hash_algorithm
    ```

#### <a id="topic12"></a>Individual Session 

To set the `password_hash_algorithm` server parameter for an individual database session:

1.  Log in to your HAWQ instance as a superuser.
2.  Set the `password_hash_algorithm` to `SHA-256` \(or `SHA-256-FIPS` to use the FIPS-compliant libraries for SHA-256\):

    ``` sql
    =# SET password_hash_algorithm = 'SHA-256'
    SET
    ```

    or:

    ``` sql
    =# SET password_hash_algorithm = 'SHA-256-FIPS'
    SET
    ```

3.  Verify the setting:

    ``` sql
    =# SHOW password_hash_algorithm;
    password_hash_algorithm
    ```

    You will see:

    ```
    SHA-256
    ```

    or:

    ```
    SHA-256-FIPS
    ```

    **Example**

    Following is an example of how the new setting works:

4.  Login in as a super user and verify the password hash algorithm setting:

    ``` sql
    =# SHOW password_hash_algorithm
    password_hash_algorithm
    -------------------------------
    SHA-256-FIPS
    ```

5.  Create a new role with password that has login privileges.

    ``` sql
    =# CREATE ROLE testdb WITH PASSWORD 'testdb12345#' LOGIN;
    ```

6.  Change the client authentication method to allow for storage of SHA-256 encrypted passwords:

    Open the `pg_hba.conf` file on the master and add the following line:

    ```
    host all testdb 0.0.0.0/0 password
    ```

7.  Restart the cluster.
8.  Login to the database as user just created `testdb`.

    ``` bash
    $ psql -U testdb
    ```

9.  Enter the correct password at the prompt.
10. Verify that the password is stored as a SHA-256 hash.

    Note that password hashes are stored in `pg_authid.rolpasswod`

    1.  Login as the super user.
    2.  Execute the following:

        ``` sql
        =# SELECT rolpassword FROM pg_authid WHERE rolname = 'testdb';
        Rolpassword
        -----------
        sha256<64 hexidecimal characters>
        ```


## <a id="topic13"></a>Time-based Authentication 

HAWQ enables the administrator to restrict access to certain times by role. Use the `CREATE ROLE` or `ALTER ROLE` commands to specify time-based constraints.
