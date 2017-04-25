---
title: Troubleshooting PXF
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

## <a id="pxerrortbl"></a>PXF Errors

The following table lists some common errors encountered while using PXF:

<table>
<caption><span class="tablecap">Table 1. PXF Errors and Explanation</span></caption>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Error</th>
<th>Common Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ERROR:  invalid URI pxf://localhost:51200/demo/file1: missing options section</td>
<td><code class="ph codeph">LOCATION</code> does not include options after the file name: <code class="ph codeph">&lt;path&gt;?&lt;key&gt;=&lt;value&gt;&amp;&lt;key&gt;=&lt;value&gt;...</code></td>
</tr>
<tr class="even">
<td>ERROR:  protocol &quot;pxf&quot; does not exist</td>
<td>HAWQ is not compiled with PXF protocol. It requires the GPSQL version of HAWQ</td>
</tr>
<tr class="odd">
<td>ERROR:  remote component error (0) from '&lt;x&gt;': There is no pxf servlet listening on the host and port specified in the external table url.</td>
<td>Wrong server or port, or the service is not started</td>
</tr>
<tr class="even">
<td>ERROR:  Missing FRAGMENTER option in the pxf uri: pxf://localhost:51200/demo/file1?a=a</td>
<td>No <code class="ph codeph">FRAGMENTER</code> option was specified in <code class="ph codeph">LOCATION</code>.</td>
</tr>
<tr class="odd">
<td>ERROR:  remote component error (500) from '&lt;x&gt;':   type  Exception report   message   org.apache.hadoop.mapred.InvalidInputException:
<p>Input path does not exist: hdfs://0.0.0.0:8020/demo/file1  </p></td>
<td>File or pattern given in <code class="ph codeph">LOCATION</code> doesn't exist on specified path.</td>
</tr>
<tr class="even">
<td>ERROR: remote component error (500) from '&lt;x&gt;':   type  Exception report   message   org.apache.hadoop.mapred.InvalidInputException : Input Pattern hdfs://0.0.0.0:8020/demo/file* matches 0 files </td>
<td>File or pattern given in <code class="ph codeph">LOCATION</code> doesn't exist on specified path.</td>
</tr>
<tr class="odd">
<td>ERROR:  remote component error (500) from '&lt;x&gt;': PXF not correctly installed in CLASSPATH</td>
<td>Cannot find PXF Jar</td>
</tr>
<tr class="even">
<td>ERROR:  PXF API encountered a HTTP 404 error. Either the PXF service (tomcat) on the DataNode was not started or the PXF webapp was not started.</td>
<td>Either the required DataNode does not exist or PXF service (tcServer) on the DataNode is not started or PXF webapp was not started</td>
</tr>
<tr class="odd">
<td>ERROR:  remote component error (500) from '&lt;x&gt;':  type  Exception report   message   java.lang.NoClassDefFoundError: org/apache/hadoop/hbase/client/HTableInterface</td>
<td>One of the classes required for running PXF or one of its plug-ins is missing. Check that all resources in the PXF classpath files exist on the cluster nodes</td>
</tr>
<tr class="even">
<td>ERROR: remote component error (500) from '&lt;x&gt;':   type  Exception report   message   java.io.IOException: Can't get Master Kerberos principal for use as renewer</td>
<td>Secure PXF: YARN isn't properly configured for secure (Kerberized) HDFS installs</td>
</tr>
<tr class="odd">
<td>ERROR: fail to get filesystem credential for uri hdfs://&lt;namenode&gt;:8020/</td>
<td>Secure PXF: Wrong HDFS host or port is not 8020</td>
</tr>
<tr class="even">
<td>ERROR: remote component error (413) from '&lt;x&gt;': HTTP status code is 413 but HTTP response string is empty</td>
<td>The PXF table number of attributes and their name sizes are too large for tcServer to accommodate in its request buffer. The solution is to increase the value of the maxHeaderCount and maxHttpHeaderSize parameters on server.xml on tcServer instance on all nodes and then restart PXF:
<p>&lt;Connector acceptCount=&quot;100&quot; connectionTimeout=&quot;20000&quot; executor=&quot;tomcatThreadPool&quot; maxKeepAliveRequests=&quot;15&quot;maxHeaderCount=&quot;&lt;some larger value&gt;&quot;maxHttpHeaderSize=&quot;&lt;some larger value in bytes&gt;&quot; port=&quot;${bio.http.port}&quot; protocol=&quot;org.apache.coyote.http11.Http11Protocol&quot; redirectPort=&quot;${bio.https.port}&quot;/&gt;</p></td>
</tr>
<tr class="odd">
<td>ERROR: remote component error (500) from '&lt;x&gt;': type Exception report message java.lang.Exception: Class com.pivotal.pxf.&lt;plugin name&gt; does not appear in classpath. Plugins provided by PXF must start with &quot;org.apache.hawq.pxf&quot;</td>
<td>Querying a PXF table that still uses the old package name (&quot;com.pivotal.pxf.*&quot;) results in an error message that recommends moving to the new package name (&quot;org.apache.hawq.pxf&quot;). </td>
</tr>
<tr class="even">
<td><strong>HBase Specific Errors</strong></td>
<td> </td>
</tr>
<tr class="odd">
<td>ERROR:  remote component error (500) from '&lt;x&gt;':   type  Exception report   message    org.apache.hadoop.hbase.client.NoServerForRegionException: Unable to find region for t1,,99999999999999 after 10 tries.</td>
<td>HBase service is down, probably HRegionServer</td>
</tr>
<tr class="even">
<td>ERROR:  remote component error (500) from '&lt;x&gt;':  type  Exception report   message   org.apache.hadoop.hbase.TableNotFoundException: nosuch</td>
<td>HBase cannot find the requested table</td>
</tr>
<tr class="odd">
<td>ERROR:  remote component error (500) from '&lt;x&gt;':  type  Exception report   message   java.lang.NoClassDefFoundError: org/apache/hadoop/hbase/client/HTableInterface</td>
<td>PXF cannot find a required JAR file, probably HBase's</td>
</tr>
<tr class="even">
<td>ERROR:  remote component error (500) from '&lt;x&gt;':   type  Exception report   message   java.lang.NoClassDefFoundError: org/apache/zookeeper/KeeperException</td>
<td>PXF cannot find ZooKeeper's JAR</td>
</tr>
<tr class="odd">
<td>ERROR:  remote component error (500) from '&lt;x&gt;':  type  Exception report   message   java.lang.Exception: java.lang.IllegalArgumentException: Illegal HBase column name a, missing :</td>
<td>PXF table has an illegal field name. Each field name must correspond to an HBase column in the syntax &lt;column family&gt;:&lt;field name&gt;</td>
</tr>
<tr class="even">
<td>ERROR: remote component error (500) from '&lt;x&gt;': type Exception report message org.apache.hadoop.hbase.regionserver.NoSuchColumnFamilyException: Column family a does not exist in region t1,,1405517248353.85f4977bfa88f4d54211cb8ac0f4e644. in table 't1', {NAME =&amp;gt; 'cf', DATA_BLOCK_ENCODING =&amp;gt; 'NONE', BLOOMFILTER =&amp;gt; 'ROW', REPLICATION_SCOPE =&amp;gt; '0', COMPRESSION =&amp;gt; 'NONE', VERSIONS =&amp;gt; '1', TTL =&amp;gt; '2147483647', MIN_VERSIONS =&amp;gt; '0', KEEP_DELETED_CELLS =&amp;gt; 'false', BLOCKSIZE =&amp;gt; '65536', ENCODE_ON_DISK =&amp;gt; 'true', IN_MEMORY =&amp;gt; 'false', BLOCKCACHE =&amp;gt; 'true'}</td>
<td>Required HBase table does not contain the requested column</td>
</tr>
<tr class="odd">
<td><strong>Hive-Specific Errors</td>
<td> </td>
</tr>
<tr class="even">
<td>ERROR:  remote component error (500) from '&lt;x&gt;':  type  Exception report   message   java.lang.RuntimeException: Failed to connect to Hive metastore: java.net.ConnectException: Connection refused</td>
<td>Hive Metastore service is down</td>
</tr>
<tr class="odd">
<td>ERROR:  remote component error (500) from '&lt;x&gt;': type  Exception report   message
<p>NoSuchObjectException(message:default.players table not found)</p></td>
<td>Table doesn't exist in Hive</td>
</tr>
<tr class="even">
<td><strong>JSON-Specific Errors</strong></td>
<td> </td>
</tr>
<tr class="odd">
<td>ERROR: No fields in record (seg0 slice1 host:&ltn&gt pid=&ltn&gt)
<p>DETAIL: External table &lttablename&gt</p></td>
<td>Check your JSON file for empty lines; remove them and try again</td>
</tr>
<tr class="odd">
<td>ERROR:  remote component error (500) from host:51200:  type  Exception report   message   &lttext&gt[0] is not an array node    description   The server encountered an internal error that prevented it from fulfilling this request.    exception   java.io.IOException: &lttext&gt[0] is not an array node (libchurl.c:878)  (seg4 host:40000 pid=&ltn&gt)  
<p>DETAIL:  External table &lttablename&gt</p></td>
<td>JSON field assumed to be an array, but it is a scalar field.
</td>
</tr>

</tbody>
</table>


## <a id="pxflogging"></a>PXF Logging
Enabling more verbose logging may aid PXF troubleshooting efforts.

PXF provides two categories of message logging - service-level and database-level.

### <a id="pxfsvclogmsg"></a>Service-Level Logging

PXF utilizes `log4j` for service-level logging. PXF-service-related log messages are captured in a log file specified by PXF's `log4j` properties file, `/etc/pxf/conf/pxf-log4j.properties`. The default PXF logging configuration will write `INFO` and more severe level logs to `/var/log/pxf/pxf-service.log`.

PXF provides more detailed logging when the `DEBUG` level is enabled.  To configure PXF `DEBUG` logging, uncomment the following line in `pxf-log4j.properties`:

``` shell
#log4j.logger.org.apache.hawq.pxf=DEBUG
```

and restart the PXF service:

``` shell
$ sudo service pxf-service restart
```

With `DEBUG` level logging now enabled, perform your PXF operations; for example, creating and querying an external table. (Make note of the time; this will direct you to the relevant log messages in `/var/log/pxf/pxf-service.log`.)

``` shell
$ psql
```

``` sql
gpadmin=# CREATE EXTERNAL TABLE hivetest(id int, newid int)
    LOCATION ('pxf://namenode:51200/pxf_hive1?PROFILE=Hive')
    FORMAT 'CUSTOM' (formatter='pxfwritable_import');
gpadmin=# select * from hivetest;
<select output>
```

Examine/collect the log messages from `pxf-service.log`.

**Note**: `DEBUG` logging is verbose and has a performance impact.  Remember to turn off PXF service `DEBUG` logging after you have collected the desired information.
 

### <a id="pxfdblogmsg"></a>Database-Level Logging

Database-level logging may provide insight into internal PXF service operations. Additionally, when you access Hive tables using `hcatalog` or the `Hive*` profiles, log messages identify the underlying `Hive*` profile(s) employed to access the data.

Enable HAWQ and PXF debug message logging during operations on PXF external tables by setting the `client_min_messages` server configuration parameter to `DEBUG2` in your `psql` session.

``` shell
$ psql
```

``` sql
gpadmin=# SET client_min_messages=DEBUG2
gpadmin=# SELECT * FROM hivetest;
...
DEBUG2:  churl http header: cell #19: X-GP-URL-HOST: localhost
DEBUG2:  churl http header: cell #20: X-GP-URL-PORT: 51200
DEBUG2:  churl http header: cell #21: X-GP-DATA-DIR: pxf_hive1
DEBUG2:  churl http header: cell #22: X-GP-profile: Hive
DEBUG2:  churl http header: cell #23: X-GP-URI: pxf://namenode:51200/pxf_hive1?profile=Hive
...
DEBUG2:  pxf: set_current_fragment_headers: using profile: Hive
...
```

Examine/collect the log messages from `stdout`.

**Note**: `DEBUG2` database session logging has a performance impact.  Remember to turn off `DEBUG2` logging after you have collected the desired information.

``` sql
gpadmin=# SET client_min_messages=NOTICE
```


## <a id="pxf-memcfg"></a>Addressing PXF Memory Issues

The Java heap size can be a limiting factor in PXF’s ability to serve many concurrent requests or to run queries against large tables.

You may run into situations where a query will hang or fail with an Out of Memory exception (OOM). This typically occurs when many threads are reading different data fragments from an external table and insufficient heap space exists to open all fragments at the same time. To avert or remedy this situation, Pivotal recommends first increasing the Java maximum heap size or decreasing the Tomcat maximum number of threads, depending upon what works best for your system configuration.

**Note**: The configuration changes described in this topic require modifying config files on *each* PXF node in your HAWQ cluster. After performing the updates, be sure to verify that the configuration on all PXF nodes is the same.

You will need to re-apply these configuration changes after any PXF version upgrades.

### <a id="pxf-heapcfg"></a>Increasing the Maximum Heap Size

Each PXF node is configured with a default Java heap size of 512MB. If the nodes in your cluster have an ample amount of memory, increasing the amount allocated to the PXF agents is the best approach. Pivotal recommends a heap size value between 1-2GB.

Perform the following steps to increase the PXF agent heap size in your HAWQ  deployment. **You must perform the configuration changes on each PXF node in your HAWQ cluster.**

1. Open `/var/pxf/pxf-service/bin/setenv.sh` in a text editor.

    ``` shell
    root@pxf-node$ vi /var/pxf/pxf-service/bin/setenv.sh
    ```

2. Update the `-Xmx` option to the desired value in the `JVM_OPTS` setting:

    ``` shell
    JVM_OPTS="-Xmx1024M -Xss256K"
    ```

3. Restart PXF:

    1. If you use Ambari to manage your cluster, restart the PXF service via the Ambari console.
    2. If you do not use Ambari, restart the PXF service from the command line on each node:

        ``` shell
        root@pxf-node$ service pxf-service restart
        ```

### <a id="pxf-heapcfg"></a>Decreasing the Maximum Number of  Threads

If increasing the maximum heap size is not suitable for your HAWQ cluster, try decreasing the number of concurrent working threads configured for the underlying Tomcat web application. A decrease in the number of running threads will prevent any PXF node from exhausting its memory, while ensuring that current queries run to completion (albeit a bit slower). As Tomcat's default behavior is to queue requests until a thread is free, decreasing this value will not result in denied requests.

The Tomcat default maximum number of threads is 300. Pivotal recommends  decreasing the maximum number of threads to under 6. (If you plan to run large workloads on a large number of files using a Hive profile, Pivotal recommends you pick an even lower value.)

Perform the following steps to decrease the maximum number of Tomcat threads in your HAWQ PXF deployment. **You must perform the configuration changes on each PXF node in your HAWQ cluster.**

1. Open the `/var/pxf/pxf-service/conf/server.xml` file in a text editor.

    ``` shell
    root@pxf-node$ vi /var/pxf/pxf-service/conf/server.xml
    ```

2. Update the `Catalina` `Executor` block to identify the desired `maxThreads` value:

    ``` xml
    <Executor maxThreads="2"
              minSpareThreads="50"
              name="tomcatThreadPool"
              namePrefix="tomcat-http--"/>
    ```

3. Restart PXF:

    1. If you use Ambari to manage your cluster, restart the PXF service via the Ambari console.
    2. If you do not use Ambari, restart the PXF service from the command line on each node:

        ``` shell
        root@pxf-node$ service pxf-service restart
        ```
