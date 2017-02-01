---
title: Defining Queries
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

HAWQ is based on the PostgreSQL implementation of the SQL standard. SQL commands are typically entered using the standard PostgreSQL interactive terminal `psql`, but other programs that have similar functionality can be used as well.


## <a id="topic3"></a>SQL Lexicon

SQL is a standard language for accessing databases. The language consists of elements that enable data storage, retrieval, analysis, viewing, and so on. You use SQL commands to construct queries and commands that the HAWQ engine understands.

SQL queries consist of a sequence of commands. Commands consist of a sequence of valid tokens in correct syntax order, terminated by a semicolon (`;`).

H uses PostgreSQL's structure and syntax, with some exceptions. For more information about SQL rules and concepts in PostgreSQL, see "SQL Syntax" in the PostgreSQL documentation.

## <a id="topic4"></a>SQL Value Expressions

SQL value expressions consist of one or more values, symbols, operators, SQL functions, and data. The expressions compare data or perform calculations and return a value as the result. Calculations include logical, arithmetic, and set operations.

The following are value expressions:

-   Aggregate expressions
-   Array constructors
-   Column references
-   Constant or literal values
-   Correlated subqueries
-   Field selection expressions
-   Function calls
-   New column values in an `INSERT`
-   Operator invocation column references
-   Positional parameter references, in the body of a function definition or prepared statement
-   Row constructors
-   Scalar subqueries
-   Search conditions in a `WHERE` clause
-   Target lists of a `SELECT` command
-   Type casts
-   Value expressions in parentheses, useful to group sub-expressions and override precedence
-   Window expressions

SQL constructs such as functions and operators are expressions but do not follow any general syntax rules. For more information about these constructs, see [Using Functions and Operators](functions-operators.html#topic26).

### <a id="topic5"></a>Column References

A column reference has the form:

```
correlation.columnname
```

Here, `correlation` is the name of a table (possibly qualified with a schema name) or an alias for a table defined with a `FROM` clause or one of the keywords `NEW` or `OLD`. `NEW` and `OLD` can appear only in rewrite rules, but you can use other correlation names in any SQL statement. If the column name is unique across all tables in the query, you can omit the "`correlation.`" part of the column reference.

### <a id="topic6"></a>Positional Parameters

Positional parameters are arguments to SQL statements or functions that you reference by their positions in a series of arguments. For example, `$1` refers to the first argument, `$2` to the second argument, and so on. The values of positional parameters are set from arguments external to the SQL statement or supplied when SQL functions are invoked. Some client libraries support specifying data values separately from the SQL command, in which case parameters refer to the out-of-line data values. A parameter reference has the form:

```
$number
```

For example:

``` pre
CREATE FUNCTION dept(text) RETURNS dept
    AS $$ SELECT * FROM dept WHERE name = $1 $$
    LANGUAGE SQL;
```

Here, the `$1` references the value of the first function argument whenever the function is invoked.

### <a id="topic7"></a>Subscripts

If an expression yields a value of an array type, you can extract a specific element of the array value as follows:

``` pre
expression[subscript]
```

You can extract multiple adjacent elements, called an array slice, as follows (including the brackets):

``` pre
expression[lower_subscript:upper_subscript]
```

Each subscript is an expression and yields an integer value.

Array expressions usually must be in parentheses, but you can omit the parentheses when the expression to be subscripted is a column reference or positional parameter. You can concatenate multiple subscripts when the original array is multidimensional. For example (including the parentheses):

``` pre
mytable.arraycolumn[4]
```

``` pre
mytable.two_d_column[17][34]
```

``` pre
$1[10:42]
```

``` pre
(arrayfunction(a,b))[42]
```

### <a id="topic8"></a>Field Selections

If an expression yields a value of a composite type (row type), you can extract a specific field of the row as follows:

```
expression.fieldname
```

The row expression usually must be in parentheses, but you can omit these parentheses when the expression to be selected from is a table reference or positional parameter. For example:

``` pre
mytable.mycolumn
```

``` pre
$1.somecolumn
```

``` pre
(rowfunction(a,b)).col3
```

A qualified column reference is a special case of field selection syntax.

### <a id="topic9"></a>Operator Invocations

Operator invocations have the following possible syntaxes:

``` pre
expression operator expression(binary infix operator)
```

``` pre
operator expression(unary prefix operator)
```

``` pre
expression operator(unary postfix operator)
```

Where *operator* is an operator token, one of the key words `AND`, `OR`, or `NOT`, or qualified operator name in the form:

``` pre
OPERATOR(schema.operatorname)
```

Available operators and whether they are unary or binary depends on the operators that the system or user defines. For more information about built-in operators, see [Built-in Functions and Operators](functions-operators.html#topic29).

### <a id="topic10"></a>Function Calls

The syntax for a function call is the name of a function (possibly qualified with a schema name), followed by its argument list enclosed in parentheses:

``` pre
function ([expression [, expression ... ]])
```

For example, the following function call computes the square root of 2:

``` pre
sqrt(2)
```

### <a id="topic11"></a>Aggregate Expressions

An aggregate expression applies an aggregate function across the rows that a query selects. An aggregate function performs a calculation on a set of values and returns a single value, such as the sum or average of the set of values. The syntax of an aggregate expression is one of the following:

-   `aggregate_name ([ , ... ] ) [FILTER (WHERE                 condition)] ` — operates across all input rows for which the expected result value is non-null. `ALL` is the default.
-   `aggregate_name(ALLexpression[ , ... ] ) [FILTER               (WHERE condition)]` — operates identically to the first form because `ALL` is the default
-   `aggregate_name(DISTINCT expression[ , ... ] )               [FILTER (WHERE condition)]` — operates across all distinct non-null values of input rows
-   `aggregate_name(*) [FILTER (WHERE               condition)]` — operates on all rows with values both null and non-null. Generally, this form is most useful for the `count(*)` aggregate function.

Where *aggregate\_name* is a previously defined aggregate (possibly schema-qualified) and *expression* is any value expression that does not contain an aggregate expression.

For example, `count(*)` yields the total number of input rows, `count(f1)` yields the number of input rows in which `f1` is <span class="ph">non-null, and </span>`count(distinct f1)` yields the number of distinct non-null values of `f1`.

You can specify a condition with the `FILTER` clause to limit the input rows to the aggregate function. For example:

``` sql
SELECT count(*) FILTER (WHERE gender='F') FROM employee;
```

The `WHERE condition` of the `FILTER` clause cannot contain a set-returning function, subquery, window function, or outer reference. If you use a user-defined aggregate function, declare the state transition function as `STRICT` (see `CREATE AGGREGATE`).

For predefined aggregate functions, see [Built-in Functions and Operators](functions-operators.html#topic29). You can also add custom aggregate functions.

HAWQ provides the `MEDIAN` aggregate function, which returns the fiftieth percentile of the `PERCENTILE_CONT` result and special aggregate expressions for inverse distribution functions as follows:

``` sql
PERCENTILE_CONT(_percentage_) WITHIN GROUP (ORDER BY _expression_)
```

``` sql
PERCENTILE_DISC(_percentage_) WITHIN GROUP (ORDER BY _expression_)
```

Currently you can use only these two expressions with the keyword `WITHIN             GROUP`.

#### <a id="topic12"></a>Limitations of Aggregate Expressions

The following are current limitations of the aggregate expressions:

-   HAWQ does not support the following keywords: ALL, DISTINCT, FILTER and OVER. See [Advanced Aggregate Functions](functions-operators.html#topic31__in2073121) for more details.
-   An aggregate expression can appear only in the result list or HAVING clause of a SELECT command. It is forbidden in other clauses, such as WHERE, because those clauses are logically evaluated before the results of aggregates form. This restriction applies to the query level to which the aggregate belongs.
-   When an aggregate expression appears in a subquery, the aggregate is normally evaluated over the rows of the subquery. If the aggregate's arguments contain only outer-level variables, the aggregate belongs to the nearest such outer level and evaluates over the rows of that query. The aggregate expression as a whole is then an outer reference for the subquery in which it appears, and the aggregate expression acts as a constant over any one evaluation of that subquery. See [Scalar Subqueries](#topic15) and [Built-in functions and operators](functions-operators.html#topic29__in204913).
-   HAWQ does not support DISTINCT with multiple input expressions.

### <a id="topic13"></a>Window Expressions

Window expressions allow application developers to more easily compose complex online analytical processing (OLAP) queries using standard SQL commands. For example, with window expressions, users can calculate moving averages or sums over various intervals, reset aggregations and ranks as selected column values change, and express complex ratios in simple terms.

A window expression represents the application of a *window function* applied to a *window frame*, which is defined in a special `OVER()` clause. A window partition is a set of rows that are grouped together to apply a window function. Unlike aggregate functions, which return a result value for each group of rows, window functions return a result value for every row, but that value is calculated with respect to the rows in a particular window partition. If no partition is specified, the window function is computed over the complete intermediate result set.

The syntax of a window expression is:

``` pre
window_function ( [expression [, ...]] ) OVER ( window_specification )
```

Where *`window_function`* is one of the functions listed in [Window functions](functions-operators.html#topic30__in164369), *`expression`* is any value expression that does not contain a window expression, and *`window_specification`* is:

```
[window_name]
[PARTITION BY expression [, ...]]
[[ORDER BY expression [ASC | DESC | USING operator] [, ...]
    [{RANGE | ROWS} 
       { UNBOUNDED PRECEDING
       | expression PRECEDING
       | CURRENT ROW
       | BETWEEN window_frame_bound AND window_frame_bound }]]
```

and where `window_frame_bound` can be one of:

``` 
    UNBOUNDED PRECEDING
    expression PRECEDING
    CURRENT ROW
    expression FOLLOWING
    UNBOUNDED FOLLOWING
```

A window expression can appear only in the select list of a `SELECT` command. For example:

``` sql
SELECT count(*) OVER(PARTITION BY customer_id), * FROM sales;
```

The `OVER` clause differentiates window functions from other aggregate or reporting functions. The `OVER` clause defines the *`window_specification`* to which the window function is applied. A window specification has the following characteristics:

-   The `PARTITION BY` clause defines the window partitions to which the window function is applied. If omitted, the entire result set is treated as one partition.
-   The `ORDER BY` clause defines the expression(s) for sorting rows within a window partition. The `ORDER BY` clause of a window specification is separate and distinct from the `ORDER BY` clause of a regular query expression. The `ORDER BY` clause is required for the window functions that calculate rankings, as it identifies the measure(s) for the ranking values. For OLAP aggregations, the `ORDER BY` clause is required to use window frames (the `ROWS` | `RANGE` clause).

**Note:** Columns of data types without a coherent ordering, such as `time`, are not good candidates for use in the `ORDER BY` clause of a window specification. `Time`, with or without a specified time zone, lacks a coherent ordering because addition and subtraction do not have the expected effects. For example, the following is not generally true: `x::time < x::time +             '2 hour'::interval`

-   The `ROWS/RANGE` clause defines a window frame for aggregate (non-ranking) window functions. A window frame defines a set of rows within a window partition. When a window frame is defined, the window function computes on the contents of this moving frame rather than the fixed contents of the entire window partition. Window frames are row-based (`ROWS`) or value-based (`RANGE`).

### <a id="topic14"></a>Type Casts

A type cast specifies a conversion from one data type to another. HAWQ accepts two equivalent syntaxes for type casts:

``` sql
CAST ( expression AS type )
expression::type
```

The `CAST` syntax conforms to SQL; the syntax with `::` is historical PostgreSQL usage.

A cast applied to a value expression of a known type is a run-time type conversion. The cast succeeds only if a suitable type conversion function is defined. This differs from the use of casts with constants. A cast applied to a string literal represents the initial assignment of a type to a literal constant value, so it succeeds for any type if the contents of the string literal are acceptable input syntax for the data type.

You can usually omit an explicit type cast if there is no ambiguity about the type a value expression must produce; for example, when it is assigned to a table column, the system automatically applies a type cast. The system applies automatic casting only to casts marked "OK to apply implicitly" in system catalogs. Other casts must be invoked with explicit casting syntax to prevent unexpected conversions from being applied without the user's knowledge.

### <a id="topic15"></a>Scalar Subqueries

A scalar subquery is a `SELECT` query in parentheses that returns exactly one row with one column. Do not use a `SELECT` query that returns multiple rows or columns as a scalar subquery. The query runs and uses the returned value in the surrounding value expression. A correlated scalar subquery contains references to the outer query block.

### <a id="topic16"></a>Correlated Subqueries

A correlated subquery (CSQ) is a `SELECT` query with a `WHERE` clause or target list that contains references to the parent outer clause. CSQs efficiently express results in terms of results of another query. HAWQ supports correlated subqueries that provide compatibility with many existing applications. A CSQ is a scalar or table subquery, depending on whether it returns one or multiple rows. HAWQ does not support correlated subqueries with skip-level correlations.

### <a id="topic17"></a>Correlated Subquery Examples

#### <a id="topic18"></a>Example 1 – Scalar correlated subquery

``` sql
SELECT * FROM t1 WHERE t1.x 
> (SELECT MAX(t2.x) FROM t2 WHERE t2.y = t1.y);
```

#### <a id="topic19"></a>Example 2 – Correlated EXISTS subquery

``` sql
SELECT * FROM t1 WHERE 
EXISTS (SELECT 1 FROM t2 WHERE t2.x = t1.x);
```

HAWQ uses one of the following methods to run CSQs:

-   Unnest the CSQ into join operations – This method is most efficient, and it is how HAWQ runs most CSQs, including queries from the TPC-H benchmark.
-   Run the CSQ on every row of the outer query – This method is relatively inefficient, and it is how HAWQ runs queries that contain CSQs in the `SELECT` list or are connected by `OR` conditions.

The following examples illustrate how to rewrite some of these types of queries to improve performance.

#### <a id="topic20"></a>Example 3 - CSQ in the Select List

*Original Query*

``` sql
SELECT T1.a,
(SELECT COUNT(DISTINCT T2.z) FROM t2 WHERE t1.x = t2.y) dt2 
FROM t1;
```

Rewrite this query to perform an inner join with `t1` first and then perform a left join with `t1` again. The rewrite applies for only an equijoin in the correlated condition.

*Rewritten Query*

``` sql
SELECT t1.a, dt2 FROM t1 
LEFT JOIN 
(SELECT t2.y AS csq_y, COUNT(DISTINCT t2.z) AS dt2 
FROM t1, t2 WHERE t1.x = t2.y 
GROUP BY t1.x) 
ON (t1.x = csq_y);
```

### <a id="topic21"></a>Example 4 - CSQs connected by OR Clauses

*Original Query*

``` sql
SELECT * FROM t1 
WHERE 
x > (SELECT COUNT(*) FROM t2 WHERE t1.x = t2.x) 
OR x < (SELECT COUNT(*) FROM t3 WHERE t1.y = t3.y)
```

Rewrite this query to separate it into two parts with a union on the `OR` conditions.

*Rewritten Query*

``` sql
SELECT * FROM t1 
WHERE x > (SELECT count(*) FROM t2 WHERE t1.x = t2.x) 
UNION 
SELECT * FROM t1 
WHERE x < (SELECT count(*) FROM t3 WHERE t1.y = t3.y)
```

To view the query plan, use `EXPLAIN SELECT` or `EXPLAIN ANALYZE             SELECT`. Subplan nodes in the query plan indicate that the query will run on every row of the outer query, and the query is a candidate for rewriting. For more information about these statements, see [Query Profiling](query-profiling.html#topic39).

### <a id="topic22"></a>Advanced Table Functions

HAWQ supports table functions with `TABLE` value expressions. You can sort input rows for advanced table functions with an `ORDER BY` clause. You can redistribute them with a `SCATTER BY` clause to specify one or more columns or an expression for which rows with the specified characteristics are available to the same process. This usage is similar to using a `DISTRIBUTED BY` clause when creating a table, but the redistribution occurs when the query runs.

**Note:**
Based on the distribution of data, HAWQ automatically parallelizes table functions with `TABLE` value parameters over the nodes of the cluster.

### <a id="topic23"></a>Array Constructors

An array constructor is an expression that builds an array value from values for its member elements. A simple array constructor consists of the key word `ARRAY`, a left square bracket `[`, one or more expressions separated by commas for the array element values, and a right square bracket `]`. For example,

``` sql
SELECT ARRAY[1,2,3+4];
```

```
  array
---------
 {1,2,7}
```

The array element type is the common type of its member expressions, determined using the same rules as for `UNION` or `CASE` constructs.

You can build multidimensional array values by nesting array constructors. In the inner constructors, you can omit the keyword `ARRAY`. For example, the following two `SELECT` statements produce the same result:

``` sql
SELECT ARRAY[ARRAY[1,2], ARRAY[3,4]];
SELECT ARRAY[[1,2],[3,4]];
```

```
     array
---------------
 {{1,2},{3,4}}
```

Since multidimensional arrays must be rectangular, inner constructors at the same level must produce sub-arrays of identical dimensions.

Multidimensional array constructor elements are not limited to a sub-`ARRAY` construct; they are anything that produces an array of the proper kind. For example:

``` sql
CREATE TABLE arr(f1 int[], f2 int[]);
INSERT INTO arr VALUES (ARRAY[[1,2],[3,4]], 
ARRAY[[5,6],[7,8]]);
SELECT ARRAY[f1, f2, '{{9,10},{11,12}}'::int[]] FROM arr;
```

```
                     array
------------------------------------------------
 {{{1,2},{3,4}},{{5,6},{7,8}},{{9,10},{11,12}}}
```

You can construct an array from the results of a subquery. Write the array constructor with the keyword `ARRAY` followed by a subquery in parentheses. For example:

``` sql
SELECT ARRAY(SELECT oid FROM pg_proc WHERE proname LIKE 'bytea%');
```

```
                          ?column?
-----------------------------------------------------------
 {2011,1954,1948,1952,1951,1244,1950,2005,1949,1953,2006,31}
```

The subquery must return a single column. The resulting one-dimensional array has an element for each row in the subquery result, with an element type matching that of the subquery's output column. The subscripts of an array value built with `ARRAY` always begin with `1`.

### <a id="topic24"></a>Row Constructors

A row constructor is an expression that builds a row value (also called a composite value) from values for its member fields. For example,

``` sql
SELECT ROW(1,2.5,'this is a test');
```

Row constructors have the syntax `rowvalue.*`, which expands to a list of the elements of the row value, as when you use the syntax `.*` at the top level of a `SELECT` list. For example, if table `t` has columns `f1` and `f2`, the following queries are the same:

``` sql
SELECT ROW(t.*, 42) FROM t;
SELECT ROW(t.f1, t.f2, 42) FROM t;
```

By default, the value created by a `ROW` expression has an anonymous record type. If necessary, it can be cast to a named composite type — either the row type of a table, or a composite type created with `CREATE TYPE AS`. To avoid ambiguity, you can explicitly cast the value if necessary. For example:

``` sql
CREATE TABLE mytable(f1 int, f2 float, f3 text);
CREATE FUNCTION getf1(mytable) RETURNS int AS 'SELECT $1.f1' 
LANGUAGE SQL;
```

In the following query, you do not need to cast the value because there is only one `getf1()` function and therefore no ambiguity:

``` sql
SELECT getf1(ROW(1,2.5,'this is a test'));
```

```
 getf1
-------
     1
```

``` sql
CREATE TYPE myrowtype AS (f1 int, f2 text, f3 numeric);
CREATE FUNCTION getf1(myrowtype) RETURNS int AS 'SELECT 
$1.f1' LANGUAGE SQL;
```

Now we need a cast to indicate which function to call:

``` sql
SELECT getf1(ROW(1,2.5,'this is a test'));
```
```
ERROR:  function getf1(record) is not unique
```

``` sql
SELECT getf1(ROW(1,2.5,'this is a test')::mytable);
```

```
 getf1
-------
     1
```

``` sql
SELECT getf1(CAST(ROW(11,'this is a test',2.5) AS myrowtype));
```

```
 getf1
-------
    11
```

You can use row constructors to build composite values to be stored in a composite-type table column or to be passed to a function that accepts a composite parameter.

### <a id="topic25"></a>Expression Evaluation Rules

The order of evaluation of subexpressions is undefined. The inputs of an operator or function are not necessarily evaluated left-to-right or in any other fixed order.

If you can determine the result of an expression by evaluating only some parts of the expression, then other subexpressions might not be evaluated at all. For example, in the following expression:

``` sql
SELECT true OR somefunc();
```

`somefunc()` would probably not be called at all. The same is true in the following expression:

``` sql
SELECT somefunc() OR true;
```

This is not the same as the left-to-right evaluation order that Boolean operators enforce in some programming languages.

Do not use functions with side effects as part of complex expressions, especially in `WHERE` and `HAVING` clauses, because those clauses are extensively reprocessed when developing an execution plan. Boolean expressions (`AND`/`OR`/`NOT` combinations) in those clauses can be reorganized in any manner that Boolean algebra laws allow.

Use a `CASE` construct to force evaluation order. The following example is an untrustworthy way to avoid division by zero in a `WHERE` clause:

``` sql
SELECT ... WHERE x <> 0 AND y/x > 1.5;
```

The following example shows a trustworthy evaluation order:

``` sql
SELECT ... WHERE CASE WHEN x <> 0 THEN y/x > 1.5 ELSE false 
END;
```

This `CASE` construct usage defeats optimization attempts; use it only when necessary.


