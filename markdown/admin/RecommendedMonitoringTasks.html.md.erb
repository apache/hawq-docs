---
title: Recommended Monitoring and Maintenance Tasks
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

This section lists monitoring and maintenance activities recommended to ensure high availability and consistent performance of your HAWQ cluster.

The tables in the following sections suggest activities that a HAWQ System Administrator can perform periodically to ensure that all components of the system are operating optimally. Monitoring activities help you to detect and diagnose problems early. Maintenance activities help you to keep the system up-to-date and avoid deteriorating performance, for example, from bloated system tables or diminishing free disk space.

It is not necessary to implement all of these suggestions in every cluster; use the frequency and severity recommendations as a guide to implement measures according to your service requirements.

## <a id="drr_5bg_rp"></a>Database State Monitoring Activities 

<table>
  <tr>
    <th>Activity</th>
    <th>Procedure</th>
    <th>Corrective Actions</th>
  </tr>
  <tr>
    <td><p>List segments that are currently down. If any rows are returned, this should generate a warning or alert.</p>
    <p>Recommended frequency: run every 5 to 10 minutes</p><p>Severity: IMPORTANT</p></td>
    <td>Run the following query in the `postgres` database:
    <pre><code>SELECT * FROM gp_segment_configuration
WHERE status <> 'u';
</code></pre>
  </td>
  <td>If the query returns any rows, follow these steps to correct the problem:
  <ol>
    <li>Verify that the hosts with down segments are responsive.</li>
    <li>If hosts are OK, check the pg_log files for the down segments to discover the root cause of the segments going down.</li>
    </ol>
    </td>
    </tr>
  <tr>
    <td>
      <p>Run a distributed query to test that it runs on all segments. One row should be returned for each segment.</p>
      <p>Recommended frequency: run every 5 to 10 minutes</p>
      <p>Severity: CRITICAL</p>
    </td>
    <td>
      <p>Execute the following query in the `postgres` database:</p>
      <pre><code>SELECT gp_segment_id, count(&#42;)
FROM gp_dist_random('pg_class')
GROUP BY 1;
</code></pre>
  </td>
  <td>If this query fails, there is an issue dispatching to some segments in the cluster. This is a rare event. Check the hosts that are not able to be dispatched to ensure there is no hardware or networking issue.</td>
  </tr>
  <tr>
    <td>
      <p>Perform a basic check to see if the master is up and functioning.</p>
      <p>Recommended frequency: run every 5 to 10 minutes</p>
      <p>Severity: CRITICAL</p>
    </td>
    <td>
      <p>Run the following query in the `postgres` database:</p>
      <pre><code>SELECT count(&#42;) FROM gp_segment_configuration;</code></pre>
    </td>
    <td>
      <p>If this query fails the active master may be down. Try again several times and then inspect the active master manually. If the active master is down, reboot or power cycle the active master to ensure no processes remain on the active master and then trigger the activation of the standby master.</p>
    </td>
  </tr>
</table>

## <a id="topic_y4c_4gg_rp"></a>Hardware and Operating System Monitoring 

<table>
  <tr>
    <th>Activity</th>
    <th>Procedure</th>
    <th>Corrective Actions</th>
  </tr>
  <tr>
    <td>
      <p>Underlying platform check for maintenance required or system down of the hardware.</p>
      <p>Recommended frequency: real-time, if possible, or every 15 minutes</p>
      <p>Severity: CRITICAL</p>
    </td>
    <td>
      <p>Set up system check for hardware and OS errors.</p>
    </td>
    <td>
      <p>If required, remove a machine from the HAWQ cluster to resolve hardware and OS issues, then add it back to the cluster.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>Check disk space usage on volumes used for HAWQ data storage and the OS. Recommended frequency: every 5 to 30 minutes</p>
      <p>Severity: CRITICAL</p>
    </td>
    <td>
      <p>Set up a disk space check.</p>
      <ul>
        <li>Set a threshold to raise an alert when a disk reaches a percentage of capacity. The recommended threshold is 75% full.</li>
        <li>It is not recommended to run the system with capacities approaching 100%.</li>
      </ul>
    </td>
    <td>
      <p>Free space on the system by removing some data or files.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>Check for errors or dropped packets on the network interfaces.</p>
      <p>Recommended frequency: hourly</p>
      <p>Severity: IMPORTANT</p>
    </td>
    <td>
      <p>Set up a network interface checks.</p>
    </td>
    <td>
      <p>Work with network and OS teams to resolve errors.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>Check for RAID errors or degraded RAID performance.</p>
      <p>Recommended frequency: every 5 minutes</p>
      <p>Severity: CRITICAL</p>
    </td>
    <td>
      <p>Set up a RAID check.</p>
    </td>
    <td>
      <ul>
        <li>Replace failed disks as soon as possible.</li>
        <li>Work with system administration team to resolve other RAID or controller errors as soon as possible.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <p>Check for adequate I/O bandwidth and I/O skew.</p>
      <p>Recommended frequency: when create a cluster or when hardware issues are suspected.</p>
    </td>
    <td>
      <p>Run the HAWQ `hawq checkperf` utility.</p>
    </td>
    <td>
      <p>The cluster may be under-specified if data transfer rates are not similar to the following:</p>
      <ul>
        <li>2GB per second disk read</li>
        <li>1 GB per second disk write</li>
        <li>10 Gigabit per second network read and write</li>
      </ul>
      <p>If transfer rates are lower than expected, consult with your data architect regarding performance expectations.</p>
      <p>If the machines on the cluster display an uneven performance profile, work with the system administration team to fix faulty machines.</p>
    </td>
  </tr>
</table>

## <a id="maintentenance_check_scripts"></a>Data Maintenance 

<table>
  <tr>
    <th>Activity</th>
    <th>Procedure</th>
    <th>Corrective Actions</th>
  </tr>
  <tr>
    <td>Check for missing statistics on tables.</td>
    <td>Check the `hawq_stats_missing` view in each database:
    <pre><code>SELECT * FROM hawq_toolkit.hawq_stats_missing;</code></pre>
    </td>
    <td>Run <code>ANALYZE</code> on tables that are missing statistics.</td>
  </tr>
</table>

## <a id="topic_dld_23h_rp"></a>Database Maintenance 

<table>
  <tr>
    <th>Activity</th>
    <th>Procedure</th>
    <th>Corrective Actions</th>
  </tr>
  <tr>
    <td>
      <p>Mark deleted rows in HAWQ system catalogs (tables in the `pg_catalog` schema) so that the space they occupy can be reused.</p>
      <p>Recommended frequency: daily</p>
      <p>Severity: CRITICAL</p>
    </td>
    <td>
      <p>Vacuum each system catalog:</p>
      <pre><code>VACUUM &lt;<i>table</i>&gt;;</code></pre>
    </td>
    <td>Vacuum system catalogues regularly to prevent bloating.</td>
  </tr>
  <tr>
    <td>
    <p>Vacuum all system catalogs (tables in the <code>pg_catalog</code> schema) that are approaching <a href="../reference/guc/parameter_definitions.html">vacuum_freeze_min_age</a>.</p>
    <p>Recommended frequency: daily</p>
    <p>Severity: CRITICAL</p>
    </td>
    <td>
      <p><p>Vacuum an individual system catalog table:</p>
      <pre><code>VACUUM &lt;<i>table</i>&gt;;</code></pre>
    </td>
    <td>After the <a href="../reference/guc/parameter_definitions.html">vacuum_freeze_min_age</a> value is reached, VACUUM will no longer replace transaction IDs with <code>FrozenXID</code> while scanning a table. Perform vacuum on these tables before the limit is reached.</td>
  </tr>
    <td>
      <p>Update table statistics.</p>
      <p>Recommended frequency: after loading data and before executing queries</p>
      <p>Severity: CRITICAL</p>
    </td>
    <td>
      <p>Analyze user tables:</p>
      <pre><code>ANALYZEDB -d &lt;<i>database</i>&gt; -a</code></pre>
    </td>
    <td>Analyze updated tables regularly so that the optimizer can produce efficient query execution plans.</td>
  </tr>
  <tr>
    <td>
      <p>Backup the database data.</p>
      <p>Recommended frequency: daily, or as required by your backup plan</p>
      <p>Severity: CRITICAL</p>
    </td>
    <td>See <a href="BackingUpandRestoringHAWQDatabases.html">Backing Up and Restoring HAWQ</a> for a discussion of backup procedures.</td>
    <td>Best practice is to have a current backup ready in case the database must be restored.</td>
  </tr>
  <tr>
    <td>
      <p>Vacuum system catalogs (tables in the <code>pg_catalog</code> schema) to maintain an efficient catalog.</p>
      <p>Recommended frequency: weekly, or more often if database objects are created and dropped frequently</p>
    </td>
    <td>
      <p><code>VACUUM</code> the system tables in each database.</p>
    </td>
    <td>The optimizer retrieves information from the system tables to create query plans. If system tables and indexes are allowed to become bloated over time, scanning the system tables increases query execution time.</td>
  </tr>
</table>

## <a id="topic_idx_smh_rp"></a>Patching and Upgrading 

<table>
  <tr>
    <th>Activity</th>
    <th>Procedure</th>
    <th>Corrective Actions</th>
  </tr>
  <tr>
    <td>
      <p>Ensure any bug fixes or enhancements are applied to the kernel.</p>
      <p>Recommended frequency: at least every 6 months</p>
      <p>Severity: IMPORTANT</p>
    </td>
    <td>Follow the vendor's instructions to update the Linux kernel.</td>
    <td>Keep the kernel current to include bug fixes and security fixes, and to avoid difficult future upgrades.</td>
  </tr>
  <tr>
    <td>
      <p>Install HAWQ minor releases.</p>
      <p>Recommended frequency: quarterly</p>
      <p>Severity: IMPORTANT</p>
    </td>
    <td>Always upgrade to the latest in the series.</td>
    <td>Keep the HAWQ software current to incorporate bug fixes, performance enhancements, and feature enhancements into your HAWQ cluster.</td>
  </tr>
</table>
