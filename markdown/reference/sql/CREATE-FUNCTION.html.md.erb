---
title: CREATE FUNCTION
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

Defines a new function.

## <a id="topic1__section2"></a>Synopsis

``` pre
CREATE [OR REPLACE] FUNCTION <name>    
    ( [ [<argmode>] [<argname>] <argtype> [, ...] ] )
      [ RETURNS { [ SETOF ] <rettype>
        | TABLE ([{ <argname> <argtype> | LIKE <other table> }
          [, ...]])
        } ]
    { LANGUAGE <langname>
    | IMMUTABLE | STABLE | VOLATILE
    | CALLED ON NULL INPUT | RETURNS NULL ON NULL INPUT | STRICT
    | [EXTERNAL] SECURITY INVOKER | [EXTERNAL] SECURITY DEFINER
    | AS '<definition>'
    | AS '<obj_file>', '<link_symbol>' } ...
    [ WITH ({ DESCRIBE = <describe_function>
           } [, ...] ) ]
```

## <a id="topic1__section3"></a>Description

`CREATE FUNCTION` defines a new function. `CREATE OR REPLACE                     FUNCTION` will either create a new function, or replace an existing definition.

The name of the new function must not match any existing function with the same argument types in the same schema. However, functions of different argument types may share a name (overloading).

To update the definition of an existing function, use `CREATE OR REPLACE                     FUNCTION`. It is not possible to change the name or argument types of a function this way (this would actually create a new, distinct function). Also, `CREATE OR REPLACE FUNCTION` will not let you change the return type of an existing function. To do that, you must drop and recreate the function. If you drop and then recreate a function, you will have to drop existing objects (rules, views, and so on) that refer to the old function. Use `CREATE OR                     REPLACE FUNCTION` to change a function definition without breaking objects that refer to the function.

For more information about creating functions, see [User-Defined Functions](../../query/functions-operators.html#topic28).

**Limited Use of VOLATILE and STABLE Functions**

To prevent data from becoming out-of-sync across the segments in HAWQ, any function classified as `STABLE` or `VOLATILE` cannot be executed at the segment level if it contains SQL or modifies the database in any way. For example, functions such as `random()` or `timeofday()` are not allowed to execute on distributed data in HAWQ because they could potentially cause inconsistent data between the segment instances.

To ensure data consistency, `VOLATILE` and `STABLE` functions can safely be used in statements that are evaluated on and execute from the master. For example, the following statements are always executed on the master (statements without a `FROM` clause):

``` pre
SELECT setval('myseq', 201);
SELECT foo();
```

In cases where a statement has a `FROM` clause containing a distributed table and the function used in the `FROM` clause simply returns a set of rows, execution may be allowed on the segments:

``` pre
SELECT * FROM foo();
```

One exception to this rule are functions that return a table reference (`rangeFuncs`) or functions that use the `refCursor` data type. Note that you cannot return a `refcursor` from any kind of function in HAWQ.

## <a id="topic1__section5"></a>Parameters

<dt> \<name\>  </dt>
<dd>The name (optionally schema-qualified) of the function to create.</dd>

<dt> \<argmode\>  </dt>
<dd>The mode of an argument: either `IN`, `OUT`, or `INOUT`. If omitted, the default is `IN`.</dd>

<dt> \<argname\>  </dt>
<dd>The name of an argument. Some languages (currently only PL/pgSQL) let you use the name in the function body. For other languages the name of an input argument is just extra documentation. But the name of an output argument is significant, since it defines the column name in the result row type. (If you omit the name for an output argument, the system will choose a default column name.)</dd>

<dt> \<argtype\>  </dt>
<dd>The data type(s) of the function's arguments (optionally schema-qualified), if any. The argument types may be base, composite, or domain types, or may reference the type of a table column.

Depending on the implementation language it may also be allowed to specify pseudotypes such as `cstring`. Pseudotypes indicate that the actual argument type is either incompletely specified, or outside the set of ordinary SQL data types.

The type of a column is referenced by writing `                             <tablename>.<columnname>%<TYPE>`. Using this feature can sometimes help make a function independent of changes to the definition of a table.</dd>

<dt> \<rettype\>  </dt>
<dd>The return data type (optionally schema-qualified). The return type can be a base, composite, or domain type, or may reference the type of a table column. Depending on the implementation language it may also be allowed to specify pseudotypes such as `cstring`. If the function is not supposed to return a value, specify `void` as the return type.

When there are `OUT` or `INOUT` parameters, the `RETURNS` clause may be omitted. If present, it must agree with the result type implied by the output parameters: `RECORD` if there are multiple output parameters, or the same type as the single output parameter.

The `SETOF` modifier indicates that the function will return a set of items, rather than a single item.

The type of a column is referenced by writing `                             <tablename>.<columnname>%<TYPE>`.</dd>

<dt> \<langname\>  </dt>
<dd>The name of the language that the function is implemented in. May be `SQL`, `C`, `internal`, or the name of a user-defined procedural language. See [CREATE LANGUAGE](CREATE-LANGUAGE.html) for the procedural languages supported in HAWQ. For backward compatibility, the name may be enclosed by single quotes.</dd>

<dt>IMMUTABLE  
STABLE  
VOLATILE  </dt>
<dd>These attributes inform the query optimizer about the behavior of the function. At most one choice may be specified. If none of these appear, `VOLATILE` is the default assumption. Since HAWQ currently has limited use of `VOLATILE` functions, if a function is truly `IMMUTABLE`, you must declare it as so to be able to use it without restrictions.

`IMMUTABLE` indicates that the function cannot modify the database and always returns the same result when given the same argument values. It does not do database lookups or otherwise use information not directly present in its argument list. If this option is given, any call of the function with all-constant arguments can be immediately replaced with the function value.

`STABLE` indicates that the function cannot modify the database, and that within a single table scan it will consistently return the same result for the same argument values, but that its result could change across SQL statements. This is the appropriate selection for functions whose results depend on database lookups, parameter values (such as the current time zone), and so on. Also note that the *current\_timestamp* family of functions qualify as stable, since their values do not change within a transaction.

`VOLATILE` indicates that the function value can change even within a single table scan, so no optimizations can be made. Relatively few database functions are volatile in this sense; some examples are `random()`, `currval()`, `timeofday()`. But note that any function that has side-effects must be classified volatile, even if its result is quite predictable, to prevent calls from being optimized away; an example is `setval()`.</dd>

<dt>CALLED ON NULL INPUT  
RETURNS NULL ON NULL INPUT  
STRICT  </dt>
<dd>`CALLED ON NULL INPUT` (the default) indicates that the function will be called normally when some of its arguments are null. It is then the function author's responsibility to check for null values if necessary and respond appropriately. `RETURNS NULL ON NULL                             INPUT` or `STRICT` indicates that the function always returns null whenever any of its arguments are null. If this parameter is specified, the function is not executed when there are null arguments; instead a null result is assumed automatically.</dd>

<dt>\[EXTERNAL\] SECURITY INVOKER  
\[EXTERNAL\] SECURITY DEFINER  </dt>
<dd>`SECURITY INVOKER` (the default) indicates that the function is to be executed with the privileges of the user that calls it. `SECURITY DEFINER` specifies that the function is to be executed with the privileges of the user that created it. The key word `EXTERNAL` is allowed for SQL conformance, but it is optional since, unlike in SQL, this feature applies to all functions not just external ones.</dd>

<dt> \<definition\>  </dt>
<dd>A string constant defining the function; the meaning depends on the language. It may be an internal function name, the path to an object file, an SQL command, or text in a procedural language.</dd>

<dt> \<obj\_file\>, \<link\_symbol\>  </dt>
<dd>This form of the `AS` clause is used for dynamically loadable C language functions when the function name in the C language source code is not the same as the name of the SQL function. The string \<obj\_file\> is the name of the file containing the dynamically loadable object, and \<link\_symbol\> is the name of the function in the C language source code. If the link symbol is omitted, it is assumed to be the same as the name of the SQL function being defined. A good practice is to locate shared libraries either relative to `$libdir` (which is located at `$GPHOME/lib`) or through the dynamic library path (set by the `dynamic_library_path` server configuration parameter). This simplifies version upgrades if the new installation is at a different location.</dd>

<dt> \<describe\_function\>  </dt>
<dd>The name of a callback function to execute when a query that calls this function is parsed. The callback function returns a tuple descriptor that indicates the result type.</dd>

## <a id="topic1__section6"></a>Notes

Any compiled code (shared library files) for custom functions must be placed in the same location on every host in your HAWQ array (master and all segments). This location must also be in the `LD_LIBRARY_PATH` so that the server can locate the files. Consider locating shared libraries either relative to `$libdir` (which is located at `$GPHOME/lib`) or through the dynamic library path (set by the `dynamic_library_path` server configuration parameter) on all master segment instances in the HAWQ array.

The full SQL type syntax is allowed for input arguments and return value. However, some details of the type specification (such as the precision field for type *numeric*) are the responsibility of the underlying function implementation and are not recognized or enforced by the `CREATE                     FUNCTION` command.

HAWQ allows function overloading. The same name can be used for several different functions so long as they have distinct argument types. However, the C names of all functions must be different, so you must give overloaded C functions different C names (for example, use the argument types as part of the C names).

Two functions are considered the same if they have the same names and input argument types, ignoring any `OUT` parameters. Thus for example these declarations conflict:

``` pre
CREATE FUNCTION foo(int) ...
CREATE FUNCTION foo(int, out text) ...
```

When repeated `CREATE FUNCTION` calls refer to the same object file, the file is only loaded once. To unload and reload the file, use the `LOAD` command.

To be able to define a function, the user must have the `USAGE` privilege on the language.

It is often helpful to use dollar quoting to write the function definition string, rather than the normal single quote syntax. Without dollar quoting, any single quotes or backslashes in the function definition must be escaped by doubling them. A dollar-quoted string constant consists of a dollar sign (`$`), an optional tag of zero or more characters, another dollar sign, an arbitrary sequence of characters that makes up the string content, a dollar sign, the same tag that began this dollar quote, and a dollar sign. Inside the dollar-quoted string, single quotes, backslashes, or any character can be used without escaping. The string content is always written literally. For example, here are two different ways to specify the string "Dianne's horse" using dollar quoting:

``` pre
$$Dianne's horse$$
$SomeTag$Dianne's horse$SomeTag$
```

## <a id="topic1__section8"></a>Examples

A very simple addition function:

``` pre
CREATE FUNCTION add(integer, integer) RETURNS integer
    AS 'select $1 + $2;'
    LANGUAGE SQL
    IMMUTABLE
    RETURNS NULL ON NULL INPUT;
```

Increment an integer, making use of an argument name, in PL/pgSQL:

``` pre
CREATE OR REPLACE FUNCTION increment(i integer) RETURNS
integer AS $$
        BEGIN
                RETURN i + 1;
        END;
$$ LANGUAGE plpgsql;
```

Return a record containing multiple output parameters:

``` pre
CREATE FUNCTION dup(in int, out f1 int, out f2 text)
    AS $$ SELECT $1, CAST($1 AS text) || ' is text' $$
    LANGUAGE SQL;
SELECT * FROM dup(42);
```

You can do the same thing more verbosely with an explicitly named composite type:

``` pre
CREATE TYPE dup_result AS (f1 int, f2 text);
CREATE FUNCTION dup(int) RETURNS dup_result
    AS $$ SELECT $1, CAST($1 AS text) || ' is text' $$
    LANGUAGE SQL;
SELECT * FROM dup(42);
```

## <a id="topic1__section9"></a>Compatibility

`CREATE FUNCTION` is defined in SQL:1999 and later. The HAWQ version of the command is similar, but not fully compatible. The attributes are not portable, neither are the different available languages.

For compatibility with some other database systems, \<argmode\> can be written either before or after \<argname\>. But only the first way is standard-compliant.

## <a id="topic1__section10"></a>See Also

[ALTER FUNCTION](ALTER-FUNCTION.html), [DROP FUNCTION](DROP-FUNCTION.html)
