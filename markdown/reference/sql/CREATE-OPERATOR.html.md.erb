---
title: CREATE OPERATOR
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

Defines a new operator.

## <a id="topic1__section2"></a>Synopsis

``` pre
CREATE OPERATOR <name> ( 
       PROCEDURE = <funcname>
       [, LEFTARG = <lefttype>] [, RIGHTARG = <righttype>]
       [, COMMUTATOR = <com_op>] [, NEGATOR = <neg_op>]
       [, RESTRICT = <res_proc>] [, JOIN = <join_proc>]
       [, HASHES] [, MERGES]
       [, SORT1 = <left_sort_op>] [, SORT2 = <right_sort_op>]
       [, LTCMP = <less_than_op>] [, GTCMP = <greater_than_op>] )
```

## <a id="topic1__section3"></a>Description

`CREATE OPERATOR` defines a new operator. The user who defines an operator becomes its owner.

The operator name is a sequence of up to `NAMEDATALEN`-1 (63 by default) characters from the following list: `` + - * / < > = ~ ! @ # % ^                     & | ` ? ``

There are a few restrictions on your choice of name:

-   `--` and `/*` cannot appear anywhere in an operator name, since they will be taken as the start of a comment.
-   A multicharacter operator name cannot end in `+` or `-`, unless the name also contains at least one of these characters: `` ~ ! @ # % ^ & | ` ? ``

For example, `@-` is an allowed operator name, but `*-` is not. This restriction allows HAWQ to parse SQL-compliant commands without requiring spaces between tokens.

The operator `!=` is mapped to `<>` on input, so these two names are always equivalent.

At least one of `LEFTARG` and `RIGHTARG` must be defined. For binary operators, both must be defined. For right unary operators, only `LEFTARG` should be defined, while for left unary operators only `RIGHTARG` should be defined.

The \<funcname\> procedure must have been previously defined using `CREATE FUNCTION`, must be `IMMUTABLE`, and must be defined to accept the correct number of arguments (either one or two) of the indicated types.

The other clauses specify optional operator optimization clauses. These clauses should be provided whenever appropriate to speed up queries that use the operator. But if you provide them, you must be sure that they are correct. Incorrect use of an optimization clause can result in server process crashes, subtly wrong output, or other unexpected results. You can always leave out an optimization clause if you are not sure about it.

## <a id="topic1__section4"></a>Parameters

<dt> \<name\>   </dt>
<dd>The (optionally schema-qualified) name of the operator to be defined. Two operators in the same schema can have the same name if they operate on different data types.</dd>

<dt> \<funcname\>   </dt>
<dd>The function used to implement this operator (must be an `IMMUTABLE` function).</dd>

<dt> \<lefttype\>   </dt>
<dd>The data type of the operator's left operand, if any. This option would be omitted for a left-unary operator.</dd>

<dt> \<righttype\>   </dt>
<dd>The data type of the operator's right operand, if any. This option would be omitted for a right-unary operator.</dd>

<dt> \<com\_op\>   </dt>
<dd>The optional `COMMUTATOR` clause names an operator that is the commutator of the operator being defined. We say that operator A is the commutator of operator B if (x A y) equals (y B x) for all possible input values x, y. Notice that B is also the commutator of A. For example, operators `<` and `>` for a particular data type are usually each others commutators, and operator + is usually commutative with itself. But operator `-` is usually not commutative with anything. The left operand type of a commutable operator is the same as the right operand type of its commutator, and vice versa. So the name of the commutator operator is all that needs to be provided in the `COMMUTATOR` clause.</dd>

<dt> \<neg\_op\>   </dt>
<dd>The optional `NEGATOR` clause names an operator that is the negator of the operator being defined. We say that operator A is the negator of operator B if both return Boolean results and (x A y) equals NOT (x B y) for all possible inputs x, y. Notice that B is also the negator of A. For example, `<` and `>=` are a negator pair for most data types. An operator's negator must have the same left and/or right operand types as the operator to be defined, so only the operator name need be given in the `NEGATOR` clause.</dd>

<dt> \<res\_proc\>   </dt>
<dd>The optional `RESTRICT` names a restriction selectivity estimation function for the operator. Note that this is a function name, not an operator name. `RESTRICT` clauses only make sense for binary operators that return `boolean`. The idea behind a restriction selectivity estimator is to guess what fraction of the rows in a table will satisfy a `WHERE`-clause condition of the form:

``` pre
column OP constant
```

for the current operator and a particular constant value. This assists the optimizer by giving it some idea of how many rows will be eliminated by `WHERE` clauses that have this form.

You can usually just use one of the following system standard estimator functions for many of your own operators:

`eqsel` for =

`neqsel` for &lt;&gt;

`scalarltsel` for &lt; or &lt;=

`scalargtsel` for &gt; or &gt;=
</dd>

<dt> \<join\_proc\>   </dt>
<dd>The optional `JOIN` clause names a join selectivity estimation function for the operator. Note that this is a function name, not an operator name. `JOIN` clauses only make sense for binary operators that return `boolean`. The idea behind a join selectivity estimator is to guess what fraction of the rows in a pair of tables will satisfy a `WHERE`-clause condition of the form:

``` pre
table1.column1 OP table2.column2
```

for the current operator. This helps the optimizer by letting it figure out which of several possible join sequences is likely to take the least work.

You can usually just use one of the following system standard join selectivity estimator functions for many of your own operators:

`eqjoinsel` for =

`neqjoinsel` for &lt;&gt;

`scalarltjoinsel` for &lt; or &lt;=

`scalargtjoinsel` for &gt; or &gt;=

`areajoinsel` for 2D area-based comparisons

`positionjoinsel` for 2D position-based comparisons

`contjoinsel` for 2D containment-based comparisons
</dd>

<dt>HASHES  </dt>
<dd>The optional `HASHES` clause tells the system that it is permissible to use the hash join method for a join based on this operator. `HASHES` only makes sense for a binary operator that returns `boolean`. The hash join operator can only return true for pairs of left and right values that hash to the same hash code. If two values get put in different hash buckets, the join will never compare them at all, implicitly assuming that the result of the join operator must be false. So it never makes sense to specify `HASHES` for operators that do not represent equality.

To be marked `HASHES`, the join operator must appear in a hash index operator class. Attempts to use the operator in hash joins will fail at run time if no such operator class exists. The system needs the operator class to find the data-type-specific hash function for the operator's input data type. You must also supply a suitable hash function before you can create the operator class. Care should be exercised when preparing a hash function, because there are machine-dependent ways in which it might fail to do the right thing.</dd>

<dt>MERGES  </dt>
<dd>The `MERGES` clause, if present, tells the system that it is permissible to use the merge-join method for a join based on this operator. `MERGES` only makes sense for a binary operator that returns `boolean`, and in practice the operator must represent equality for some data type or pair of data types.

Merge join is based on the idea of sorting the left- and right-hand tables into order and then scanning them in parallel. So, both data types must be capable of being fully ordered, and the join operator must be one that can only succeed for pairs of values that fall at the same place in the sort order. In practice this means that the join operator must behave like equality. It is possible to merge-join two distinct data types so long as they are logically compatible. For example, the smallint-versus-integer equality operator is merge-joinable. We only need sorting operators that will bring both data types into a logically compatible sequence.

Execution of a merge join requires that the system be able to identify four operators related to the merge-join equality operator: less-than comparison for the left operand data type, less-than comparison for the right operand data type, less-than comparison between the two data types, and greater-than comparison between the two data types. It is possible to specify these operators individually by name, as the `SORT1`, `SORT2`, `LTCMP`, and `GTCMP` options respectively. The system will fill in the default names if any of these are omitted when `MERGES` is specified.</dd>

<dt> \<left\_sort\_op\>   </dt>
<dd>If this operator can support a merge join, the less-than operator that sorts the left-hand data type of this operator. `<` is the default if not specified.</dd>

<dt> \<right\_sort\_op\>   </dt>
<dd>If this operator can support a merge join, the less-than operator that sorts the right-hand data type of this operator. `<` is the default if not specified.</dd>

<dt> \<less\_than\_op\>   </dt>
<dd>If this operator can support a merge join, the less-than operator that compares the input data types of this operator. `<` is the default if not specified.</dd>

<dt> \<greater\_than\_op\>   </dt>
<dd>If this operator can support a merge join, the greater-than operator that compares the input data types of this operator. `>` is the default if not specified.

To give a schema-qualified operator name in optional arguments, use the `OPERATOR()` syntax, for example:

``` pre
COMMUTATOR = OPERATOR(myschema.===) ,
```
</dd>

## <a id="topic1__section5"></a>Notes

Any functions used to implement the operator must be defined as `IMMUTABLE`.

## <a id="topic1__section6"></a>Examples

Here is an example of creating an operator for adding two complex numbers, assuming we have already created the definition of type `complex`. First define the function that does the work, then define the operator:

``` pre
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

To use this operator in a query:

``` pre
SELECT (a + b) AS c FROM test_complex;
```

## <a id="topic1__section7"></a>Compatibility

`CREATE OPERATOR` is a HAWQ language extension. The SQL standard does not provide for user-defined operators.

## <a id="topic1__section8"></a>See Also

[CREATE FUNCTION](CREATE-FUNCTION.html), [CREATE TYPE](CREATE-TYPE.html), [ALTER OPERATOR](ALTER-OPERATOR.html), [DROP OPERATOR](DROP-OPERATOR.html)
