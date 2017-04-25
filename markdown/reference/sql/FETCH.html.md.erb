---
title: FETCH
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

Retrieves rows from a query using a cursor.

## <a id="topic1__section2"></a>Synopsis

``` pre
FETCH [ <forward_direction> { FROM | IN } ] <cursorname>

```

where *forward\_direction* can be empty or one of:

``` pre
    NEXT
    FIRST
    LAST
    ABSOLUTE <count>
    RELATIVE <count>
    <count>
    ALL
    FORWARD
    FORWARD <count>
    FORWARD ALL
```

## <a id="topic1__section3"></a>Description

`FETCH` retrieves rows using a previously-created cursor.

A cursor has an associated position, which is used by `FETCH`. The cursor position can be before the first row of the query result, on any particular row of the result, or after the last row of the result. When created, a cursor is positioned before the first row. After fetching some rows, the cursor is positioned on the row most recently retrieved. If `FETCH` runs off the end of the available rows then the cursor is left positioned after the last row. `FETCH           ALL` will always leave the cursor positioned after the last row.

The forms `NEXT`, `FIRST`, `LAST`, `ABSOLUTE`, `RELATIVE` fetch a single row after moving the cursor appropriately. If there is no such row, an empty result is returned, and the cursor is left positioned before the first row or after the last row as appropriate.

The forms using `FORWARD` retrieve the indicated number of rows moving in the forward direction, leaving the cursor positioned on the last-returned row (or after all rows, if the count exceeds the number of rows available). Note that it is not possible to move a cursor position backwards in HAWQ, since scrollable cursors are not supported. You can only move a cursor forward in position using `FETCH`.

`RELATIVE 0` and `FORWARD 0` request fetching the current row without moving the cursor, that is, re-fetching the most recently fetched row. This will succeed unless the cursor is positioned before the first row or after the last row, in which case no row is returned.

**Outputs**

On successful completion, a `FETCH` command returns a command tag of the form

``` pre
FETCH count

```

The count is the number of rows fetched (possibly zero). Note that in `psql`, the command tag will not actually be displayed, since `psql` displays the fetched rows instead.

## <a id="topic1__section5"></a>Parameters

<dt>\<forward\_direction\>  </dt>
<dd>Defines the fetch direction and number of rows to fetch. Only forward fetches are allowed in HAWQ. It can be one of the following:</dd>

<dt>NEXT  </dt>
<dd>Fetch the next row. This is the default if direction is omitted.</dd>

<dt>FIRST  </dt>
<dd>Fetch the first row of the query (same as `ABSOLUTE 1`). Only allowed if it is the first `FETCH` operation using this cursor.</dd>

<dt>LAST  </dt>
<dd>Fetch the last row of the query (same as `ABSOLUTE -1`).</dd>

<dt>ABSOLUTE \<count\>  </dt>
<dd>Fetch the specified row of the query. Position after last row if count is out of range. Only allowed if the row specified by *count* moves the cursor position forward.</dd>

<dt>RELATIVE \<count\>  </dt>
<dd>Fetch the specified row of the query *count* rows ahead of the current cursor position. `RELATIVE 0` re-fetches the current row, if any. Only allowed if *count* moves the cursor position forward.</dd>

<dt>\<count\> </dt>
<dd>Fetch the next *count* number of rows (same as `FORWARD                 count                   `).</dd>

<dt>ALL  </dt>
<dd>Fetch all remaining rows (same as `FORWARD ALL`).</dd>

<dt>FORWARD  </dt>
<dd>Fetch the next row (same as `NEXT`).</dd>

<dt>FORWARD \<count\>  </dt>
<dd>Fetch the next *count* number of rows. `FORWARD 0` re-fetches the current row.</dd>

<dt>FORWARD ALL  </dt>
<dd>Fetch all remaining rows.</dd>

<dt>\<cursorname\> </dt>
<dd>The name of an open cursor.</dd>

## <a id="topic1__section6"></a>Notes

HAWQ does not support scrollable cursors, so you can only use `FETCH` to move the cursor position forward.

`ABSOLUTE` fetches are not any faster than navigating to the desired row with a relative move: the underlying implementation must traverse all the intermediate rows anyway.

Updating data via a cursor is currently not supported by HAWQ.

`DECLARE` is used to define a cursor. Use `MOVE` to change cursor position without retrieving data.

## <a id="topic1__section7"></a>Examples

-- Start the transaction:

``` pre
BEGIN;
```

-- Set up a cursor:

``` pre
DECLARE mycursor CURSOR FOR SELECT * FROM films;
```

-- Fetch the first 5 rows in the cursor `mycursor`:

``` pre
FETCH FORWARD 5 FROM mycursor;
 code  |          title          | did | date_prod  |   kind   |  len
-------+-------------------------+-----+------------+----------+-------
 BL101 | The Third Man           | 101 | 1949-12-23 | Drama    | 01:44
 BL102 | The African Queen       | 101 | 1951-08-11 | Romantic | 01:43
 JL201 | Une Femme est une Femme | 102 | 1961-03-12 | Romantic | 01:25
 P_301 | Vertigo                 | 103 | 1958-11-14 | Action   | 02:08
 P_302 | Becket                  | 103 | 1964-02-03 | Drama    | 02:28
```

-- Close the cursor and end the transaction:

``` pre
CLOSE mycursor;
COMMIT;
```

## <a id="topic1__section8"></a>Compatibility

SQL standard allows cursors only in embedded SQL and in modules. HAWQ permits cursors to be used interactively.

The variant of `FETCH` described here returns the data as if it were a `SELECT` result rather than placing it in host variables. Other than this point, `FETCH` is fully upward-compatible with the SQL standard.

The `FETCH` forms involving `FORWARD`, as well as the forms `FETCH` count and `FETCH ALL`, in which `FORWARD` is implicit, are HAWQ extensions. `BACKWARD` is not supported.

The SQL standard allows only `FROM` preceding the cursor name; the option to use `IN` is an extension.

## <a id="topic1__section9"></a>See Also

[DECLARE](DECLARE.html), [CLOSE](CLOSE.html)
