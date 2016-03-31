---
title: Choosing the Table Storage Model <a id="topic_r2v_zvy_sp"></a>
---

HAWQ supports several storage models and a mix of storage models. When you create a table, you choose how to store its data. This topic explains the options for table storage and how to choose the best storage model for your workload.

-   [Choosing Row or Column-Oriented Storage](#topic39)
-   [Altering a Table](#topic55)
-   [Dropping a Table](#topic62)

**Note:** To simplify the creation of database tables, you can specify the default values for some table storage options with the HAWQ server configuration parameter `gp_default_storage_options`.

## Choosing Row or Column-Oriented Storage <a id="topic39"></a>

HAWQ provides a choice of storage orientation models: row, column, or a combination of both. This topic provides general guidelines for choosing the optimum storage orientation for a table. Evaluate performance using your own data and query workloads.

-   Row-oriented storage: good for OLTP types of workloads with many iterative transactions and many columns of a single row needed all at once, so retrieving is efficient.
-   Column-oriented storage: good for data warehouse workloads with aggregations of data computed over a small number of columns, or for single columns that require regular updates without modifying other column data.

    **Note:** Column-oriented storage is deprecated, and can only be enabled by specifically enabling the `gp_enable_ column_oriented_table` parameter. Parquet storage should be used, instead.


Parquet tables are preferred for HAWQ internal tables. For most general purpose or mixed workloads, row-oriented storage offers the best combination of flexibility and performance, as HAWQ storage is implemented with one file per column, which can put a burden on hdfs. For example, if a table with 20 segments, 1000 columns, and 500 partitions is stored in HAWQ with `orientation=column` , it will generate about 20x1000x500 files in hdfs. Selecting `orientation=parquet` results in only 20x500 files.

However, there are use cases where a column-oriented storage model could provide more efficient I/O and storage. Consider the following requirements when deciding on the storage orientation model for a table:

-   **Updates of table data.** If you load and update the table data frequently, choose a row-oriented table.
-   **Frequent INSERTs.** If rows are frequently inserted into the table, choose a row-oriented model. Column-oriented tables are not optimized for write operations, as column values for a row must be written to different places on disk.
-   **Number of columns requested in queries.** If you typically request all or the majority of columns in the `SELECT` list or `WHERE` clause of your queries, choose a row-oriented model. Column-oriented tables are best suited to queries that aggregate many values of a single column where the `WHERE` or `HAVING` predicate is also on the aggregate column. For example:

    ```
    SELECT SUM(salary)...
    ```

    ```
    SELECT AVG(salary)... WHERE salary > 10000
    ```

    Or where the `WHERE` predicate is on a single column and returns a relatively small number of rows. For example:

    ```
    SELECT salary, dept ... WHERE state='CA'
    ```

-   **Number of columns in the table.** Row-oriented storage is most efficient when many columns are required at the same time, or when the row-size of a table is relatively small. Keep in mind that hdfs is not good at handling large numbers of files and using `orientation=column`, generates one file per column in hdfs. However, column-oriented tables might offer better query performance on tables with many columns, provided you access only a small subset of columns in your queries.
-   **Compression.** Column data has the same data type, so storage size optimizations are available in column-oriented data that are not available in row-oriented data. For example, many compression schemes use the similarity of adjacent data to compress. However, the greater adjacent compression achieved, the more difficult random access becomes, as data must be uncompressed to be read.

### To create a column-oriented table <a id="im169305"></a>

The `WITH` clause of the `CREATE TABLE` command specifies the table's storage options. The default is a row-oriented.

**Note:** Column orientation is deprecated. To use column orientation, you must first set the `gp_enable_column_oriented_table parameter` to `on`.

For example, to create a column-oriented table:

```
=> CREATE TABLE bar (a int, b text)
    WITH (appendonly=true, orientation=column)
    DISTRIBUTED BY (a);
```

## Altering a Table <a id="topic55"></a>

The `ALTER TABLE`command changes the definition of a table. Use `ALTER TABLE` to change table attributes such as column definitions, distribution policy, storage model, and partition structure \(see also [Maintaining Partitioned Tables](ddl-partition.html)\). For example, to add a not-null constraint to a table column:

```
=> ALTER TABLE address ALTER COLUMN street SET NOT NULL;
```

### Altering Table Distribution <a id="topic56"></a>

`ALTER TABLE` provides options to change a table's distribution policy . When the table distribution options change, the table data is redistributed on disk, which can be resource intensive. You can also redistribute table data using the existing distribution policy.

### Changing the Distribution Policy <a id="topic57"></a>

For partitioned tables, changes to the distribution policy apply recursively to the child partitions. This operation preserves the ownership and all other attributes of the table. For example, the following command redistributes the table sales across all segments using the customer\_id column as the distribution key:

```
ALTER TABLE sales SET DISTRIBUTED BY (customer_id);
```

When you change the hash distribution of a table, table data is automatically redistributed. Changing the distribution policy to a random distribution does not cause the data to be redistributed. For example:

```
ALTER TABLE sales SET DISTRIBUTED RANDOMLY;
```

### Redistributing Table Data <a id="topic58"></a>

To redistribute table data for tables with a random distribution policy \(or when the hash distribution policy has not changed\) use `REORGANIZE=TRUE`. Reorganizing data may be necessary to correct a data skew problem, or when segment resources are added to the system. For example, the following command redistributes table data across all segments using the current distribution policy, including random distribution.

```
ALTER TABLE sales SET WITH (REORGANIZE=TRUE);
```

## Dropping a Table <a id="topic62"></a>

The`DROP TABLE`command removes tables from the database. For example:

```
DROP TABLE mytable;
```

To empty a table of rows without removing the table definition, use `DELETE` or `TRUNCATE`. For example:

```
DELETE FROM mytable;

TRUNCATE mytable;
```

`DROP TABLE`always removes any indexes, rules, triggers, and constraints that exist for the target table. Specify `CASCADE`to drop a table that is referenced by a view. `CASCADE` removes dependent views.
