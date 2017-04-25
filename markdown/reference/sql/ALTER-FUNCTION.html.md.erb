---
title: ALTER FUNCTION
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

Changes the definition of a function.

## <a id="alterfunction__section2"></a>Synopsis

``` sql
ALTER FUNCTION <name> ( [ [<argmode>] [<argname>] <argtype> [, ...] ] )
   <action> [, ... ] [RESTRICT]

ALTER FUNCTION <name> ( [ [<argmode>] [<argname>] <argtype> [, ...] ] )
   RENAME TO <new_name>

ALTER FUNCTION <name> ( [ [<argmode>] [<argname>] <argtype> [, ...] ] )
   OWNER TO <new_owner>

ALTER FUNCTION <name> ( [ [<argmode>] [<argname>] <argtype> [, ...] ] )
   SET SCHEMA <new_schema>

```

where \<action\> is one of:

```pre
{ CALLED ON NULL INPUT | RETURNS NULL ON NULL INPUT | STRICT }
{ IMMUTABLE | STABLE | VOLATILE }
{ [EXTERNAL] SECURITY INVOKER | [EXTERNAL] SECURITY DEFINER }
```

## <a id="desc"></a>Description

`ALTER FUNCTION` changes the definition of a function. 

You must own the function to use `ALTER FUNCTION`. To change a function’s schema, you must also have `CREATE` privilege on the new schema. To alter the owner, you must also be a direct or indirect member of the new owning role, and that role must have `CREATE` privilege on the function’s schema. (These restrictions enforce that altering the owner does not do anything you could not do by dropping and recreating the function. However, a superuser can alter ownership of any function anyway.)

## <a id="alterfunction__section4"></a>Parameters

<dt> \<name\>  </dt>
<dd>The name (optionally schema-qualified) of an existing function.</dd>

<dt>\<argmode\>  </dt>
<dd>The mode of an argument: either `IN`, `OUT`, or `INOUT`. If omitted, the default is `IN`. Note that `ALTER FUNCTION` does not actually pay any attention to `OUT` arguments, since only the input arguments are needed to determine the function's identity. So it is sufficient to list the `IN` and `INOUT` arguments.</dd>

<dt> \<argname\>  </dt>
<dd>The name of an argument. Note that `ALTER FUNCTION` does not actually pay any attention to argument names, since only the argument data types are needed to determine the function's identity.</dd>

<dt> \<argtype\>  </dt>
<dd>The data type(s) of the function's arguments (optionally schema-qualified), if any.</dd>

<dt> \<new\_name\>  </dt>
<dd>The new name of the function.</dd>

<dt> \<new\_owner\>  </dt>
<dd>The new owner of the function. Note that if the function is marked `SECURITY DEFINER`, it will subsequently execute as the new owner.</dd>

<dt> \<new\_schema\>  </dt>
<dd>The new schema for the function.</dd>

<dt>CALLED ON NULL INPUT  
RETURNS NULL ON NULL INPUT  
STRICT  </dt>
<dd>`CALLED ON NULL INPUT` changes the function so that it will be invoked when some or all of its arguments are null. `RETURNS NULL ON NULL                      INPUT` or `STRICT` changes the function so that it is not invoked if any of its arguments are null; instead, a null result is assumed automatically. See `CREATE FUNCTION` for more information.</dd>

<dt>IMMUTABLE  
STABLE  
VOLATILE  </dt>
<dd>Change the volatility of the function to the specified setting. See `CREATE FUNCTION` for details.</dd>

<dt>\[ EXTERNAL \] SECURITY INVOKER  
\[ EXTERNAL \] SECURITY DEFINER  </dt>
<dd>Change whether the function is a security definer or not. The key word `EXTERNAL` is ignored for SQL conformance. See `CREATE                      FUNCTION` for more information about this capability.</dd>

<dt>RESTRICT  </dt>
<dd>Ignored for conformance with the SQL standard.</dd>

## <a id="notes"></a>Notes

HAWQ has limitations on the use of functions defined as `STABLE` or `VOLATILE`. See [CREATE FUNCTION](CREATE-FUNCTION.html) for more information.

## <a id="alterfunction__section6"></a>Examples

To rename the function `sqrt` for type `integer` to `square_root`:

``` pre
ALTER FUNCTION sqrt(integer) RENAME TO square_root;
```

To change the owner of the function `sqrt` for type `integer` to `joe`:

``` pre
ALTER FUNCTION sqrt(integer) OWNER TO joe;
```

To change the schema of the function `sqrt` for type `integer` to `math`:

``` pre
ALTER FUNCTION sqrt(integer) SET SCHEMA math;
```

## <a id="compat"></a>Compatibility

This statement is partially compatible with the `ALTER FUNCTION` statement in the SQL standard. The standard allows more properties of a function to be modified, but does not provide the ability to rename a function, make a function a security definer, or change the owner, schema, or volatility of a function. The standard also requires the `RESTRICT` key word, which is optional in HAWQ.

## <a id="see"></a>See Also

[CREATE AGGREGATE](CREATE-AGGREGATE.html), [DROP AGGREGATE](DROP-AGGREGATE.html)
