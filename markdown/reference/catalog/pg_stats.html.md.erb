---
title: pg_stats
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

The `pg_stats` is a publicly readable view on `pg_statistic` that only exposes information about those tables that are readable by the current user. The `pg_stats` view presents the contents of `pg_statistic` in a friendlier format.

All the statistical data is inherently approximate, even assuming that it is up-to-date. The `pg_stats` schema must be extended whenever new slot types are defined.

<a id="topic1__table_ckx_t2w_jv"></a>
<span class="tablecap">Table 1. pg\_stats</span>

| Name                | Type     | References                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------|----------|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| schemaname          | name     | [pg\_namespace](pg_namespace.html#topic1).nspname. | The name of the schema containing the table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| tablename           | name     | [pg\_class](pg_class.html#topic1).relname          | The name of the table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| attname             | name     | [pg\_attribute](pg_attribute.html#topic1).attname  | The name of the column this row describes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| null\_frac          | real     |                                                                            | The fraction of column entries that are null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| avg\_width          | integer  |                                                                            | The average storage width in bytes of the column's entries, calculated as `avg(pg_column_size(column_name))`.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| n\_distinct         | real     |                                                                            | A positive number is an estimate of the number of distinct values in the column; the number is not expected to vary with the number of rows. A negative value is the number of distinct values divided by the number of rows, that is, the ratio of rows with distinct values for the column, negated. This form is used when the number of distinct values increases with the number of rows. A unique column, for example, has an `n_distinct` value of -1.0. Columns with an average width greater than 1024 are considered unique. |
| most\_common-vals   | anyarray |                                                                            | An array containing the most common values in the column, or null if no values seem to be more common. If the `n_distinct` column is -1, `most_common_vals` is null. The length of the array is the lesser of the number of actual distinct column values or the value of the `default_statistics_target` configuration parameter. The number of values can be overridden for a column using `ALTER TABLE                   table SET COLUMN column SET STATISTICS                   N`.                                               |
| most\_common\_freqs | real\[\] |                                                                            | An array containing the frequencies of the values in the `most_common_vals` array. This is the number of occurrences of the value divided by the total number of rows. The array is the same length as the `most_common_vals` array. It is null if `most_common_vals` is null.                                                                                                                                                                                                                                                         |
| histogram\_bounds   | anyarray |                                                                            | An array of values that divide the column values into groups of approximately the same size. A histogram can be defined only if there is a `max()` aggregate function for the column. The number of groups in the histogram is the same as the `most_common_vals` array size.                                                                                                                                                                                                                                                          |
| correlation         | real     |                                                                            | HAWQ does not calculate the correlation statistic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |




