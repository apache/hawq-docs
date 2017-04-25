---
title: Monitoring a HAWQ System
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

You can monitor a HAWQ system using a variety of tools included with the system or available as add-ons.

Observing the HAWQ system day-to-day performance helps administrators understand the system behavior, plan workflow, and troubleshoot problems. This chapter discusses tools for monitoring database performance and activity.

Also, be sure to review [Recommended Monitoring and Maintenance Tasks](RecommendedMonitoringTasks.html) for monitoring activities you can script to quickly detect problems in the system.


## <a id="topic31"></a>Using hawq\_toolkit 

Use HAWQ's administrative schema [*hawq\_toolkit*](../reference/toolkit/hawq_toolkit.html) to query the system catalogs, log files, and operating environment for system status information. The *hawq\_toolkit* schema contains several views you can access using SQL commands. The *hawq\_toolkit* schema is accessible to all database users. Some objects require superuser permissions. Use a command similar to the following to add the *hawq\_toolkit* schema to your schema search path:

```sql
=> SET ROLE 'gpadmin' ;
=# SET search_path TO myschema, hawq_toolkit ;
```

## <a id="topic3"></a>Monitoring System State 

As a HAWQ administrator, you must monitor the system for problem events such as a segment going down or running out of disk space on a segment host. The following topics describe how to monitor the health of a HAWQ system and examine certain state information for a HAWQ system.

-   [Checking System State](#topic12)
-   [Checking Disk Space Usage](#topic15)
-   [Viewing Metadata Information about Database Objects](#topic24)
-   [Viewing Query Workfile Usage Information](#topic27)

### <a id="topic12"></a>Checking System State 

A HAWQ system is comprised of multiple PostgreSQL instances \(the master and segments\) spanning multiple machines. To monitor a HAWQ system, you need to know information about the system as a whole, as well as status information of the individual instances. The `hawq state` utility provides status information about a HAWQ system.

#### <a id="topic13"></a>Viewing Master and Segment Status and Configuration 

The default `hawq state` action is to check segment instances and show a brief status of the valid and failed segments. For example, to see a quick status of your HAWQ system:

```shell
$ hawq state -b
```

You can also display information about the HAWQ master data directory by invoking `hawq state` with the `-d` option:

```shell
$ hawq state -d <master_data_dir>
```


### <a id="topic15"></a>Checking Disk Space Usage 

#### <a id="topic16"></a>Checking Sizing of Distributed Databases and Tables 

The *hawq\_toolkit* administrative schema contains several views that you can use to determine the disk space usage for a distributed HAWQ database, schema, table, or index.

##### <a id="topic17"></a>Viewing Disk Space Usage for a Database 

To see the total size of a database \(in bytes\), use the *hawq\_size\_of\_database* view in the *hawq\_toolkit* administrative schema. For example:

```sql
=> SELECT * FROM hawq_toolkit.hawq_size_of_database
     ORDER BY sodddatname;
```

##### <a id="topic18"></a>Viewing Disk Space Usage for a Table 

The *hawq\_toolkit* administrative schema contains several views for checking the size of a table. The table sizing views list the table by object ID \(not by name\). To check the size of a table by name, you must look up the relation name \(`relname`\) in the *pg\_class* table. For example:

```sql
=> SELECT relname AS name, sotdsize AS size, sotdtoastsize
     AS toast, sotdadditionalsize AS other
     FROM hawq_toolkit.hawq_size_of_table_disk AS sotd, pg_class
   WHERE sotd.sotdoid=pg_class.oid ORDER BY relname;
```

##### <a id="topic19"></a>Viewing Disk Space Usage for Indexes 

The *hawq\_toolkit* administrative schema contains a number of views for checking index sizes. To see the total size of all index\(es\) on a table, use the *hawq\_size\_of\_all\_table\_indexes* view. To see the size of a particular index, use the *hawq\_size\_of\_index* view. The index sizing views list tables and indexes by object ID \(not by name\). To check the size of an index by name, you must look up the relation name \(`relname`\) in the *pg\_class* table. For example:

```sql
=> SELECT soisize, relname AS indexname
     FROM pg_class, hawq_size_of_index
   WHERE pg_class.oid=hawq_size_of_index.soioid
     AND pg_class.relkind='i';
```

### <a id="topic24"></a>Viewing Metadata Information about Database Objects 

HAWQ uses its system catalogs to track various metadata information about the objects stored in a database (tables, views, indexes and so on), as well as global objects including roles and tablespaces.

#### <a id="topic25"></a>Viewing the Last Operation Performed 

You can use the system views *pg\_stat\_operations* and *pg\_stat\_partition\_operations* to look up actions performed on a database object. For example, to view when the `cust` table was created and when it was last analyzed:

```sql
=> SELECT schemaname AS schema, objname AS table,
     usename AS role, actionname AS action,
     subtype AS type, statime AS time
   FROM pg_stat_operations
   WHERE objname='cust';
```

```
 schema | table | role | action  | type  | time
--------+-------+------+---------+-------+--------------------------
  sales | cust  | main | CREATE  | TABLE | 2010-02-09 18:10:07.867977-08
  sales | cust  | main | VACUUM  |       | 2010-02-10 13:32:39.068219-08
  sales | cust  | main | ANALYZE |       | 2010-02-25 16:07:01.157168-08
(3 rows)

```

#### <a id="topic26"></a>Viewing the Definition of an Object 

You can use the `psql` `\d` meta-command to display the definition of an object, such as a table or view. For example, to see the definition of a table named `sales`:

``` sql
=> \d sales
```

```
Append-Only Table "public.sales"
 Column |  Type   | Modifiers 
--------+---------+-----------
 id     | integer | 
 year   | integer | 
 qtr    | integer | 
 day    | integer | 
 region | text    | 
Compression Type: None
Compression Level: 0
Block Size: 32768
Checksum: f
Distributed by: (id)
```


### <a id="topic27"></a>Viewing Query Workfile Usage Information 

The HAWQ administrative schema *hawq\_toolkit* contains views that display information about HAWQ workfiles. HAWQ creates workfiles on disk if it does not have sufficient memory to execute the query in memory. This information can be used for troubleshooting and tuning queries. The information in the views can also be used to specify the values for the HAWQ configuration parameters `hawq_workfile_limit_per_query` and `hawq_workfile_limit_per_segment`.

Views in the *hawq\_toolkit* schema include:

-   *hawq\_workfile\_entries* - one row for each operator currently using disk space for workfiles on a segment
-   *hawq\_workfile\_usage\_per\_query* - one row for each running query currently using disk space for workfiles on a segment
-   *hawq\_workfile\_usage\_per\_segment* - one row for each segment where each row displays the total amount of disk space currently in use for workfiles on the segment


## <a id="topic_jx2_rqg_kp"></a>HAWQ Error Codes 

The following section describes SQL error codes for certain database events.

### <a id="topic_pyh_sqg_kp"></a>SQL Standard Error Codes 

The following table lists all the defined error codes. Some are not used, but are defined by the SQL standard. The error classes are also shown. For each error class there is a standard error code having the last three characters 000. This code is used only for error conditions that fall within the class but do not have any more-specific code assigned.

The PL/pgSQL condition name for each error code is the same as the phrase shown in the table, with underscores substituted for spaces. For example, code 22012, DIVISION BY ZERO, has condition name DIVISION\_BY\_ZERO. Condition names can be written in either upper or lower case.

**Note:** PL/pgSQL does not recognize warning, as opposed to error, condition names; those are classes 00, 01, and 02.

|Error Code|Meaning|Constant|
|----------|-------|--------|
|**Class 00**— Successful Completion|
|00000|SUCCESSFUL COMPLETION|successful\_completion|
|Class 01 — Warning|
|01000|WARNING|warning|
|0100C|DYNAMIC RESULT SETS RETURNED|dynamic\_result\_sets\_returned|
|01008|IMPLICIT ZERO BIT PADDING|implicit\_zero\_bit\_padding|
|01003|NULL VALUE ELIMINATED IN SET FUNCTION|null\_value\_eliminated\_in\_set\_function|
|01007|PRIVILEGE NOT GRANTED|privilege\_not\_granted|
|01006|PRIVILEGE NOT REVOKED|privilege\_not\_revoked|
|01004|STRING DATA RIGHT TRUNCATION|string\_data\_right\_truncation|
|01P01|DEPRECATED FEATURE|deprecated\_feature|
|**Class 02** — No Data \(this is also a warning class per the SQL standard\)|
|02000|NO DATA|no\_data|
|02001|NO ADDITIONAL DYNAMIC RESULT SETS RETURNED|no\_additional\_dynamic\_result\_sets\_returned|
|**Class 03** — SQL Statement Not Yet Complete|
|03000|SQL STATEMENT NOT YET COMPLETE|sql\_statement\_not\_yet\_complete|
|**Class 08** — Connection Exception|
|08000|CONNECTION EXCEPTION|connection\_exception|
|08003|CONNECTION DOES NOT EXIST|connection\_does\_not\_exist|
|08006|CONNECTION FAILURE|connection\_failure|
|08001|SQLCLIENT UNABLE TO ESTABLISH SQLCONNECTION|sqlclient\_unable\_to\_establish\_sqlconnection|
|08004|SQLSERVER REJECTED ESTABLISHMENT OF SQLCONNECTION|sqlserver\_rejected\_establishment\_of\_sqlconnection|
|08007|TRANSACTION RESOLUTION UNKNOWN|transaction\_resolution\_unknown|
|08P01|PROTOCOL VIOLATION|protocol\_violation|
|**Class 09** — Triggered Action Exception|
|09000|TRIGGERED ACTION EXCEPTION|triggered\_action\_exception|
|**Class 0A** — Feature Not Supported|
|0A000|FEATURE NOT SUPPORTED|feature\_not\_supported|
|**Class 0B** — Invalid Transaction Initiation|
|0B000|INVALID TRANSACTION INITIATION|invalid\_transaction\_initiation|
|**Class 0F** — Locator Exception|
|0F000|LOCATOR EXCEPTION|locator\_exception|
|0F001|INVALID LOCATOR SPECIFICATION|invalid\_locator\_specification|
|**Class 0L** — Invalid Grantor|
|0L000|INVALID GRANTOR|invalid\_grantor|
|0LP01|INVALID GRANT OPERATION|invalid\_grant\_operation|
|**Class 0P** — Invalid Role Specification|
|0P000|INVALID ROLE SPECIFICATION|invalid\_role\_specification|
|**Class 21** — Cardinality Violation|
|21000|CARDINALITY VIOLATION|cardinality\_violation|
|**Class 22** — Data Exception|
|22000|DATA EXCEPTION|data\_exception|
|2202E|ARRAY SUBSCRIPT ERROR|array\_subscript\_error|
|22021|CHARACTER NOT IN REPERTOIRE|character\_not\_in\_repertoire|
|22008|DATETIME FIELD OVERFLOW|datetime\_field\_overflow|
|22012|DIVISION BY ZERO|division\_by\_zero|
|22005|ERROR IN ASSIGNMENT|error\_in\_assignment|
|2200B|ESCAPE CHARACTER CONFLICT|escape\_character\_conflict|
|22022|INDICATOR OVERFLOW|indicator\_overflow|
|22015|INTERVAL FIELD OVERFLOW|interval\_field\_overflow|
|2201E|INVALID ARGUMENT FOR LOGARITHM|invalid\_argument\_for\_logarithm|
|2201F|INVALID ARGUMENT FOR POWER FUNCTION|invalid\_argument\_for\_power\_function|
|2201G|INVALID ARGUMENT FOR WIDTH BUCKET FUNCTION|invalid\_argument\_for\_width\_bucket\_function|
|22018|INVALID CHARACTER VALUE FOR CAST|invalid\_character\_value\_for\_cast|
|22007|INVALID DATETIME FORMAT|invalid\_datetime\_format|
|22019|INVALID ESCAPE CHARACTER|invalid\_escape\_character|
|2200D|INVALID ESCAPE OCTET|invalid\_escape\_octet|
|22025|INVALID ESCAPE SEQUENCE|invalid\_escape\_sequence|
|22P06|NONSTANDARD USE OF ESCAPE CHARACTER|nonstandard\_use\_of\_escape\_character|
|22010|INVALID INDICATOR PARAMETER VALUE|invalid\_indicator\_parameter\_value|
|22020|INVALID LIMIT VALUE|invalid\_limit\_value|
|22023|INVALID PARAMETER VALUE|invalid\_parameter\_value|
|2201B|INVALID REGULAR EXPRESSION|invalid\_regular\_expression|
|22009|INVALID TIME ZONE DISPLACEMENT VALUE|invalid\_time\_zone\_displacement\_value|
|2200C|INVALID USE OF ESCAPE CHARACTER|invalid\_use\_of\_escape\_character|
|2200G|MOST SPECIFIC TYPE MISMATCH|most\_specific\_type\_mismatch|
|22004|NULL VALUE NOT ALLOWED|null\_value\_not\_allowed|
|22002|NULL VALUE NO INDICATOR PARAMETER|null\_value\_no\_indicator\_parameter|
|22003|NUMERIC VALUE OUT OF RANGE|numeric\_value\_out\_of\_range|
|22026|STRING DATA LENGTH MISMATCH|string\_data\_length\_mismatch|
|22001|STRING DATA RIGHT TRUNCATION|string\_data\_right\_truncation|
|22011|SUBSTRING ERROR|substring\_error|
|22027|TRIM ERROR|trim\_error|
|22024|UNTERMINATED C STRING|unterminated\_c\_string|
|2200F|ZERO LENGTH CHARACTER STRING|zero\_length\_character\_string|
|22P01|FLOATING POINT EXCEPTION|floating\_point\_exception|
|22P02|INVALID TEXT REPRESENTATION|invalid\_text\_representation|
|22P03|INVALID BINARY REPRESENTATION|invalid\_binary\_representation|
|22P04|BAD COPY FILE FORMAT|bad\_copy\_file\_format|
|22P05|UNTRANSLATABLE CHARACTER|untranslatable\_character|
|**Class 23** — Integrity Constraint Violation|
|23000|INTEGRITY CONSTRAINT VIOLATION|integrity\_constraint\_violation|
|23001|RESTRICT VIOLATION|restrict\_violation|
|23502|NOT NULL VIOLATION|not\_null\_violation|
|23503|FOREIGN KEY VIOLATION|foreign\_key\_violation|
|23505|UNIQUE VIOLATION|unique\_violation|
|23514|CHECK VIOLATION|check\_violation|
|**Class 24** — Invalid Cursor State|
|24000|INVALID CURSOR STATE|invalid\_cursor\_state|
|**Class 25** — Invalid Transaction State|
|25000|INVALID TRANSACTION STATE|invalid\_transaction\_state|
|25001|ACTIVE SQL TRANSACTION|active\_sql\_transaction|
|25002|BRANCH TRANSACTION ALREADY ACTIVE|branch\_transaction\_already\_active|
|25008|HELD CURSOR REQUIRES SAME ISOLATION LEVEL|held\_cursor\_requires\_same\_isolation\_level|
|25003|INAPPROPRIATE ACCESS MODE FOR BRANCH TRANSACTION|inappropriate\_access\_mode\_for\_branch\_transaction|
|25004|INAPPROPRIATE ISOLATION LEVEL FOR BRANCH TRANSACTION|inappropriate\_isolation\_level\_for\_branch\_transaction|
|25005|NO ACTIVE SQL TRANSACTION FOR BRANCH TRANSACTION|no\_active\_sql\_transaction\_for\_branch\_transaction|
|25006|READ ONLY SQL TRANSACTION|read\_only\_sql\_transaction|
|25007|SCHEMA AND DATA STATEMENT MIXING NOT SUPPORTED|schema\_and\_data\_statement\_mixing\_not\_supported|
|25P01|NO ACTIVE SQL TRANSACTION|no\_active\_sql\_transaction|
|25P02|IN FAILED SQL TRANSACTION|in\_failed\_sql\_transaction|
|**Class 26** — Invalid SQL Statement Name|
|26000|INVALID SQL STATEMENT NAME|invalid\_sql\_statement\_name|
|**Class 27** — Triggered Data Change Violation|
|27000|TRIGGERED DATA CHANGE VIOLATION|triggered\_data\_change\_violation|
|**Class 28** — Invalid Authorization Specification|
|28000|INVALID AUTHORIZATION SPECIFICATION|invalid\_authorization\_specification|
|**Class 2B** — Dependent Privilege Descriptors Still Exist|
|2B000|DEPENDENT PRIVILEGE DESCRIPTORS STILL EXIST|dependent\_privilege\_descriptors\_still\_exist|
|2BP01|DEPENDENT OBJECTS STILL EXIST|dependent\_objects\_still\_exist|
|**Class 2D** — Invalid Transaction Termination|
|2D000|INVALID TRANSACTION TERMINATION|invalid\_transaction\_termination|
|**Class 2F** — SQL Routine Exception|
|2F000|SQL ROUTINE EXCEPTION|sql\_routine\_exception|
|2F005|FUNCTION EXECUTED NO RETURN STATEMENT|function\_executed\_no\_return\_statement|
|2F002|MODIFYING SQL DATA NOT PERMITTED|modifying\_sql\_data\_not\_permitted|
|2F003|PROHIBITED SQL STATEMENT ATTEMPTED|prohibited\_sql\_statement\_attempted|
|2F004|READING SQL DATA NOT PERMITTED|reading\_sql\_data\_not\_permitted|
|**Class 34** — Invalid Cursor Name|
|34000|INVALID CURSOR NAME|invalid\_cursor\_name|
|**Class 38** — External Routine Exception|
|38000|EXTERNAL ROUTINE EXCEPTION|external\_routine\_exception|
|38001|CONTAINING SQL NOT PERMITTED|containing\_sql\_not\_permitted|
|38002|MODIFYING SQL DATA NOT PERMITTED|modifying\_sql\_data\_not\_permitted|
|38003|PROHIBITED SQL STATEMENT ATTEMPTED|prohibited\_sql\_statement\_attempted|
|38004|READING SQL DATA NOT PERMITTED|reading\_sql\_data\_not\_permitted|
|**Class 39** — External Routine Invocation Exception|
|39000|EXTERNAL ROUTINE INVOCATION EXCEPTION|external\_routine\_invocation\_exception|
|39001|INVALID SQLSTATE RETURNED|invalid\_sqlstate\_returned|
|39004|NULL VALUE NOT ALLOWED|null\_value\_not\_allowed|
|39P01|TRIGGER PROTOCOL VIOLATED|trigger\_protocol\_violated|
|39P02|SRF PROTOCOL VIOLATED|srf\_protocol\_violated|
|**Class 3B** — Savepoint Exception|
|3B000|SAVEPOINT EXCEPTION|savepoint\_exception|
|3B001|INVALID SAVEPOINT SPECIFICATION|invalid\_savepoint\_specification|
|**Class 3D** — Invalid Catalog Name|
|3D000|INVALID CATALOG NAME|invalid\_catalog\_name|
|**Class 3F** — Invalid Schema Name|
|3F000|INVALID SCHEMA NAME|invalid\_schema\_name|
|**Class 40** — Transaction Rollback|
|40000|TRANSACTION ROLLBACK|transaction\_rollback|
|40002|TRANSACTION INTEGRITY CONSTRAINT VIOLATION|transaction\_integrity\_constraint\_violation|
|40001|SERIALIZATION FAILURE|serialization\_failure|
|40003|STATEMENT COMPLETION UNKNOWN|statement\_completion\_unknown|
|40P01|DEADLOCK DETECTED|deadlock\_detected|
|**Class 42** — Syntax Error or Access Rule Violation|
|42000|SYNTAX ERROR OR ACCESS RULE VIOLATION|syntax\_error\_or\_access\_rule\_violation|
|42601|SYNTAX ERROR|syntax\_error|
|42501|INSUFFICIENT PRIVILEGE|insufficient\_privilege|
|42846|CANNOT COERCE|cannot\_coerce|
|42803|GROUPING ERROR|grouping\_error|
|42830|INVALID FOREIGN KEY|invalid\_foreign\_key|
|42602|INVALID NAME|invalid\_name|
|42622|NAME TOO LONG|name\_too\_long|
|42939|RESERVED NAME|reserved\_name|
|42804|DATATYPE MISMATCH|datatype\_mismatch|
|42P18|INDETERMINATE DATATYPE|indeterminate\_datatype|
|42809|WRONG OBJECT TYPE|wrong\_object\_type|
|42703|UNDEFINED COLUMN|undefined\_column|
|42883|UNDEFINED FUNCTION|undefined\_function|
|42P01|UNDEFINED TABLE|undefined\_table|
|42P02|UNDEFINED PARAMETER|undefined\_parameter|
|42704|UNDEFINED OBJECT|undefined\_object|
|42701|DUPLICATE COLUMN|duplicate\_column|
|42P03|DUPLICATE CURSOR|duplicate\_cursor|
|42P04|DUPLICATE DATABASE|duplicate\_database|
|42723|DUPLICATE FUNCTION|duplicate\_function|
|42P05|DUPLICATE PREPARED STATEMENT|duplicate\_prepared\_statement|
|42P06|DUPLICATE SCHEMA|duplicate\_schema|
|42P07|DUPLICATE TABLE|duplicate\_table|
|42712|DUPLICATE ALIAS|duplicate\_alias|
|42710|DUPLICATE OBJECT|duplicate\_object|
|42702|AMBIGUOUS COLUMN|ambiguous\_column|
|42725|AMBIGUOUS FUNCTION|ambiguous\_function|
|42P08|AMBIGUOUS PARAMETER|ambiguous\_parameter|
|42P09|AMBIGUOUS ALIAS|ambiguous\_alias|
|42P10|INVALID COLUMN REFERENCE|invalid\_column\_reference|
|42611|INVALID COLUMN DEFINITION|invalid\_column\_definition|
|42P11|INVALID CURSOR DEFINITION|invalid\_cursor\_definition|
|42P12|INVALID DATABASE DEFINITION|invalid\_database\_definition|
|42P13|INVALID FUNCTION DEFINITION|invalid\_function\_definition|
|42P14|INVALID PREPARED STATEMENT DEFINITION|invalid\_prepared\_statement\_definition|
|42P15|INVALID SCHEMA DEFINITION|invalid\_schema\_definition|
|42P16|INVALID TABLE DEFINITION|invalid\_table\_definition|
|42P17|INVALID OBJECT DEFINITION|invalid\_object\_definition|
|**Class 44** — WITH CHECK OPTION Violation|
|44000|WITH CHECK OPTION VIOLATION|with\_check\_option\_violation|
|**Class 53** — Insufficient Resources|
|53000|INSUFFICIENT RESOURCES|insufficient\_resources|
|53100|DISK FULL|disk\_full|
|53200|OUT OF MEMORY|out\_of\_memory|
|53300|TOO MANY CONNECTIONS|too\_many\_connections|
|**Class 54** — Program Limit Exceeded|
|54000|PROGRAM LIMIT EXCEEDED|program\_limit\_exceeded|
|54001|STATEMENT TOO COMPLEX|statement\_too\_complex|
|54011|TOO MANY COLUMNS|too\_many\_columns|
|54023|TOO MANY ARGUMENTS|too\_many\_arguments|
|**Class 55** — Object Not In Prerequisite State|
|55000|OBJECT NOT IN PREREQUISITE STATE|object\_not\_in\_prerequisite\_state|
|55006|OBJECT IN USE|object\_in\_use|
|55P02|CANT CHANGE RUNTIME PARAM|cant\_change\_runtime\_param|
|55P03|LOCK NOT AVAILABLE|lock\_not\_available|
|**Class 57** — Operator Intervention|
|57000|OPERATOR INTERVENTION|operator\_intervention|
|57014|QUERY CANCELED|query\_canceled|
|57P01|ADMIN SHUTDOWN|admin\_shutdown|
|57P02|CRASH SHUTDOWN|crash\_shutdown|
|57P03|CANNOT CONNECT NOW|cannot\_connect\_now|
|**Class 58** — System Error \(errors external to HAWQ \)|
|58030|IO ERROR|io\_error|
|58P01|UNDEFINED FILE|undefined\_file|
|58P02|DUPLICATE FILE|duplicate\_file|
|Class F0 — Configuration File Error|
|F0000|CONFIG FILE ERROR|config\_file\_error|
|F0001|LOCK FILE EXISTS|lock\_file\_exists|
|**Class P0** — PL/pgSQL Error|
|P0000|PLPGSQL ERROR|plpgsql\_error|
|P0001|RAISE EXCEPTION|raise\_exception|
|P0002|NO DATA FOUND|no\_data\_found|
|P0003|TOO MANY ROWS|too\_many\_rows|
|**Class XX** — Internal Error|
|XX000|INTERNAL ERROR|internal\_error|
|XX001|DATA CORRUPTED|data\_corrupted|
|XX002|INDEX CORRUPTED|index\_corrupted|
