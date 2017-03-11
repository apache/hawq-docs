---
title: Using PL/pgSQL in HAWQ
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

PL/pgSQL is a trusted procedural language that is automatically installed and registered in all HAWQ databases. With PL/pgSQL, you can:

-   Create functions
-   Add control structures to the SQL language
-   Perform complex computations
-   Use all of the data types, functions, and operators defined in SQL

SQL is the language most relational databases use as a query language. While it is portable and easy to learn, every SQL statement is individually executed by the database server. Your client application sends each query to the database server, waits for it to be processed, receives and processes the results, does some computation, then sends further queries to the server. This back-and-forth requires interprocess communication and incurs network overhead if your client is on a different host than the HAWQ master.

The PL/pgSQL language addresses some of these limitations. When creating functions with PL/pgSQL, you can group computation blocks and queries inside the database server, combining the power of a procedural language and the ease of use of SQL, but with considerable savings of client/server communication overhead. With PL/pgSQL:

-   Extra round trips between client and server are eliminated
-   Intermediate, and perhaps unneeded, results do not have to be marshaled or transferred between the server and client
-   Re-using prepared queries avoids multiple rounds of query parsing
 

## <a id="plpgsql_structure"></a>PL/pgSQL Function Syntax

PL/pgSQL is a block-structured language. The complete text of a function definition must be a block, which is defined as:

``` sql
[ <label> ]
[ DECLARE
    declarations ]
BEGIN
    statements
END [ label ];
```

Each declaration and each statement within a block is terminated by a semicolon. A block that appears within another block must have a semicolon after `END`, as shown above; however the final `END` that concludes a function body does not require a semicolon.

You can specify all key words and identifiers in mixed upper and lower case. Identifiers are implicitly converted to lowercase unless they are double-quoted.

PL/pgSQL supports two types of comments. A double dash (`--`) starts a comment that extends to the end of the line. A `/*` starts a block comment that extends to the next occurrence of `*/`. Block comments cannot be nested, but you can enclose double dash comments into a block comment and a double dash can hide the block comment delimiters `/*` and `*/`.

This example PL/pgSQL function adds thirteen to an integer:

``` sql
=> CREATE FUNCTION add_thirteen(i integer) RETURNS integer AS 
   $$
   DECLARE
       incvalue integer := 13;
   BEGIN
       -- add thirteen to i
       RETURN i + incvalue;
   END;
   $$ LANGUAGE plpgsql;
=> SELECT add_thirteen( 11 );
    increment 
   -----------
           24
   (1 row)
```

**Note**: Do not to confuse the use of `BEGIN/END` for grouping statements in PL/pgSQL with the database commands for transaction control. PL/pgSQL's BEGIN/END are only for statement grouping; they do not start or end a transaction. 


## <a id="plpgsql_structure"></a>PL/pgSQL Statements and Control Structures

Refer to the PostgreSQL documentation for detailed information on the statements and control structures supported by the PL/pgSQL language:

-  You can execute SQL commands in PL/pgSQL functions using `EXECUTE`, `PERFORM`, and `SELECT ... INTO` statements.  Refer to [Basic Statements](https://www.postgresql.org/docs/8.2/static/plpgsql-statements.html) for PL/pgSQL specifics in this area.

- [Control Structures](https://www.postgresql.org/docs/8.2/static/plpgsql-control-structures.html) identifies the data manipulation and control constructs supported by PL/pgSQL, including those for looping through query results and trapping errors.


## <a id="supportedargumentandresultdatatypes"></a>PL/pgSQL Argument and Result Data Types 

Functions written in PL/pgSQL accept as arguments any base or array data type supported by the server, and they can return a result containing any of these data types. PL/pgSQL functions can also accept and return any composite type (row-type) specified by name.

You can declare PL/pgSQL functions to accept and return the polymorphic `anyelement` and `anyarray` types. PL/pgSQL functions can also be declared to return a set (or table) of any data type that can be returned as a single instance. Finally, you can declare a PL/pgSQL function to return `void` if it has no useful return value.

In place of an explicit specification of the return type, you can declare PL/pgSQL functions with output parameters. This does not add any fundamental capability to the language, but it is often convenient, especially when returning multiple values.

Upcoming sections provide specific PL/pgSQL examples using base, composite, and polymorphic argument and return types.


### <a id="plpgsql_namingargs"></a>Naming PL/pgSQL Function Arguments

Arguments passed to PL/pgSQL functions are named with identfiers `$1`, `$2`, `$3`, etc. If you choose, you can also declare aliases for the `$<n>` argument names.

One way to declare an alias is to give the argument a name in the PL/pgSQL function signature. In the following example, the single input argument `$1` is named `subtotal`. `subtotal` is used by name in the sales tax calculation in the body of the function.

``` sql
=> CREATE FUNCTION calculate_sales_tax(subtotal real) RETURNS real AS $$
   BEGIN
     RETURN subtotal * 0.06;
   END;
   $$ LANGUAGE plpgsql;
=> SELECT calculate_sales_tax( 123.45 );
    calculate_sales_tax 
   ---------------------
                  7.407
   (1 row)
```

You can also explicitly use the `DECLARE` block to declare an alias for a function argument:

``` sql
=> CREATE FUNCTION calculate_sales_tax(real) RETURNS real AS $$
   DECLARE
      subtotal ALIAS FOR $1;
   BEGIN
     RETURN subtotal * 0.06;
   END;
   $$ LANGUAGE plpgsql;
```

### <a id="plpgsql_inoutargs"></a>Input and Output PL/pgSQL Function Arguments

You can declare PL/pgSQL functions with both input (default) and output arguments.  Output arguments provide a convenient way of defining functions that return several values or columns. 

Output arguments are named `$<n>` and aliased in the same way as input arguments. You identify output arguments in the function signature using the `OUT` keyword.

In this example, you re-write the `calculate_sales_tax()` function to return the tax in an output argument.

``` sql
=> CREATE FUNCTION calculate_sales_tax(subtotal real, OUT tax real) AS $$
   BEGIN
      tax := subtotal * 0.06;
   END;
   $$ LANGUAGE plpgsql;
=> SELECT calculate_sales_tax( 123.45 );
```

Notice that you do not include the output arguments when you invoke the `calculate_sales_tax()` function. HAWQ considers only the input arguments to define the function's calling signature.

## <a id="plpgsqltypes"></a>Identifying Column and Row Data Types

You may need your PL/pgSQL function to operate on column or row data of which you do not know the data type. PL/pgSQL provides `%TYPE` and `%ROWTYPE` keywords for this purpose.

For additional information on PL/pgSQL declarations, see [Declarations](https://www.postgresql.org/docs/8.2/static/plpgsql-declarations.html) in the PostgreSQL documentation.

### <a id="plpgsqltypes_column"></a>Column Type

Use the `<variable>%TYPE` notation to access the data type of a variable. You would use this syntax when you want to declare a variable with the same type as a specific table column.

For example, if you have a column named `order_id` in your `orders` table and you want to declare a variable with the same data type as `orders.order_id`:

``` sql
DECLARE
    local_order_id orders.order_id%TYPE
```

`%TYPE` is particularly valuable in polymorphic functions, as the data types required for internal variables may change from one function invocation to the next.

### <a id="plpgsqltypes_row"></a>Row Type

A variable of a composite type is called a row-type variable. Row-type variables can hold a whole row of a query result, providing that the query's column set matches the declared type of the variable.

You can declare a row-type variable to have the same type as the rows of an existing table or view using the `<table_name>%ROWTYPE` notation. The fields of the row-type variable inherit the table's field sizes and precisions. You access the individual fields of a row-type variable using dot notation, for example `<row_variable>.<field>`.

When a function argument is a composite type, the corresponding argument `$<n>` is a row-type variable; you would use the `$<n>.<field>` syntax to access a specific field or column in the row.

**Note**: Only user-defined columns of a table row are accessible via a row-type variable; system and OID columns are not available. 

An example using a row-type variable follows. `table1` has integer fields named `order_id` and `order_item_id` and a text field named `product_name`. You will create and execute a `get_order_product()` function to return the order item and product concatenated together in a text string.

``` sql
=> CREATE TABLE table1 (order_id integer, order_item_id integer, product_name text );
=> INSERT INTO table1 VALUES( 1, 13, 'Paper Towels' );
=> INSERT INTO table1 VALUES( 1, 17, 'Pencils' );
=> INSERT INTO table1 VALUES( 2, 19, 'Light Bulbs' );
=> CREATE FUNCTION get_order_product( oid integer ) RETURNS text AS $$
   DECLARE
     table1_row table1%ROWTYPE;
   BEGIN
     SELECT * FROM table1 WHERE table1.order_id = oid INTO table1_row;
     RETURN table1_row.order_item_id || table1_row.product_name;
   END;
   $$ LANGUAGE plpgsql;
=> SELECT get_order_product(2);
    get_order_product 
   -------------------
    19Light Bulbs
   (1 row)
```

## <a id="plpgsqlexamples"></a>PL/pgSQL Functions as Table Sources

You can use PL/pgSQL functions in the same way you specify a table, view, or subquery in the `FROM` clause of a query. These functions are referred to as table functions, and can return both base and composite types. Functions that return base types produce a one-column table. Functions that return composite types produce a table column for each attribute of the composite type. You can use the columns returned by table functions in `SELECT`, `JOIN`, or `WHERE` clauses in the same manner as you would a table, view, or subquery column.

If a table function returns a base data type, the name of the single result column matches the function name. If the function returns a composite type, the result columns are assigned the same names as the individual attributes of the type.

You can choose to alias a table function in the `FROM` clause. If you do not alias a table function in the `FROM` clause, the resulting table name is assigned the function name.

In the following example, you populate a table and create a function to return the results of a specific query on the table:

```sql
=> CREATE TABLE sample1 (id int, name text);
=> INSERT INTO sample1 VALUES (1, 'Bill');
=> INSERT INTO sample1 VALUES (1, 'Jill');
=> INSERT INTO sample1 VALUES (2, 'Will');

=> CREATE OR REPLACE FUNCTION getfrom_sample1(int) RETURNS sample1 AS $$ 
   DECLARE                          
     sample1_row sample1%ROWTYPE;
   BEGIN                                                     
     SELECT * INTO sample1_row FROM sample1 WHERE id = $1;
     RETURN sample1_row;
   END;
   $$ LANGUAGE plpgsql;
```

Note the use of `sample1%ROWTYPE` to identify the type of a row of the `sample1` table.

Perform a query that executes the table function you created above:

``` sql
=> SELECT * getfrom_sample1(1);
    getfrom_sample1 
   -----------------
       (1,Bill)
   (1 row)
```

Even though the query filter matched 2 rows, the query returned only one row from the table because you specified a single `RETURNS` type when you created the `getfrom_sample1()` function. To return the full result of the query, you need to use the `SETOF` keyword.

When a PL/pgSQL function is decared as returning a `SETOF <type>`, each row of the function's final `SELECT` query is output as an element of the result set. `SETOF` is most often used when the function is called in the `FROM` clause of a query. In this case, each row returned by the function becomes a row input to the query. Using the above example:

``` sql
=> CREATE OR REPLACE FUNCTION getfrom_sample1(int) RETURNS SETOF sample1 AS $$         
   DECLARE                          
     sample1_row sample1%ROWTYPE;
   BEGIN                                                     
     FOR sample1_row IN SELECT * FROM sample1 WHERE id = $1 LOOP
       RETURN NEXT sample1_row;
     END LOOP;
     RETURN;
   END;
   $$ LANGUAGE plpgsql;
=> SELECT * FROM getfrom_sample1(1);
    id | name 
   ----+------
     1 | Bill
     1 | Jill
   (2 rows)
```

## <a id="plpgsqlpolymorphic"></a>Polymorphic PL/pgSQL Functions

PL/pgSQL supports the polymorphic `anyelement` and `anyarray` types. Using these types, you can create a single PL/pgSQL function that operates on multiple data types. Refer to [Polymorphic Types](../reference/HAWQDataTypes.html#polymorphictypes) for additional information in this area.

A special parameter named `$0` is created when the return type of a PL/pgSQL function is declared as a polymorphic type. The data type of `$0` identifies the return type of the function as deduced from the actual input types.

In this example, you create a polymorphic function that returns the sum of two values.

``` sql
=> CREATE FUNCTION add_two_values(v1 anyelement, v2 anyelement)
     RETURNS anyelement AS $$
   DECLARE
     sum ALIAS FOR $0;
   BEGIN
     sum := v1 + v2;
     RETURN sum;
   END;
   $$ LANGUAGE plpgsql;
```

Execute the function with integer input values:

``` sql
=> SELECT add_two_values( 1, 2 );
    add_two_values 
   ----------------
                 3
   (1 row)
```

Now execute the same function with float input values:

``` sql
=> SELECT add_two_values( 1.1, 2.2 );
    add_two_values 
   ----------------
                3.3
   (1 row)
```
