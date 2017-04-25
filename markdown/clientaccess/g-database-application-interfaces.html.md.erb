---
title: HAWQ Database Drivers and APIs
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

You may want to connect your existing Business Intelligence (BI) or Analytics applications with HAWQ. The database application programming interfaces most commonly used with HAWQ are the Postgres and ODBC and JDBC APIs.

HAWQ provides the following connectivity tools for connecting to the database:

  - ODBC driver
  - JDBC driver
  - `libpq` - PostgreSQL C API

## <a id="dbdriver"></a>HAWQ Drivers

ODBC and JDBC drivers for HAWQ are available as a separate download from Pivotal Network [Pivotal Network](https://network.pivotal.io/products/pivotal-hdb).

### <a id="odbc_driver"></a>ODBC Driver

The ODBC API specifies a standard set of C interfaces for accessing database management systems.  For additional information on using the ODBC API, refer to the [ODBC Programmer's Reference](https://msdn.microsoft.com/en-us/library/ms714177(v=vs.85).aspx) documentation.

HAWQ supports the DataDirect ODBC Driver. Installation instructions for this driver are provided on the Pivotal Network driver download page. Refer to [HAWQ ODBC Driver](http://media.datadirect.com/download/docs/odbc/allodbc/#page/odbc%2Fthe-greenplum-wire-protocol-driver.html%23) for HAWQ-specific ODBC driver information.

#### <a id="odbc_driver_connurl"></a>Connection Data Source
The information required by the HAWQ ODBC driver to connect to a database is typically stored in a named data source. Depending on your platform, you may use [GUI](http://media.datadirect.com/download/docs/odbc/allodbc/index.html#page/odbc%2FData_Source_Configuration_through_a_GUI_14.html%23) or [command line](http://media.datadirect.com/download/docs/odbc/allodbc/index.html#page/odbc%2FData_Source_Configuration_in_the_UNIX_2fLinux_odbc_13.html%23) tools to create your data source definition. On Linux, ODBC data sources are typically defined in a file named `odbc.ini`. 

Commonly-specified HAWQ ODBC data source connection properties include:

| Property Name                                                    | Value Description                                                                                                                                                                                         |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Database | Name of the database to which you want to connect. |
| Driver   | Full path to the ODBC driver library file.                                                                                           |
| HostName              | HAWQ master host name.                                                                                     |
| MaxLongVarcharSize      | Maximum size of columns of type long varchar.                                                                                      |
| Password              | Password used to connect to the specified database.                                                                                       |
| PortNumber              | HAWQ master database port number.                                                                                      |

Refer to [Connection Option Descriptions](http://media.datadirect.com/download/docs/odbc/allodbc/#page/odbc%2Fgreenplum-connection-option-descriptions.html%23) for a list of ODBC connection properties supported by the HAWQ DataDirect ODBC driver.

Example HAWQ DataDirect ODBC driver data source definition:

``` shell
[HAWQ-201]
Driver=/usr/local/hawq_drivers/odbc/lib/ddgplm27.so
Description=DataDirect 7.1 Greenplum Wire Protocol - for HAWQ
Database=getstartdb
HostName=hdm1
PortNumber=5432
Password=changeme
MaxLongVarcharSize=8192
```

The first line, `[HAWQ-201]`, identifies the name of the data source.

ODBC connection properties may also be specified in a connection string identifying either a data source name, the name of a file data source, or the name of a driver.  A HAWQ ODBC connection string has the following format:

``` shell
([DSN=<data_source_name>]|[FILEDSN=<filename.dsn>]|[DRIVER=<driver_name>])[;<attribute=<value>[;...]]
```

For additional information on specifying a HAWQ ODBC connection string, refer to [Using a Connection String](http://media.datadirect.com/download/docs/odbc/allodbc/index.html#page/odbc%2FUsing_a_Connection_String_16.html%23).

### <a id="jdbc_driver"></a>JDBC Driver
The JDBC API specifies a standard set of Java interfaces to SQL-compliant databases. For additional information on using the JDBC API, refer to the [Java JDBC API](https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/) documentation.

HAWQ supports the DataDirect JDBC Driver. Installation instructions for this driver are provided on the Pivotal Network driver download page. Refer to [HAWQ JDBC Driver](http://media.datadirect.com/download/docs/jdbc/alljdbc/help.html#page/jdbcconnect%2Fgreenplum-driver.html%23) for HAWQ-specific JDBC driver information.

#### <a id="jdbc_driver_connurl"></a>Connection URL
Connection URLs for accessing the HAWQ DataDirect JDBC driver must be in the following format:

``` shell
jdbc:pivotal:greenplum://host:port[;<property>=<value>[;...]]
```

Commonly-specified HAWQ JDBC connection properties include:

| Property Name                                                    | Value Description                                                                                                                                                                                         |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DatabaseName | Name of the database to which you want to connect. |
| User                         | Username used to connect to the specified database.                                                                                           |
| Password              | Password used to connect to the specified database.                                                                                       |

Refer to [Connection Properties](http://media.datadirect.com/download/docs/jdbc/alljdbc/help.html#page/jdbcconnect%2FConnection_Properties_10.html%23) for a list of JDBC connection properties supported by the HAWQ DataDirect JDBC driver.

Example HAWQ JDBC connection string:

``` shell
jdbc:pivotal:greenplum://hdm1:5432;DatabaseName=getstartdb;User=hdbuser;Password=hdbpass
```

## <a id="libpq_api"></a>libpq API
`libpq` is the C API to PostgreSQL/HAWQ. This API provides a set of library functions enabling client programs to pass queries to the PostgreSQL backend server and to receive the results of those queries.

`libpq` is installed in the `lib/` directory of your HAWQ distribution. `libpq-fe.h`, the header file required for developing front-end PostgreSQL applications, can be found in the `include/` directory.

For additional information on using the `libpq` API, refer to [libpq - C Library](https://www.postgresql.org/docs/8.2/static/libpq.html) in the PostgreSQL documentation.

