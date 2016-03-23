---
title: Database Application Interfaces
---

You may want to develop your own client applications that interface to HAWQ. PostgreSQL provides a number of database drivers for the most commonly used database application programming interfaces \(APIs\), which can also be used with HAWQ. These drivers are available as a separate download. Each driver is an independent PostgreSQL development project and must be downloaded, installed and configured to connect to HAWQ. The following drivers are available:

|API|PostgreSQL Driver|Download Link|
|---|-----------------|-------------|
|ODBC|pgodbc|Available on [Pivotal Network](https://network.pivotal.io/products/pivotal-hawq#/releases/272/file_groups/230).|
|JDBC|pgjdbc|Available on [Pivotal Network](https://network.pivotal.io/products/pivotal-hawq#/releases/272/file_groups/230).|
|Perl DBI|pgperl|[http://search.cpan.org/dist/DBD-Pg/](http://search.cpan.org/dist/DBD-Pg/)|
|Python DBI|pygresql|[http://www.pygresql.org/](http://www.pygresql.org/)|

General instructions for accessing a HAWQ with an API are:

1.  Download your programming language platform and respective API from the appropriate source. For example, you can get the Java Development Kit \(JDK\) and JDBC API from Sun.
2.  Write your client application according to the API specifications. When programming your application, be aware of the SQL support in HAWQ so you do not include any unsupported SQL syntax.
