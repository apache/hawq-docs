---
title: Configuring Kerberos User Authentication for HAWQ
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

When Kerberos authentication is enabled at the user level, HAWQ uses the Generic Security Service Application Program Interface \(GSSAPI\) to provide automatic authentication \(single sign-on\). When HAWQ uses Kerberos user authentication, both the HAWQ server and those HAWQ users \(roles\) that use Kerberos authentication require a principal and a keytab. When a user attempts to log in to HAWQ, the HAWQ server uses its Kerberos principal to connect to the Kerberos server, and presents the user's principal for Kerberos validation. If the user's principal is valid, then login succeeds and the user can access HAWQ. Conversely, the login fails and HAWQ denies access to the user if the principal is not valid.

When HAWQ utilizes Kerberos for user authentication, it uses a single HAWQ server principal to connect to the Kerberos KDC. The format of the HAWQ server principal is `postgres/<FQDN_of_master>@<realm>`, where \<FQDN\_of\_master\> refers to the fully qualified distinguish name of the HAWQ master node.

(You may choose to configure HAWQ user principals before you enable Kerberos user authentication for HAWQ. See [Configuring Kerberos-Authenticated HAWQ Users](#hawq_kerb_user_cfg).)

The procedure to configure Kerberos user authentication for HAWQ includes:

1. Configuring the HAWQ principal:

    1. If you use an MIT Kerberos KDC Server, refer to [Configuring the HAWQ Principals using an MIT KDC Server](#hawq_kerb_cfg_mitkdc).  

    2. If you use an Active Directory Kerberos KDC Server, refer to [Configuring the HAWQ Principal using an AD KDC Server](#hawq_kerb_cfg_adkdc).  

2. [Configuring HAWQ to use Kerberos Authentication](#hawq_kerb_cfg)  
3. [Configuring Kerberos-Authenticated HAWQ Users](#hawq_kerb_user_cfg)  
4. [Authenticating User Access to HAWQ](#hawq_kerb_dbaccess)  

## <a id="hawq_kerb_cfg_mitkdc"></a>Step 1a: Configuring the HAWQ Principals using an MIT KDC Server

Perform the following procedure to configure HAWQ Kerberos and `gpadmin` principals when you are using an MIT KDC server. 

**Note**: Some operations may differ based on whether or not you have configured secure HDFS. These operations are called out below.

1. Log in to the Kerberos KDC server system:

    ``` shell
    $ ssh root@<kdc-server>
    root@kdc-server$ 
    ```

2. Create a keytab entry for the HAWQ server principal using the `kadmin.local` command. Substitute the HAWQ master node fully qualified distinguished hostname and your Kerberos realm. For example:

    ``` shell
    root@kdc-server$ kadmin.local -q "addprinc -randkey postgres/<master>@REALM.DOMAIN"
    ```
    
    The `addprinc` command adds the principal `postgres/<master>` to the KDC managing your \<realm\>.

3. Generate a keytab file for the HAWQ server principal. Provide the same name you used to create the principal.

    **If you have configured Kerberos for your HDFS filesystem**, add the keytab to the HAWQ client HDFS keytab file:
    
    ``` shell
    root@kdc-server$ kadmin.local -q "xst -norandkey -k /etc/security/keytabs/hawq.service.keytab postgres/<master>@REALM.DOMAIN"
    ```
    
    **Otherwise**, generate a new file for the keytab:

    ``` shell
    root@kdc-server$ kadmin.local -q "xst -norandkey -k hawq-krb5.keytab postgres/<master>@REALM.DOMAIN"
    ```

4. Use the `klist` command to view the key you just generated:

    ``` shell
    root@kdc-server$ klist -ket ./hawq-krb5.keytab
    ```
    
    Or:
    
    ``` shell
    root@kdc-server$ klist -ket /etc/security/keytabs/hawq.service.keytab
    ```
    
    The `-ket` option lists the keytabs and encryption types in the identified key file.

5. When you enable Kerberos user authentication for HAWQ, you must create a Kerberos principal for `gpadmin` or another HAWQ administrative user. Create a Kerberos principal for the HAWQ `gpadmin` administrative role, substituting your Kerberos realm. For example:

    ``` shell
    root@kdc-server$ kadmin.local -q "addprinc -pw changeme gpadmin@REALM.DOMAIN"
    ```
    
    This `addprinc` command adds the principal `gpadmin` to the Kerberos KDC managing your \<realm\>. When you invoke `kadmin.local` as specified in the example above, `gpadmin` will be required to provide the password identified by the `-pw` option when authenticating. Alternatively, you can create a keytab file for the `gpadmin` principal and distribute the file to HAWQ client nodes.

6. Copy the file in which you added the `postgres/<master>@<realm>` keytab to the HAWQ master node:

    ``` shell
    root@kdc-server$ scp ./hawq-krb5.keytab gpadmin@<master>:/home/gpadmin/
    ```
    
    Or:
    
    ``` shell
    root@kdc-server$ scp /etc/security/keytabs/hawq.service.keytab gpadmin@<master>:/etc/security/keytabs/hawq.service.keytab
    ```

## <a id="hawq_kerb_cfg_adkdc"></a>Step 1b: Configuring the HAWQ Principal using an AD KDC Server

Perform the following procedure to configure a HAWQ Kerberos principal when you are using an AD KDC server.

1. Log on to the Windows Active Directory Kerberos KDC server system as a user with administrator privileges.

2. From the **Start** menu, select **Control Panel > Administrative Tools > Active Directory Users and Computers**. (If the **Active Directory Users and Computers** menu item is not available, the Active Directory service may not have been correctly installed.)

    The **Active Directory Users and Computers** window displays.

3. When you enable Kerberos user authentication for HAWQ, you must create a Kerberos principal for the `gpadmin` HAWQ administrative user. Use the left pane tree view to navigate to your Kerberos \<realm\> **Managed Service Accounts** folder, right-click, and select **New > User** to create a user with this name.

    The **New Object - User** wizard displays.
   
4. Fill in the **New Object - User** fields:

    **First name:**  gpadmin  
    **User logon name:**  gpadmin
    
5. Click **Next** to advance to the next screen.

6. Add and confirm the password. Be sure to enable the **Password never expires** checkbox.

7. Click **Next**, and then **Finish** to complete creation of the `gpadmin` user.

8. Open an administrative terminal window or command prompt session on the Windows AD KDC server system. Be sure to select **Run as administrator -> Yes**.

9. Add a Service Name Principal (SNP) for the `gpadmin` account you just created. Substitute the fully qualified distinguished name of your HAWQ master node. This hostname must be resolvable from the Windows AD KDC server. For example:

    ``` shell
    PS C:\Users\Administrator> setspn -A postgres/<master> gpadmin
    ```
    
    The `setspn` command adds the principal `postgres/<master>` to the KDC managing your \<realm\>.

10. Create a keytab file for the `postgres/<master>` SPN using the `ktpass` command. Substitute the HAWQ master node fully qualified distinguished hostname and your Kerberos realm. For example:

    ```shell
    PS C:\Users\Administrator> ktpass -princ postgres/<master>@<realm> -pass changeme -mapuser gpadmin -crypto ALL -ptype KRB5_NT_PRINCIPAL -out hawq-krb5.keytab -kvno 0
    ```

    The `ktpass` command generates a keytab file named `hawq-krb5.keytab`.

11. Copy the keytab file to the HAWQ master node.


## <a id="hawq_kerb_cfg"></a>Step 2: Configuring HAWQ to use Kerberos Authentication

Perform the following procedure to configure Kerberos user authentication for HAWQ. You will perform operations on the HAWQ \<master\> node. 

1. Log in to the HAWQ master node as the `gpadmin` user and set up the HAWQ environment:

    ``` shell
    $ ssh gpadmin@<master>
    gpadmin@master$ . /usr/local/hawq/greenplum_path.sh
    ```
    
2. If you copied the `hawq-krb5.keytab` file, verify the ownership and mode of this file:

    ``` shell
    gpadmin@master$ chown gpadmin:gpadmin /home/gpadmin/hawq-krb5.keytab
    gpadmin@master$ chmod 400 /home/gpadmin/hawq-krb5.keytab
    ```

    The HAWQ server keytab file must be readable (and preferably only readable) by the HAWQ `gpadmin` administrative account.

3. Add a `pg_hba.conf` entry that mandates Kerberos authentication for HAWQ. The `pg_hba.conf` file resides in the directory specified by the `hawq_master_directory` server configuration parameter value. For example, add:

    ``` pre
    host all all 0.0.0.0/0 gss include_realm=0 krb_realm=REALM.DOMAIN
    ``` 

    This `pg_hba.conf` entry specifies that any remote access (i.e. from any user on any remote host) to HAWQ must be authenticated through the Kerberos realm named `REALM.DOMAIN`.
   
    **Note**: Place the Kerberos entry in the appropriate location in the `pg_hba.conf` file. For example, you may choose to retain `pg_hba.conf` entries for the `gpadmin` user that grant `trust` or `ident` authentication for local connections. Locate the Kerberos entry after these line(s). Refer to [Configuring Client Authentication](client_auth.html) for additional information about the `pg_hba.conf` file.

4. Update the HAWQ configuration and restart your cluster. You will perform different procedures if you manage your cluster from the command line or use Ambari to manage your cluster.

    **Note**: After you restart your hawq cluster, Kerberos user authentication is enabled for HAWQ, and all users, including `gpadmin`, must authenticate before performing any HAWQ operations.

    1. If you manage your cluster using Ambari or are employing a Windows Active Directory KDC server:
    
        1.  Login in to the Ambari UI from a supported web browser.

        2. Navigate to the **HAWQ** service, **Configs > Advanced** tab and expand the **Custom hawq-site** drop down.

        3. Set the `krb_server_keyfile` path value to the new keytab file location, `/home/gpadmin/hawq-krb5.keytab`.

        4. **Save** this configuration change and then select the now orange **Restart > Restart All Affected** menu button to restart your HAWQ cluster.

        5. Exit the Ambari UI.  
    
    2. If you manage your cluster from the command line:
    
        1.  Update the `krb_server_keyfile` configuration parameter:

            ``` shell
            gpadmin@master$ hawq config -c krb_server_keyfile -v '/home/gpadmin/hawq-krb5.keytab'
            GUC krb_server_keyfile already exist in hawq-site.xml
            Update it with value: /home/gpadmin/hawq-krb5.keytab
            GUC      : krb_server_keyfile
            Value    : /home/gpadmin/hawq-krb5.keytab
            ```

        2.  Restart your HAWQ cluster:

            ``` shell
            gpadmin@master$ hawq restart cluster
            ```

5. When Kerberos user authentication is enabled for HAWQ, all users, including the `gpadmin` administrative user, must request a ticket to authenticate before performing HAWQ operations. Generate a ticket for `gpadmin` on the HAWQ master node. You may be required to enter a password if you specified one when you created the principal. For example:

    ``` shell
    gpadmin@master$ kinit gpadmin@<realm>
    ```

    **Note**: If you are using an Active Directory KDC server and the `kinit` command fails with the error "Preauthentication failed while getting initial credentials", navigate to the `gpadmin` **Account options** view on the Windows AD server system and enable the **Do not require Kerberos preauthentication** checkbox.

    See [Authenticate User Access to HAWQ](#hawq_kerb_dbaccess) for more information about requesting and generating Kerberos tickets. 


## <a id="hawq_kerb_user_cfg"></a>Step 3: Configuring Kerberos-Authenticated HAWQ Users

You must configure HAWQ user principals for Kerberos. The first component of a HAWQ user principal must be the HAWQ user/role name:

``` pre
<hawq-user>@<realm>
```

This procedure includes:

- Identifying an existing HAWQ role or creating a new HAWQ role for each user you want to authenticate with Kerberos
- Creating a Kerberos principal for each role
- Optionally generating and distributing a keytab file to all HAWQ clients from which you will access HAWQ as the new role


### <a id="hawq_kerb_user_cfg_proc" class="no-quick-link"></a>Procedure 

Perform the following steps to configure Kerberos authentication for specific HAWQ users. You will perform operations on both the HAWQ \<master\> and the \<kdc-server\> nodes.

1. Log in to the HAWQ master node as the `gpadmin` user and set up your HAWQ environment:

    ``` shell
    $ ssh gpadmin@master
    gpadmin@master$ . /usr/local/hawq/greenplum_path.sh
    ```

2. Identify the name of an existing HAWQ user/role or create a new HAWQ user/role. For example:

    ``` shell
    gpadmin@master$ psql -d template1 -c 'CREATE ROLE "bill_kerberos" with LOGIN;'
    ```

    This step creates a HAWQ operational role. Create an administrative HAWQ role by adding the `SUPERUSER` clause to the `CREATE ROLE` command.

2. Create a principal for the HAWQ role. Substitute the Kerberos realm you noted earlier. 

    MIT KDC server example:

    ``` shell
    $ ssh root@<kdc-server>
    root@kdc-server$ kadmin.local -q "addprinc -pw changeme bill_kerberos@REALM.DOMAIN"
    ```

    Active Directory KDC server example (generates a keytab file):

    ```shell
    PS C:\Users\Administrator> ktpass -princ bill_kerberos@REALM.DOMAIN -pass changeme -mapuser bill -crypto ALL -ptype KRB5_NT_PRINCIPAL -out bill-krb5.keytab -kvno 0
    ```

3. You may choose to authenticate the HAWQ role with a password or a keytab file. 

    1. If you choose password authentication, no further configuration is required. `bill_kerberos` will provide the password identified by the `-pw` or `pass` option when authenticating. Skip the rest of this step.
    
    2. If you choose authentication via a keytab file:
    
        1. Generate a keytab file for the HAWQ principal you created, again substituting your Kerberos realm. 

            MIT KDC server example:

            ``` shell
            root@kdc-server$ kadmin.local -q "xst -k bill-krb5.keytab bill_kerberos@REALM.DOMAIN"
            ```

            The keytab entry is saved to the `./bill-krb5.keytab` file.

        2. View the key you just added to `bill-krb5.keytab`:

            ``` shell
            root@kdc-server$ klist -ket ./bill-krb5.keytab
            ```

        3. Distribute the keytab file to **each** HAWQ node from which you will access the HAWQ master as the user/role. For example:

            ``` shell
            root@kdc-server$ scp ./bill-krb5.keytab bill@<hawq-node>:/home/bill/
            ```

4. Log in to the HAWQ node as the user for whom you created the principal and set up your HAWQ environment:

    ``` shell
    $ ssh bill@<hawq-node>
    bill@hawq-node$ . /usr/local/hawq/greenplum_path.sh
    ```

5. If you are using keytab file authentication, verify the ownership and mode of the keytab file:

    ``` shell
    bill@hawq-node$ chown bill:bill /home/bill/bill-krb5.keytab
    bill@hawq-node$ chmod 400 /home/bill/bill-krb5.keytab
    ```

8. Access HAWQ as the new `bill_kerberos` user:

    ``` shell
    bill@hawq-node$ psql -d testdb -h <master> -U bill_kerberos
    psql: GSSAPI continuation error: Unspecified GSS failure.  Minor code may provide more information
    GSSAPI continuation error: Credentials cache file '/tmp/krb5cc_502' not found
    ```

    The operation fails. The `bill_kerberos` user has not yet authenticated with the Kerberos server. The next section, [Authenticating User Access to HAWQ](#hawq_kerb_dbaccess), identifies the procedure required for HAWQ users to authenticate with Kerberos.

## <a id="hawq_kerb_dbaccess"></a>Step 4: Authenticating User Access to HAWQ 

When Kerberos user authentication is enabled for HAWQ, users must request a ticket from the Kerberos KDC server before connecting to HAWQ. You must request the ticket for a principal matching the requested database user name. When granted, the ticket expires after a set period of time, after which you will need to request another ticket.
   
To generate a Kerberos ticket, run the `kinit` command. Specify the Kerberos principal for which you are requesting the ticket in a command option. You may optionally specify a path to a keytab file.

For example, to request a ticket for the `bill_kerberos` user principal you created above using the keytab file for authentication:

``` shell
bill@hawq-node$ kinit -k -t /home/bill/bill-krb5.keytab bill_kerberos@REALM.DOMAIN
```

To request a ticket for the `bill_kerberos` user principal using password authentication:

``` shell
bill@hawq-node$ kinit bill_kerberos@REALM.DOMAIN
Password for bill_kerberos@REALM.DOMAIN:
```

`kinit` prompts you for the password; enter the password at the prompt.

For more information about the ticket, use the `klist` command. `klist` invoked without any arguments lists the currently held Kerberos principal and tickets. The command output also provides the ticket expiration time. 

Example output from the `klist` command:

``` shell
bill@hawq-node$ klist
Ticket cache: FILE:/tmp/krb5cc_502
Default principal: bill_kerberos@REALM.DOMAIN

Valid starting     Expires            Service principal
06/07/17 23:16:04  06/08/17 23:16:04  krbtgt/REALM.DOMAIN@REALM.DOMAIN
	renew until 06/07/17 23:16:04
06/07/17 23:16:07  06/08/17 23:16:04  postgres/master@
	renew until 06/07/17 23:16:04
06/07/17 23:16:07  06/08/17 23:16:04  postgres/master@REALM.DOMAIN
	renew until 06/07/17 23:16:04
```

After generating a ticket, you can connect to a HAWQ database as a kerberos-authenticated user using `psql` or other client programs.

### <a id="topic7" class="no-quick-link"></a>Name Mapping 

To simplify Kerberos-authenticated HAWQ user login, you can define a mapping between a user's Kerberos principal name and a HAWQ database user name. You define the mapping in the `pg_ident.conf` file. You use a mapping by specifying a `map=<map-name>` option to a specific entry in the `pg_hba.conf` file. 

The `pg_ident.conf` and `pg_hba.conf` files reside on the HAWQ master node in the directory identified by the `hawq_master_directory` server configuration parameter setting value.

You use the `pg_ident.conf` file to define user name maps. You can create entries in this file that define a mapping name, a Kerberos principal name, and a HAWQ database user name. For example:

```
# MAPNAME   SYSTEM-USERNAME      HAWQ-USERNAME
kerbmap     /^([a-z]+)_kerberos      \1
```

This entry extracts the component prefacing the `_kerberos` of the Kerberos principal name and maps that to a HAWQ user/role.

You identify the map name in the `pg_hba.conf` file entry that enables Kerberos support using the `map=<mapname>` option. For example:

```
host all all 0.0.0.0/0 gss include_realm=0 krb_realm=REALM.DOMAIN map=kerbmap
```

Suppose that you are logged in as Linux user `bsmith`, your Kerberos principal is `bill_kerberos@REALM.DOMAIN`, and you want to log in to HAWQ as user `bill`. With the `kerbmap` mapping configured in `pg_ident.conf` and `pg_hba.conf` as described above and a ticket for Kerberos principal `bill_kerberos`, you log in to HAWQ with the user name `bill` as follows:

``` shell
bsmith@hawq-node$ klist
Ticket cache: FILE:/tmp/krb5cc_500
Default principal: bill_kerberos@REALM.DOMAIN
bsmith@hawq-node$ psql -d testdb -h <master> -U bill
psql (8.2.15)
Type "help" for help.

testdb=> SELECT current_user;
 current_user
--------------
 bill
(1 row)
```

For more information about specifying username maps see [Username maps](http://www.postgresql.org/docs/8.4/static/auth-username-maps.html) in the PostgreSQL documentation.

## <a id="client_considerations"></a>Kerberos Considerations for Non-HAWQ Clients

If you access HAWQ databases from any clients outside of your HAWQ cluster, and Kerberos user authentication for HAWQ is enabled, you must specifically configure Kerberos access on each client system. Ensure that:

- You have created the appropriate Kerberos principal for the HAWQ user and optionally generated and distributed the keytab file.
- The `krb5-libs` and `krb5-workstation` Kerberos client packages are installed on each Linux client.
- You copy the `/etc/krb5.conf` Kerberos configuration file from the KDC or HAWQ master node to each client system.
- The HAWQ user requests a ticket before connecting to HAWQ.

## <a id="topic9"></a>Configuring JDBC for Kerberos-Enabled HAWQ

JDBC applications that you run must utilize a secure connection when Kerberos is configured for HAWQ user authentication.

The following example database connection URL uses a PostgreSQL JDBC driver and specifies parameters for Kerberos authentication:

```
jdbc:postgresql://master:5432/testdb?kerberosServerName=postgres&jaasApplicationName=pgjdbc&user=bill_kerberos
```

The connection URL parameter names and values specified will depend upon how the Java application performs Kerberos authentication.

Before configuring JDBC access to a kerberized HAWQ, verify that:

- The Java Cryptography Extension (JCE) is installed on the client system (non-OpenJDK Java installations).
- Kerberos user authentication is configured for HAWQ as described in [Configure Kerberos User Authentication for HAWQ](#hawq_kerb_cfg).
- If you are accessing HAWQ from a client node that resides outside of your HAWQ cluster, verify that the client is configured as described in [Kerberos Considerations for Non-HAWQ Clients](#client_considerations).

### <a id="topic9_proc" class="no-quick-link"></a>Procedure

Perform the following procedure to enable Kerberos-authenticated JDBC access to HAWQ from a client system.

1.  Create or add the following to the `.java.login.config` file in the `$HOME` directory of the user account under which the application will run:

    ``` pre
    pgjdbc {
      com.sun.security.auth.module.Krb5LoginModule required
      doNotPrompt=true
      useTicketCache=true
      debug=true
      client=true;
    };
    ```

2.  Generate a Kerberos ticket.

3.  Run the JDBC-based HAWQ application.
