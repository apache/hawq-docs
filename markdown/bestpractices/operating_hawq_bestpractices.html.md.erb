---
title: Best Practices for Operating HAWQ
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

This topic provides best practices for operating HAWQ, including recommendations for stopping, starting and monitoring HAWQ.

## <a id="task_qgk_bz3_1v"></a>Best Practices Using the Command Line to Start/Stop HAWQ Cluster Members

The following best practices are recommended when using `hawq start` and `hawq stop` to manage your HAWQ cluster.

-   Always use HAWQ management commands to start and stop HAWQ, instead of Postgres equivalents.
-   Use `hawq start cluster` or `hawq restart cluster` to start the entire cluster, rather than starting the master and individual segments.
-   If you do decide to use `hawq start standby|master|segment` to start nodes individually, always start the standby before the active master. Otherwise, the standby can become unsynchronized with the active master.
-   When stopping a cluster, issue the `CHECKPOINT` command to update and flush all data files to disk and update the log file before stopping the cluster. A checkpoint ensures that, in the event of a crash, files can be restored from the checkpoint snapshot.
-   Stop the entire HAWQ system by stopping the cluster on the master host:
    ```shell
    $ hawq stop cluster
    ```

-   To stop segments and kill any running queries without causing data loss or inconsistency issues, use `fast` or `immediate` mode on the cluster:

    ```shell
    $ hawq stop cluster -M fast
    ```
    ```shell
    $ hawq stop cluster -M immediate
    ```

-   Use `hawq stop master` to stop the master only. If you cannot stop the master due to running transactions, try using fast shutdown. If fast shutdown does not work, use immediate shutdown. Use immediate shutdown with caution, as it will result in a crash-recovery run when the system is restarted. 

    ```shell
    $ hawq stop master -M fast
    ```
    ```shell
    $ hawq stop master -M immediate
    ```

-   When stopping a segment or all segments, you can use the default mode of smart mode. Using fast or immediate mode on segments will have no effect since segments are stateless.

    ```shell
    $ hawq stop segment
    ```
    ```shell
    $ hawq stop allsegments
    ```

## <a id="id_trr_m1j_1v"></a>Guidelines for Cluster Expansion

This topic provides some guidelines around expanding your HAWQ cluster.

There are several recommendations to keep in mind when modifying the size of your running HAWQ cluster:

-   When you add a new node, install both a DataNode and a physical segment on the new node.
-   After adding a new node, you should always rebalance HDFS data to maintain cluster performance.
-   Adding or removing a node also necessitates an update to the HDFS metadata cache. This update will happen eventually, but can take some time. To speed the update of the metadata cache, execute **`select gp_metadata_cache_clear();`**.
-   Note that for hash distributed tables, expanding the cluster will not immediately improve performance since hash distributed tables use a fixed number of virtual segments. In order to obtain better performance with hash distributed tables, you must redistribute the table to the updated cluster by either the [ALTER TABLE](../reference/sql/ALTER-TABLE.html) or [CREATE TABLE AS](../reference/sql/CREATE-TABLE-AS.html#topic1) command.
-   If you are using hash tables, consider updating the `default_hash_table_bucket_number` server configuration parameter to a larger value after expanding the cluster but before redistributing the hash tables.

## <a id="best_pract_monitoring"></a>Best Practices for Monitoring a HAWQ System
The sections below provide recommendations for common monitoring tasks. 

**Note:** If your HAWQ cluster is managed through the Ambari interface, use Ambari to perform the suggested monitoring tasks. 

### <a id="id_o5n_p1j_1v"></a>Database State Monitoring Activities

<a id="id_o5n_p1j_1v__d112e31"></a>

<table>
<caption><span class="tablecap">Table 1. Database State Monitoring Activities</span></caption>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Activity</th>
<th>Procedure</th>
<th>Corrective Actions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>List segments that are currently down. If any rows are returned, this should generate a warning or alert.
<p>Recommended frequency: run every 5 to 10 minutes</p>
<p>Severity: IMPORTANT</p></td>
<td>Run the following query in the <code class="ph codeph">postgres</code> database:
<pre class="pre codeblock"><code>SELECT * FROM gp_segment_configuration
WHERE status &lt;&gt; &#39;u&#39;;</code></pre></td>
<td>If the query returns any rows, follow these steps to correct the problem:
<ol>
<li>Verify that the hosts with down segments are responsive.</li>
<li>If hosts are OK, check the <span class="ph filepath">pg_log</span> files for the down segments to discover the root cause of the segments going down.</li>
</ol></td>
</tr>
</tbody>
</table>


### <a id="id_d3w_p1j_1v"></a>Hardware and Operating System Monitoring

<a id="id_d3w_p1j_1v__d112e111"></a>

<table>
<caption><span class="tablecap">Table 2. Hardware and Operating System Monitoring Activities</span></caption>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Activity</th>
<th>Procedure</th>
<th>Corrective Actions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Underlying platform check for maintenance required or system down of the hardware.
<p>Recommended frequency: real-time, if possible, or every 15 minutes</p>
<p>Severity: CRITICAL</p></td>
<td>Set up system check for hardware and OS errors.</td>
<td>If required, remove a machine from the HAWQ cluster to resolve hardware and OS issues, then add it back to the cluster after the issues are resolved.</td>
</tr>
<tr class="even">
<td>Check disk space usage on volumes used for HAWQ data storage and the OS.
<p>Recommended frequency: every 5 to 30 minutes</p>
<p>Severity: CRITICAL</p></td>
<td><div class="p">
Set up a disk space check.
<ul>
<li>Set a threshold to raise an alert when a disk reaches a percentage of capacity. The recommended threshold is 75% full.</li>
<li>It is not recommended to run the system with capacities approaching 100%.</li>
</ul>
</div></td>
<td>Free space on the system by removing some data or files.</td>
</tr>
<tr class="odd">
<td>Check for errors or dropped packets on the network interfaces.
<p>Recommended frequency: hourly</p>
<p>Severity: IMPORTANT</p></td>
<td>Set up a network interface checks.</td>
<td><p>Work with network and OS teams to resolve errors.</p></td>
</tr>
<tr class="even">
<td>Check for RAID errors or degraded RAID performance.
<p>Recommended frequency: every 5 minutes</p>
<p>Severity: CRITICAL</p></td>
<td>Set up a RAID check.</td>
<td><ul>
<li>Replace failed disks as soon as possible.</li>
<li>Work with system administration team to resolve other RAID or controller errors as soon as possible.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Check for adequate I/O bandwidth and I/O skew.
<p>Recommended frequency: when create a cluster or when hardware issues are suspected.</p></td>
<td>Run the HAWQ <code class="ph codeph">hawq checkperf</code> utility.</td>
<td><div class="p">
The cluster may be under-specified if data transfer rates are not similar to the following:
<ul>
<li>2GB per second disk read</li>
<li>1 GB per second disk write</li>
<li>10 Gigabit per second network read and write</li>
</ul>
If transfer rates are lower than expected, consult with your data architect regarding performance expectations.
</div>
<p>If the machines on the cluster display an uneven performance profile, work with the system administration team to fix faulty machines.</p></td>
</tr>
</tbody>
</table>


### <a id="id_khd_q1j_1v"></a>Data Maintenance

<a id="id_khd_q1j_1v__d112e279"></a>

<table>
<caption><span class="tablecap">Table 3. Data Maintenance Activities</span></caption>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Activity</th>
<th>Procedure</th>
<th>Corrective Actions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Check for missing statistics on tables.</td>
<td>Check the <code class="ph codeph">hawq_stats_missing</code> view in each database:
<pre class="pre codeblock"><code>SELECT * FROM hawq_toolkit.hawq_stats_missing;</code></pre></td>
<td>Run <code class="ph codeph">ANALYZE</code> on tables that are missing statistics.</td>
</tr>
</tbody>
</table>


### <a id="id_lx4_q1j_1v"></a>Database Maintenance

<a id="id_lx4_q1j_1v__d112e343"></a>

<table>
<caption><span class="tablecap">Table 4. Database Maintenance Activities</span></caption>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Activity</th>
<th>Procedure</th>
<th>Corrective Actions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Mark deleted rows in HAWQ system catalogs (tables in the <code class="ph codeph">pg_catalog</code> schema) so that the space they occupy can be reused.
<p>Recommended frequency: daily</p>
<p>Severity: CRITICAL</p></td>
<td>Vacuum each system catalog:
<pre class="pre codeblock"><code>VACUUM &lt;table&gt;;</code></pre></td>
<td>Vacuum system catalogs regularly to prevent bloating.</td>
</tr>
<tr class="even">
<td>Update table statistics.
<p>Recommended frequency: after loading data and before executing queries</p>
<p>Severity: CRITICAL</p></td>
<td>Analyze user tables:
<pre class="pre codeblock"><code>ANALYZEDB -d &lt;database&gt; -a</code></pre></td>
<td>Analyze updated tables regularly so that the optimizer can produce efficient query execution plans.</td>
</tr>
<tr class="odd">
<td>Backup the database data.
<p>Recommended frequency: daily, or as required by your backup plan</p>
<p>Severity: CRITICAL</p></td>
<td>See <a href="../admin/BackingUpandRestoringHAWQDatabases.html">Backing up and Restoring HAWQ Databases</a> for a discussion of backup procedures</td>
<td>Best practice is to have a current backup ready in case the database must be restored.</td>
</tr>
<tr class="even">
<td>Reindex system catalogs (tables in the <code class="ph codeph">pg_catalog</code> schema) to maintain an efficient catalog.
<p>Recommended frequency: weekly, or more often if database objects are created and dropped frequently</p></td>
<td>Run <code class="ph codeph">REINDEX SYSTEM</code> in each database.
<pre class="pre codeblock"><code>REINDEXDB -s</code></pre></td>
<td>The optimizer retrieves information from the system tables to create query plans. If system tables and indexes are allowed to become bloated over time, scanning the system tables increases query execution time.</td>
</tr>
</tbody>
</table>


### <a id="id_blv_q1j_1v"></a>Patching and Upgrading

<a id="id_blv_q1j_1v__d112e472"></a>

<table>
<caption><span class="tablecap">Table 5. Patch and Upgrade Activities</span></caption>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Activity</th>
<th>Procedure</th>
<th>Corrective Actions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Ensure any bug fixes or enhancements are applied to the kernel.
<p>Recommended frequency: at least every 6 months</p>
<p>Severity: IMPORTANT</p></td>
<td>Follow the vendor's instructions to update the Linux kernel.</td>
<td>Keep the kernel current to include bug fixes and security fixes, and to avoid difficult future upgrades.</td>
</tr>
<tr class="even">
<td>Install HAWQ minor releases.
<p>Recommended frequency: quarterly</p>
<p>Severity: IMPORTANT</p></td>
<td>Always upgrade to the latest in the series.</td>
<td>Keep the HAWQ software current to incorporate bug fixes, performance enhancements, and feature enhancements into your HAWQ cluster.</td>
</tr>
</tbody>
</table>



