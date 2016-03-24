# Recommended Monitoring and Maintenance Tasks {#topic_kmz_lbg_rp}

This section lists monitoring and maintenance activities recommended to ensure high availability and consistent performance of your HAWQ cluster.

The tables in the following sections suggest activities that a HAWQ System Administrator can perform periodically to ensure that all components of the system are operating optimally. Monitoring activities help you to detect and diagnose problems early. Maintenance activities help you to keep the system up-to-date and avoid deteriorating performance, for example, from bloated system tables or diminishing free disk space.

It is not necessary to implement all of these suggestions in every cluster; use the frequency and severity recommendations as a guide to implement measures according to your service requirements.

## Database State Monitoring Activities {#drr_5bg_rp}

|Activity|Procedure|Corrective Actions|
|--------|---------|------------------|
|List segments that are currently down. If any rows are returned, this should generate a warning or alert.Recommended frequency: run every 5 to 10 minutes

Severity: IMPORTANT

|Run the following query in the `postgres` database:```
SELECT * FROM gp_segment_configuration
WHERE status <> 'u';
```

|If the query returns any rows, follow these steps to correct the problem:1.  Verify that the hosts with down segments are responsive.
2.  If hosts are OK, check the pg\_log files for the down segments to discover the root cause of the segments going down.
3.  If no unexpected errors are found, run the `gprecoverseg` utility to bring the segments back online.

|
|Run a distributed query to test that it runs on all segments. One row should be returned for each segment. Recommended frequency: run every 5 to 10 minutes

Severity: CRITICAL

|Execute the following query in the `postgres` database:

```
SELECT gp_segment_id, count(*)
FROM gp_dist_random('pg_class')
GROUP BY 1;
```

|If this query fails, there is an issue dispatching to some segments in the cluster. This is a rare event. Check the hosts that are not able to be dispatched to ensure there is no hardware or networking issue.

|
|Perform a basic check to see if the master is up and functioning.Recommended frequency: run every 5 to 10 minutes

Severity: CRITICAL

|Run the following query in the `postgres` database:

```
SELECT count(*) FROM gp_segment_configuration;
```

|If this query fails the active master may be down. Try again several times and then inspect the active master manually. If the active master is down, reboot or power cycle the active master to ensure no processes remain on the active master and then trigger the activation of the standby master.

|

## Hardware and Operating System Monitoring {#topic_y4c_4gg_rp}

|Activity|Procedure|Corrective Actions|
|--------|---------|------------------|
|Underlying platform check for maintenance required or system down of the hardware.Recommended frequency: real-time, if possible, or every 15 minutes

Severity: CRITICAL

|Set up system check for hardware and OS errors.|If required, remove a machine from the HAWQ cluster to resolve hardware and OS issues, then, after add it back to the cluster and run `gprecoverseg`.|
|Check disk space usage on volumes used for HAWQ data storage and the OS. Recommended frequency: every 5 to 30 minutes

Severity: CRITICAL

|Set up a disk space check.

-   Set a threshold to raise an alert when a disk reaches a percentage of capacity. The recommended threshold is 75% full.
-   It is not recommended to run the system with capacities approaching 100%.

|Free space on the system by removing some data or files.|
|Check for errors or dropped packets on the network interfaces.Recommended frequency: hourly

Severity: IMPORTANT

|Set up a network interface checks.|Work with network and OS teams to resolve errors.

|
|Check for RAID errors or degraded RAID performance. Recommended frequency: every 5 minutes

Severity: CRITICAL

|Set up a RAID check.|-   Replace failed disks as soon as possible.
-   Work with system administration team to resolve other RAID or controller errors as soon as possible.

|
|Check for adequate I/O bandwidth and I/O skew.Recommended frequency: when create a cluster or when hardware issues are suspected.

|Run the HAWQ `hawq checkperf` utility.|The cluster may be under-specified if data transfer rates are not similar to the following:

-   2GB per second disk read
-   1 GB per second disk write
-   10 Gigabit per second network read and write

If transfer rates are lower than expected, consult with your data architect regarding performance expectations.

If the machines on the cluster display an uneven performance profile, work with the system administration team to fix faulty machines.

|

## Data Maintenance {#maintentenance_check_scripts}

|Activity|Procedure|Corrective Actions|
|--------|---------|------------------|
|Check for missing statistics on tables.|Check the `hawq_stats_missing` view in each database:```
SELECT * FROM hawq_toolkit.hawq_stats_missing;
```

|Run `ANALYZE` on tables that are missing statistics.|

## Database Maintenance {#topic_dld_23h_rp}

|Activity|Procedure|Corrective Actions|
|--------|---------|------------------|
|Mark deleted rows in HAWQ system catalogs \(tables in the `pg_catalog` schema\) so that the space they occupy can be reused.Recommended frequency: daily

Severity: CRITICAL

|Vacuum each system catalog:```
VACUUM *<table\>*;
```

|Vacuum system catalogzs regularly to prevent bloating.|
|Vacuum all system catalogs \(tables in the `pg_catalog` schema\) that are approaching [vacuum\_freeze\_min\_age](../reference/guc/parameter_definitions.md#).Recommended frequency: daily

Severity: CRITICAL

|Vacuum an individual table:```
VACUUM *<table\>*;
```

|After the [vacuum\_freeze\_min\_age](../reference/guc/parameter_definitions.md#) value is reached, VACUUM will no longer replace transaction IDs with `FrozenXID` while scanning a table. Perform vacuum on these tables before the limit is reached.|
|Update table statistics. Recommended frequency: after loading data and before executing queries

Severity: CRITICAL

|Analyze user tables:```
ANALYZEDB -d <database\> -a
```

|Analyze updated tables regularly so that the optimizer can produce efficient query execution plans.|
|Backup the database data.Recommended frequency: daily, or as required by your backup plan

Severity: CRITICAL

|See [Backing Up and Restoring HAWQ](BackingUpandRestoringHAWQDatabases.md) for a discussion of backup procedures.|Best practice is to have a current backup ready in case the database must be restored.|
|Vacuum and reindex system catalogs \(tables in the `pg_catalog` schema\) to maintain an efficient catalog.Recommended frequency: weekly, or more often if database objects are created and dropped frequently

|1.  `VACUUM` the system tables in each database.
2.  Run `REINDEX SYSTEM` in each database.

    ```
REINDEXDB -s
    ```


|The optimizer retrieves information from the system tables to create query plans. If system tables and indexes are allowed to become bloated over time, scanning the system tables increases query execution time.|

## Patching and Upgrading {#topic_idx_smh_rp}

|Activity|Procedure|Corrective Actions|
|--------|---------|------------------|
|Ensure any bug fixes or enhancements are applied to the kernel.Recommended frequency: at least every 6 months

Severity: IMPORTANT

|Follow the vendor's instructions to update the Linux kernel.|Keep the kernel current to include bug fixes and security fixes, and to avoid difficult future upgrades.|
|Install HAWQ minor releases.Recommended frequency: quarterly

Severity: IMPORTANT

|Always upgrade to the latest in the series.|Keep the HAWQ software current to incorporate bug fixes, performance enhancements, and feature enhancements into your HAWQ cluster.|

