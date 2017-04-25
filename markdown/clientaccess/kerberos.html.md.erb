---
title: Using Kerberos Authentication
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

**Note:** The following steps for enabling Kerberos *are not required* if you install HAWQ using Ambari.

You can control access to HAWQ with a Kerberos authentication server.

HAWQ supports the Generic Security Service Application Program Interface \(GSSAPI\) with Kerberos authentication. GSSAPI provides automatic authentication \(single sign-on\) for systems that support it. You specify the HAWQ users \(roles\) that require Kerberos authentication in the HAWQ configuration file `pg_hba.conf`. The login fails if Kerberos authentication is not available when a role attempts to log in to HAWQ.

Kerberos provides a secure, encrypted authentication service. It does not encrypt data exchanged between the client and database and provides no authorization services. To encrypt data exchanged over the network, you must use an SSL connection. To manage authorization for access to HAWQ databases and objects such as schemas and tables, you use settings in the `pg_hba.conf` file and privileges given to HAWQ users and roles within the database. For information about managing authorization privileges, see [Managing Roles and Privileges](roles_privs.html).

For more information about Kerberos, see [http://web.mit.edu/kerberos/](http://web.mit.edu/kerberos/).

## <a id="kerberos_prereq"></a>Requirements for Using Kerberos with HAWQ 

The following items are required for using Kerberos with HAWQ:

-   Kerberos Key Distribution Center \(KDC\) server using the `krb5-server` library
-   Kerberos version 5 `krb5-libs` and `krb5-workstation` packages installed on the HAWQ master host
-   System time on the Kerberos server and HAWQ master host must be synchronized. \(Install Linux `ntp` package on both servers.\)
-   Network connectivity between the Kerberos server and the HAWQ master
-   Java 1.7.0\_17 or later is required to use Kerberos-authenticated JDBC on Red Hat Enterprise Linux 6.x
-   Java 1.6.0\_21 or later is required to use Kerberos-authenticated JDBC on Red Hat Enterprise Linux 4.x or 5.x

## <a id="nr166539"></a>Enabling Kerberos Authentication for HAWQ 

Complete the following tasks to set up Kerberos authentication with HAWQ:

1.  Verify your system satisfies the prequisites for using Kerberos with HAWQ. See [Requirements for Using Kerberos with HAWQ](#kerberos_prereq).
2.  Set up, or identify, a Kerberos Key Distribution Center \(KDC\) server to use for authentication. See [Install and Configure a Kerberos KDC Server](#task_setup_kdc).
3.  Create and deploy principals for your HDFS cluster, and ensure that kerberos authentication is enabled and functioning for all HDFS services. See your Hadoop documentation for additional details.
4.  In a Kerberos database on the KDC server, set up a Kerberos realm and principals on the server. For HAWQ, a principal is a HAWQ role that uses Kerberos authentication. In the Kerberos database, a realm groups together Kerberos principals that are HAWQ roles.
5.  Create Kerberos keytab files for HAWQ. To access HAWQ, you create a service key known only by Kerberos and HAWQ. On the Kerberos server, the service key is stored in the Kerberos database.

    On the HAWQ master, the service key is stored in key tables, which are files known as keytabs. The service keys are usually stored in the keytab file `/etc/krb5.keytab`. This service key is the equivalent of the service's password, and must be kept secure. Data that is meant to be read-only by the service is encrypted using this key.

6.  Install the Kerberos client packages and the keytab file on HAWQ master.
7.  Create a Kerberos ticket for `gpadmin` on the HAWQ master node using the keytab file. The ticket contains the Kerberos authentication credentials that grant access to the HAWQ.

With Kerberos authentication configured on the HAWQ, you can use Kerberos for PSQL and JDBC.

[Set up HAWQ with Kerberos for PSQL](#topic6)

[Set up HAWQ with Kerberos for JDBC](#topic9)

## <a id="task_setup_kdc"></a>Install and Configure a Kerberos KDC Server 

Steps to set up a Kerberos Key Distribution Center \(KDC\) server on a Red Hat Enterprise Linux host for use with HAWQ.

Follow these steps to install and configure a Kerberos Key Distribution Center \(KDC\) server on a Red Hat Enterprise Linux host.

1.  Install the Kerberos server packages:

    ```
    sudo yum install krb5-libs krb5-server krb5-workstation
    ```

2.  Edit the `/etc/krb5.conf` configuration file. The following example shows a Kerberos server with a default `KRB.EXAMPLE.COM` realm.

    ```
    [logging]
     default = FILE:/var/log/krb5libs.log
     kdc = FILE:/var/log/krb5kdc.log
     admin_server = FILE:/var/log/kadmind.log

    [libdefaults]
     default_realm = KRB.EXAMPLE.COM
     dns_lookup_realm = false
     dns_lookup_kdc = false
     ticket_lifetime = 24h
     renew_lifetime = 7d
     forwardable = true
     default_tgs_enctypes = aes128-cts des3-hmac-sha1 des-cbc-crc des-cbc-md5
     default_tkt_enctypes = aes128-cts des3-hmac-sha1 des-cbc-crc des-cbc-md5
     permitted_enctypes = aes128-cts des3-hmac-sha1 des-cbc-crc des-cbc-md5

    [realms]
     KRB.EXAMPLE.COM = {
      kdc = kerberos-gpdb:88
      admin_server = kerberos-gpdb:749
      default_domain = kerberos-gpdb
     }

    [domain_realm]
     .kerberos-gpdb = KRB.EXAMPLE.COM
     kerberos-gpdb = KRB.EXAMPLE.COM

    [appdefaults]
     pam = {
        debug = false
        ticket_lifetime = 36000
        renew_lifetime = 36000
        forwardable = true
        krb4_convert = false
       }
    ```

    The `kdc` and `admin_server` keys in the `[realms]` section specify the host \(`kerberos-gpdb`\) and port where the Kerberos server is running. IP numbers can be used in place of host names.

    If your Kerberos server manages authentication for other realms, you would instead add the `KRB.EXAMPLE.COM` realm in the `[realms]` and `[domain_realm]` section of the `kdc.conf` file. See the [Kerberos documentation](http://web.mit.edu/kerberos/krb5-latest/doc/) for information about the `kdc.conf` file.

3.  To create a Kerberos KDC database, run the `kdb5_util`.

    ```
    kdb5_util create -s
    ```

    The `kdb5_util`create option creates the database to store keys for the Kerberos realms that are managed by this KDC server. The `-s` option creates a stash file. Without the stash file, every time the KDC server starts it requests a password.

4.  Add an administrative user to the KDC database with the `kadmin.local` utility. Because it does not itself depend on Kerberos authentication, the `kadmin.local` utility allows you to add an initial administrative user to the local Kerberos server. To add the user `gpadmin` as an administrative user to the KDC database, run the following command:

    ```
    kadmin.local -q "addprinc gpadmin/admin"
    ```

    Most users do not need administrative access to the Kerberos server. They can use `kadmin` to manage their own principals \(for example, to change their own password\). For information about `kadmin`, see the [Kerberos documentation](http://web.mit.edu/kerberos/krb5-latest/doc/).

5.  If needed, edit the `/var/kerberos/krb5kdc/kadm5.acl` file to grant the appropriate permissions to `gpadmin`.
6.  Start the Kerberos daemons:

    ```
    /sbin/service krb5kdc start
    /sbin/service kadmin start
    ```

7.  To start Kerberos automatically upon restart:

    ```
    /sbin/chkconfig krb5kdc on
    /sbin/chkconfig kadmin on
    ```


## <a id="task_m43_vwl_2p"></a>Create HAWQ Roles in the KDC Database 

Add principals to the Kerberos realm for HAWQ.

Start `kadmin.local` in interactive mode, then add two principals to the HAWQ Realm.

1.  Start `kadmin.local` in interactive mode:

    ```
    kadmin.local
    ```

2.  Add principals:

    ```
    kadmin.local: addprinc gpadmin/kerberos-gpdb@KRB.EXAMPLE.COM
    kadmin.local: addprinc postgres/master.test.com@KRB.EXAMPLE.COM
    ```

    The `addprinc` commands prompt for passwords for each principal. The first `addprinc` creates a HAWQ user as a principal, `gpadmin/kerberos-gpdb`. The second `addprinc` command creates the `postgres` process on the HAWQ master host as a principal in the Kerberos KDC. This principal is required when using Kerberos authentication with HAWQ.

3.  Create a Kerberos keytab file with `kadmin.local`. The following example creates a keytab file `gpdb-kerberos.keytab` in the current directory with authentication information for the two principals.

    ```
    kadmin.local: xst -k gpdb-kerberos.keytab
        gpadmin/kerberos-gpdb@KRB.EXAMPLE.COM
        postgres/master.test.com@KRB.EXAMPLE.COM
    ```

    You will copy this file to the HAWQ master host.

4.  Exit `kadmin.local` interactive mode with the `quit` command:`kadmin.local: quit`

## <a id="topic6"></a>Install and Configure the Kerberos Client 

Steps to install the Kerberos client on the HAWQ master host.

Install the Kerberos client libraries on the HAWQ master and configure the Kerberos client.

1.  Install the Kerberos packages on the HAWQ master.

    ```
    sudo yum install krb5-libs krb5-workstation
    ```

2.  Ensure that the `/etc/krb5.conf` file is the same as the one that is on the Kerberos server.
3.  Copy the `gpdb-kerberos.keytab` file that was generated on the Kerberos server to the HAWQ master host.
4.  Remove any existing tickets with the Kerberos utility `kdestroy`. Run the utility as root.

    ```
    sudo kdestroy
    ```

5.  Use the Kerberos utility `kinit` to request a ticket using the keytab file on the HAWQ master for `gpadmin/kerberos-gpdb@KRB.EXAMPLE.COM`. The `-t` option specifies the keytab file on the HAWQ master.

    ```
    # kinit -k -t gpdb-kerberos.keytab gpadmin/kerberos-gpdb@KRB.EXAMPLE.COM
    ```

6.  Use the Kerberos utility `klist` to display the contents of the Kerberos ticket cache on the HAWQ master. The following is an example:

    ```screen
    # klist
    Ticket cache: FILE:/tmp/krb5cc_108061
    Default principal: gpadmin/kerberos-gpdb@KRB.EXAMPLE.COM
    Valid starting     Expires            Service principal
    03/28/13 14:50:26  03/29/13 14:50:26  krbtgt/KRB.EXAMPLE.COM     @KRB.EXAMPLE.COM
        renew until 03/28/13 14:50:26
    ```


### <a id="topic7"></a>Set up HAWQ with Kerberos for PSQL 

Configure a HAWQ to use Kerberos.

After you have set up Kerberos on the HAWQ master, you can configure HAWQ to use Kerberos. For information on setting up the HAWQ master, see [Install and Configure the Kerberos Client](#topic6).

1.  Create a HAWQ administrator role in the database `template1` for the Kerberos principal that is used as the database administrator. The following example uses `gpamin/kerberos-gpdb`.

    ``` bash
    $ psql template1 -c 'CREATE ROLE "gpadmin/kerberos-gpdb" LOGIN SUPERUSER;'

    ```

    The role you create in the database `template1` will be available in any new HAWQ that you create.

2.  Modify `hawq-site.xml` to specify the location of the keytab file. For example, adding this line to the `hawq-site.xml` specifies the folder /home/gpadmin as the location of the keytab filegpdb-kerberos.keytab.

    ``` xml
      <property>
          <name>krb_server_keyfile</name>
          <value>/home/gpadmin/gpdb-kerberos.keytab</value>
      </property>
    ```

3.  Modify the HAWQ file `pg_hba.conf` to enable Kerberos support. Then restart HAWQ \(`hawq restart -a`\). For example, adding the following line to `pg_hba.conf` adds GSSAPI and Kerberos support. The value for `krb_realm` is the Kerberos realm that is used for authentication to HAWQ.

    ```
    host all all 0.0.0.0/0 gss include_realm=0 krb_realm=KRB.EXAMPLE.COM
    ```

    For information about the `pg_hba.conf` file, see [The pg\_hba.conf file](http://www.postgresql.org/docs/9.0/static/auth-pg-hba-conf.html) in the Postgres documentation.

4.  Create a ticket using `kinit` and show the tickets in the Kerberos ticket cache with `klist`.
5.  As a test, log in to the database as the `gpadmin` role with the Kerberos credentials `gpadmin/kerberos-gpdb`:

    ``` bash
    $ psql -U "gpadmin/kerberos-gpdb" -h master.test template1
    ```

    A username map can be defined in the `pg_ident.conf` file and specified in the `pg_hba.conf` file to simplify logging into HAWQ. For example, this `psql` command logs into the default HAWQ on `mdw.proddb` as the Kerberos principal `adminuser/mdw.proddb`:

    ``` bash
    $ psql -U "adminuser/mdw.proddb" -h mdw.proddb
    ```

    If the default user is `adminuser`, the `pg_ident.conf` file and the `pg_hba.conf` file can be configured so that the `adminuser` can log in to the database as the Kerberos principal `adminuser/mdw.proddb` without specifying the `-U` option:

    ``` bash
    $ psql -h mdw.proddb
    ```

    The `pg_ident.conf` file defines the username map. This file is located in the HAWQ master data directory (identified by the `hawq_master_directory` property value in `hawq-site.xml`):

    ```
    # MAPNAME   SYSTEM-USERNAME        GP-USERNAME
    mymap       /^(.*)mdw\.proddb$     adminuser
    ```

    The map can be specified in the `pg_hba.conf` file as part of the line that enables Kerberos support:

    ```
    host all all 0.0.0.0/0 krb5 include_realm=0 krb_realm=proddb map=mymap
    ```

    For more information about specifying username maps see [Username maps](http://www.postgresql.org/docs/9.0/static/auth-username-maps.html) in the Postgres documentation.

6.  If a Kerberos principal is not a HAWQ user, a message similar to the following is displayed from the `psql` command line when the user attempts to log in to the database:

    ```
    psql: krb5_sendauth: Bad response
    ```

    The principal must be added as a HAWQ user.


### <a id="topic9"></a>Set up HAWQ with Kerberos for JDBC 

Enable Kerberos-authenticated JDBC access to HAWQ.

You can configure HAWQ to use Kerberos to run user-defined Java functions.

1.  Ensure that Kerberos is installed and configured on the HAWQ master. See [Install and Configure the Kerberos Client](#topic6).
2.  Create the file `.java.login.config` in the folder `/home/gpadmin` and add the following text to the file:

    ```
    pgjdbc {
      com.sun.security.auth.module.Krb5LoginModule required
      doNotPrompt=true
      useTicketCache=true
      debug=true
      client=true;
    };
    ```

3.  Create a Java application that connects to HAWQ using Kerberos authentication. The following example database connection URL uses a PostgreSQL JDBC driver and specifies parameters for Kerberos authentication:

    ```
    jdbc:postgresql://mdw:5432/mytest?kerberosServerName=postgres&jaasApplicationName=pgjdbc&user=gpadmin/kerberos-gpdb
    ```

    The parameter names and values specified depend on how the Java application performs Kerberos authentication.

4.  Test the Kerberos login by running a sample Java application from HAWQ.
