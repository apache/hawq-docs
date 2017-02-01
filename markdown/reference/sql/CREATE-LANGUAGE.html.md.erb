---
title: CREATE LANGUAGE
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

Defines a new procedural language.

## <a id="topic1__section2"></a>Synopsis

``` pre
CREATE [PROCEDURAL] LANGUAGE <name>

CREATE [TRUSTED] [PROCEDURAL] LANGUAGE <name>
       HANDLER <call_handler> [VALIDATOR <valfunction>]
```

## <a id="topic1__section3"></a>Description

`CREATE LANGUAGE` registers a new procedural language with a HAWQ database. Subsequently, functions can be defined in this new language. You must be a superuser to register a new language.

When you register a new procedural language, you effectively associate the language name with a call handler that is responsible for executing functions written in that language. For a function written in a procedural language (a language other than C or SQL), the database server has no built-in knowledge about how to interpret the function's source code. The task is passed to a special handler that knows the details of the language. The handler could either do all the work of parsing, syntax analysis, execution, and so on, or it could serve as a bridge between HAWQ and an existing implementation of a programming language. The handler itself is a C language function compiled into a shared object and loaded on demand, just like any other C function.

There are two forms of the `CREATE LANGUAGE` command. In the first form, the user specifies the name of the desired language and the HAWQ server uses the `pg_pltemplate` system catalog to determine the correct parameters. In the second form, the user specifies the language parameters as well as the language name. You can use the second form to create a language that is not defined in `pg_pltemplate`.

When the server finds an entry in the `pg_pltemplate` catalog for the given language name, it will use the catalog data even if the command includes language parameters. This behavior simplifies loading of old dump files, which are likely to contain out-of-date information about language support functions.

## <a id="topic1__section4"></a>Parameters

<dt>TRUSTED  </dt>
<dd>Ignored if the server has an entry for the specified language name in *pg\_pltemplate*. Specifies that the call handler for the language is safe and does not offer an unprivileged user any functionality to bypass access restrictions. If this key word is omitted when registering the language, only users with the superuser privilege can use this language to create new functions.</dd>

<dt>PROCEDURAL  </dt>
<dd>Indicates that this is a procedural language.</dd>

<dt> \<name\>   </dt>
<dd>The name of the new procedural language. The language name is case insensitive. The name must be unique among the languages in the database. Built-in support is included for `plpgsql`, `plpython`, `plpythonu`, and `plr`. `plpgsql` is installed by default in HAWQ.</dd>

<dt>HANDLER \<call\_handler\>   </dt>
<dd>Ignored if the server has an entry for the specified language name in `pg_pltemplate`. The name of a previously registered function that will be called to execute the procedural language functions. The call handler for a procedural language must be written in a compiled language such as C with version 1 call convention and registered with HAWQ as a function taking no arguments and returning the `language_handler` type, a placeholder type that is simply used to identify the function as a call handler.</dd>

<dt>VALIDATOR \<valfunction\>   </dt>
<dd>Ignored if the server has an entry for the specified language name in `pg_pltemplate`. \<valfunction\> is the name of a previously registered function that will be called when a new function in the language is created, to validate the new function. If no validator function is specified, then a new function will not be checked when it is created. The validator function must take one argument of type `oid`, which will be the OID of the to-be-created function, and will typically return `void`.

A validator function would typically inspect the function body for syntactical correctness, but it can also look at other properties of the function, for example if the language cannot handle certain argument types. To signal an error, the validator function should use the `ereport()` function. The return value of the function is ignored.</dd>

## <a id="topic1__section5"></a>Notes

The procedural language packages included in the standard HAWQ distribution are:

-   `PL/pgSQL` - registered in all databases by default
-   `PL/Perl`
-   `PL/Python`
-   `PL/Java`

HAWQ supports a language handler for `PL/R`, but the `PL/R` language package is not pre-installed with HAWQ.

The system catalog `pg_language` records information about the currently installed languages.

To create functions in a procedural language, a user must have the `USAGE` privilege for the language. By default, `USAGE` is granted to `PUBLIC` (everyone) for trusted languages. This may be revoked if desired.

Procedural languages are local to individual databases. However, a language can be installed into the `template1` database, which will cause it to be available automatically in all subsequently-created databases.

The call handler function and the validator function (if any) must already exist if the server does not have an entry for the language in `pg_pltemplate`. But when there is an entry, the functions need not already exist; they will be automatically defined if not present in the database.

Any shared library that implements a language must be located in the same `LD_LIBRARY_PATH` location on all segment hosts in your HAWQ array.

## <a id="topic1__section6"></a>Examples

The preferred way of creating any of the standard procedural languages in a database:

``` pre
CREATE LANGUAGE plr;
CREATE LANGUAGE plpythonu;
CREATE LANGUAGE plperl;
```

For a language not known in the `pg_pltemplate` catalog:

``` pre
CREATE FUNCTION plsample_call_handler() RETURNS 
language_handler
    AS '$libdir/plsample'
    LANGUAGE C;
CREATE LANGUAGE plsample
    HANDLER plsample_call_handler;
```

## <a id="topic1__section7"></a>Compatibility

`CREATE LANGUAGE` is a HAWQ extension.

## <a id="topic1__section8"></a>See Also

[CREATE FUNCTION](CREATE-FUNCTION.html), [DROP LANGUAGE](DROP-LANGUAGE.html)
