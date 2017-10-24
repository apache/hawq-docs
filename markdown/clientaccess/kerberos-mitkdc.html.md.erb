---
title: Example - Setting up an MIT KDC Server
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

Follow this procedure to install and configure a Kerberos KDC server on a Red Hat Enterprise Linux host. The KDC server resides on the host named \<kdc-server\>.

1. Log in to the Kerberos KDC Server system as a superuser:

    ``` shell
    $ ssh root@<kdc-server>
    root@kdc-server$ 
    ```

2.  Install the Kerberos server packages:

    ``` shell
    root@kdc-server$ yum install krb5-libs krb5-server krb5-workstation
    ```

3.  Define the Kerberos realm for your cluster by editting the `/etc/krb5.conf` configuration file. The following example configures a Kerberos server with a realm named `REALM.DOMAIN` residing on a host named `hawq-kdc`.

    ```
    [logging]
     default = FILE:/var/log/krb5libs.log
     kdc = FILE:/var/log/krb5kdc.log
     admin_server = FILE:/var/log/kadmind.log

    [libdefaults]
     default_realm = REALM.DOMAIN
     dns_lookup_realm = false
     dns_lookup_kdc = false
     ticket_lifetime = 24h
     renew_lifetime = 7d
     forwardable = true
     default_tgs_enctypes = aes128-cts des3-hmac-sha1 des-cbc-crc des-cbc-md5
     default_tkt_enctypes = aes128-cts des3-hmac-sha1 des-cbc-crc des-cbc-md5
     permitted_enctypes = aes128-cts des3-hmac-sha1 des-cbc-crc des-cbc-md5

    [realms]
     REALM.DOMAIN = {
      kdc = hawq-kdc:88
      admin_server = hawq-kdc:749
      default_domain = hawq-kdc
     }

    [domain_realm]
     .hawq-kdc = REALM.DOMAIN
     hawq-kdc = REALM.DOMAIN

    [appdefaults]
     pam = {
        debug = false
        ticket_lifetime = 36000
        renew_lifetime = 36000
        forwardable = true
        krb4_convert = false
       }
    ```

    The `kdc` and `admin_server` keys in the `[realms]` section specify the host \(`hawq-kdc`\) and port on which the Kerberos server is running. You can use an IP address in place of a host name.

    If your Kerberos server manages authentication for other realms, you would instead add the `REALM.DOMAINM` realm in the `[realms]` and `[domain_realm]` sections of the `krb5.conf` file. See the [Kerberos documentation](http://web.mit.edu/kerberos/krb5-latest/doc/) for detailed information about the `krb5.conf` configuration file.

4. Note the Kerberos KDC server host name or IP address and the name of the realm in which your cluster resides. You will need this information in later procedures.
5.  Create a Kerberos KDC database by running the `kdb5_util` command:

    ```
    root@kdc-server$ kdb5_util create -s
    ```

    The `kdb5_util create` command creates the database in which the keys for the Kerberos realms managed by this KDC server are stored. The `-s` option instructs the command to create a stash file. Without the stash file, the KDC server will request a password every time it starts.

6.  Add an administrative user to the Kerberos KDC database with the `kadmin.local` utility. Because it does not itself depend on Kerberos authentication, the `kadmin.local` utility allows you to add an initial administrative user to the local Kerberos server. To add the user `admin` as an administrative user to the KDC database, run the following command:

    ```
    root@kdc-server$ kadmin.local -q "addprinc admin/admin"
    ```

    Most users do not need administrative access to the Kerberos server. They can use `kadmin` to manage their own principals \(for example, to change their own password\). For information about `kadmin`, see the [Kerberos documentation](http://web.mit.edu/kerberos/krb5-latest/doc/).

7.  If required, edit the `/var/kerberos/krb5kdc/kadm5.acl` file to grant the appropriate permissions to `admin`.
8.  Start the Kerberos daemons:

    ```
    root@kdc-server$ /sbin/service krb5kdc start
    root@kdc-server$ /sbin/service kadmin start
    ```

9.  To start Kerberos automatically upon system restart:

    ```
    root@kdc-server$ /sbin/chkconfig krb5kdc on
    root@kdc-server$ /sbin/chkconfig kadmin on
    ```
