---
title: Configuring Client Authentication
---

This topic explains how to configure client connections and authentication for HAWQ.

When a HAWQ system is first initialized, the system contains one predefined *superuser* role. This role will have the same name as the operating system user who initialized the HAWQ system. This role is referred to as `gpadmin`. By default, the system is configured to only allow local connections to the database from the `gpadmin` role. To allow any other roles to connect, or to allow connections from remote hosts, you configure HAWQ to allow such connections.

## Allowing Connections to HAWQ <a id="topic2"></a>

Client access and authentication is controlled by the standard PostgreSQL host-based authentication file, pg\_hba.conf. In HAWQ, the pg\_hba.conf file of the master instance controls client access and authentication to your HAWQ system. HAWQ segments have pg\_hba.conf files that are configured to allow only client connections from the master host and never accept client connections. Do not alter the pg\_hba.conf file on your segments.

See [The pg\_hba.conf File](http://www.postgresql.org/docs/9.0/interactive/auth-pg-hba-conf.html) in the PostgreSQL documentation for more information.

The general format of the pg\_hba.conf file is a set of records, one per line. HAWQ ignores blank lines and any text after the `#` comment character. A record consists of a number of fields that are separated by spaces and/or tabs. Fields can contain white space if the field value is quoted. Records cannot be continued across lines. Each remote client access record has the following format:

```
*host*   *database*   *role*   *CIDR-address*   *authentication-method*
```

Each UNIX-domain socket access record has the following format:

```
*local*   *database*   *role*   *authentication-method*
```

The following table describes meaning of each field.

|Field|Description|
|-----|-----------|
|local|Matches connection attempts using UNIX-domain sockets. Without a record of this type, UNIX-domain socket connections are disallowed.|
|host|Matches connection attempts made using TCP/IP. Remote TCP/IP connections will not be possible unless the server is started with an appropriate value for the listen\_addresses server configuration parameter.|
|hostssl|Matches connection attempts made using TCP/IP, but only when the connection is made with SSL encryption. SSL must be enabled at server start time by setting the ssl configuration parameter|
|hostnossl|Matches connection attempts made over TCP/IP that do not use SSL.|
|database|Specifies which database names this record matches. The value `all` specifies that it matches all databases. Multiple database names can be supplied by separating them with commas. A separate file containing database names can be specified by preceding the file name with @.|
|role|Specifies which database role names this record matches. The value `all` specifies that it matches all roles. If the specified role is a group and you want all members of that group to be included, precede the role name with a +. Multiple role names can be supplied by separating them with commas. A separate file containing role names can be specified by preceding the file name with @.|
|CIDR-address|Specifies the client machine IP address range that this record matches. It contains an IP address in standard dotted decimal notation and a CIDR mask length. IP addresses can only be specified numerically, not as domain or host names. The mask length indicates the number of high-order bits of the client IP address that must match. Bits to the right of this must be zero in the given IP address. There must not be any white space between the IP address, the /, and the CIDR mask length. Typical examples of a CIDR-address are 172.20.143.89/32 for a single host, or 172.20.143.0/24 for a small network, or 10.6.0.0/16 for a larger one. To specify a single host, use a CIDR mask of 32 for IPv4 or 128 for IPv6. In a network address, do not omit trailing zeroes.|
|IP-address, IP-mask|These fields can be used as an alternative to the CIDR-address notation. Instead of specifying the mask length, the actual mask is specified in a separate column. For example, 255.0.0.0 represents an IPv4 CIDR mask length of 8, and 255.255.255.255 represents a CIDR mask length of 32. These fields only apply to host, hostssl, and hostnossl records.|
|authentication-method|Specifies the authentication method to use when connecting. HAWQ supports the [authentication methods](http://www.postgresql.org/docs/9.0/static/auth-methods.html) supported by PostgreSQL 9.0.|

### Editing the pg\_hba.conf File <a id="topic3"></a>

This example shows how to edit the pg\_hba.conf file of the master to allow remote client access to all databases from all roles using encrypted password authentication.

**Note:** For a more secure system, consider removing all connections that use trust authentication from your master pg\_hba.conf. Trust authentication means the role is granted access without any authentication, therefore bypassing all security. Replace trust entries with ident authentication if your system has an ident service available.

#### Editing pg\_hba.conf <a id="ip144328"></a>

1.  Open the file $MASTER\_DATA\_DIRECTORY/pg\_hba.conf in a text editor.
2.  Add a line to the file for each type of connection you want to allow. Records are read sequentially, so the order of the records is significant. Typically, earlier records will have tight connection match parameters and weaker authentication methods, while later records will have looser match parameters and stronger authentication methods. For example:

    ```
    # allow the gpadmin user local access to all databases
    # using ident authentication
    local   all   gpadmin   ident         sameuser
    host    all   gpadmin   127.0.0.1/32  ident
    host    all   gpadmin   ::1/128       ident
    # allow the 'dba' role access to any database from any
    # host with IP address 192.168.x.x and use md5 encrypted
    # passwords to authenticate the user
    # Note that to use SHA-256 encryption, replace *md5* with
    # password in the line below
    host    all   dba   192.168.0.0/32  md5
    # allow all roles access to any database from any
    # host and use ldap to authenticate the user. HAWQ role
    # names must match the LDAP common name.
    host    all   all   192.168.0.0/32  ldap ldapserver=usldap1
    ldapport=1389 ldapprefix="cn="
    ldapsuffix=",ou=People,dc=company,dc=com"
    ```

3.  Save and close the file.
4.  Reload the pg\_hba.conf configuration file for your changes to take effect:

    ```
    $ hawq stop -u
    ```


## Limiting Concurrent Connections <a id="topic4"></a>

HAWQ allocates some resources on a per-connection basis, so setting the maximum number of connections allowed is recommended.

To limit the number of active concurrent sessions to your HAWQ system, you can configure the `max_connections` server configuration parameter on master or the `seg_max_connections` server configuration parameter on segments. These parameters are *local* parameters, meaning that you must set them in the `hawq-site.xml` file of all HAWQ instances. The current recommendation is to set the value of `seg_max_connections` to 5-10 the value of `max_connections`.

When you set `max_connections`, you must also set the dependent parameter `max_prepared_transactions`. This value must be at least as large as the value of `max_connections`, and all HAWQ instances should be set to the same value.

For example, in `$GPHOME/etc/hawq-site.xml`:

```
  <property>
      <name>max_connections</name>
      <value>500</value>
  </property>
  <property>
      <name>max_prepared_transactions</name>
      <value>1000</value>
  </property>
  <property>
      <name>seg_max_connections</name>
      <value>3200</value>
  </property>
```

The following steps set the parameter values with the HAWQ utility `hawq config`.

### To change the number of allowed connections <a id="ip142411"></a>

1.  Log into the HAWQ master host as the HAWQ administrator and source the file `$GPHOME/greenplum_path.sh`.
2.  Set the value of the `max_connections` parameter. This `hawq config` command sets the value to 100 on all HAWQ instances.

    ```
    $ hawq config -c max_connections -v 100
    ```

    This configuration command sets the value on the master.

3.  Set the value of the `seg_max_connections` parameter. This `hawq config` command sets the value to 6400 on all HAWQ instances.

    ```
    $ hawq config -c seg_max_connections -v 6400
    ```

    This configuration command sets the value on all segment instances.

4.  Set the value of the `max_prepared_transactions` parameter. This `hawq config` command sets the value to 200 on the master and all segments.

    ```
    $ hawq config -c max_prepared_transactions -v 200
    ```

    The value of `max_prepared_transactions` must be greater than or equal to `max_connections`.

5.  Stop and restart your HAWQ system.

    ```
    $ hawq restart
    ```

6.  You can check the value of parameters on the master and segments with the `hawq config``-s` option. These `hawq config` commands display the values of the `max_connections` and `seg_max_connections` parameter.

    ```
    $ hawq config -s max_connections
    $ hawq config -s seg_max_connections
    ```


**Note:** Raising the values of these parameters may cause HAWQ to request more shared memory. To mitigate this effect, consider decreasing other memory-related parameters such as `gp_cached_segworkers_threshold`.

## Encrypting Client/Server Connections <a id="topic5"></a>

Enable SSL for client connections to HAWQ to encrypt the data passed over the network between the client and the database.

HAWQ has native support for SSL connections between the client and the master server. SSL connections prevent third parties from snooping on the packets, and also prevent man-in-the-middle attacks. SSL should be used whenever the client connection goes through an insecure link, and must be used whenever client certificate authentication is used.

To enable SSL requires that OpenSSL be installed on both the client and the master server systems. HAWQ can be started with SSL enabled by setting the server configuration parameter `ssl` to `on` in the master `hawq-site.xml`. When starting in SSL mode, the server will look for the files server.key \(server private key\) and server.crt \(server certificate\) in the master data directory. These files must be set up correctly before an SSL-enabled HAWQ system can start.

**Important:** Do not protect the private key with a passphrase. The server does not prompt for a passphrase for the private key, and the database startup fails with an error if one is required.

A self-signed certificate can be used for testing, but a certificate signed by a certificate authority \(CA\) should be used in production, so the client can verify the identity of the server. Either a global or local CA can be used. If all the clients are local to the organization, a local CA is recommended.

### Creating a Self-signed Certificate without a Passphrase for Testing Only <a id="topic6"></a>

To create a quick self-signed certificate for the server for testing, use the following OpenSSL command:

```
# openssl req -new -text -out server.req
```

Enter the information requested by the prompts. Be sure to enter the local host name as *Common Name*. The challenge password can be left blank.

The program will generate a key that is passphrase protected, and does not accept a passphrase that is less than four characters long.

To use this certificate with HAWQ, remove the passphrase with the following commands:

```
# openssl rsa -in privkey.pem -out server.key
# rm privkey.pem
```

Enter the old passphrase when prompted to unlock the existing key.

Then, enter the following command to turn the certificate into a self-signed certificate and to copy the key and certificate to a location where the server will look for them.

```
# openssl req -x509 -in server.req -text -key server.key -out server.crt
```

Finally, change the permissions on the key with the following command. The server will reject the file if the permissions are less restrictive than these.

```
# chmod og-rwx server.key
```

For more details on how to create your server private key and certificate, refer to the [OpenSSL documentation](https://www.openssl.org/docs/).
