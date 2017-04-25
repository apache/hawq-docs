---
title: Using LDAP Authentication with TLS/SSL
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

You can control access to HAWQ with an LDAP server and, optionally, secure the connection with encryption by adding parameters to pg\_hba.conf file entries.

HAWQ supports LDAP authentication with the TLS/SSL protocol to encrypt communication with an LDAP server:

-   LDAP authentication with STARTTLS and TLS protocol – STARTTLS starts with a clear text connection \(no encryption\) and upgrades it to a secure connection \(with encryption\).
-   LDAP authentication with a secure connection and TLS/SSL \(LDAPS\) – HAWQ uses the TLS or SSL protocol based on the protocol that is used by the LDAP server.

If no protocol is specified, HAWQ communicates with the LDAP server with a clear text connection.

To use LDAP authentication, the HAWQ master host must be configured as an LDAP client. See your LDAP documentation for information about configuring LDAP clients.

## Enabing LDAP Authentication with STARTTLS and TLS

To enable STARTTLS with the TLS protocol, specify the `ldaptls` parameter with the value 1. The default port is 389. In this example, the authentication method parameters include the `ldaptls` parameter.

```
ldap ldapserver=ldap.example.com ldaptls=1 ldapprefix="uid=" ldapsuffix=",ou=People,dc=example,dc=com"
```

Specify a non-default port, with the `ldapport` parameter. In this example, the authentication method includes the `ldaptls` parameter and the `ldapport` parameter to specify the port 550.

```
ldap ldapserver=ldap.example.com ldaptls=1 ldapport=500 ldapprefix="uid=" ldapsuffix=",ou=People,dc=example,dc=com"
```

## Enabling LDAP Authentication with a Secure Connection and TLS/SSL

To enable a secure connection with TLS/SSL, add `ldaps://` as the prefix to the LDAP server name specified in the `ldapserver` parameter. The default port is 636.

This example `ldapserver` parameter specifies a secure connection and the TLS/SSL protocol for the LDAP server `ldap.example.com`.

```
ldapserver=ldaps://ldap.example.com
```

To specify a non-default port, add a colon \(:\) and the port number after the LDAP server name. This example `ldapserver` parameter includes the `ldaps://` prefix and the non-default port 550.

```
ldapserver=ldaps://ldap.example.com:550
```

### Notes

HAWQ logs an error if the following are specified in a pg\_hba.conf file entry:

-   If both the `ldaps://` prefix and the `ldaptls=1` parameter are specified.
-   If both the `ldaps://` prefix and the `ldapport` parameter are specified.

Enabling encrypted communication for LDAP authentication only encrypts the communication between HAWQ and the LDAP server.

## Configuring Authentication with a System-wide OpenLDAP System

If you have a system-wide OpenLDAP system and logins are configured to use LDAP with TLS or SSL in the pg_hba.conf file, logins may fail with the following message:

```shell
could not start LDAP TLS session: error code '-11'
```

To use an existing OpenLDAP system for authentication, HAWQ must be set up to use the LDAP server's CA certificate to validate user certificates. Follow these steps on both the master and standby hosts to configure HAWQ:

1. Copy the base64-encoded root CA chain file from the Active Directory or LDAP server to
the HAWQ master and standby master hosts. This example uses the directory `/etc/pki/tls/certs`.

2. Change to the directory where you copied the CA certificate file and, as the root user, generate the hash for OpenLDAP:

    ```
    # cd /etc/pki/tls/certs
    # openssl x509 -noout -hash -in <ca-certificate-file>
    # ln -s <ca-certificate-file> <ca-certificate-file>.0
    ```

3. Configure an OpenLDAP configuration file for HAWQ with the CA certificate directory and certificate file specified.

    As the root user, edit the OpenLDAP configuration file `/etc/openldap/ldap.conf`:

    ```
    SASL_NOCANON on
    URI ldaps://ldapA.example.priv ldaps://ldapB.example.priv ldaps://ldapC.example.priv
    BASE dc=example,dc=priv
    TLS_CACERTDIR /etc/pki/tls/certs
    TLS_CACERT /etc/pki/tls/certs/<ca-certificate-file>
    ```

    **Note**: For certificate validation to succeed, the hostname in the certificate must match a hostname in the URI property. Otherwise, you must also add `TLS_REQCERT allow` to the file.

4. As the gpadmin user, edit `/usr/local/hawq/greenplum_path.sh` and add the following line.

    ```bash
    export LDAPCONF=/etc/openldap/ldap.conf
    ```

## Examples

These are example entries from an pg\_hba.conf file.

This example specifies LDAP authentication with no encryption between HAWQ and the LDAP server.

```
host all plainuser 0.0.0.0/0 ldap ldapserver=ldap.example.com ldapprefix="uid=" ldapsuffix=",ou=People,dc=example,dc=com"
```

This example specifies LDAP authentication with the STARTTLS and TLS protocol between HAWQ and the LDAP server.

```
host all tlsuser 0.0.0.0/0 ldap ldapserver=ldap.example.com ldaptls=1 ldapprefix="uid=" ldapsuffix=",ou=People,dc=example,dc=com"
```

This example specifies LDAP authentication with a secure connection and TLS/SSL protocol between HAWQ and the LDAP server.

```
host all ldapsuser 0.0.0.0/0 ldap ldapserver=ldaps://ldap.example.com ldapprefix="uid=" ldapsuffix=",ou=People,dc=example,dc=com"
```
