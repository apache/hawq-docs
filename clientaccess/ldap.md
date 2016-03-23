---
title: Using LDAP Authentication with TLS/SSL
---

You can control access to HAWQ with an LDAP server and, optionally, secure the connection with encryption by adding parameters to pg\_hba.conf file entries.

HAWQ supports LDAP authentication with the TLS/SSL protocol to encrypt communication with an LDAP server:

-   LDAP authentication with STARTTLS and TLS protocol – STARTTLS starts with a clear text connection \(no encryption\) and upgrades it to a secure connection \(with encryption\).
-   LDAP authentication with a secure connection and TLS/SSL \(LDAPS\) – HAWQ uses the TLS or SSL protocol based on the protocol that is used by the LDAP server.

If no protocol is specified, HAWQ communicates with the LDAP server with a clear text connection.

To use LDAP authentication, the HAWQ master host must be configured as an LDAP client. See your LDAP documentation for information about configuring LDAP clients.

## Enabing LDAP Authentication with STARTTLS and TLS

To enable STARTTLS with the TLS protocol, specify the `ldaptls` parameter with the value 1. The default port is 389. In this example, the authentication method parameters include the `ldaptls` parameter.

```
ldap ldapserver=myldap.com ldaptls=1 ldapprefix="uid=" ldapsuffix=",ou=People,dc=pivotal,dc=com"
```

Specify a non-default port, with the `ldapport` parameter. In this example, the authentication method includes the `ldaptls` parameter and the and `ldapport` parameter to specify the port 550.

```
ldap ldapserver=myldap.com ldaptls=1 ldapport=500 ldapprefix="uid=" ldapsuffix=",ou=People,dc=pivotal,dc=com"
```

## Enabing LDAP Authentication with a Secure Connection and TLS/SSL

To enable a secure connection with TLS/SSL, add `ldaps://` as the prefix to the LDAP server name specified in the `ldapserver` parameter. The default port is 636.

This example `ldapserver` parameter specifies a secure connection and the TLS/SSL protocol for the LDAP server `myldap.com`.

```
ldapserver=ldaps://myldap.com
```

To specify a non-default port, add a colon \(:\) and the port number after the LDAP server name. This example `ldapserver` parameter includes the `ldaps://` prefix and the non-default port 550.

```
ldapserver=ldaps://myldap.com:550
```

## Notes

HAWQ logs an error if the following are specified in an pg\_hba.conf file entry:

-   If both the `ldaps://` prefix and the `ldaptls=1` parameter are specified.
-   If both the `ldaps://` prefix and the `ldapport` parameter are specified.

Enabling encrypted communication for LDAP authentication only encrypts the communication between HAWQ and the LDAP server.

## Examples

These are example entries from an pg\_hba.conf file.

This example specifies LDAP authentication with no encryption between HAWQ and the LDAP server.

```
host all plainuser 0.0.0.0/0 ldap ldapserver=myldap.com ldapprefix="uid=" ldapsuffix=",ou=People,dc=pivotal,dc=com"
```

This example specifies LDAP authentication with the STARTTLS and TLS protocol between HAWQ and the LDAP server.

```
host all tlsuser 0.0.0.0/0 ldap ldapserver=myldap.com ldaptls=1 ldapprefix="uid=" ldapsuffix=",ou=People,dc=pivotal,dc=com"
```

This example specifies LDAP authentication with a secure connection and TLS/SSL protocol between HAWQ and the LDAP server.

```
host all ldapsuser 0.0.0.0/0 ldap ldapserver=ldaps://myldap.com ldapprefix="uid=" ldapsuffix=",ou=People,dc=pivotal,dc=com"
```
