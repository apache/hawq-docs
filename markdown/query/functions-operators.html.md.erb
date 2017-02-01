---
title: Using Functions and Operators
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

HAWQ evaluates functions and operators used in SQL expressions.

## <a id="topic27"></a>Using Functions in HAWQ

In HAWQ, functions can only be run on master.

<a id="topic27__in201681"></a>

<span class="tablecap">Table 1. Functions in HAWQ</span>


| Function Type | HAWQ Support       | Description                                                                                                               | Comments                                                                                                                                               |
|---------------|--------------------|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMMUTABLE     | Yes                | Relies only on information directly in its argument list. Given the same argument values, always returns the same result. |                                                                                                                                                        |
| STABLE        | Yes, in most cases | Within a single table scan, returns the same result for same argument values, but results change across SQL statements.   | Results depend on database lookups or parameter values. `current_timestamp` family of functions is `STABLE`; values do not change within an execution. |
| VOLATILE      | Restricted         | Function values can change within a single table scan. For example: `random()`, `currval()`, `timeofday()`.               | Any function with side effects is volatile, even if its result is predictable. For example: `setval()`.                                                |

HAWQ does not support functions that return a table reference (`rangeFuncs`) or functions that use the `refCursor` datatype.

## <a id="topic28"></a>User-Defined Functions

HAWQ supports user-defined functions. See [Extending SQL](http://www.postgresql.org/docs/8.2/static/extend.html) in the PostgreSQL documentation for more information.

In HAWQ, the shared library files for user-created functions must reside in the same library path location on every host in the HAWQ array (masters and segments).

**Important:**
HAWQ does not support the following:

-   Enhanced table functions
-   PL/Java Type Maps


Use the `CREATE FUNCTION` statement to register user-defined functions that are used as described in [Using Functions in HAWQ](#topic27). By default, user-defined functions are declared as `VOLATILE`, so if your user-defined function is `IMMUTABLE` or `STABLE`, you must specify the correct volatility level when you register your function.

### <a id="functionvolatility"></a>Function Volatility

Every function has a **volatility** classification, with the possibilities being VOLATILE, STABLE, or IMMUTABLE. VOLATILE is the default if the [CREATE FUNCTION](../reference/sql/CREATE-FUNCTION.html) command does not specify a category. The volatility category is a promise to the optimizer about the behavior of the function:

-   A VOLATILE function can do anything, including modifying the database. It can return different results on successive calls with the same arguments. The optimizer makes no assumptions about the behavior of such functions. A query using a volatile function will re-evaluate the function at every row where its value is needed.
-   A STABLE function cannot modify the database and is guaranteed to return the same results given the same arguments for all rows within a single statement. This category allows the optimizer to optimize multiple calls of the function to a single call.
-   An IMMUTABLE function cannot modify the database and is guaranteed to return the same results given the same arguments forever. This category allows the optimizer to pre-evaluate the function when a query calls it with constant arguments. For example, a query like SELECT ... WHERE x = 2 + 2 can be simplified on sight to SELECT ... WHERE x = 4, because the function underlying the integer addition operator is marked IMMUTABLE.

For best optimization results, you should label your functions with the strictest volatility category that is valid for them.

Any function with side-effects must be labeled VOLATILE, so that calls to it cannot be optimized away. Even a function with no side-effects needs to be labeled VOLATILE if its value can change within a single query; some examples are random(), currval(), timeofday().

Another important example is that the `current_timestamp` family of functions qualify as STABLE, since their values do not change within a transaction.

There is relatively little difference between STABLE and IMMUTABLE categories when considering simple interactive queries that are planned and immediately executed: it doesn't matter a lot whether a function is executed once during planning or once during query execution startup. But there is a big difference if the plan is saved and reused later. Labeling a function IMMUTABLE when it really isn't might allow it to be prematurely folded to a constant during planning, resulting in a stale value being re-used during subsequent uses of the plan. This is a hazard when using prepared statements or when using function languages that cache plans (such as PL/pgSQL).

For functions written in SQL or in any of the standard procedural languages, there is a second important property determined by the volatility category, namely the visibility of any data changes that have been made by the SQL command that is calling the function. A VOLATILE function will see such changes, a STABLE or IMMUTABLE function will not. STABLE and IMMUTABLE functions use a snapshot established as of the start of the calling query, whereas VOLATILE functions obtain a fresh snapshot at the start of each query they execute.

Because of this snapshotting behavior, a function containing only SELECT commands can safely be marked STABLE, even if it selects from tables that might be undergoing modifications by concurrent queries. PostgreSQL will execute all commands of a STABLE function using the snapshot established for the calling query, and so it will see a fixed view of the database throughout that query.

The same snapshotting behavior is used for SELECT commands within IMMUTABLE functions. It is generally unwise to select from database tables within an IMMUTABLE function at all, since the immutability will be broken if the table contents ever change. However, PostgreSQL does not enforce that you do not do that.

A common error is to label a function IMMUTABLE when its results depend on a configuration parameter. For example, a function that manipulates timestamps might well have results that depend on the timezone setting. For safety, such functions should be labeled STABLE instead.

When you create user defined functions, avoid using fatal errors or destructive calls. HAWQ may respond to such errors with a sudden shutdown or restart.

### <a id="nestedUDFs"></a>Nested Function Query Limitations

HAWQ queries employing nested user-defined functions will fail when dispatched to segment node(s). 

HAWQ stores the system catalog only on the master node. User-defined functions are stored in system catalog tables. HAWQ has no built-in knowledge about how to interpret the source text of a user-defined function. Consequently, the text is not parsed by HAWQ.

This behavior may be problematic in queries where a user-defined function includes a nested function(s). When a query includes a user-defined function, metadata passed to the query executor includes function invocation information.  If run on the HAWQ master node, the nested function will be recognized. If such a query is dispatched to a segment, the nested function will not be found and the query will throw an error.

## <a id="userdefinedtypes"></a>User Defined Types

HAWQ can be extended to support new data types. This section describes how to define new base types, which are data types defined below the level of the SQL language. Creating a new base type requires implementing functions to operate on the type in a low-level language, usually C.

A user-defined type must always have input and output functions.  These functions determine how the type appears in strings (for input by the user and output to the user) and how the type is organized in memory. The input function takes a null-terminated character string as its argument and returns the internal (in memory) representation of the type. The output function takes the internal representation of the type as argument and returns a null-terminated character string. If we want to do anything more with the type than merely store it, we must provide additional functions to implement whatever operations we'd like to have for the type.

You should be careful to make the input and output functions inverses of each other. If you do not, you will have severe problems when you need to dump your data into a file and then read it back in. This is a particularly common problem when floating-point numbers are involved.

Optionally, a user-defined type can provide binary input and output routines. Binary I/O is normally faster but less portable than textual I/O. As with textual I/O, it is up to you to define exactly what the external binary representation is. Most of the built-in data types try to provide a machine-independent binary representation. 

Once we have written the I/O functions and compiled them into a shared library, we can define the complex type in SQL. First we declare it as a shell type:

``` sql
CREATE TYPE complex;
```

This serves as a placeholder that allows us to reference the type while defining its I/O functions. Now we can define the I/O functions:

``` sql
CREATE FUNCTION complex_in(cstring)
    RETURNS complex
    AS 'filename'
    LANGUAGE C IMMUTABLE STRICT;

CREATE FUNCTION complex_out(complex)
    RETURNS cstring
    AS 'filename'
    LANGUAGE C IMMUTABLE STRICT;

CREATE FUNCTION complex_recv(internal)
   RETURNS complex
   AS 'filename'
   LANGUAGE C IMMUTABLE STRICT;

CREATE FUNCTION complex_send(complex)
   RETURNS bytea
   AS 'filename'
   LANGUAGE C IMMUTABLE STRICT;
```

Finally, we can provide the full definition of the data type:

``` sql
CREATE TYPE complex (
   internallength = 16, 
   input = complex_in,
   output = complex_out,
   receive = complex_recv,
   send = complex_send,
   alignment = double
);
```

When you define a new base type, HAWQ automatically provides support for arrays of that type. For historical reasons, the array type has the same name as the base type with the underscore character (\_) prepended.

Once the data type exists, we can declare additional functions to provide useful operations on the data type. Operators can then be defined atop the functions, and if needed, operator classes can be created to support indexing of the data type. 

For further details, see the description of the [CREATE TYPE](../reference/sql/CREATE-TYPE.html) command.

## <a id="userdefinedoperators"></a>User Defined Operators

Every operator is "syntactic sugar" for a call to an underlying function that does the real work; so you must first create the underlying function before you can create the operator. However, an operator is not merely syntactic sugar, because it carries additional information that helps the query planner optimize queries that use the operator. The next section will be devoted to explaining that additional information.

HAWQ supports left unary, right unary, and binary operators. Operators can be overloaded; that is, the same operator name can be used for different operators that have different numbers and types of operands. When a query is executed, the system determines the operator to call from the number and types of the provided operands.

Here is an example of creating an operator for adding two complex numbers. We assume we've already created the definition of type complex. First we need a function that does the work, then we can define the operator:

``` sql
CREATE FUNCTION complex_add(complex, complex)
    RETURNS complex
    AS 'filename', 'complex_add'
    LANGUAGE C IMMUTABLE STRICT;

CREATE OPERATOR + (
    leftarg = complex,
    rightarg = complex,
    procedure = complex_add,
    commutator = +
);
```

Now we could execute a query like this:

``` sql
SELECT (a + b) AS c FROM test_complex;
```

```
        c
-----------------
 (5.2,6.05)
 (133.42,144.95)
```

We've shown how to create a binary operator here. To create unary operators, just omit one of leftarg (for left unary) or rightarg (for right unary). The procedure clause and the argument clauses are the only required items in CREATE OPERATOR. The commutator clause shown in the example is an optional hint to the query optimizer. Further details aboutcommutator and other optimizer hints appear in the next section.

## <a id="topic29"></a>Built-in Functions and Operators

The following table lists the categories of built-in functions and operators supported by PostgreSQL. All functions and operators are supported in HAWQ as in PostgreSQL with the exception of `STABLE` and `VOLATILE` functions, which are subject to the restrictions noted in [Using Functions in HAWQ](#topic27). See the [Functions and Operators](http://www.postgresql.org/docs/8.2/static/functions.html) section of the PostgreSQL documentation for more information about these built-in functions and operators.

<a id="topic29__in204913"></a>

<table>
<caption><span class="tablecap">Table 2. Built-in functions and operators</span></caption>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Operator/Function Category</th>
<th>VOLATILE Functions</th>
<th>STABLE Functions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions.html#FUNCTIONS-LOGICAL">Logical Operators</a></td>
<td> </td>
<td> </td>
</tr>
<tr class="even">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-comparison.html">Comparison Operators</a></td>
<td> </td>
<td> </td>
</tr>
<tr class="odd">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-math.html">Mathematical Functions and Operators</a></td>
<td>random
<p>setseed</p></td>
<td> </td>
</tr>
<tr class="even">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-string.html">String Functions and Operators</a></td>
<td><em>All built-in conversion functions</em></td>
<td>convert
<p>pg_client_encoding</p></td>
</tr>
<tr class="odd">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-binarystring.html">Binary String Functions and Operators</a></td>
<td> </td>
<td> </td>
</tr>
<tr class="even">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-bitstring.html">Bit String Functions and Operators</a></td>
<td> </td>
<td> </td>
</tr>
<tr class="odd">
<td><a href="http://www.postgresql.org/docs/8.3/static/functions-matching.html">Pattern Matching</a></td>
<td> </td>
<td> </td>
</tr>
<tr class="even">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-formatting.html">Data Type Formatting Functions</a></td>
<td> </td>
<td>to_char
<p>to_timestamp</p></td>
</tr>
<tr class="odd">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-datetime.html">Date/Time Functions and Operators</a></td>
<td>timeofday</td>
<td>age
<p>current_date</p>
<p>current_time</p>
<p>current_timestamp</p>
<p>localtime</p>
<p>localtimestamp</p>
<p>now</p></td>
</tr>
<tr class="even">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-geometry.html">Geometric Functions and Operators</a></td>
<td> </td>
<td> </td>
</tr>
<tr class="odd">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-net.html">Network Address Functions and Operators</a></td>
<td> </td>
<td> </td>
</tr>
<tr class="even">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-sequence.html">Sequence Manipulation Functions</a></td>
<td>currval
<p>lastval</p>
<p>nextval</p>
<p>setval</p></td>
<td> </td>
</tr>
<tr class="odd">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-conditional.html">Conditional Expressions</a></td>
<td> </td>
<td> </td>
</tr>
<tr class="even">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-array.html">Array Functions and Operators</a></td>
<td> </td>
<td><em>All array functions</em></td>
</tr>
<tr class="odd">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-aggregate.html">Aggregate Functions</a></td>
<td> </td>
<td> </td>
</tr>
<tr class="even">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-subquery.html">Subquery Expressions</a></td>
<td> </td>
<td> </td>
</tr>
<tr class="odd">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-comparisons.html">Row and Array Comparisons</a></td>
<td> </td>
<td> </td>
</tr>
<tr class="even">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-srf.html">Set Returning Functions</a></td>
<td>generate_series</td>
<td> </td>
</tr>
<tr class="odd">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-info.html">System Information Functions</a></td>
<td> </td>
<td><em>All session information functions</em>
<p><em>All access privilege inquiry functions</em></p>
<p><em>All schema visibility inquiry functions</em></p>
<p><em>All system catalog information functions</em></p>
<p><em>All comment information functions</em></p></td>
</tr>
<tr class="even">
<td><a href="http://www.postgresql.org/docs/8.2/static/functions-admin.html">System Administration Functions</a></td>
<td>set_config
<p>pg_cancel_backend</p>
<p>pg_reload_conf</p>
<p>pg_rotate_logfile</p>
<p>pg_start_backup</p>
<p>pg_stop_backup</p>
<p>pg_size_pretty</p>
<p>pg_ls_dir</p>
<p>pg_read_file</p>
<p>pg_stat_file</p></td>
<td>current_setting
<p><em>All database object size functions</em></p></td>
</tr>
<tr class="odd">
<td><a href="http://www.postgresql.org/docs/9.1/interactive/functions-xml.html">XML Functions</a></td>
<td> </td>
<td>xmlagg(xml)
<p>xmlexists(text, xml)</p>
<p>xml_is_well_formed(text)</p>
<p>xml_is_well_formed_document(text)</p>
<p>xml_is_well_formed_content(text)</p>
<p>xpath(text, xml)</p>
<p>xpath(text, xml, text[])</p>
<p>xpath_exists(text, xml)</p>
<p>xpath_exists(text, xml, text[])</p>
<p>xml(text)</p>
<p>text(xml)</p>
<p>xmlcomment(xml)</p>
<p>xmlconcat2(xml, xml)</p></td>
</tr>
</tbody>
</table>

## <a id="topic30"></a>Window Functions

The following built-in window functions are HAWQ extensions to the PostgreSQL database. All window functions are *immutable*. For more information about window functions, see [Window Expressions](defining-queries.html#topic13).

<a id="topic30__in164369"></a>

<span class="tablecap">Table 3. Window functions</span>

| Function                                             | Return Type               | Full Syntax                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cume_dist()`                                        | `double precision`        | `CUME_DIST() OVER ( [PARTITION BY ` *expr* `] ORDER BY ` *expr* ` )`                                      | Calculates the cumulative distribution of a value in a group of values. Rows with equal values always evaluate to the same cumulative distribution value.                                                                                                                                                                                                                                                                                                  |
| `dense_rank()`                                       | `bigint`                  | `DENSE_RANK () OVER ( [PARTITION BY ` *expr* `] ORDER BY ` *expr* `)`                                     | Computes the rank of a row in an ordered group of rows without skipping rank values. Rows with equal values are given the same rank value.                                                                                                                                                                                                                                                                                                                 |
| `first_value(expr)`                                  | same as input *expr* type | FIRST\_VALUE expr ) OVER ( \[PARTITION BY expr \] ORDER BY expr \[ROWS|RANGE frame\_expr \] )             | Returns the first value in an ordered set of values.                                                                                                                                                                                                                                                                                                                                                                                                       |
| `lag(expr [,offset] [,default])`                     | same as input *expr* type | `LAG(` *expr* ` [,` *offset* `] [,` *default* `]) OVER ( [PARTITION BY ` *expr* `] ORDER BY ` *expr* ` )` | Provides access to more than one row of the same table without doing a self join. Given a series of rows returned from a query and a position of the cursor, `LAG` provides access to a row at a given physical offset prior to that position. The default `offset` is 1. *default* sets the value that is returned if the offset goes beyond the scope of the window. If *default* is not specified, the default value is null.                           |
| `last_valueexpr`                                     | same as input *expr* type | LAST\_VALUE(expr) OVER ( \[PARTITION BY expr\] ORDER BY expr \[ROWS|RANGE frame\_expr\] )                 | Returns the last value in an ordered set of values.                                                                                                                                                                                                                                                                                                                                                                                                        |
| `                   lead(expr [,offset] [,default])` | same as input *expr* type | `LEAD(expr [,offset] [,exprdefault]) OVER (                   [PARTITION BY expr] ORDER BY expr )`        | Provides access to more than one row of the same table without doing a self join. Given a series of rows returned from a query and a position of the cursor, `lead` provides access to a row at a given physical offset after that position. If *offset* is not specified, the default offset is 1. *default* sets the value that is returned if the offset goes beyond the scope of the window. If *default* is not specified, the default value is null. |
| `ntile(expr)`                                        | bigint                    | `NTILE(expr) OVER ( [PARTITION BY expr] ORDER BY expr                   )`                                | Divides an ordered data set into a number of buckets (as defined by *expr*) and assigns a bucket number to each row.                                                                                                                                                                                                                                                                                                                                       |
| `percent_rank(`)                                     | `double precision`        | `PERCENT_RANK () OVER ( [PARTITION BY expr] ORDER BY expr                   )`                            | Calculates the rank of a hypothetical row `R` minus 1, divided by 1 less than the number of rows being evaluated (within a window partition).                                                                                                                                                                                                                                                                                                              |
| `rank()`                                             | bigint                    | `RANK () OVER ( [PARTITION BY expr] ORDER BY expr )`                                                      | Calculates the rank of a row in an ordered group of values. Rows with equal values for the ranking criteria receive the same rank. The number of tied rows are added to the rank number to calculate the next rank value. Ranks may not be consecutive numbers in this case.                                                                                                                                                                               |
| `row_number(`)                                       | `bigint`                  | `ROW_NUMBER () OVER ( [PARTITION BY expr] ORDER BY expr                   )`                              | Assigns a unique number to each row to which it is applied (either each row in a window partition or each row of the query).                                                                                                                                                                                                                                                                                                                               |


## <a id="topic31"></a>Advanced Aggregate Functions

The following built-in advanced aggregate functions are HAWQ extensions of the PostgreSQL database.

<a id="topic31__in2073121"></a>

<table>

<caption><span class="tablecap">Table 4. Advanced Aggregate Functions</span></caption>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Return Type</th>
<th>Full Syntax</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">MEDIAN (expr)</code></td>
<td><code class="ph codeph">timestamp, timestampz, interval, float</code></td>
<td><code class="ph codeph">MEDIAN (expression)</code>
<p><em>Example:</em></p>
<pre class="pre codeblock"><code>SELECT department_id, MEDIAN(salary) 
FROM employees 
GROUP BY department_id; </code></pre></td>
<td>Can take a two-dimensional array as input. Treats such arrays as matrices.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">PERCENTILE_CONT (expr) WITHIN GROUP (ORDER BY expr                   [DESC/ASC])</code></td>
<td><code class="ph codeph">timestamp, timestampz, interval, float</code></td>
<td><code class="ph codeph">PERCENTILE_CONT(percentage) WITHIN GROUP (ORDER BY                   expression)</code>
<p><em>Example:</em></p>
<pre class="pre codeblock"><code>SELECT department_id,
PERCENTILE_CONT (0.5) WITHIN GROUP (ORDER BY salary DESC)
&quot;Median_cont&quot;; 
FROM employees GROUP BY department_id;</code></pre></td>
<td>Performs an inverse function that assumes a continuous distribution model. It takes a percentile value and a sort specification and returns the same datatype as the numeric datatype of the argument. This returned value is a computed result after performing linear interpolation. Null are ignored in this calculation.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">PERCENTILE_DISC (expr) WITHIN GROUP (ORDER BY                     expr [DESC/ASC]</code>)</td>
<td><code class="ph codeph">timestamp, timestampz, interval, float</code></td>
<td><code class="ph codeph">PERCENTILE_DISC(percentage) WITHIN GROUP (ORDER BY                   expression)</code>
<p><em>Example:</em></p>
<pre class="pre codeblock"><code>SELECT department_id, 
PERCENTILE_DISC (0.5) WITHIN GROUP (ORDER BY salary DESC)
&quot;Median_desc&quot;; 
FROM employees GROUP BY department_id;</code></pre></td>
<td>Performs an inverse distribution function that assumes a discrete distribution model. It takes a percentile value and a sort specification. This returned value is an element from the set. Null are ignored in this calculation.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">sum(array[])</code></td>
<td><code class="ph codeph">smallint[]int[], bigint[], float[]</code></td>
<td><code class="ph codeph">sum(array[[1,2],[3,4]])</code>
<p><em>Example:</em></p>
<pre class="pre codeblock"><code>CREATE TABLE mymatrix (myvalue int[]);
INSERT INTO mymatrix VALUES (array[[1,2],[3,4]]);
INSERT INTO mymatrix VALUES (array[[0,1],[1,0]]);
SELECT sum(myvalue) FROM mymatrix;
 sum 
---------------
 {{1,3},{4,4}}</code></pre></td>
<td>Performs matrix summation. Can take as input a two-dimensional array that is treated as a matrix.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">pivot_sum (label[], label, expr)</code></td>
<td><code class="ph codeph">int[], bigint[], float[]</code></td>
<td><code class="ph codeph">pivot_sum( array['A1','A2'], attr, value)</code></td>
<td>A pivot aggregation using sum to resolve duplicate entries.</td>
</tr>
</tbody>
</table>


