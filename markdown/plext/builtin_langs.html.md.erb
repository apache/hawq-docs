---
title: Using HAWQ Built-In Languages
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

This section provides an introduction to using the HAWQ built-in languages.

HAWQ supports user-defined functions created with the SQL and C built-in languages. HAWQ also supports user-defined aliases for internal functions.


## <a id="enablebuiltin"></a>Enabling Built-in Language Support

Support for SQL and C language user-defined functions and aliasing of internal functions is enabled by default for all HAWQ databases.

## <a id="builtinsql"></a>Defining SQL Functions

SQL functions execute an arbitrary list of SQL statements. The SQL statements in the body of a SQL function must be separated by semicolons. The final statement in a non-void-returning SQL function must be a [SELECT](../reference/sql/SELECT.html) that returns data of the type specified by the function's return type. The function will return a single or set of rows corresponding to this last SQL query.

The following example creates and calls a SQL function to count the number of rows of the table named `orders`:

``` sql
gpadmin=# CREATE FUNCTION count_orders() RETURNS bigint AS $$
 SELECT count(*) FROM orders;
$$ LANGUAGE SQL;
CREATE FUNCTION
gpadmin=# SELECT count_orders();
 my_count 
----------
   830513
(1 row)
```

For additional information about creating SQL functions, refer to [Query Language (SQL) Functions](https://www.postgresql.org/docs/8.2/static/xfunc-sql.html) in the PostgreSQL documentation.

## <a id="builtininternal"></a>Aliasing Internal Functions

Many HAWQ internal functions are written in C. These functions are declared during initialization of the database cluster and statically linked to the HAWQ server. See [Built-in Functions and Operators](../query/functions-operators.html#topic29) for detailed information about HAWQ internal functions.

You cannot define new internal functions, but you can create aliases for existing internal functions.

The following example creates a new function named `all_caps` that is an alias for the `upper` HAWQ internal function:


``` sql
gpadmin=# CREATE FUNCTION all_caps (text) RETURNS text AS 'upper'
            LANGUAGE internal STRICT;
CREATE FUNCTION
gpadmin=# SELECT all_caps('change me');
 all_caps  
-----------
 CHANGE ME
(1 row)

```

For more information about aliasing internal functions, refer to [Internal Functions](https://www.postgresql.org/docs/8.2/static/xfunc-internal.html) in the PostgreSQL documentation.

## <a id="builtinc_lang"></a>Defining C Functions

You must compile user-defined functions written in C into shared libraries so that the HAWQ server can load them on demand. This dynamic loading distinguishes C language functions from internal functions that are written in C.

The [CREATE FUNCTION](../reference/sql/CREATE-FUNCTION.html) call for a user-defined C function must include both the name of the shared library and the name of the function.

If an absolute path to the shared library is not provided, an attempt is made to locate the library relative to the: 

1. HAWQ PostgreSQL library directory (obtained via the `pg_config --pkglibdir` command)
2. `dynamic_library_path` configuration value
3. current working directory

in that order. 

Example:

``` c
#include "postgres.h"
#include "fmgr.h"

#ifdef PG_MODULE_MAGIC
PG_MODULE_MAGIC;
#endif

PG_FUNCTION_INFO_V1(double_it);
         
Datum
double_it(PG_FUNCTION_ARGS)
{
    int32   arg = PG_GETARG_INT32(0);

    PG_RETURN_INT64(arg + arg);
}
```

If the above function is compiled into a shared object named `libdoubleit.so` located in `/share/libs`, you would register and invoke the function with HAWQ as follows:

``` sql
gpadmin=# CREATE FUNCTION double_it_c(integer) RETURNS integer
            AS '/share/libs/libdoubleit', 'double_it'
            LANGUAGE C STRICT;
CREATE FUNCTION
gpadmin=# SELECT double_it_c(27);
 double_it 
-----------
        54
(1 row)

```

The shared library `.so` extension may be omitted.

For additional information about using the C language to create functions, refer to [C-Language Functions](https://www.postgresql.org/docs/8.2/static/xfunc-c.html) in the PostgreSQL documentation.

