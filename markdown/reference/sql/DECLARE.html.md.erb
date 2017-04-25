---
title: DECLARE
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

Defines a cursor.

## <a id="topic1__section2"></a>Synopsis

``` pre
DECLARE <name> [BINARY] [INSENSITIVE] [NO SCROLL] CURSOR
     [{WITH | WITHOUT} HOLD]
     FOR <query> [FOR READ ONLY]
```

## <a id="topic1__section3"></a>Description

`DECLARE` allows a user to create cursors, which can be used to retrieve a small number of rows at a time out of a larger query. Cursors can return data either in text or in binary format using [FETCH](FETCH.html).

Normal cursors return data in text format, the same as a `SELECT` would produce. Since data is stored natively in binary format, the system must do a conversion to produce the text format. Once the information comes back in text form, the client application may need to convert it to a binary format to manipulate it. In addition, data in the text format is often larger in size than in the binary format. Binary cursors return the data in a binary representation that may be more easily manipulated. Nevertheless, if you intend to display the data as text anyway, retrieving it in text form will save you some effort on the client side.

As an example, if a query returns a value of one from an integer column, you would get a string of 1 with a default cursor whereas with a binary cursor you would get a 4-byte field containing the internal representation of the value (in big-endian byte order).

Binary cursors should be used carefully. Many applications, including psql, are not prepared to handle binary cursors and expect data to come back in the text format.

**Note:**
When the client application uses the 'extended query' protocol to issue a `FETCH` command, the Bind protocol message specifies whether data is to be retrieved in text or binary format. This choice overrides the way that the cursor is defined. The concept of a binary cursor as such is thus obsolete when using extended query protocol — any cursor can be treated as either text or binary.

## <a id="topic1__section4"></a>Parameters

<dt>\<name\>  </dt>
<dd>The name of the cursor to be created.</dd>

<dt>BINARY  </dt>
<dd>Causes the cursor to return data in binary rather than in text format.</dd>

<dt>INSENSITIVE  </dt>
<dd>Indicates that data retrieved from the cursor should be unaffected by updates to the tables underlying the cursor while the cursor exists. In HAWQ, all cursors are insensitive. This key word currently has no effect and is present for compatibility with the SQL standard.</dd>

<dt>NO SCROLL  </dt>
<dd>A cursor cannot be used to retrieve rows in a nonsequential fashion. This is the default behavior in HAWQ, since scrollable cursors (`SCROLL`) are not supported.</dd>

<dt>WITH HOLD  
WITHOUT HOLD  </dt>
<dd>`WITH HOLD` specifies that the cursor may continue to be used after the transaction that created it successfully commits. `WITHOUT HOLD` specifies that the cursor cannot be used outside of the transaction that created it. `WITHOUT HOLD` is the default.</dd>

<dt>\<query\> </dt>
<dd>A [SELECT](SELECT.html) command which will provide the rows to be returned by the cursor.</dd>

<!-- -->

<dt>FOR READ ONLY  </dt>
<dd>`FOR READ ONLY` indicates that the cursor is used in a read-only mode. Cursors can only be used in a read-only mode in HAWQ. HAWQ does not support updatable cursors (FOR UPDATE), so this is the default behavior.</dd>

## <a id="topic1__section5"></a>Notes

Unless `WITH HOLD` is specified, the cursor created by this command can only be used within the current transaction. Thus, `DECLARE` without `WITH           HOLD` is useless outside a transaction block: the cursor would survive only to the completion of the statement. Therefore HAWQ reports an error if this command is used outside a transaction block. Use `BEGIN`, `COMMIT` and `ROLLBACK` to define a transaction block.

If `WITH HOLD` is specified and the transaction that created the cursor successfully commits, the cursor can continue to be accessed by subsequent transactions in the same session. (But if the creating transaction is aborted, the cursor is removed.) A cursor created with `WITH HOLD` is closed when an explicit `CLOSE` command is issued on it, or the session ends. In the current implementation, the rows represented by a held cursor are copied into a temporary file or memory area so that they remain available for subsequent transactions.

Scrollable cursors are not currently supported in HAWQ. You can only use `FETCH` to move the cursor position forward, not backwards.

You can see all available cursors by querying the `pg_cursors` system view.

## <a id="topic1__section6"></a>Examples

Declare a cursor:

``` pre
DECLARE mycursor CURSOR FOR SELECT * FROM mytable;
```

## <a id="topic1__section7"></a>Compatibility

SQL standard allows cursors only in embedded SQL and in modules. HAWQ permits cursors to be used interactively.

HAWQ does not implement an `OPEN` statement for cursors. A cursor is considered to be open when it is declared.

The SQL standard allows cursors to move both forward and backward. All HAWQ cursors are forward moving only (not scrollable).

Binary cursors are a HAWQ extension.

## <a id="topic1__section8"></a>See Also

[CLOSE](CLOSE.html), [FETCH](FETCH.html), [SELECT](SELECT.html)
