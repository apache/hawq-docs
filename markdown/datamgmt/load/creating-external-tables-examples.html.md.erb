---
title: Creating External Tables - Examples
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

The following examples show how to define external data with different protocols. Each `CREATE EXTERNAL TABLE` command can contain only one protocol.

**Note:** When using IPv6, always enclose the numeric IP addresses in square brackets.

Start `gpfdist` before you create external tables with the `gpfdist` protocol. The following code starts the `gpfdist` file server program in the background on port *8081* serving files from directory `/var/data/staging`. The logs are saved in `/home/gpadmin/log`.

``` shell
$ gpfdist -p 8081 -d /var/data/staging -l /home/gpadmin/log &
```

## <a id="ex1"></a>Example 1 - Single gpfdist instance on single-NIC machine

Creates a readable external table, `ext_expenses`, using the `gpfdist` protocol. The files are formatted with a pipe (|) as the column delimiter.

``` sql
=# CREATE EXTERNAL TABLE ext_expenses
        ( name text, date date, amount float4, category text, desc1 text )
    LOCATION ('gpfdist://etlhost-1:8081/*')
    FORMAT 'TEXT' (DELIMITER '|');
```

## <a id="ex2"></a>Example 2 - Multiple gpfdist instances

Creates a readable external table, *ext\_expenses*, using the `gpfdist` protocol from all files with the *txt* extension. The column delimiter is a pipe ( | ) and NULL is a space (' ').

``` sql
=# CREATE EXTERNAL TABLE ext_expenses
        ( name text, date date, amount float4, category text, desc1 text )
    LOCATION ('gpfdist://etlhost-1:8081/*.txt', 'gpfdist://etlhost-2:8081/*.txt')
    FORMAT 'TEXT' ( DELIMITER '|' NULL ' ') ;
    
```

## <a id="ex3"></a>Example 3 - Multiple gpfdists instances

Creates a readable external table, *ext\_expenses,* from all files with the *txt* extension using the `gpfdists` protocol. The column delimiter is a pipe ( | ) and NULL is a space (' '). For information about the location of security certificates, see [gpfdists Protocol](g-gpfdists-protocol.html).

1.  Run `gpfdist` with the `--ssl` option.
2.  Run the following command.

    ``` sql
    =# CREATE EXTERNAL TABLE ext_expenses
             ( name text, date date, amount float4, category text, desc1 text )
        LOCATION ('gpfdists://etlhost-1:8081/*.txt', 'gpfdists://etlhost-2:8082/*.txt')
        FORMAT 'TEXT' ( DELIMITER '|' NULL ' ') ;
        
    ```

## <a id="ex4"></a>Example 4 - Single gpfdist instance with error logging

Uses the gpfdist protocol to create a readable external table, `ext_expenses,` from all files with the *txt* extension. The column delimiter is a pipe ( | ) and NULL (' ') is a space.

Access to the external table is single row error isolation mode. Input data formatting errors can be captured so that you can view the errors, fix the issues, and then reload the rejected data. If the error count on a segment is greater than five (the `SEGMENT REJECT LIMIT` value), the entire external table operation fails and no rows are processed.

``` sql
=# CREATE EXTERNAL TABLE ext_expenses
         ( name text, date date, amount float4, category text, desc1 text )
    LOCATION ('gpfdist://etlhost-1:8081/*.txt', 'gpfdist://etlhost-2:8082/*.txt')
    FORMAT 'TEXT' ( DELIMITER '|' NULL ' ')
    LOG ERRORS INTO expenses_errs SEGMENT REJECT LIMIT 5;
    
```

To create the readable `ext_expenses` table from CSV-formatted text files:

``` sql
=# CREATE EXTERNAL TABLE ext_expenses
         ( name text, date date, amount float4, category text, desc1 text )
    LOCATION ('gpfdist://etlhost-1:8081/*.txt', 'gpfdist://etlhost-2:8082/*.txt')
    FORMAT 'CSV' ( DELIMITER ',' )
    LOG ERRORS INTO expenses_errs SEGMENT REJECT LIMIT 5;
    
```

## <a id="ex5"></a>Example 5 - Readable Web External Table with Script

Creates a readable web external table that executes a script once on five virtual segments:

``` sql
=# CREATE EXTERNAL WEB TABLE log_output (linenum int, message text)
    EXECUTE '/var/load_scripts/get_log_data.sh' ON 5
    FORMAT 'TEXT' (DELIMITER '|');
    
```

## <a id="ex6"></a>Example 6 - Writable External Table with gpfdist

Creates a writable external table, *sales\_out*, that uses `gpfdist` to write output data to the file *sales.out*. The column delimiter is a pipe ( | ) and NULL is a space (' '). The file will be created in the directory specified when you started the gpfdist file server.

``` sql
=# CREATE WRITABLE EXTERNAL TABLE sales_out (LIKE sales)
    LOCATION ('gpfdist://etl1:8081/sales.out')
    FORMAT 'TEXT' ( DELIMITER '|' NULL ' ')
    DISTRIBUTED BY (txn_id);
    
```

## <a id="ex7"></a>Example 7 - Writable External Web Table with Script

Creates a writable external web table, `campaign_out`, that pipes output data recieved by the segments to an executable script, `to_adreport_etl.sh`:

``` sql
=# CREATE WRITABLE EXTERNAL WEB TABLE campaign_out
        (LIKE campaign)
        EXECUTE '/var/unload_scripts/to_adreport_etl.sh' ON 6
        FORMAT 'TEXT' (DELIMITER '|');
```

## <a id="ex8"></a>Example 8 - Readable and Writable External Tables with XML Transformations

HAWQ can read and write XML data to and from external tables with gpfdist. For information about setting up an XML transform, see [Transforming XML Data](g-transforming-xml-data.html#topic75).


