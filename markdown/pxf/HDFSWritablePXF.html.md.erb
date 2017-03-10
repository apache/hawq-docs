---
title: Writing Data to HDFS
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

The PXF HDFS plug-in supports writable external tables using the `HdfsTextSimple` and `SequenceWritable` profiles.  You might create a writable table to export data from a HAWQ internal table to binary or text HDFS files.

Use the `HdfsTextSimple` profile when writing text data. Use the `SequenceWritable` profile when dealing with binary data.

This section describes how to use these PXF profiles to create writable external tables.

**Note**: Tables that you create with writable profiles can only be used for INSERT operations.  If you want to query inserted data, you must define a separate external readable table that references the new HDFS file using the equivalent readable profile.

## <a id="pxfwrite_prereq"></a>Prerequisites

Before working with HDFS file data using HAWQ and PXF, ensure that:

-   The HDFS plug-in is installed on all cluster nodes. See [Installing PXF Plug-ins](InstallPXFPlugins.html) for PXF plug-in installation information.
-   All HDFS users have read permissions to HDFS services.
-   HDFS write permissions are provided to a restricted set of users.

## <a id="hdfsplugin_writeextdata"></a>Writing to PXF External Tables
The PXF HDFS plug-in supports two writable profiles: `HdfsTextSimple` and `SequenceWritable`.

Use the following syntax to create a HAWQ external writable table representing HDFS data: 

``` sql
CREATE WRITABLE EXTERNAL TABLE <table_name> 
    ( <column_name> <data_type> [, ...] | LIKE <other_table> )
LOCATION ('pxf://<host>[:<port>]/<path-to-hdfs-file>
    ?PROFILE=HdfsTextSimple|SequenceWritable[&<custom-option>=<value>[...]]')
FORMAT '[TEXT|CSV|CUSTOM]' (<formatting-properties>);
```

HDFS-plug-in-specific keywords and values used in the [CREATE EXTERNAL TABLE](../reference/sql/CREATE-EXTERNAL-TABLE.html) call are described in the table below.

| Keyword  | Value |
|-------|-------------------------------------|
| \<host\>    | The PXF host. While \<host\> may identify any PXF agent node, use the HDFS NameNode as it is guaranteed to be available in a running HDFS cluster. If HDFS High Availability is enabled, \<host\> must identify the HDFS NameService. |
| \<port\>    | The PXF port. If \<port\> is omitted, PXF assumes \<host\> identifies a High Availability HDFS Nameservice and connects to the port number designated by the `pxf_service_port` server configuration parameter value. Default is 51200. |
| \<path-to-hdfs-file\>    | The path to the file in the HDFS data store. |
| PROFILE    | The `PROFILE` keyword must specify one of the values `HdfsTextSimple` or `SequenceWritable`. |
| \<custom-option\>  | \<custom-option\> is profile-specific. These options are discussed in the next topic.|
| FORMAT 'TEXT' | Use '`TEXT`' `FORMAT` with the `HdfsTextSimple` profile to create a plain-text-delimited file at the location specified by \<path-to-hdfs-file\>. The `HdfsTextSimple` '`TEXT`' `FORMAT` supports only the built-in `(delimiter=<delim>)` \<formatting-property\>. |
| FORMAT 'CSV' | Use '`CSV`' `FORMAT` with the `HdfsTextSimple` profile to create a comma-separated-value file at the location specified by \<path-to-hdfs-file\>.  |
| FORMAT 'CUSTOM' | Use the `'CUSTOM'` `FORMAT` with the `SequenceWritable` profile. The `SequenceWritable` '`CUSTOM`' `FORMAT` supports only the built-in `(formatter='pxfwritable_export)` (write) and `(formatter='pxfwritable_import)` (read) \<formatting-properties\>.

**Note**: When creating PXF external tables, you cannot use the `HEADER` option in your `FORMAT` specification.

## <a id="profile_hdfstextsimple"></a>Custom Options

The `HdfsTextSimple` and `SequenceWritable` profiles support the following custom options:

| Option  | Value Description | Profile |
|-------|-------------------------------------|--------|
| COMPRESSION_CODEC    | The compression codec Java class name. If this option is not provided, no data compression is performed. Supported compression codecs include: `org.apache.hadoop.io.compress.DefaultCodec` and `org.apache.hadoop.io.compress.BZip2Codec` | HdfsTextSimple, SequenceWritable |
|  COMPRESSION_CODEC  |  `org.apache.hadoop.io.compress.GzipCodec` | HdfsTextSimple |
| COMPRESSION_TYPE    | The compression type to employ; supported values are `RECORD` (the default) or `BLOCK`. | HdfsTextSimple, SequenceWritable |
| DATA-SCHEMA    | The name of the writer serialization/deserialization class. The jar file in which this class resides must be in the PXF classpath. This option is required for the `SequenceWritable` profile and has no default value. | SequenceWritable|
| THREAD-SAFE | Boolean value determining if a table query can run in multi-threaded mode. The default value is `TRUE`. Set this option to `FALSE` to handle all requests in a single thread for operations that are not thread-safe (for example, compression). | HdfsTextSimple, SequenceWritable| 

## <a id="profile_hdfstextsimple"></a>HdfsTextSimple Profile

Use the `HdfsTextSimple` profile when writing delimited data to a plain text file where each line is a single record.

Writable tables created using the `HdfsTextSimple` profile can optionally use record or block compression. The following compression codecs are supported:

- org.apache.hadoop.io.compress.DefaultCodec
- org.apache.hadoop.io.compress.GzipCodec
- org.apache.hadoop.io.compress.BZip2Codec

The `HdfsTextSimple` profile supports the following \<formatting-properties\>:

| Keyword  | Value |
|-------|-------------------------------------|
| delimiter    | The delimiter character to use when writing the file. Default value is a comma `,`.|


### <a id="profile_hdfstextsimple_writing"></a>Example: Writing Data Using the HdfsTextSimple Profile

This example uses the data schema introduced in [Example: Using the HdfsTextSimple Profile] (HDFSFileDataPXF.html#profile_hdfstextsimple_query):


| Field Name  | Data Type |
|-------|-------------------------------------|
| location | text |
| month | text |
| number\_of\_orders | int |
| total\_sales | float8 |

This example also uses the HAWQ table `pxf_hdfs_textsimple` created in that exercise and expects it to exist.


Perform the following operations to use the PXF `HdfsTextSimple` profile to create a HAWQ writable external table with the same data schema as defined above. You will also create a separate external readable table to read the associated HDFS file.

1. Create a writable HAWQ external table with the data schema described above. Write to the HDFS file `/data/pxf_examples/pxfwritable_hdfs_textsimple1`. Create the table specifying a comma `,` as the delimiter:

    ``` sql
    gpadmin=# CREATE WRITABLE EXTERNAL TABLE pxf_hdfs_writabletbl_1(location text, month text, num_orders int, total_sales float8)
                LOCATION ('pxf://namenode:51200/data/pxf_examples/pxfwritable_hdfs_textsimple1?PROFILE=HdfsTextSimple')
              FORMAT 'TEXT' (delimiter=E',');
    ```
    
    The `FORMAT` subclause `delimiter` value is specified as the single ascii comma character `,`. `E` escapes the character.

2. Write a few records to the `pxfwritable_hdfs_textsimple1` HDFS file by invoking the SQL `INSERT` command on `pxf_hdfs_writabletbl_1`:

    ``` sql
    gpadmin=# INSERT INTO pxf_hdfs_writabletbl_1 VALUES ( 'Frankfurt', 'Mar', 777, 3956.98 );
    gpadmin=# INSERT INTO pxf_hdfs_writabletbl_1 VALUES ( 'Cleveland', 'Oct', 3812, 96645.37 );
    ```

3. Insert the contents of the `pxf_hdfs_textsimple` table created in [Example: Using the HdfsTextSimple Profile] (HDFSFileDataPXF.html#profile_hdfstextsimple_query) into `pxf_hdfs_writabletbl_1`:

    ``` sql
    gpadmin=# INSERT INTO pxf_hdfs_writabletbl_1 SELECT * FROM pxf_hdfs_textsimple;
    ```

4. View the file contents in HDFS:

    ``` shell
    $ hdfs dfs -cat /data/pxf_examples/pxfwritable_hdfs_textsimple1/*
    Frankfurt,Mar,777,3956.98
    Cleveland,Oct,3812,96645.37
    Prague,Jan,101,4875.33
    Rome,Mar,87,1557.39
    Bangalore,May,317,8936.99
    Beijing,Jul,411,11600.67
    ```

    Because you specified comma `,` as the delimiter, this character is the field separator used in each record of the HDFS file.

5. Querying an external writable table is not supported in HAWQ. To query data from the newly-created HDFS file, create a readable external HAWQ table referencing the HDFS file:

    ``` sql
    gpadmin=# CREATE EXTERNAL TABLE pxf_hdfs_textsimple_r1(location text, month text, num_orders int, total_sales float8)
                LOCATION ('pxf://namenode:51200/data/pxf_examples/pxfwritable_hdfs_textsimple1?PROFILE=HdfsTextSimple')
			    FORMAT 'CSV';
    ```

    Specify the `'CSV'` `FORMAT` for the readable table, because you created the writable table with a comma `,` as the delimiter character.

6. Query the readable external table `pxf_hdfs_textsimple_r1`:

    ``` sql
    gpadmin=# SELECT * FROM pxf_hdfs_textsimple_r1;
    ```

    ``` pre
     location  | month | num_orders | total_sales
    -----------+-------+------------+-------------
      Frankfurt | Mar   |        777 |     3956.98
      Cleveland | Oct   |       3812 |    96645.37
      Prague    | Jan   |        101 |     4875.33
      Rome      | Mar   |         87 |     1557.39
      Bangalore | May   |        317 |     8936.99
      Beijing   | Jul   |        411 |    11600.67
    (6 rows)
    ```

    The table includes the records you individually inserted, as well as the full contents of the `pxf_hdfs_textsimple` table.

7. Create a second HAWQ external writable table, this time using Gzip compression and employing a colon `:` as the delimiter:

    ``` sql
    gpadmin=# CREATE WRITABLE EXTERNAL TABLE pxf_hdfs_writabletbl_2 (location text, month text, num_orders int, total_sales float8)
                LOCATION ('pxf://namenode:51200/data/pxf_examples/pxfwritable_hdfs_textsimple2?PROFILE=HdfsTextSimple&COMPRESSION_CODEC=org.apache.hadoop.io.compress.GzipCodec')
              FORMAT 'TEXT' (delimiter=E':');
    ```

8. Write a few records to the `pxfwritable_hdfs_textsimple2` HDFS file by inserting into the `pxf_hdfs_writabletbl_2` table:

    ``` sql
    gpadmin=# INSERT INTO pxf_hdfs_writabletbl_2 VALUES ( 'Frankfurt', 'Mar', 777, 3956.98 );
    gpadmin=# INSERT INTO pxf_hdfs_writabletbl_2 VALUES ( 'Cleveland', 'Oct', 3812, 96645.37 );
    ```

9. View the file contents in HDFS; use the `-text` option to `hdfs dfs` to view the compressed data as text:

    ``` shell
    $ hdfs dfs -text /data/pxf_examples/pxfwritable_hdfs_textsimple2/*
    Frankfurt:Mar:777:3956.98
    Cleveland:Oct:3812:96645.3
    ```

    Notice that the colon `:` is the field separator in the HDFS file.

    As described in Step 5 above, to query data from the newly-created HDFS file named `pxfwritable_hdfs_textsimple2`, you can create a readable external HAWQ table referencing this HDFS file.


## <a id="profile_hdfsseqwritable_using"></a>SequenceWritable Profile

Use the HDFS plug-in `SequenceWritable` profile when writing SequenceFile format files. Files of this type consist of binary key/value pairs. Sequence files are a common data transfer format between MapReduce jobs. 

SequenceFile format files can optionally use record or block compression. The following compression codecs are supported:

- org.apache.hadoop.io.compress.DefaultCodec
- org.apache.hadoop.io.compress.BZip2Codec

When using the `SequenceWritable` profile to write a SequenceFile format file, you must provide the name of the Java class to use for serializing/deserializing the data. This class must provide read and write methods for the fields in the schema associated with the data.

### <a id="profile_hdfsseqwritable_writing"></a>Example: Writing Data Using the SequenceWritable Profile

In this example, you will create a Java class named `PxfExample_CustomWritable` that will serialize/deserialize the fields in the sample schema used in previous examples. You will then use this class to access a writable external table created with the `SequenceWritable` profile. 

Perform the following steps to create the Java class and writable table.

1. Prepare to create the sample Java class:

    ``` shell
    $ mkdir -p pxfex/com/hawq/example/pxf/hdfs/writable/dataschema
    $ cd pxfex/com/hawq/example/pxf/hdfs/writable/dataschema
    $ vi PxfExample_CustomWritable.java
    ```

2. Copy and paste the following text into the `PxfExample_CustomWritable.java` file:

    ``` java
    package com.hawq.example.pxf.hdfs.writable.dataschema;
    
    import org.apache.hadoop.io.*;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
import java.lang.reflect.Field;

    /**
 * PxfExample_CustomWritable class - used to serialize and deserialize data with
 * text, int, and float data types
 */
public class PxfExample_CustomWritable implements Writable {

    public String st1, st2;
    public int int1;
    public float ft;

    public PxfExample_CustomWritable() {
        st1 = new String("");
        st2 = new String("");
        int1 = 0;
        ft = 0.f;
    }

    public PxfExample_CustomWritable(int i1, int i2, int i3) {

        st1 = new String("short_string___" + i1);
        st2 = new String("short_string___" + i1);
        int1 = i2;
        ft = i1 * 10.f * 2.3f;

    }

    String GetSt1() {
        return st1;
    }

    String GetSt2() {
        return st2;
    }

    int GetInt1() {
        return int1;
    }
    
    float GetFt() {
        return ft;
    }

    @Override
    public void write(DataOutput out) throws IOException {

        Text txt = new Text();
        txt.set(st1);
        txt.write(out);
        txt.set(st2);
        txt.write(out);

        IntWritable intw = new IntWritable();
        intw.set(int1);
        intw.write(out);

        FloatWritable fw = new FloatWritable();
        fw.set(ft);
        fw.write(out);
    }

    @Override
    public void readFields(DataInput in) throws IOException {

        Text txt = new Text();
        txt.readFields(in);
        st1 = txt.toString();
        txt.readFields(in);
        st2 = txt.toString();

        IntWritable intw = new IntWritable();
        intw.readFields(in);
        int1 = intw.get();

        FloatWritable fw = new FloatWritable();
        fw.readFields(in);
        ft = fw.get();
    }

    public void printFieldTypes() {
        Class myClass = this.getClass();
        Field[] fields = myClass.getDeclaredFields();

        for (int i = 0; i < fields.length; i++) {
            System.out.println(fields[i].getType().getName());
        }
    }
}
    ```

3. Compile and create a Java class JAR file for `PxfExample_CustomWritable`:

    ``` shell
    $ javac -classpath /usr/hdp/2.5.3.0-37/hadoop/hadoop-common.jar  PxfExample_CustomWritable.java
    $ cd ../../../../../../../
    $ jar cf pxfex-customwritable.jar com
    $ cp pxfex-customwritable.jar /tmp/
    ```

    (Your Hadoop library classpath may differ.)

4. Include the new jar file in the PXF Agent classpath by updating the `pxf-public.classpath` file. If you use Ambari to manage your cluster, add the following line via the Ambari UI and restart the PXF Agent:

    ``` pre
    /tmp/pxfex-customwritable.jar
    ```

    If you have a command-line-managed HAWQ cluster, perform the following steps on each node in your HAWQ cluster:
   - Directly edit `/etc/pxf/conf/pxf-public.classpath` and add the line above.
   - Restart the PXF Agent:

        ``` shell
        $ sudo service pxf-service restart
        ```

5. Use the PXF `SequenceWritable` profile to create a writable HAWQ external table. Identify the serialization/deserialization Java class you created above in the `DATA-SCHEMA` \<custom-option\>. Use `BLOCK` mode compression with `BZip2` when creating the writable table.

    ``` sql
    gpadmin=# CREATE WRITABLE EXTERNAL TABLE pxf_tbl_seqwrit (location text, month text, number_of_orders integer, total_sales real)
                LOCATION ('pxf://namenode:51200/data/pxf_examples/pxf_seqwrit_file?PROFILE=SequenceWritable&DATA-SCHEMA=com.hawq.example.pxf.hdfs.writable.dataschema.PxfExample_CustomWritable&COMPRESSION_TYPE=BLOCK&COMPRESSION_CODEC=org.apache.hadoop.io.compress.BZip2Codec')
              FORMAT 'CUSTOM' (formatter='pxfwritable_export');
    ```

    Notice that the `'CUSTOM'` `FORMAT` \<formatting-properties\> specify the built-in `pxfwritable_export` formatter.

6. Insert some data into `pxf_tbl_seqwrit`:

    ``` sql
    gpadmin=# INSERT INTO pxf_tbl_seqwrit VALUES ( 'Frankfurt', 'Mar', 777, 3956.98 );
    gpadmin=# INSERT INTO pxf_tbl_seqwrit VALUES ( 'Cleveland', 'Oct', 3812, 96645.37 );
    ```

6. Recall that querying an external writable table is not supported in HAWQ. To read the newly-created writable table, create a HAWQ readable external table referencing the writable table's HDFS file:

    ``` sql
    gpadmin=# CREATE EXTERNAL TABLE read_pxf_tbl_seqwrit (location text, month text, number_of_orders integer, total_sales real)
                LOCATION ('pxf://namenode:51200/data/pxf_examples/pxf_seqwrit_file?PROFILE=SequenceWritable&DATA-SCHEMA=com.hawq.example.pxf.hdfs.writable.dataschema.PxfExample_CustomWritable')
              FORMAT 'CUSTOM' (formatter='pxfwritable_import');
    ```
    The `DATA-SCHEMA` \<custom-option\> must be specified when reading an HDFS file via the `SequenceWritable` profile. Compression-related options need not be provided.
    
6. Query the readable external table `read_pxf_tbl_seqwrit`:

    ``` sql
    gpadmin=# SELECT * FROM read_pxf_tbl_seqwrit;
    ```
    
    ``` pre
     location  | month | number_of_orders | total_sales 
    -----------+-------+------------------+-------------
     Frankfurt | Mar   |              777 |     3956.98
     Cleveland | Oct   |             3812 |     96645.4
    (2 rows)
    ```

## <a id="recordkeyinkey-valuefileformats"></a>Reading the Record Key 

When a HAWQ external table references a SequenceFile or another file format that store rows in a key-value format, you can access the key values in HAWQ queries by using the `recordkey` keyword as a field name.

The field type of `recordkey` must correspond to the key type, much as the other fields must match the HDFS data. 

`recordkey` can be any of the following Hadoop types:

-   BooleanWritable
-   ByteWritable
-   DoubleWritable
-   FloatWritable
-   IntWritable
-   LongWritable
-   Text

### <a id="example1"></a>Example: Using Record Keys

Create an external readable table to access the record keys from the writable table `pxf_tbl_seqwrit` that you created in [Example: Writing Data Using the SequenceWritable Profile](#profile_hdfsseqwritable_writing).  The `recordkey` is of type `int8`.

``` sql
gpadmin=# CREATE  EXTERNAL TABLE read_pxf_tbl_seqwrit_RECKEY (recordkey int8, location text, month text, number_of_orders integer, total_sales real)
                LOCATION ('pxf://namenode:51200/data/pxf_examples/pxf_seqwrit_file?PROFILE=SequenceWritable&DATA-SCHEMA=com.hawq.example.pxf.hdfs.writable.dataschema.PxfExample_CustomWritable')
          FORMAT 'CUSTOM' (formatter='pxfwritable_import');
gpadmin=# SELECT * FROM read_pxf_tbl_seqwrit_RECKEY;
```

``` pre
 recordkey |  location   | month | number_of_orders | total_sales 
-----------+-------------+-------+------------------+-------------
         0 | Frankfurt   | Mar   |              777 |     3956.98
         0 | Cleveland   | Oct   |             3812 |     96645.4
(2 rows)
```

The `recordkey` is `0` because you did not identify a record key when you inserted entries into the writable table.
