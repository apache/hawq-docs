# Elastic Virtual Segment Allocation {#hawqarchitecture}

HAWQ uses dynamically allocated virtual segments to provide resources for query execution.

In HAWQ 1.x, the number of segments \(compute resource carrier\) used to run a query is fixed, no matter whether the underlying query is big query requiring many resources or a small query requiring little resources. This architecture is simple, however it uses resources inefficiently.

To address this issue, HAWQ now uses the elastic virtual segment allocation feature, which is based on virtual segments. HAWQ allocates virtual segments on demand based on the costs of queries. In other words, for big queries, HAWQ starts a large number of virtual segments, while for small queries HAWQ starts fewer virtual segments.

## Storage { .section}

In HAWQ 2.0, the number of invoked segments varies based on cost of query. In order to simplify table data management, all data of one relation are saved under one HDFS folder.

For all the HAWQ 2.0 table storage formats, AO \(Append-Only\) and Parquet, the data files are splittable, so that HAWQ can assign multiple virtual segments to consume one data file concurrently to increase the parallelism of a query.

## Physical Segments and Virtual Segments { .section}

In HAWQ 2.0, only one physical segment needs to be installed on one host, in which multiple virtual segments can be started to run queries. HAWQ 2.0 allocates multiple virtual segments distributed across different hosts on demand to run one query. Virtual segments are carriers \(containers\) for resources such as memory and CPU. Queries are executed by query executors in virtual segments.

**Note:** In this documentation, when we refer to segment by itself, we mean a *physical segment*.

## Virtual Segment Allocation Policy { .section}

Different number of virtual segments are allocated based on virtual segment allocation policies. The following factors determine the number of virtual segments that are used for a query:

-   Resources available at the query running time
-   The cost of the query
-   The distribution of the table; in other words, randomly distributed tables and hash distributed tables
-   Whether the query involves UDFs and external tables

