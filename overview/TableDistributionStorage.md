# Table Distribution and Storage {#hawqarchitecture}

HAWQ stores all table data, except the system table, in HDFS. When a user creates a table, the metadata is stored on the master's local file system and the table content is stored in HDFS.

In order to simplify table data management, all the data of one relation are saved under one HDFS folder.

For all HAWQ table storage formats, AO \(Append-Only\) and Parquet, the data files are splittable, so that HAWQ can assign multiple virtual segments to consume one data file concurrently. This increases the degree of query parallelism.

## Table Distribution Policy { .section}

The default table distribution policy in HAWQ is random.

Randomly distributed tables have some benefits over hash distributed tables. For example, after cluster expansion, HAWQ can use more resources automatically without redistributing the data. For huge tables, redistribution is very expensive, and data locality for randomly distributed tables is better after the underlying HDFS redistributes its data during rebalance or data node failures. This is quite common when the cluster is large.

On the other hand, for some queries, hash distributed tables are faster than randomly distributed tables. For example, hash distributed tables have some performance benefits for some TPC-H queries. You should choose the distribution policy that is best suited for your application's scenario.

See [Choosing the Table Distribution Policy](../ddl/ddl-table.md#) for more details.

## Data Locality { .section}

Data is distributed across HDFS DataNodes. Since remote read involves network I/O, a data locality algorithm improves the local read ratio. HAWQ considers three aspects when allocating data blocks to virtual segments:

-   Ratio of local read
-   Continuity of file read
-   Data balance among virtual segments

