---
title: CREATE EXTERNAL TABLE
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

Defines a new external table.

## <a id="topic1__section2"></a>Synopsis

``` pre
CREATE [READABLE] EXTERNAL TABLE <table_name>     
    ( <column_name>
            <data_type> [, ...] | LIKE <other_table> )
      LOCATION ('gpfdist://<filehost>[:<port>]/<file_pattern>[#<transform>]' [, ...])
        | ('gpfdists://<filehost>[:<port>]/<file_pattern>[#<transform>]' [, ...])
        | ('pxf://<host>[:<port>]/<path-to-data><pxf parameters>') 
      FORMAT 'TEXT' 
            [( [HEADER]
               [DELIMITER [AS] '<delimiter>' | 'OFF']
               [NULL [AS] '<null string>']
               [ESCAPE [AS] '<escape>' | 'OFF']
               [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
               [FILL MISSING FIELDS] )]
           | 'CSV'
            [( [HEADER]
               [QUOTE [AS] '<quote>'] 
               [DELIMITER [AS] '<delimiter>']
               [NULL [AS] '<null string>']
               [FORCE NOT NULL <column> [, ...]]
               [ESCAPE [AS] '<escape>']
               [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
               [FILL MISSING FIELDS] )]
           | 'CUSTOM' (Formatter=<formatter specifications>)
     [ ENCODING '<encoding>' ]
     [ [LOG ERRORS INTO <error_table>] SEGMENT REJECT LIMIT <count>
       [ROWS | PERCENT] ]

CREATE [READABLE] EXTERNAL WEB TABLE <table_name>     
   ( <column_name>
            <data_type> [, ...] | LIKE <other_table> )
      LOCATION ('http://<webhost>[:<port>]/<path>/<file>' [, ...])
    | EXECUTE '<command>' ON { MASTER | <number_of_segments> | SEGMENT #<num> }
      FORMAT 'TEXT' 
            [( [HEADER]
               [DELIMITER [AS] '<delimiter>' | 'OFF']
               [NULL [AS] '<null string>']
               [ESCAPE [AS] '<escape>' | 'OFF']
               [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
               [FILL MISSING FIELDS] )]
           | 'CSV'
            [( [HEADER]
               [QUOTE [AS] '<quote>'] 
               [DELIMITER [AS] '<delimiter>']
               [NULL [AS] '<null string>']
               [FORCE NOT NULL <column> [, ...]]
               [ESCAPE [AS] '<escape>']
               [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
               [FILL MISSING FIELDS] )]
           | 'CUSTOM' (Formatter=<formatter specifications>)
     [ ENCODING '<encoding>' ]
     [ [LOG ERRORS INTO <error_table>] SEGMENT REJECT LIMIT <count>
       [ROWS | PERCENT] ]

CREATE WRITABLE EXTERNAL TABLE <table_name>
    ( <column_name>
            <data_type> [, ...] | LIKE <other_table> )
     LOCATION('gpfdist://<outputhost>[:<port>]/<filename>[#<transform>]'
      | ('gpfdists://<outputhost>[:<port>]/<file_pattern>[#<transform>]'
          [, ...])
      | ('pxf://<host>[:<port>]/<path-to-data>?<pxf parameters>'
      FORMAT 'TEXT' 
               [( [DELIMITER [AS] '<delimiter>']
               [NULL [AS] '<null string>']
               [ESCAPE [AS] '<escape>' | 'OFF'] )]
          | 'CSV'
               [([QUOTE [AS] '<quote>'] 
               [DELIMITER [AS] '<delimiter>']
               [NULL [AS] '<null string>']
               [FORCE QUOTE <column> [, ...]] ]
               [ESCAPE [AS] '<escape>'] )]
           | 'CUSTOM' (Formatter=<formatter specifications>)
    [ ENCODING '<write_encoding>' ]
    [ DISTRIBUTED BY (<column>, [ ... ] ) | DISTRIBUTED RANDOMLY ]

CREATE WRITABLE EXTERNAL WEB TABLE <table_name>
    ( <column_name>
            <data_type> [, ...] | LIKE <other_table> )
    EXECUTE '<command>' ON #<num>
    FORMAT 'TEXT' 
               [( [DELIMITER [AS] '<delimiter>']
               [NULL [AS] '<null string>']
               [ESCAPE [AS] '<escape>' | 'OFF'] )]
          | 'CSV'
               [([QUOTE [AS] '<quote>'] 
               [DELIMITER [AS] '<delimiter>']
               [NULL [AS] '<null string>']
               [FORCE QUOTE <column> [, ...]] ]
               [ESCAPE [AS] '<escape>'] )]
          | 'CUSTOM' (Formatter=<formatter specifications>)
    [ ENCODING '<write_encoding>' ]
    [ DISTRIBUTED BY (<column>, [ ... ] ) | DISTRIBUTED RANDOMLY ]
```

where \<pxf parameters\> is:

``` pre
   ?FRAGMENTER=<class>&ACCESSOR=<class>&RESOLVER=<class>[&<custom-option>=<value>...]
 | ?PROFILE=<profile-name>[&<custom-option>=<value>...]
```

## <a id="topic1__section3"></a>Description

`CREATE EXTERNAL TABLE` or `CREATE EXTERNAL WEB TABLE` creates a new readable external table definition in HAWQ. Readable external tables are typically used for fast, parallel data loading. Once an external table is defined, you can query its data directly (and in parallel) using SQL commands. For example, you can select, join, or sort external table data. You can also create views for external tables. DML operations (`UPDATE`, `INSERT`, `DELETE`, or `TRUNCATE`) are not permitted on readable external tables.

`CREATE WRITABLE EXTERNAL TABLE` or `CREATE WRITABLE EXTERNAL WEB           TABLE` creates a new writable external table definition in HAWQ. Writable external tables are typically used for unloading data from the database into a set of files or named pipes.

Writable external web tables can also be used to output data to an executable program. Once a writable external table is defined, data can be selected from database tables and inserted into the writable external table. Writable external tables only allow `INSERT` operations – `SELECT`, `UPDATE`, `DELETE`, or `TRUNCATE` are not allowed.

Regular readable external tables can access static flat files or, by using HAWQ Extensions Framework (PXF), data from other sources. PXF plug-ins are included for HDFS, HBase, and Hive tables. Custom plug-ins can be created for other external data sources using the PXF API.

Web external tables access dynamic data sources – either on a web server or by executing OS commands or scripts.

The LOCATION clause specifies the location of the external data. The location string begins with a protocol string that specifies the storage type and protocol used to access the data. The `gpfdist://` protocol specifies data files served by one or more instances of the HAWQ file server `gpfdist`. The `http://` protocol specifies one or more HTTP URLs and is used with web tables. The `pxf://` protocol specifies data accessed through the PXF service, which provides access to data in a Hadoop system. Using the PXF API, you can create PXF plug-ins to provide HAWQ access to any other data source.

**Note:** The `file://` protocol is deprecated. Instead, use the `gpfdist://`, `gpfdists://`, or `pxf://` protocol, or the `COPY` command instead.

The `FORMAT` clause is used to describe how external table files are formatted. Valid flat file formats, including files in HDFS, are delimited text (`TEXT`) and comma separated values (`CSV`) format for `gpfdist` protocols. If the data in the file does not use the default column delimiter, escape character, null string, and so on, you must specify the additional formatting options so that the data in the external file is read correctly by HAWQ.

## <a id="topic1__section4"></a>Parameters

<dt>READABLE | WRITABLE  </dt>
<dd>Specifiies the type of external table, readable being the default. Readable external tables are used for loading data into HAWQ. Writable external tables are used for unloading data.</dd>

<dt>WEB  </dt>
<dd>Creates a readable or writable web external table definition in HAWQ. There are two forms of readable web external tables – those that access files via the `http://` protocol or those that access data by executing OS commands. Writable web external tables output data to an executable program that can accept an input stream of data. Web external tables are not rescannable during query execution.</dd>

<dt> \<table\_name\>   </dt>
<dd>The name of the new external table.</dd>

<dt> \<column\_name\>   </dt>
<dd>The name of a column to create in the external table definition. Unlike regular tables, external tables do not have column constraints or default values, so do not specify those.</dd>

<dt>LIKE \<other\_table\>   </dt>
<dd>The `LIKE` clause specifies a table from which the new external table automatically copies all column names, data types and HAWQ distribution policy. If the original table specifies any column constraints or default column values, those will not be copied over to the new external table definition.</dd>

<dt> \<data\_type\>   </dt>
<dd>The data type of the column.</dd>

<dt>LOCATION ('\<protocol\>://\<host\>\[:\<port\>\]/\<path\>/\<file\>' \[, ...\])   </dt>
<dd>For readable external tables, specifies the URI of the external data source(s) to be used to populate the external table or web table. Regular readable external tables allow the `file`, `gpfdist`, and `pxf` protocols. Web external tables allow the `http` protocol. If \<port\> is omitted, the `http` and `gpfdist` protocols assume port `8080` and the `pxf` protocol assumes the \<host\> specifies a high availability Nameservice ID. If using the `gpfdist` protocol, the \<path\> is relative to the directory from which `gpfdist` is serving files (the directory specified when you started the `gpfdist` program). Also, the \<path\> can use wildcards (or other C-style pattern matching) in the \<file\> name part of the location to denote multiple files in a directory. For example:

``` pre
'gpfdist://filehost:8081/*'
'gpfdist://masterhost/my_load_file'
'http://intranet.example.com/finance/expenses.csv'
'pxf://mdw:41200/sales/*.csv?Profile=HDFS'
```

For writable external tables, specifies the URI location of the `gpfdist` process that will collect data output from the HAWQ segments and write it to the named file. The \<path\> is relative to the directory from which `gpfdist` is serving files (the directory specified when you started the `gpfdist` program). If multiple `gpfdist` locations are listed, the segments sending data will be evenly divided across the available output locations. For example:

``` pre
'gpfdist://outputhost:8081/data1.out',
'gpfdist://outputhost:8081/data2.out'
```

With two `gpfdist` locations listed as in the above example, half of the segments would send their output data to the `data1.out` file and the other half to the `data2.out` file.

For the `pxf` protocol, the `LOCATION` string specifies the HDFS NameNode \<host\> and the \<port\> of the PXF service, the location of the data, and the PXF profile or Java classes used to convert the data between storage format and HAWQ format. If the \<port\> is omitted, the \<host\> is taken to be the logical name for the high availability Nameservice, and the \<port\> is the value of the `pxf_service_port` configuration parameter, 51200 by default. The URL parameters `FRAGMENTER`, `ACCESSOR`, and `RESOLVER` are the names of PXF plug-ins (Java classes) that convert between the external data format and HAWQ data format. The `FRAGMENTER` parameter is only used with readable external tables. PXF allows combinations of these parameters to be configured as profiles so that a single `PROFILE` parameter can be specified to access external data, for example `?PROFILE=Hive`. Additional \<custom-option\>s can be added to the LOCATION URI to further describe the external data format or storage options. For details about the plug-ins and profiles provided with PXF and information about creating custom plug-ins for other data sources see [Using PXF with Unmanaged Data](../../pxf/HawqExtensionFrameworkPXF.html).</dd>

<dt>EXECUTE '\<command\>' ON ...  </dt>
<dd>Allowed for readable web external tables or writable external tables only. For readable web external tables, specifies the OS command to be executed by the segment instances. The \<command\> can be a single OS command or a script. If \<command\> executes a script, that script must reside in the same location on all of the segment hosts and be executable by the HAWQ superuser (`gpadmin`).

For writable external tables, the \<command\> specified in the `EXECUTE` clause must be prepared to have data piped into it, as segments having data to send write their output to the specified program. HAWQ uses virtual elastic segments to run its queries.

The `ON` clause is used to specify which segment instances will execute the given command. For writable external tables, only `ON` \<number\> is supported.

**Note:** ON ALL/HOST is deprecated when creating a readable external table, as HAWQ cannot guarantee scheduling executors on a specific host. Instead, use `ON                 MASTER`, `ON <number>`, or `SEGMENT <virtual_segment>` to specify which segment instances will execute the command.

-   `ON MASTER` runs the command on the master host only.
-   `ON <number>` means the command will be executed by the specified number of virtual segments. The particular segments are chosen by the HAWQ system's Resource Manager at runtime.
-   `ON SEGMENT <virtual_segment>` means the command will be executed only once by the specified segment.
</dd>

<dt>FORMAT 'TEXT | CSV' (\<options\>)   </dt>
<dd>Specifies the format of the external or web table data - either plain text (`TEXT`) or comma separated values (`CSV`) format.</dd>

<dt>DELIMITER  </dt>
<dd>Specifies a single ASCII character that separates columns within each row (line) of data. The default is a tab character in `TEXT` mode, a comma in `CSV` mode. In `TEXT` mode for readable external tables, the delimiter can be set to `OFF` for special use cases in which unstructured data is loaded into a single-column table.</dd>

<dt>NULL  </dt>
<dd>Specifies the string that represents a `NULL` value. The default is `\N` (backslash-N) in `TEXT` mode, and an empty value with no quotations in `CSV` mode. You might prefer an empty string even in `TEXT` mode for cases where you do not want to distinguish `NULL` values from empty strings. When using external and web tables, any data item that matches this string will be considered a `NULL` value.</dd>

<dt>ESCAPE  </dt>
<dd>Specifies the single character that is used for C escape sequences (such as `\n`,`\t`,`\100`, and so on) and for escaping data characters that might otherwise be taken as row or column delimiters. Make sure to choose an escape character that is not used anywhere in your actual column data. The default escape character is a \\ (backslash) for text-formatted files and a `"` (double quote) for csv-formatted files, however it is possible to specify another character to represent an escape. It is also possible to disable escaping in text-formatted files by specifying the value `'OFF'` as the escape value. This is very useful for data such as text-formatted web log data that has many embedded backslashes that are not intended to be escapes.</dd>

<dt>NEWLINE  </dt>
<dd>Specifies the newline used in your data files – `LF` (Line feed, 0x0A), `CR` (Carriage return, 0x0D), or `CRLF` (Carriage return plus line feed, 0x0D 0x0A). If not specified, a HAWQ segment will detect the newline type by looking at the first row of data it receives and using the first newline type encountered.</dd>

<dt>HEADER  </dt>
<dd>For readable external tables, specifies that the first line in the data file(s) is a header row (contains the names of the table columns) and should not be included as data for the table. If using multiple data source files, all files must have a header row.

**Note:** The `HEADER` formatting option is not allowed with PXF.
For CSV files or other files that include a header line, use an error table instead of the `HEADER` formatting option.</dd>

<dt>QUOTE  </dt>
<dd>Specifies the quotation character for `CSV` mode. The default is double-quote (`"`).</dd>

<dt>FORCE NOT NULL  </dt>
<dd>In `CSV` mode, processes each specified column as though it were quoted and hence not a `NULL` value. For the default null string in `CSV` mode (nothing between two delimiters), this causes missing values to be evaluated as zero-length strings.</dd>

<dt>FORCE QUOTE  </dt>
<dd>In `CSV` mode for writable external tables, forces quoting to be used for all non-`NULL` values in each specified column. `NULL` output is never quoted.</dd>

<dt>FILL MISSING FIELDS  </dt>
<dd>In both `TEXT` and `CSV` mode for readable external tables, specifying `FILL MISSING FIELDS` will set missing trailing field values to `NULL` (instead of reporting an error) when a row of data has missing data fields at the end of a line or row. Blank rows, fields with a `NOT               NULL` constraint, and trailing delimiters on a line will still report an error.</dd>

<dt>ENCODING '\<encoding\>'   </dt>
<dd>Character set encoding to use for the external table. Specify a string constant (such as `'SQL_ASCII'`), an integer encoding number, or `DEFAULT` to use the default client encoding.</dd>

<dt>LOG ERRORS INTO \<error\_table\>  </dt>
<dd>This is an optional clause that can precede a `SEGMENT REJECT LIMIT` clause to log information about rows with formatting errors. It specifies an error table where rows with formatting errors will be logged when running in single row error isolation mode. You can then examine this \<error\_table\> to see error rows that were not loaded (if any). If the \<error\_table\> specified already exists, it will be used. If it does not exist, it will be automatically generated.</dd>

<dt>SEGMENT REJECT LIMIT \<count\> \[ROWS | PERCENT\]  </dt>
<dd>Runs a `COPY FROM` operation in single row error isolation mode. If the input rows have format errors they will be discarded provided that the reject limit \<count\> is not reached on any HAWQ segment instance during the load operation. The reject limit \<count\> can be specified as number of rows (the default) or percentage of total rows (1-100). If `PERCENT` is used, each segment starts calculating the bad row percentage only after the number of rows specified by the parameter `gp_reject_percent_threshold` has been processed. The default for `gp_reject_percent_threshold` is 300 rows. Constraint errors such as violation of a `NOT NULL` or `CHECK` constraint will still be handled in "all-or-nothing" input mode. If the limit is not reached, all good rows will be loaded and any error rows discarded.</dd>

<dt>DISTRIBUTED RANDOMLY  </dt>
<dd>Used to declare the HAWQ distribution policy for a writable external table. By default, writable external tables are distributed randomly. If the source table you are exporting data from has a hash distribution policy, defining the same distribution key column(s) for the writable external table will improve unload performance by eliminating the need to move rows over the interconnect. When you issue an unload command such as `INSERT INTO wex_table SELECT * FROM                 source_table             `, the rows that are unloaded can be sent directly from the segments to the output location if the two tables have the same hash distribution policy.</dd>

## <a id="topic1__section5"></a>Examples

Start the `gpfdist` file server program in the background on port `8081` serving files from directory `/var/data/staging`:

``` pre
gpfdist -p 8081 -d /var/data/staging -l /home/gpadmin/log &
```

Create a readable external table named `ext_customer` using the `gpfdist` protocol and any text formatted files (`*.txt`) found in the `gpfdist` directory. The files are formatted with a pipe (`|`) as the column delimiter and an empty space as `NULL`. Also access the external table in single row error isolation mode:

``` pre
CREATE EXTERNAL TABLE ext_customer
   (id int, name text, sponsor text) 
   LOCATION ( 'gpfdist://filehost:8081/*.txt' ) 
   FORMAT 'TEXT' ( DELIMITER '|' NULL ' ')
   LOG ERRORS INTO err_customer SEGMENT REJECT LIMIT 5;
```

Create the same readable external table definition as above, but with CSV formatted files:

``` pre
CREATE EXTERNAL TABLE ext_customer 
   (id int, name text, sponsor text) 
   LOCATION ( 'gpfdist://filehost:8081/*.csv' ) 
   FORMAT 'CSV' ( DELIMITER ',' );
```

Create a readable external table using the `pxf` protocol to read data in HDFS files:

``` pre
CREATE EXTERNAL TABLE ext_customer 
    (id int, name text, sponsor text)
LOCATION ('pxf://mdw:51200/sales/customers/customers.tsv.gz'
          '?Fragmenter=org.apache.hawq.pxf.plugins.hdfs.HdfsDataFragmenter'
          '&Accessor=org.apache.hawq.pxf.plugins.hdfs.LineBreakAccessor'
          '&Resolver=org.apache.hawq.pxf.plugins.hdfs.StringPassResolver')
FORMAT 'TEXT' (DELIMITER = E'\t');
```

The `LOCATION` string in this command is equivalent to the previous example, but using a PXF Profile:

``` pre
CREATE EXTERNAL TABLE ext_customer 
    (id int, name text, sponsor text)
LOCATION ('pxf://mdw:51200/sales/customers/customers.tsv.gz?Profile=HdfsTextSimple')
FORMAT 'TEXT' (DELIMITER = E'\t');
```

Create a readable web external table that executes a script on five virtual segment hosts. (The script must reside at the same location on all segment hosts.)

``` pre
CREATE EXTERNAL WEB TABLE log_output (linenum int, message text)  
EXECUTE '/var/load_scripts/get_log_data.sh' ON 5 
FORMAT 'TEXT' (DELIMITER '|');
```

Create a writable external table named `sales_out` that uses `gpfdist` to write output data to a file named `sales.out`. The files are formatted with a pipe (`|`) as the column delimiter and an empty space as `NULL`.

``` pre
CREATE WRITABLE EXTERNAL TABLE sales_out (LIKE sales) 
   LOCATION ('gpfdist://etl1:8081/sales.out')
   FORMAT 'TEXT' ( DELIMITER '|' NULL ' ')
   DISTRIBUTED BY (txn_id);
```

The following command sequence shows how to create a writable external web table using a specified number of elastic virtual segments to run the query:

``` pre
postgres=# CREATE TABLE a (i int);
CREATE TABLE
postgres=# INSERT INTO a VALUES(1);
INSERT 0 1
postgres=# INSERT INTO a VALUES(2);
INSERT 0 1
postgres=# INSERT INTO a VALUES(10);
INSERT 0 1
postgres=# CREATE WRITABLE EXTERNAL WEB TABLE externala (output text) 
postgres-# EXECUTE 'cat > /tmp/externala' ON 3 
postgres-# FORMAT 'TEXT' DISTRIBUTED RANDOMLY;
CREATE EXTERNAL TABLE
postgres=# INSERT INTO externala SELECT * FROM a;
INSERT 0 3
```

Create a writable external web table that pipes output data received by the segments to an executable script named `to_adreport_etl.sh`:

``` pre
CREATE WRITABLE EXTERNAL WEB TABLE campaign_out (LIKE campaign)  
EXECUTE '/var/unload_scripts/to_adreport_etl.sh'
FORMAT 'TEXT' (DELIMITER '|');
```

Use the writable external table defined above to unload selected data:

``` pre
INSERT INTO campaign_out 
    SELECT * FROM campaign WHERE customer_id=123;
```

## <a id="topic1__section6"></a>Compatibility

`CREATE EXTERNAL TABLE` is a HAWQ extension. The SQL standard makes no provisions for external tables.

## <a id="topic1__section7"></a>See Also

[CREATE TABLE](CREATE-TABLE.html), [CREATE TABLE AS](CREATE-TABLE-AS.html), [COPY](COPY.html), [INSERT](INSERT.html), [SELECT INTO](SELECT-INTO.html)
