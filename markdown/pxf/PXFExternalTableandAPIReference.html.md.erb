---
title: PXF External Tables and API
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

You can use the PXF API to create your own connectors to access any other type of parallel data store or processing engine.

The PXF Java API lets you extend PXF functionality and add new services and formats without changing HAWQ. The API includes three classes that are extended to allow HAWQ to access an external data source: `Fragmenter`, `Accessor`, and `Resolver`.

The `Fragmenter` produces a list of data fragments that can be read in parallel from the data source. The `Accessor` produces a list of records from a single fragment, and the `Resolver` both deserializes and serializes records.

Together, the `Fragmenter`, `Accessor`, and `Resolver` classes implement a connector. PXF includes plug-ins for HDFS and JSON files and tables in HBase and Hive.

## <a id="creatinganexternaltable"></a>Creating an External Table

The syntax for an `EXTERNAL TABLE` that uses the PXF protocol is as follows:

``` sql
CREATE [READABLE|WRITABLE] EXTERNAL TABLE <table_name>
        ( <column_name> <data_type> [, ...] | LIKE <other_table> )
LOCATION('pxf://<host>[:<port>]/<path-to-data>?<pxf-parameters>[&<custom-option>=<value>[...]]')
FORMAT 'custom' (formatter='pxfwritable_import|pxfwritable_export');
```

 where \<pxf\-parameters\> is:

``` pre
    [FRAGMENTER=<fragmenter_class>&ACCESSOR=<accessor_class>
         &RESOLVER=<resolver_class>] | ?PROFILE=profile-name
```

**Note**: Not every PXF profile supports writable external tables. Refer to [Writing Data to HDFS](HDFSWritablePXF.html) for a detailed discussion of the HDFS plug-in profiles that support this feature.

<caption><span class="tablecap">Table 1. Parameter values and description</span></caption>

<a id="creatinganexternaltable__table_pfy_htz_4p"></a>

| Parameter               | Value and description                                                                                                                                                                                                                                                          |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \<host\>    | The PXF host. While \<host\> may identify any PXF agent node, use the HDFS NameNode as it is guaranteed to be available in a running HDFS cluster. If HDFS High Availability is enabled, \<host\> must identify the HDFS NameService. |
| \<port\>    | The PXF port. If \<port\> is omitted, PXF assumes \<host\> identifies a High Availability HDFS Nameservice and connects to the port number designated by the `pxf_service_port` server configuration parameter value. Default is 51200. |
| \<path\-to\-data\>        | A directory, file name, wildcard pattern, table name, etc.                                                                                                                                                                                                                     |
| PROFILE              | The profile PXF uses to access the data. PXF supports multiple plug-ins that currently expose profiles named `HBase`, `Hive`, `HiveRC`, `HiveText`, `HiveORC`,  `HiveVectorizedORC`, `HdfsTextSimple`, `HdfsTextMulti`, `Avro`, `SequenceWritable`, and `Json`.                                                                                                                                                                                   |
| FRAGMENTER              | The Java class the plug-in uses for fragmenting data. Used for READABLE external tables only.                                                                                                                                                                                   |
| ACCESSOR                | The Java class the plug-in uses for accessing the data. Used for READABLE and WRITABLE tables.                                                                                                                                                                                  |
| RESOLVER                | The Java class the plug-in uses for serializing and deserializing the data. Used for READABLE and WRITABLE tables.                                                                                                                                                                                                                                                                                                                     |
| \<custom-option\> | Additional values to pass to the plug-in at runtime. A plug-in can parse custom options with the PXF helper class  `org.apache.hawq.pxf.api.utilities.InputData`.                                                                  |

**Note:** When creating PXF external tables, you cannot use the `HEADER` option in your `FORMAT` specification.


## <a id="aboutthejavaclassservicesandformats"></a>About the Java Class Services and Formats

The `LOCATION` string in a PXF `CREATE EXTERNAL TABLE` statement is a URI that specifies the host and port of an external data source and the path to the data in the external data source. The query portion of the URI, introduced by the question mark (?), must include the PXF profile name or the plug-in's  `FRAGMENTER` (readable tables only), `ACCESSOR`, and `RESOLVER` class names.

PXF profiles are defined in the `/etc/pxf/conf/pxf-profiles.xml` file. Profile definitions include plug-in class names. For example, the `HdfsTextSimple` profile definition is:

``` xml
<profile>
    <name>HdfsTextSimple</name>
    <description> This profile is suitable for use when reading delimited
      single line records from plain text files on HDFS.
    </description>
    <plugins>
        <fragmenter>org.apache.hawq.pxf.plugins.hdfs.HdfsDataFragmenter</fragmenter>
        <accessor>org.apache.hawq.pxf.plugins.hdfs.LineBreakAccessor</accessor>
        <resolver>org.apache.hawq.pxf.plugins.hdfs.StringPassResolver</resolver>
    </plugins>
</profile>
```

The parameters in the PXF URI are passed from HAWQ as headers to the PXF Java service. You can pass custom information to user-implemented PXF plug-ins by adding optional parameters to the `LOCATION` string.

The Java PXF service retrieves the source data from the external data source and converts it to a HAWQ-readable table format.

The `Accessor`, `Resolver`, and `Fragmenter` Java classes extend the `org.apache.hawq.pxf.api.utilities.Plugin` class:

``` java
package org.apache.hawq.pxf.api.utilities;
/**
 * Base class for all plug-in types (Accessor, Resolver, Fragmenter, ...).
 * Manages the meta data.
 */
public class Plugin {
    protected InputData inputData;
    /**
     * Constructs a plug-in.
     *
     * @param input the input data
     */
    public Plugin(InputData input) {
        this.inputData = input;
    }
    /**
     * Checks if the plug-in is thread safe or not, based on inputData.
     *
     * @return true if plug-in is thread safe
     */
    public boolean isThreadSafe() {
        return true;
    }
}
```

The parameters in the `LOCATION` string are available to the plug-ins through methods in the `org.apache.hawq.pxf.api.utilities.InputData` class. Plug-ins can look up the custom parameters added to the location string with the `getUserProperty()` method.

``` java
/**
 * Common configuration available to all PXF plug-ins. Represents input data
 * coming from client applications, such as HAWQ.
 */
public class InputData {

    /**
     * Constructs an InputData from a copy.
     * Used to create from an extending class.
     *
     * @param copy the input data to copy
     */
    public InputData(InputData copy);

    /**
     * Returns value of a user defined property.
     *
     * @param userProp the lookup user property
     * @return property value as a String
     */
    public String getUserProperty(String userProp);

    /**
     * Sets the byte serialization of a fragment meta data
     * @param location start, len, and location of the fragment
     */
    public void setFragmentMetadata(byte[] location);

    /** Returns the byte serialization of a data fragment */
    public byte[] getFragmentMetadata();

    /**
     * Gets any custom user data that may have been passed from the
     * fragmenter. Will mostly be used by the accessor or resolver.
     */
    public byte[] getFragmentUserData();

    /**
     * Sets any custom user data that needs to be shared across plug-ins.
     * Will mostly be set by the fragmenter.
     */
    public void setFragmentUserData(byte[] userData);

    /** Returns the number of segments in GP. */
    public int getTotalSegments();

    /** Returns the current segment ID. */
    public int getSegmentId();

    /** Returns true if there is a filter string to parse. */
    public boolean hasFilter();

    /** Returns the filter string, <tt>null</tt> if #hasFilter is <tt>false</tt> */
    public String getFilterString();

    /** Returns tuple description. */
    public ArrayList<ColumnDescriptor> getTupleDescription();

    /** Returns the number of columns in tuple description. */
    public int getColumns();

    /** Returns column index from tuple description. */
    public ColumnDescriptor getColumn(int index);

    /**
     * Returns the column descriptor of the recordkey column. If the recordkey
     * column was not specified by the user in the create table statement will
     * return null.
     */
    public ColumnDescriptor getRecordkeyColumn();

    /** Returns the data source of the required resource (i.e a file path or a table name). */
    public String getDataSource();

    /** Sets the data source for the required resource */
    public void setDataSource(String dataSource);

    /** Returns the ClassName for the java class that was defined as Accessor */
    public String getAccessor();

    /** Returns the ClassName for the java class that was defined as Resolver */
    public String getResolver();

    /**
     * Returns the ClassName for the java class that was defined as Fragmenter
     * or null if no fragmenter was defined
     */
    public String getFragmenter();

    /**
     * Returns the contents of pxf_remote_service_login set in Hawq.
     * Should the user set it to an empty string this function will return null.
     *
     * @return remote login details if set, null otherwise
     */
    public String getLogin();

    /**
     * Returns the contents of pxf_remote_service_secret set in Hawq.
     * Should the user set it to an empty string this function will return null.
     *
     * @return remote password if set, null otherwise
     */
    public String getSecret();

    /**
     * Returns true if the request is thread safe. Default true. Should be set
     * by a user to false if the request contains non thread-safe plug-ins or
     * components, such as BZip2 codec.
     */
    public boolean isThreadSafe();

    /**
     * Returns a data fragment index. plan to deprecate it in favor of using
     * getFragmentMetadata().
     */
    public int getDataFragment();
}
```

-   **[Fragmenter](../pxf/PXFExternalTableandAPIReference.html#fragmenter)**

-   **[Accessor](../pxf/PXFExternalTableandAPIReference.html#accessor)**

-   **[Resolver](../pxf/PXFExternalTableandAPIReference.html#resolver)**

### <a id="fragmenter"></a>Fragmenter

**Note:** You use the `Fragmenter` class to read data into HAWQ. You cannot use this class to write data out of HAWQ.

The `Fragmenter` is responsible for passing datasource metadata back to HAWQ. It also returns a list of data fragments to the `Accessor` or `Resolver`. Each data fragment describes some part of the requested data set. It contains the datasource name, such as the file or table name, including the hostname where it is located. For example, if the source is an HDFS file, the `Fragmenter` returns a list of data fragments containing an HDFS file block. Each fragment includes the location of the block. If the source data is an HBase table, the `Fragmenter` returns information about table regions, including their locations.

The `ANALYZE` command now retrieves advanced statistics for PXF readable tables by estimating the number of tuples in a table, creating a sample table from the external table, and running advanced statistics queries on the sample table in the same way statistics are collected for native HAWQ tables.

The configuration parameter `pxf_enable_stat_collection` controls collection of advanced statistics. If `pxf_enable_stat_collection` is set to false, no analysis is performed on PXF tables. An additional parameter, `pxf_stat_max_fragments`, controls the number of fragments sampled to build a sample table. By default `pxf_stat_max_fragments` is set to 100, which means that even if there are more than 100 fragments, only this number of fragments will be used in `ANALYZE` to sample the data. Increasing this number will result in better sampling, but can also impact performance.

When a PXF table is analyzed, any of the following conditions might result in a warning message with no statistics gathered for the table:

- `pxf_enable_stat_collection` is set to off,
- an error occurs because the table is not defined correctly,
- the PXF service is down, or
- `getFragmentsStats()` is not implemented 

If `ANALYZE` is running over all tables in the database, the next table will be processed – a failure processing one table does not stop the command.

For a detailed explanation about HAWQ statistical data gathering, refer to the [`ANALYZE`](../reference/sql/ANALYZE.html) SQL command reference.

**Note:**

-   Depending on external table size, the time required to complete an `ANALYZE` operation can be lengthy. The boolean parameter `pxf_enable_stat_collection` enables statistics collection for PXF. The default value is `on`. Turning this parameter off (disabling PXF statistics collection) can help decrease the time needed for the `ANALYZE` operation.
-   You can also use `pxf_stat_max_fragments` to limit the number of fragments to be sampled by decreasing it from the default (100). However, if the number is too low, the sample might not be uniform and the statistics might be skewed.
-   You can also implement `getFragmentsStats()` to return an error. This will cause `ANALYZE` on a table with this `Fragmenter` to fail immediately, and default statistics values will be used for that table.

The following table lists the `Fragmenter` plug-in implementations included with the PXF API.

<a id="fragmenter__table_cgs_svp_3s"></a>

<table>
<caption><span class="tablecap">Table 2. Fragmenter base classes </span></caption>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Fragmenter class</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>org.apache.hawq.pxf.plugins.hdfs.HdfsDataFragmenter</td>
<td>Fragmenter for HDFS, JSON files</td>
</tr>
<tr class="even">
<td>org.apache.hawq.pxf.plugins.hbase.HBaseDataFragmenter</td>
<td>Fragmenter for HBase tables</td>
</tr>
<tr class="odd">
<td>org.apache.hawq.pxf.plugins.hive.HiveDataFragmenter</li>
<td>Fragmenter for Hive tables </td>
</tr>
<tr class="even">
<td>org.apache.hawq.pxf.plugins.hdfs.HiveInputFormatFragmenter</td>
<td>Fragmenter for Hive tables with RC, ORC, or text file formats </td>
</tr>
</tbody>
</table>

A `Fragmenter` class extends `org.apache.hawq.pxf.api.Fragmenter`:

#### <a id="com.pivotal.pxf.api.fragmenter"></a>org.apache.hawq.pxf.api.Fragmenter

``` java
package org.apache.hawq.pxf.api;
/**
 * Abstract class that defines the splitting of a data resource into fragments
 * that can be processed in parallel.
 */
public abstract class Fragmenter extends Plugin {
        protected List<Fragment> fragments;

    public Fragmenter(InputData metaData) {
        super(metaData);
        fragments = new LinkedList<Fragment>();
    }

       /**
        * Gets the fragments of a given path (source name and location of each
        * fragment). Used to get fragments of data that could be read in parallel
        * from the different segments.
        */
    public abstract List<Fragment> getFragments() throws Exception;

    /**
        * Default implementation of statistics for fragments. The default is:
        * <ul>
        * <li>number of fragments - as gathered by {@link #getFragments()}</li>
        * <li>first fragment size - 64MB</li>
        * <li>total size - number of fragments times first fragment size</li>
        * </ul>
        * Each fragmenter implementation can override this method to better match
        * its fragments stats.
        *
        * @return default statistics
        * @throws Exception if statistics cannot be gathered
        */
       public FragmentsStats getFragmentsStats() throws Exception {
        List<Fragment> fragments = getFragments();
        long fragmentsNumber = fragments.size();
        return new FragmentsStats(fragmentsNumber,
                FragmentsStats.DEFAULT_FRAGMENT_SIZE, fragmentsNumber
                        * FragmentsStats.DEFAULT_FRAGMENT_SIZE);
    }
}
  
```

`getFragments()` returns a string in JSON format of the retrieved fragment. For example, if the input path is a HDFS directory, the source name for each fragment should include the file name including the path for the fragment.

#### <a id="classdescription"></a>Class Description

The `Fragmenter.getFragments()` method returns a `List<Fragment>`:

``` java
package org.apache.hawq.pxf.api;
/*
 * Fragment holds a data fragment' information.
 * Fragmenter.getFragments() returns a list of fragments.
 */
public class Fragment
{
    private String sourceName;    // File path+name, table name, etc.
    private int index;            // Fragment index (incremented per sourceName)
    private String[] replicas;    // Fragment replicas (1 or more)
    private byte[]   metadata;    // Fragment metadata information (starting point + length, region location, etc.)
    private byte[]   userData;    // ThirdParty data added to a fragment. Ignored if null
    ...
}
```

#### <a id="topic_fzd_tlv_c5"></a>org.apache.hawq.pxf.api.FragmentsStats

The `Fragmenter.getFragmentsStats()` method returns a `FragmentsStats`:

``` java
package org.apache.hawq.pxf.api;
/**
 * FragmentsStats holds statistics for a given path.
 */
public class FragmentsStats {

    // number of fragments
    private long fragmentsNumber;
    // first fragment size
    private SizeAndUnit firstFragmentSize;
    // total fragments size
    private SizeAndUnit totalSize;

   /**
     * Enum to represent unit (Bytes/KB/MB/GB/TB)
     */
    public enum SizeUnit {
        /**
         * Byte
         */
        B,
        /**
         * KB
         */
        KB,
        /**
         * MB
         */
        MB,
        /**
         * GB
         */
        GB,
        /**
         * TB
         */
        TB;
    };

    /**
     * Container for size and unit
     */
    public class SizeAndUnit {
        long size;
        SizeUnit unit;
    ... 

```

`getFragmentsStats()` returns a string in JSON format of statistics for the data source. For example, if the input path is a HDFS directory of 3 files, each one of 1 block, the output will be the number of fragments (3), the size of the first file, and the size of all files in that directory.

### <a id="accessor"></a>Accessor

The `Accessor` retrieves specific fragments and passes records back to the Resolver. For example, the HDFS plug-ins create a `org.apache.hadoop.mapred.FileInputFormat` and a `org.apache.hadoop.mapred.RecordReader` for an HDFS file and sends this to the `Resolver`. In the case of HBase or Hive files, the `Accessor` returns single rows from an HBase or Hive table. PXF includes the following `Accessor` implementations:

<a id="accessor__table_ewm_ttz_4p"></a>

<table>
<caption><span class="tablecap">Table 3. Accessor base classes </span></caption>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Accessor class</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>org.apache.hawq.pxf.plugins.hdfs.HdfsAtomicDataAccessor</td>
<td>Base class for accessing datasources which cannot be split. These will be accessed by a single HAWQ segment</td>
</tr>
<tr class="even">
<td>org.apache.hawq.pxf.plugins.hdfs.QuotedLineBreakAccessor</td>
<td>Accessor for TEXT files that have records with embedded linebreaks</td>
</tr>
<tr class="odd">
<td>org.apache.hawq.pxf.plugins.hdfs.HdfsSplittableDataAccessor</td>
<td><p>Base class for accessing HDFS files using <code class="ph codeph">RecordReaders</code></p></td>
</tr>
<tr class="even">
<td>org.apache.hawq.pxf.plugins.hdfs.LineBreakAccessor</td>
<td>Accessor for TEXT files (replaced the deprecated <code class="ph codeph">TextFileAccessor</code>, <code class="ph codeph">LineReaderAccessor</code>)</td>
</tr>
<tr class="odd">
<td>org.apache.hawq.pxf.plugins.hdfs.AvroFileAccessor</td>
<td>Accessor for Avro files</td>
</tr>
<tr class="even">
<td>org.apache.hawq.pxf.plugins.hdfs.SequenceFileAccessor</td>
<td>Accessor for Sequence files</td>
</tr>
<tr class="odd">
<td>org.apache.hawq.pxf.plugins.hbase.HBaseAccessor </td>
<td>Accessor for HBase tables </td>
</tr>
<tr class="even">
<td>org.apache.hawq.pxf.plugins.hive.HiveAccessor</td>
<td>Accessor for Hive tables </td>
</tr>
<tr class="odd">
<td>org.apache.hawq.pxf.plugins.hive.HiveLineBreakAccessor</td>
<td>Accessor for Hive tables stored as text file format</td>
</tr>
<tr class="even">
<td>org.apache.hawq.pxf.plugins.hive.HiveRCFileAccessor</td>
<td>Accessor for Hive tables stored as RC file format</td>
</tr>
</tr>
<tr class="odd">
<td>org.apache.hawq.pxf.plugins.hive.HiveORCAccessor</td>
<td>Accessor for Hive tables stored as ORC format </td>
</tr>
<tr class="even">
<td>org.apache.hawq.pxf.plugins.hive.HiveORCVectorizedAccessor</td>
<td>Accessor for Hive tables stored as ORC format </td>
</tr>
</tr>
<tr class="odd">
<td>org.apache.hawq.pxf.plugins.json.JsonAccessor</td>
<td>Accessor for JSON files</td>
</tr>
</tbody>
</table>

The class must extend the `org.apache.hawq.pxf.Plugin`  class, and implement one or both of the interfaces:

-   `org.apache.hawq.pxf.api.ReadAccessor`
-   `org.apache.hawq.pxf.api.WriteAccessor`

``` java
package org.apache.hawq.pxf.api;
/*
 * Internal interface that defines the access to data on the source
 * data store (e.g, a file on HDFS, a region of an HBase table, etc).
 * All classes that implement actual access to such data sources must
 * respect this interface
 */
public interface ReadAccessor {
    boolean openForRead() throws Exception;
    OneRow readNextObject() throws Exception;
    void closeForRead() throws Exception;
}
```

``` java
package org.apache.hawq.pxf.api;
/*
 * An interface for writing data into a data store
 * (e.g, a sequence file on HDFS).
 * All classes that implement actual access to such data sources must
 * respect this interface
 */
public interface WriteAccessor {
    boolean openForWrite() throws Exception;
    OneRow writeNextObject(OneRow onerow) throws Exception;
    void closeForWrite() throws Exception;
}
```

The `Accessor` calls `openForRead()` to read existing data. After reading the data, it calls `closeForRead()`. `readNextObject()` returns one of the following:

-   a single record, encapsulated in a `OneRow` object
-   null if it reaches `EOF`

The `Accessor` calls `openForWrite()` to write data out. After writing the data, it writes a `OneRow` object with `writeNextObject()`, and when done calls `closeForWrite()`. `OneRow` represents a key-value item.

#### <a id="com.pivotal.pxf.api.onerow"></a>org.apache.hawq.pxf.api.OneRow

``` java
package org.apache.hawq.pxf.api;
/*
 * Represents one row in the external system data store. Supports
 * the general case where one row contains both a record and a
 * separate key like in the HDFS key/value model for MapReduce
 * (Example: HDFS sequence file)
 */
public class OneRow {
    /*
     * Default constructor
     */
    public OneRow();

    /*
     * Constructor sets key and data
     */
    public OneRow(Object inKey, Object inData);

    /*
     * Setter for key
     */
    public void setKey(Object inKey);
    
    /*
     * Setter for data
     */
    public void setData(Object inData);

    /*
     * Accessor for key
     */
    public Object getKey();

    /*
     * Accessor for data
     */
    public Object getData();

    /*
     * Show content
     */
    public String toString();
}
```

### <a id="resolver"></a>Resolver

The `Resolver` deserializes records in the `OneRow` format and serializes them to a list of `OneField` objects. PXF converts a `OneField` object to a HAWQ-readable `GPDBWritable` format. PXF 1.x or higher contains the following implementations:

<a id="resolver__table_nbd_d5z_4p"></a>

<table>
<caption><span class="tablecap">Table 4. Resolver base classes</span></caption>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Resolver class</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>org.apache.hawq.pxf.plugins.hdfs.StringPassResolver</p></td>
<td><p><code class="ph codeph">StringPassResolver</code> replaced the deprecated <code class="ph codeph">TextResolver</code>. It passes whole records (composed of any data types) as strings without parsing them</p></td>
</tr>
<tr class="even">
<td><p>org.apache.hawq.pxf.plugins.hdfs.WritableResolver</p></td>
<td><p>Resolver for custom Hadoop Writable implementations. Custom class can be specified with the schema in `DATA-SCHEMA`. Supports the following types:</p>
<pre class="pre codeblock"><code>DataType.BOOLEAN
DataType.INTEGER
DataType.BIGINT
DataType.REAL
DataType.FLOAT8
DataType.VARCHAR
DataType.BYTEA</code></pre></td>
</tr>
<tr class="odd">
<td><p>org.apache.hawq.pxf.plugins.hdfs.AvroResolver</p></td>
<td><p>Supports the same field objects as <code class="ph codeph">WritableResolver</code>. </p></td>
</tr>
<tr class="even">
<td><p>org.apache.hawq.pxf.plugins.hbase.HBaseResolver</p></td>
<td><p>Supports the same field objects as <code class="ph codeph">WritableResolver</code> and also supports the following:</p>
<pre class="pre codeblock"><code>DataType.SMALLINT
DataType.NUMERIC
DataType.TEXT
DataType.BPCHAR
DataType.TIMESTAMP</code></pre></td>
</tr>
<tr class="odd">
<td><p>org.apache.hawq.pxf.plugins.hive.HiveResolver</p></td>
<td><p>Supports the same field objects as <code class="ph codeph">WritableResolver</code> and also supports the following:</p>
<pre class="pre codeblock"><code>DataType.SMALLINT
DataType.TEXT
DataType.TIMESTAMP</code></pre></td>
</tr>
<tr class="even">
<td><p>org.apache.hawq.pxf.plugins.hive.HiveStringPassResolver</p></td>
<td>Specialized <code class="ph codeph">HiveResolver</code> for a Hive table stored as Text files. Should be used together with <code class="ph codeph">HiveInputFormatFragmenter</code>/<code class="ph codeph">HiveLineBreakAccessor</code>.</td>
</tr>
<tr class="odd">
<td>org.apache.hawq.pxf.plugins.hive.HiveColumnarSerdeResolver</td>
<td>Specialized <code class="ph codeph">HiveResolver</code> for a Hive table stored as RC file. Should be used together with <code class="ph codeph">HiveInputFormatFragmenter</code>/<code class="ph codeph">HiveRCFileAccessor</code>.</td>
</tr>
<tr class="even">
<td>org.apache.hawq.pxf.plugins.hive.HiveORCSerdeResolver</td>
<td>Specialized <code class="ph codeph">HiveResolver</code> for a Hive table stored in ORC format. Should be used together with <code class="ph codeph">HiveInputFormatFragmenter</code>/<code class="ph codeph">HiveORCAccessor</code>.</td>
</tr>
<tr class="odd">
<td>org.apache.hawq.pxf.plugins.hive.HiveORCVectorizedResolver</td>
<td>Specialized <code class="ph codeph">HiveResolver</code> for a Hive table stored in ORC format. Should be used together with <code class="ph codeph">HiveInputFormatFragmenter</code>/<code class="ph codeph">HiveORCVectorizedAccessor</code>.</td>
</tr>
</tbody>
</table>

The class needs to extend the `org.apache.hawq.pxf.resolvers.Plugin class                `, and implement one or both interfaces:

-   `org.apache.hawq.pxf.api.ReadResolver`
-   `org.apache.hawq.pxf.api.WriteResolver`

``` java
package org.apache.hawq.pxf.api;
/*
 * Interface that defines the deserialization of one record brought from
 * the data Accessor. Every implementation of a deserialization method
 * (e.g, Writable, Avro, ...) must implement this interface.
 */
public interface ReadResolver {
    public List<OneField> getFields(OneRow row) throws Exception;
}
```

``` java
package org.apache.hawq.pxf.api;
/*
* Interface that defines the serialization of data read from the DB
* into a OneRow object.
* Every implementation of a serialization method
* (e.g, Writable, Avro, ...) must implement this interface.
*/
public interface WriteResolver {
    public OneRow setFields(List<OneField> record) throws Exception;
}
```

**Note:**

-   `getFields()` should return a `List<OneField>`, with each `OneField` representing a single field.
-   `setFields()` should return a single `OneRow` object, given a `List<OneField>`.

#### <a id="com.pivotal.pxf.api.onefield"></a>org.apache.hawq.pxf.api.OneField

``` java
package org.apache.hawq.pxf.api;
/*
 * Defines one field on a deserialized record.
 * 'type' is in OID values recognized by GPDBWritable
 * 'val' is the actual field value
 */
public class OneField {
    public OneField() {}
    public OneField(int type, Object val) {
        this.type = type;
        this.val = val;
    }

    public int type;
    public Object val;
}
```

The value of `type` should follow the `org.apache.hawq.pxf.api.io.DataType` `enums`. `val` is the appropriate Java class. Supported types are:

<a id="com.pivotal.pxf.api.onefield__table_f4x_35z_4p"></a>

<table>
<caption><span class="tablecap">Table 5. Resolver supported types</span></caption>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>DataType recognized OID</p></th>
<th><p>Field value</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code class="ph codeph">DataType.SMALLINT</code></p></td>
<td><p><code class="ph codeph">Short</code></p></td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">DataType.INTEGER</code></p></td>
<td><p><code class="ph codeph">Integer</code></p></td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">DataType.BIGINT</code></p></td>
<td><p><code class="ph codeph">Long</code></p></td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">DataType.REAL</code></p></td>
<td><p><code class="ph codeph">Float</code></p></td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">DataType.FLOAT8</code></p></td>
<td><p><code class="ph codeph">Double</code></p></td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">DataType.NUMERIC</code></p></td>
<td><p><code class="ph codeph">String (&quot;651687465135468432168421&quot;)</code></p></td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">DataType.BOOLEAN</code></p></td>
<td><p><code class="ph codeph">Boolean</code></p></td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">DataType.VARCHAR</code></p></td>
<td><p><code class="ph codeph">String</code></p></td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">DataType.BPCHAR</code></p></td>
<td><p><code class="ph codeph">String</code></p></td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">DataType.TEXT</code></p></td>
<td><p><code class="ph codeph">String</code></p></td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">DataType.BYTEA</code></p></td>
<td><p><code class="ph codeph">byte []</code></p></td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">DataType.TIMESTAMP</code></p></td>
<td><p><code class="ph codeph">Timestamp</code></p></td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">DataType.Date</code></p></td>
<td><p><code class="ph codeph">Date</code></p></td>
</tr>
</tbody>
</table>

## <a id="aboutcustomprofiles"></a>About Custom Profiles

Administrators can add new profiles or edit the built-in profiles in `/etc/pxf/conf/pxf-profiles.xml`. See [Using Profiles to Read and Write Data](ReadWritePXF.html#readingandwritingdatawithpxf) for information on how to add custom profiles.

## <a id="aboutqueryfilterpush-down"></a>About Query Filter Push-Down

If a query includes a number of `WHERE` clause filters,  HAWQ may push all or some queries to PXF. If pushed to PXF, the `Accessor` can use the filtering information when accessing the data source to fetch tuples. These filters only return records that pass filter evaluation conditions. This reduces data processing and reduces network traffic from the SQL engine.

This topic includes the following information:

-   Filter Availability and Ordering 
-   Creating a Filter Builder class
-   Filter Operations
-   Sample Implementation
-   Using Filters

### <a id="filteravailabilityandordering"></a>Filter Availability and Ordering

PXF allows push-down filtering if the following rules are met:

-   Uses only single expressions or a group of AND'ed expressions - no OR'ed expressions.
-   Uses only expressions of supported data types and operators.

`FilterParser` scans the pushed down filter list and uses the user's `build()` implementation to build the filter.

-   For simple expressions (e.g, a &gt;= 5), `FilterParser` places column objects on the left of the expression and constants on the right.
-   For compound expressions (e.g &lt;expression&gt; AND &lt;expression&gt;) it handles three cases in the `build()` function:
    1.  Simple Expression: &lt;Column Index&gt; &lt;Operation&gt; &lt;Constant&gt;
    2.  Compound Expression: &lt;Filter Object&gt; AND &lt;Filter Object&gt;
    3.  Compound Expression: &lt;List of Filter Objects&gt; AND &lt;Filter Object&gt;

### <a id="creatingafilterbuilderclass"></a>Creating a Filter Builder Class

To check if a filter queried PXF, call the `InputData.hasFilter()` function:

``` java
/*
 * Returns true if there is a filter string to parse
 */
public boolean hasFilter()
{
   return filterStringValid;
}
```

If `hasFilter()` returns `false`, there is no filter information. If it returns `true`, PXF parses the serialized filter string into a meaningful filter object to use later. To do so, create a filter builder class that implements the `FilterParser.FilterBuilder` interface:

``` java
package org.apache.hawq.pxf.api;
/*
 * Interface a user of FilterParser should implement
 * This is used to let the user build filter expressions in the manner she 
 * sees fit
 *
 * When an operator is parsed, this function is called to let the user decide
 * what to do with its operands.
 */
interface FilterBuilder {
   public Object build(Operation operation, Object left, Object right) throws Exception;
}
```

While PXF parses the serialized filter string from the incoming HAWQ query, it calls the `build()` function. PXF calls this function for each condition or filter pushed down to PXF. Implementing this function returns some Filter object or representation that the `Fragmenter`, `Accessor`, or `Resolver` uses in runtime to filter out records. The `build()` function accepts an Operation as input, and left and right operands.

### <a id="filteroperations"></a>Filter Operations

``` java
/*
 * Operations supported by the parser
 */
public enum Operation
{
    HDOP_LT, //less than
    HDOP_GT, //greater than
    HDOP_LE, //less than or equal
    HDOP_GE, //greater than or equal
    HDOP_EQ, //equal
    HDOP_NE, //not equal
    HDOP_LIKE,
    HDOP_IS_NULL,
    HDOP_IS_NOT_NULL,
    HDOP_IN
};

/**
 * Logical operators
 */
public enum LogicalOperation {
    HDOP_AND,
    HDOP_OR,
    HDOP_NOT
}
```

#### <a id="filteroperands"></a>Filter Operands

There are three types of operands:

-   Column Index
-   Constant
-   Filter Object

#### <a id="columnindex"></a>Column Index

``` java
/*
 * Represents a column index
 */
public class ColumnIndex
{
   public ColumnIndex(int idx);

   public int index();
}
```

#### <a id="constant"></a>Constant

``` java
/*
 * The class represents a constant object (String, Long, ...)
 */
public class Constant
{
    public Constant(Object obj);

    public Object constant();
}
```

#### <a id="filterobject"></a>Filter Object

Filter Objects can be internal - such as those you define - or external, those that the remote system uses. For example, for HBase you define the HBase `Filter` class (`org.apache.hadoop.hbase.filter.Filter`), while for Hive you use an internal default representation created by the PXF framework, called `BasicFilter`. You can choose the filter object to use, including writing a new one. `BasicFilter` is the most common:

``` java
/*
 * Basic filter provided for cases where the target storage system does not provide its own filter
 * For example: Hbase storage provides its own filter but for a Writable based record in a SequenceFile
 * there is no filter provided and so we need to have a default
 */
static public class BasicFilter
{
   /*
    * C'tor
    */
   public BasicFilter(Operation inOper, ColumnIndex inColumn, Constant inConstant);

   /*
    * Returns oper field
    */
   public Operation getOperation();

   /*
    * Returns column field
    */
   public ColumnIndex getColumn();

   /*
    * Returns constant field
    */
   public Constant getConstant();
}
```

### <a id="sampleimplementation"></a>Sample Implementation

Let's look at the following sample implementation of the filter builder class and its `build()` function that handles all 3 cases. Let's assume that `BasicFilter` was used to hold our filter operations.

``` java
import java.util.LinkedList;
import java.util.List;

import org.apache.hawq.pxf.api.FilterParser;
import org.apache.hawq.pxf.api.utilities.InputData;

public class MyDemoFilterBuilder implements FilterParser.FilterBuilder
{
    private InputData inputData;

    public MyDemoFilterBuilder(InputData input)
    {
        inputData = input;
    }

    /*
     * Translates a filterString into a FilterParser.BasicFilter or a list of such filters
     */
    public Object getFilterObject(String filterString) throws Exception
    {
        FilterParser parser = new FilterParser(this);
        Object result = parser.parse(filterString);

        if (!(result instanceof FilterParser.BasicFilter) && !(result instanceof List))
            throw new Exception("String " + filterString + " resolved to no filter");

        return result;
    }
 
    public Object build(FilterParser.Operation opId,
                        Object leftOperand,
                        Object rightOperand) throws Exception
    {
        if (leftOperand instanceof FilterParser.BasicFilter)
        {
            //sanity check
            if (opId != FilterParser.Operation.HDOP_AND || !(rightOperand instanceof FilterParser.BasicFilter))
                throw new Exception("Only AND is allowed between compound expressions");

            //case 3
            if (leftOperand instanceof List)
                return handleCompoundOperations((List<FilterParser.BasicFilter>)leftOperand, (FilterParser.BasicFilter)rightOperand);
            //case 2
            else
                return handleCompoundOperations((FilterParser.BasicFilter)leftOperand, (FilterParser.BasicFilter)rightOperand);
        }

        //sanity check
        if (!(rightOperand instanceof FilterParser.Constant))
            throw new Exception("expressions of column-op-column are not supported");

        //case 1 (assume column is on the left)
        return handleSimpleOperations(opId, (FilterParser.ColumnIndex)leftOperand, (FilterParser.Constant)rightOperand);
    }

    private FilterParser.BasicFilter handleSimpleOperations(FilterParser.Operation opId,
                                                            FilterParser.ColumnIndex column,
                                                            FilterParser.Constant constant)
    {
        return new FilterParser.BasicFilter(opId, column, constant);
    }

    private  List handleCompoundOperations(List<FilterParser.BasicFilter> left,
                                       FilterParser.BasicFilter right)
    {
        left.add(right);
        return left;
    }

    private List handleCompoundOperations(FilterParser.BasicFilter left,
                                          FilterParser.BasicFilter right)
    {
        List<FilterParser.BasicFilter> result = new LinkedList<FilterParser.BasicFilter>();

        result.add(left);
        result.add(right);
        return result;
    }
}
```

Here is an example of creating a filter-builder class to implement the Filter interface, implement the `build()` function, and generate the Filter object. To do this, use either the `Accessor`, `Resolver`, or both to call the `getFilterObject()` function:

``` java
if (inputData.hasFilter())
{
    String filterStr = inputData.filterString();
    MyDemoFilterBuilder demobuilder = new MyDemoFilterBuilder(inputData);
    Object filter = demobuilder.getFilterObject(filterStr);
    ...
}
```

### <a id="usingfilters"></a>Using Filters

Once you have built the Filter object(s), you can use them to read data and filter out records that do not meet the filter conditions:

1.  Check whether you have a single or multiple filters.
2.  Evaluate each filter and iterate over each filter in the list. Disqualify the record if filter conditions fail.

``` java
if (filter instanceof List)
{
    for (Object f : (List)filter)
        <evaluate f>; //may want to break if evaluation results in negative answer for any filter.
}
else
{
    <evaluate filter>;
}
```

Example showing evaluation of a single filter:

``` java
//Get our BasicFilter Object
FilterParser.BasicFilter bFilter = (FilterParser.BasicFilter)filter;

 
//Get operation and operator values
FilterParser.Operation op = bFilter.getOperation();
int colIdx = bFilter.getColumn().index();
String val = bFilter.getConstant().constant().toString();

//Get more info about the column if desired
ColumnDescriptor col = input.getColumn(colIdx);
String colName = filterColumn.columnName();
 
//Now evaluate it against the actual column value in the record...
```

## <a id="reference"></a>Examples

This section contains the following information:

-   **[External Table Examples](#externaltableexamples)**
-   **[Plug-in Examples](#pluginexamples)**

### <a id="externaltableexamples"></a>External Table Examples

#### <a id="example1"></a>Example 1

Shows an external table that can analyze all `Sequencefiles` that are populated `Writable` serialized records and exist inside the hdfs directory `sales/2012/01`. `SaleItem.class` is a Java class that implements the `Writable` interface and describes a Java record that includes three class members.

**Note:** In this example, the class member names do not necessarily match the database attribute names, but the types match. `SaleItem.class` must exist in the classpath of every DataNode and NameNode.

``` sql
CREATE EXTERNAL TABLE jan_2012_sales (id int, total int, comments varchar)
LOCATION ('pxf://10.76.72.26:51200/sales/2012/01/*.seq'
          '?FRAGMENTER=org.apache.hawq.pxf.plugins.hdfs.HdfsDataFragmenter'
          '&ACCESSOR=org.apache.hawq.pxf.plugins.hdfs.SequenceFileAccessor'
          '&RESOLVER=org.apache.hawq.pxf.plugins.hdfs.WritableResolver'
          '&DATA-SCHEMA=SaleItem')
FORMAT 'custom' (formatter='pxfwritable_import');
```

#### <a id="example2"></a>Example 2

Example 2 shows an external table that can analyze an HBase table called `sales`. It has 10 column families `(cf1 – cf10)` and many qualifier names in each family. This example focuses on the `rowkey`, the qualifier `saleid` inside column family `cf1`, and the qualifier `comments` inside column family `cf8` and uses direct mapping:

``` sql
CREATE EXTERNAL TABLE hbase_sales
  (hbaserowkey text, "cf1:saleid" int, "cf8:comments" varchar)
LOCATION ('pxf://10.76.72.26:51200/sales?PROFILE=HBase')
FORMAT 'custom' (formatter='pxfwritable_import');
```

#### <a id="example3"></a>Example 3

This example uses indirect mapping. Note how the attribute name changes and how they correspond to the HBase lookup table. Executing `SELECT FROM                      my_hbase_sales`, the attribute names automatically convert to their HBase correspondents.

``` sql
CREATE EXTERNAL TABLE my_hbase_sales (hbaserowkey text, id int, cmts varchar)
LOCATION
('pxf://10.76.72.26:51200/sales?PROFILE=HBase')
FORMAT 'custom' (formatter='pxfwritable_import');
```

#### <a id="example4"></a>Example 4

Shows an example for a writable table of compressed data. 

``` sql
CREATE WRITABLE EXTERNAL TABLE sales_aggregated_2012
    (id int, total int, comments varchar)
LOCATION ('pxf://10.76.72.26:51200/sales/2012/aggregated'
          '?PROFILE=HdfsTextSimple'
          '&COMPRESSION_CODEC=org.apache.hadoop.io.compress.BZip2Codec')
FORMAT 'TEXT';
```

#### <a id="example5"></a>Example 5

Shows an example for a writable table into a sequence file, using a schema file. For writable tables, the formatter is `pxfwritable_export`.

``` sql
CREATE WRITABLE EXTERNAL TABLE sales_max_2012
    (id int, total int, comments varchar)
LOCATION ('pxf://10.76.72.26:51200/sales/2012/max'
          '?FRAGMENTER=org.apache.hawq.pxf.plugins.hdfs.HdfsDataFragmenter'
          '&ACCESSOR=org.apache.hawq.pxf.plugins.hdfs.SequenceFileAccessor'
          '&RESOLVER=org.apache.hawq.pxf.plugins.hdfs.WritableResolver'
          '&DATA-SCHEMA=SaleItem')
FORMAT 'custom' (formatter='pxfwritable_export');
```

### <a id="pluginexamples"></a>Plug-in Examples

This section contains sample dummy implementations of all three plug-ins. It also includes a usage example.

#### <a id="dummyfragmenter"></a>Dummy Fragmenter

``` java
import org.apache.hawq.pxf.api.Fragmenter;
import org.apache.hawq.pxf.api.Fragment;
import org.apache.hawq.pxf.api.utilities.InputData;
import java.util.List;

/*
 * Class that defines the splitting of a data resource into fragments that can
 * be processed in parallel
 * getFragments() returns the fragments information of a given path (source name and location of each fragment).
 * Used to get fragments of data that could be read in parallel from the different segments.
 * Dummy implementation, for documentation
 */
public class DummyFragmenter extends Fragmenter {
    public DummyFragmenter(InputData metaData) {
        super(metaData);
    }
    /*
     * path is a data source URI that can appear as a file name, a directory name or a wildcard
     * returns the data fragments - identifiers of data and a list of available hosts
     */
    @Override
    public List<Fragment> getFragments() throws Exception {
        String localhostname = java.net.InetAddress.getLocalHost().getHostName();
        String[] localHosts = new String[]{localhostname, localhostname};
        fragments.add(new Fragment(inputData.getDataSource() + ".1" /* source name */,
                localHosts /* available hosts list */,
                "fragment1".getBytes()));
        fragments.add(new Fragment(inputData.getDataSource() + ".2" /* source name */,
                localHosts /* available hosts list */,
                "fragment2".getBytes()));
        fragments.add(new Fragment(inputData.getDataSource() + ".3" /* source name */,
                localHosts /* available hosts list */,
                "fragment3".getBytes()));
        return fragments;
    }
}
```

#### <a id="dummyaccessor"></a>Dummy Accessor

``` java
import org.apache.hawq.pxf.api.WriteAccessor;
import org.apache.hawq.pxf.api.OneRow;
import org.apache.hawq.pxf.api.utilities.InputData;
import org.apache.hawq.pxf.api.utilities.Plugin;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

/*
 * Internal interface that defines the access to a file on HDFS.  All classes
 * that implement actual access to an HDFS file (sequence file, avro file,...)
 * must respect this interface
 * Dummy implementation, for documentation
 */
public class DummyAccessor extends Plugin implements ReadAccessor, WriteAccessor {
    private static final Log LOG = LogFactory.getLog(DummyAccessor.class);
    private int rowNumber;
    private int fragmentNumber;
    public DummyAccessor(InputData metaData) {
        super(metaData);
    }
    @Override
    public boolean openForRead() throws Exception {
        /* fopen or similar */
        return true;
    }
    @Override
    public OneRow readNextObject() throws Exception {
        /* return next row , <key=fragmentNo.rowNo, val=rowNo,text,fragmentNo>*/
        /* check for EOF */
        if (fragmentNumber > 0)
            return null; /* signal EOF, close will be called */
        int fragment = inputData.getDataFragment();
        String fragmentMetadata = new String(inputData.getFragmentMetadata());
        /* generate row */
        OneRow row = new OneRow(fragment + "." + rowNumber, /* key */
                rowNumber + "," + fragmentMetadata + "," + fragment /* value */);
        /* advance */
        rowNumber += 1;
        if (rowNumber == 2) {
            rowNumber = 0;
            fragmentNumber += 1;
        }
        /* return data */
        return row;
    }
    @Override
    public void closeForRead() throws Exception {
        /* fclose or similar */
    }
    @Override
    public boolean openForWrite() throws Exception {
        /* fopen or similar */
        return true;
    }
    @Override
    public boolean writeNextObject(OneRow onerow) throws Exception {
        LOG.info(onerow.getData());
        return true;
    }
    @Override
    public void closeForWrite() throws Exception {
        /* fclose or similar */
    }
}
```

#### <a id="dummyresolver"></a>Dummy Resolver

``` java
import org.apache.hawq.pxf.api.OneField;
import org.apache.hawq.pxf.api.OneRow;
import org.apache.hawq.pxf.api.ReadResolver;
import org.apache.hawq.pxf.api.WriteResolver;
import org.apache.hawq.pxf.api.utilities.InputData;
import org.apache.hawq.pxf.api.utilities.Plugin;
import java.util.LinkedList;
import java.util.List;
import static org.apache.hawq.pxf.api.io.DataType.INTEGER;
import static org.apache.hawq.pxf.api.io.DataType.VARCHAR;

/*
 * Class that defines the deserializtion of one record brought from the external input data.
 * Every implementation of a deserialization method (Writable, Avro, BP, Thrift, ...)
 * must inherit this abstract class
 * Dummy implementation, for documentation
 */
public class DummyResolver extends Plugin implements ReadResolver, WriteResolver {
    private int rowNumber;
    public DummyResolver(InputData metaData) {
        super(metaData);
        rowNumber = 0;
    }
    @Override
    public List<OneField> getFields(OneRow row) throws Exception {
        /* break up the row into fields */
        List<OneField> output = new LinkedList<OneField>();
        String[] fields = ((String) row.getData()).split(",");
        output.add(new OneField(INTEGER.getOID() /* type */, Integer.parseInt(fields[0]) /* value */));
        output.add(new OneField(VARCHAR.getOID(), fields[1]));
        output.add(new OneField(INTEGER.getOID(), Integer.parseInt(fields[2])));
        return output;
    }
    @Override
    public OneRow setFields(List<OneField> record) throws Exception {
        /* should read inputStream row by row */
        return rowNumber > 5
                ? null
                : new OneRow(null, "row number " + rowNumber++);
    }
}
```

#### <a id="usageexample"></a>Usage Example

``` sql
psql=# CREATE EXTERNAL TABLE dummy_tbl
    (int1 integer, word text, int2 integer)
LOCATION ('pxf://localhost:51200/dummy_location'
          '?FRAGMENTER=DummyFragmenter'
          '&ACCESSOR=DummyAccessor'
          '&RESOLVER=DummyResolver')
FORMAT 'custom' (formatter = 'pxfwritable_import');
 
CREATE EXTERNAL TABLE
psql=# SELECT * FROM dummy_tbl;
int1 | word | int2
------+------+------
0 | fragment1 | 0
1 | fragment1 | 0
0 | fragment2 | 0
1 | fragment2 | 0
0 | fragment3 | 0
1 | fragment3 | 0
(6 rows)

psql=# CREATE WRITABLE EXTERNAL TABLE dummy_tbl_write
    (int1 integer, word text, int2 integer)
LOCATION ('pxf://localhost:51200/dummy_location'
          '?ACCESSOR=DummyAccessor'
          '&RESOLVER=DummyResolver')
FORMAT 'custom' (formatter = 'pxfwritable_export');
 
CREATE EXTERNAL TABLE
psql=# INSERT INTO dummy_tbl_write VALUES (1, 'a', 11), (2, 'b', 22);
INSERT 0 2
```


