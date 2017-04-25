---
title: CREATE CAST
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

Defines a new cast.

## <a id="topic1__section2"></a>Synopsis

``` pre
CREATE CAST (<sourcetype> AS <targettype>) 
       WITH FUNCTION <funcname (argtypes)> 
       [AS ASSIGNMENT | AS IMPLICIT]

CREATE CAST (<sourcetype> AS <targettype>) WITHOUT FUNCTION 
       [AS ASSIGNMENT | AS IMPLICIT]
```

## <a id="topic1__section3"></a>Description

`CREATE CAST` defines a new cast. A cast specifies how to perform a conversion between two data types. For example,

```pre
SELECT CAST(42 AS text);
```

converts the integer constant `42` to type `text` by invoking a previously specified function, in this case `text(int4)`. If no suitable cast has been defined, the conversion fails.

Two types may be binary compatible, which means that they can be converted into one another without invoking any function. This requires that corresponding values use the same internal representation. For instance, the types `text` and `varchar` are binary compatible.

By default, a cast can be invoked only by an explicit cast request, that is an explicit `CAST(x AS typename)` or `x:: typename` construct.

If the cast is marked `AS ASSIGNMENT` then it can be invoked implicitly when assigning a value to a column of the target data type. For example, supposing that `foo.f1` is a column of type `text`, then:

``` pre
INSERT INTO foo (f1) VALUES (42);
```
will be allowed if the cast from type integer to type `text` is marked `AS ASSIGNMENT`, otherwise not. The term *assignment cast* is typically used to describe this kind of cast.

If the cast is marked `AS IMPLICIT` then it can be invoked implicitly in any context, whether by assignment or internally in an expression. The term *implicit cast* is typically used to describe this kind of cast. For example, since `||` takes `text` operands,

``` pre
SELECT 'The time is ' || now();
```
It is wise to be conservative about marking casts `AS IMPLICIT`. An overabundance of implicit casting paths can cause HAWQ to choose surprising interpretations of commands, or to be unable to resolve commands at all because there are multiple possible interpretations. A good rule of thumb is to make a cast implicitly invokable only for information-preserving transformations between types in the same general type category. For example, the cast from `int2` to `int4` can reasonably be implicit, but the cast from `float8` to `int4` should probably be assignment-only. Cross-type-category casts, such as `text` to `int4`, are best made explicit-only.

To be able to create a cast, you must own the source or the target data type. To create a binary-compatible cast, you must be superuser.


## <a id="topic1__section4"></a>Parameters

<dt>\<sourcetype\>  </dt>
<dd>The name of the source data type of the cast.</dd>

<dt>\<targettype\>  </dt>
<dd>The name of the target data type of the cast.</dd>

<dt> \<funcname(argtypes)\>   </dt>
<dd>The function used to perform the cast. The function name may be schema-qualified. If it is not, the function is looked up in the schema search path. The function's result data type must match the target type of the cast.
Cast implementation functions may have one to three arguments. The first argument type must be identical to the cast's source type. The second argument, if present, must be type `integer`; it receives the type modifier associated with the destination type, or `-1` if there is none. The third argument, if present, must be type `boolean`; it receives `true` if the cast is an explicit cast, `false` otherwise. In some cases, the SQL specification demands different behaviors for explicit and implicit casts. This argument is supplied for functions that must implement such casts. Designing  your own data types this way is not recommended.
Ordinarily, a cast must have different source and target data types. However, declaring a cast with identical source and target types is allowed if it has a cast implementation function with more than one argument. This is used to represent type-specific length coercion functions in the system catalogs. The named function is used to coerce a value of the type to the type modifier value specified by its second argument. (Since the grammar presently permits only certain built-in data types to have type modifiers, this feature is of no use for user-defined target types.)
When a cast has different source and target types and a function that takes more than one argument, it represents a conversion from one type to another and applying a length coercion in a single step. When no such entry is available, coercion to a type that uses a type modifier involves two steps, one to convert between data types and a second to apply the modifier.
</dd>

<dt>WITHOUT FUNCTION</dt>
<dd>Indicates that the source type and the target type are binary compatible, so no function is required to perform the cast.</dd>

<dt>AS ASSIGNMENT </dt>
<dd>Indicates that the cast may be invoked implicitly in assignment contexts.</dd>

<dt>AS IMPLICIT  </dt>
<dd>Indicates that the cast may be invoked implicitly in any context.</dd>

## <a id="topic1__section5"></a>Notes

For this release of HAWQ, user-defined functions used in a user-defined cast must be defined as `IMMUTABLE`. Any compiled code (shared library files) for custom functions must be placed in the same location on every host in your HAWQ array (master and all segments). This location must also be in the `LD_LIBRARY_PATH` so that the server can locate the files.

Remember that if you want to be able to convert types both ways, you need to declare casts both ways explicitly.

We recommend that you follow the convention of naming cast implementation functions after the target data type, as the built-in cast implementation functions are named. Many users are used to being able to cast data types using a function-style notation, that is `typename(x)`.

## <a id="topic1__section6"></a>Examples

Create a cast from type `text` to type `int4` using the function `int4(text)`. (This cast is already predefined in the system.):

``` pre
CREATE CAST (text AS int4) WITH FUNCTION int4(text);
```

## <a id="topic1__section7"></a>Compatibility

The `CREATE CAST` command conforms to the SQL standard, except that SQL does not make provisions for binary-compatible types or extra arguments to implementation functions. `AS IMPLICIT` is also a HAWQ extension.

## <a id="topic1__section8"></a>See Also

[DROP CAST](DROP-CAST.html),  [CREATE FUNCTION](CREATE-FUNCTION.html)

