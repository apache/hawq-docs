---
title: COPY
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

Copies data between a file and a table.

## <a id="topic1__section2"></a>Synopsis

``` pre
COPY <table> [(<column> [, ...])] FROM {'<file>' | STDIN}
     [ [WITH] 
       [OIDS]
       [HEADER]
       [DELIMITER [ AS ] '<delimiter>']
       [NULL [ AS ] '<null string>']
       [ESCAPE [ AS ] '<escape>' | 'OFF']
       [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
       [CSV [QUOTE [ AS ] '<quote>'] 
            [FORCE NOT NULL <column> [, ...]]
       [FILL MISSING FIELDS]
       [[LOG ERRORS INTO <error_table> [KEEP] 
       SEGMENT REJECT LIMIT <count> [ROWS | PERCENT] ]

COPY {<table> [(<column> [, ...])] | (<query>)} TO {'<file>' | STDOUT}
      [ [WITH] 
        [OIDS]
        [HEADER]
        [DELIMITER [ AS ] '<delimiter>']
        [NULL [ AS ] '<null string>']
        [ESCAPE [ AS ] '<escape>' | 'OFF']
        [CSV [QUOTE [ AS ] '<quote>'] 
             [FORCE QUOTE <column> [, ...]] ]
```

## <a id="topic1__section3"></a>Description

`COPY` moves data between HAWQ tables and standard file-system files. `COPY TO` copies the contents of a table to a file, while `COPY FROM` copies data from a file to a table (appending the data to whatever is in the table already). `COPY TO` can also copy the results of a `SELECT` query.

If a list of columns is specified, `COPY` will only copy the data in the specified columns to or from the file. If there are any columns in the table that are not in the column list, `COPY FROM` will insert the default values for those columns.

`COPY` with a file name instructs the HAWQ master host to directly read from or write to a file. The file must be accessible to the master host and the name must be specified from the viewpoint of the master host. When `STDIN` or `STDOUT` is specified, data is transmitted via the connection between the client and the master.

If `SEGMENT REJECT LIMIT` is used, then a `COPY FROM` operation will operate in single row error isolation mode. In this release, single row error isolation mode only applies to rows in the input file with format errors — for example, extra or missing attributes, attributes of a wrong data type, or invalid client encoding sequences. Constraint errors such as violation of a `NOT  NULL`, `CHECK`, or `UNIQUE` constraint will still be handled in 'all-or-nothing' input mode. The user can specify the number of error rows acceptable (on a per-segment basis), after which the entire `COPY FROM` operation will be aborted and no rows will be loaded. Note that the count of error rows is per-segment, not per entire load operation. If the per-segment reject limit is not reached, then all rows not containing an error will be loaded. If the limit is not reached, all good rows will be loaded and any error rows discarded. If you would like to keep error rows for further examination, you can optionally declare an error table using the `LOG ERRORS INTO` clause. Any rows containing a format error would then be logged to the specified error table.

**Outputs**

On successful completion, a `COPY` command returns a command tag of the form, where \<count\> is the number of rows copied:

``` pre
COPY <count>
            
```

If running a `COPY FROM` command in single row error isolation mode, the following notice message will be returned if any rows were not loaded due to format errors, where \<count\> is the number of rows rejected:

``` pre
NOTICE: Rejected <count> badly formatted rows.
```

## <a id="topic1__section5"></a>Parameters

<dt> \<table\>   </dt>
<dd>The name (optionally schema-qualified) of an existing table.</dd>

<dt> \<column\>   </dt>
<dd>An optional list of columns to be copied. If no column list is specified, all columns of the table will be copied.</dd>

<dt> \<query\>   </dt>
<dd>A `SELECT` or `VALUES` command whose results are to be copied. Note that parentheses are required around the query.</dd>

<dt> \<file\>   </dt>
<dd>The absolute path name of the input or output file.</dd>

<dt>STDIN  </dt>
<dd>Specifies that input comes from the client application.</dd>

<dt>STDOUT  </dt>
<dd>Specifies that output goes to the client application.</dd>

<dt>OIDS  </dt>
<dd>Specifies copying the OID for each row. (An error is raised if OIDS is specified for a table that does not have OIDs, or in the case of copying a query.)</dd>

<dt> \<delimiter\>   </dt>
<dd>The single ASCII character that separates columns within each row (line) of the file. The default is a tab character in text mode, a comma in `CSV` mode.</dd>

<dt> \<null string\>   </dt>
<dd>The string that represents a null value. The default is `\N` (backslash-N) in text mode, and a empty value with no quotes in `CSV` mode. You might prefer an empty string even in text mode for cases where you don't want to distinguish nulls from empty strings. When using `COPY FROM`, any data item that matches this string will be stored as a null value, so you should make sure that you use the same string as you used with `COPY TO`.</dd>

<dt> \<escape\>   </dt>
<dd>Specifies the single character that is used for C escape sequences (such as `\n`,`\t`,`\100`, and so on) and for quoting data characters that might otherwise be taken as row or column delimiters. Make sure to choose an escape character that is not used anywhere in your actual column data. The default escape character is `\` (backslash) for text files or `"` (double quote) for CSV files, however it is possible to specify any other character to represent an escape. It is also possible to disable escaping on text-formatted files by specifying the value '`OFF'` as the escape value. This is very useful for data such as web log data that has many embedded backslashes that are not intended to be escapes.</dd>

<dt>NEWLINE  </dt>
<dd>Specifies the newline used in your data files — `LF` (Line feed, 0x0A), `CR` (Carriage return, 0x0D), or `CRLF` (Carriage return plus line feed, 0x0D 0x0A). If not specified, a HAWQ segment will detect the newline type by looking at the first row of data it receives and using the first newline type encountered.</dd>

<dt>CSV  </dt>
<dd>Selects Comma Separated Value (CSV) mode.</dd>

<dt>HEADER  </dt>
<dd>Specifies that a file contains a header line with the names of each column in the file. On output, the first line contains the column names from the table, and on input, the first line is ignored.</dd>

<dt> \<quote\>   </dt>
<dd>Specifies the quotation character in CSV mode. The default is double-quote.</dd>

<dt>FORCE QUOTE  </dt>
<dd>In `CSV COPY TO` mode, forces quoting to be used for all non-`NULL` values in each specified column. `NULL` output is never quoted.</dd>

<dt>FORCE NOT NULL  </dt>
<dd>In `CSV COPY FROM` mode, process each specified column as though it were quoted and hence not a `NULL` value. For the default null string in `CSV` mode (nothing between two delimiters), this causes missing values to be evaluated as zero-length strings.</dd>

<dt>FILL MISSING FIELDS  </dt>
<dd>In `COPY FROM` more for both `TEXT` and `CSV`, specifying `FILL MISSING FIELDS` will set missing trailing field values to `NULL` (instead of reporting an error) when a row of data has missing data fields at the end of a line or row. Blank rows, fields with a `NOT NULL` constraint, and trailing delimiters on a line will still report an error.</dd>

<dt>LOG ERRORS INTO \<error\_table\> \[KEEP\]  </dt>

<dd>This is an optional clause that can precede a `SEGMENT REJECT LIMIT` clause to log information about rows with formatting errors. The `INTO <error_table>` clause specifies an error table where rows with formatting errors will be logged when running in single row error isolation mode. You can then examine this error table to see error rows that were not loaded (if any). If the \<error\_table\> specified already exists, it will be used. If it does not exist, it will be automatically generated. If the command auto-generates the error table and no errors are produced, the default is to drop the error table after the operation completes unless `KEEP` is specified. If the table is auto-generated and the error limit is exceeded, the entire transaction is rolled back and no error data is saved. If you want the error table to persist in this case, create the error table prior to running the `COPY`. An error table is defined as follows:


``` pre
CREATE TABLE <error_table_name> ( cmdtime timestamptz, relname text, 
    filename text, linenum int, bytenum int, errmsg text, 
    rawdata text, rawbytes bytea ) DISTRIBUTED RANDOMLY;
```
</dd>

<dt>SEGMENT REJECT LIMIT \<count\> \[ROWS | PERCENT\]  </dt>
<dd>Runs a `COPY FROM` operation in single row error isolation mode. If the input rows have format errors they will be discarded provided that the reject limit count is not reached on any HAWQ segment instance during the load operation. The reject limit count can be specified as number of rows (the default) or percentage of total rows (1-100). If `PERCENT` is used, each segment starts calculating the bad row percentage only after the number of rows specified by the parameter `gp_reject_percent_threshold` has been processed. The default for `gp_reject_percent_threshold` is 300 rows. Constraint errors such as violation of a `NOT NULL` or `CHECK` constraint will still be handled in 'all-or-nothing' input mode. If the limit is not reached, all good rows will be loaded and any error rows discarded.</dd>

## <a id="topic1__section6"></a>Notes

`COPY` can only be used with tables, not with views. However, you can write `COPY (SELECT * FROM viewname) TO ...`

The `BINARY` key word causes all data to be stored/read as binary format rather than as text. It is somewhat faster than the normal text mode, but a binary-format file is less portable across machine architectures and HAWQ versions. Also, you cannot run `COPY FROM` in single row error isolation mode if the data is in binary format.

You must have `SELECT` privilege on the table whose values are read by `COPY TO`, and insert privilege on the table into which values are inserted by `COPY FROM`.

Files named in a `COPY` command are read or written directly by the database server, not by the client application. Therefore, they must reside on or be accessible to the HAWQ master host machine, not the client. They must be accessible to and readable or writable by the HAWQ system user (the user ID the server runs as), not the client. `COPY` naming a file is only allowed to database superusers, since it allows reading or writing any file that the server has privileges to access.

`COPY FROM` will invoke any check constraints on the destination table. However, it will not invoke rewrite rules. Note that in this release, violations of constraints are not evaluated for single row error isolation mode.

`COPY` input and output is affected by `DateStyle`. To ensure portability to other HAWQ installations that might use non-default `DateStyle` settings, `DateStyle` should be set to ISO before using `COPY TO`.

By default, `COPY` stops operation at the first error. This should not lead to problems in the event of a `COPY TO`, but the target table will already have received earlier rows in a `COPY FROM`. These rows will not be visible or accessible, but they still occupy disk space. This may amount to a considerable amount of wasted disk space if the failure happened well into a large `COPY FROM` operation. You may wish to use single row error isolation mode to filter out error rows while still loading good rows.

COPY supports creating readable foreign tables with error tables. The default for concurrently inserting into the error table is 127. You can use error tables with foreign tables under the following circumstances:

-   Multiple foreign tables can use different error tables
-   Multiple foreign tables cannot use the same error table

## <a id="topic1__section7"></a>File Formats

File formats supported by `COPY`.

**Text Format**
When `COPY` is used without the `BINARY` or `CSV` options, the data read or written is a text file with one line per table row. Columns in a row are separated by the \<delimiter\> character (tab by default). The column values themselves are strings generated by the output function, or acceptable to the input function, of each attribute's data type. The specified null string is used in place of columns that are null. `COPY             FROM` will raise an error if any line of the input file contains more or fewer columns than are expected. If `OIDS` is specified, the OID is read or written as the first column, preceding the user data columns.

The data file has two reserved characters that have special meaning to `COPY`:

-   The designated delimiter character (tab by default), which is used to separate fields in the data file.
-   A UNIX-style line feed (`\n` or `0x0a`), which is used to designate a new row in the data file. It is strongly recommended that applications generating `COPY` data convert data line feeds to UNIX-style line feeds rather than Microsoft Windows style carriage return line feeds (`\r\n` or `0x0a 0x0d`).

If your data contains either of these characters, you must escape the character so `COPY` treats it as data and not as a field separator or new row.

By default, the escape character is a `\` (backslash) for text-formatted files and a `"` (double quote) for csv-formatted files. If you want to use a different escape character, you can do so using the `ESCAPE AS `clause. Make sure to choose an escape character that is not used anywhere in your data file as an actual data value. You can also disable escaping in text-formatted files by using `ESCAPE 'OFF'`.

For example, suppose you have a table with three columns and you want to load the following three fields using COPY.

-   percentage sign = %
-   vertical bar = |
-   backslash = \\

Your designated \<delimiter\> character is `|` (pipe character), and your designated \<escape\> character is `*` (asterisk). The formatted row in your data file would look like this:

``` pre
percentage sign = % | vertical bar = *| | backslash = \
```

Notice how the pipe character that is part of the data has been escaped using the asterisk character (\*). Also notice that we do not need to escape the backslash since we are using an alternative escape character.

The following characters must be preceded by the escape character if they appear as part of a column value: the escape character itself, newline, carriage return, and the current delimiter character. You can specify a different escape character using the `ESCAPE             AS` clause.

**CSV Format**

This format is used for importing and exporting the Comma Separated Value (CSV) file format used by many other programs, such as spreadsheets. Instead of the escaping used by HAWQ standard text mode, it produces and recognizes the common CSV escaping mechanism.

The values in each record are separated by the `DELIMITER` character. If the value contains the delimiter character, the `QUOTE` character, the `ESCAPE` character (which is double quote by default), the `NULL` string, a carriage return, or line feed character, then the whole value is prefixed and suffixed by the `QUOTE` character. You can also use `FORCE QUOTE` to force quotes when outputting non-`NULL` values in specific columns.

The CSV format has no standard way to distinguish a `NULL` value from an empty string. HAWQ `COPY` handles this by quoting. A `NULL` is output as the `NULL` string and is not quoted, while a data value matching the `NULL` string is quoted. Therefore, using the default settings, a `NULL` is written as an unquoted empty string, while an empty string is written with double quotes (""). Reading values follows similar rules. You can use `FORCE NOT NULL` to prevent `NULL` input comparisons for specific columns.

Because backslash is not a special character in the `CSV` format, `\.`, the end-of-data marker, could also appear as a data value. To avoid any misinterpretation, a `\.` data value appearing as a lone entry on a line is automatically quoted on output, and on input, if quoted, is not interpreted as the end-of-data marker. If you are loading a file created by another application that has a single unquoted column and might have a value of `\.`, you might need to quote that value in the input file.

**Note:** In `CSV` mode, all characters are significant. A quoted value surrounded by white space, or any characters other than `DELIMITER`, will include those characters. This can cause errors if you import data from a system that pads CSV lines with white space out to some fixed width. If such a situation arises you might need to preprocess the CSV file to remove the trailing white space, before importing the data into HAWQ.

**Note:** `CSV` mode will both recognize and produce CSV files with quoted values containing embedded carriage returns and line feeds. Thus the files are not strictly one line per table row like text-mode files.

**Note:** Many programs produce strange and occasionally perverse CSV files, so the file format is more a convention than a standard. Thus you might encounter some files that cannot be imported using this mechanism, and `COPY` might produce files that other programs cannot process.

**Binary Format**

The `BINARY` format consists of a file header, zero or more tuples containing the row data, and a file trailer. Headers and data are in network byte order.

-   **File Header** — The file header consists of 15 bytes of fixed fields, followed by a variable-length header extension area. The fixed fields are:
    -   **Signature** — 11-byte sequence PGCOPY\\n\\377\\r\\n\\0 — note that the zero byte is a required part of the signature. (The signature is designed to allow easy identification of files that have been munged by a non-8-bit-clean transfer. This signature will be changed by end-of-line-translation filters, dropped zero bytes, dropped high bits, or parity changes.)
    -   **Flags field** — 32-bit integer bit mask to denote important aspects of the file format. Bits are numbered from 0 (LSB) to 31 (MSB). Note that this field is stored in network byte order (most significant byte first), as are all the integer fields used in the file format. Bits 16-31 are reserved to denote critical file format issues; a reader should abort if it finds an unexpected bit set in this range. Bits 0-15 are reserved to signal backwards-compatible format issues; a reader should simply ignore any unexpected bits set in this range. Currently only one flag is defined, and the rest must be zero (Bit 16: 1 if data has OIDs, 0 if not).
    -   **Header extension area length** — 32-bit integer, length in bytes of remainder of header, not including self. Currently, this is zero, and the first tuple follows immediately. Future changes to the format might allow additional data to be present in the header. A reader should silently skip over any header extension data it does not know what to do with. The header extension area is envisioned to contain a sequence of self-identifying chunks. The flags field is not intended to tell readers what is in the extension area. Specific design of header extension contents is left for a later release.
-   **Tuples** — Each tuple begins with a 16-bit integer count of the number of fields in the tuple. (Presently, all tuples in a table will have the same count, but that might not always be true.) Then, repeated for each field in the tuple, there is a 32-bit length word followed by that many bytes of field data. (The length word does not include itself, and can be zero.) As a special case, -1 indicates a NULL field value. No value bytes follow in the NULL case.

    There is no alignment padding or any other extra data between fields.

    Presently, all data values in a COPY BINARY file are assumed to be in binary format (format code one). It is anticipated that a future extension may add a header field that allows per-column format codes to be specified.

    If OIDs are included in the file, the OID field immediately follows the field-count word. It is a normal field except that it's not included in the field-count. In particular it has a length word — this will allow handling of 4-byte vs. 8-byte OIDs without too much pain, and will allow OIDs to be shown as null if that ever proves desirable.

-   **File Trailer** — The file trailer consists of a 16-bit integer word containing `-1`. This is easily distinguished from a tuple's field-count word. A reader should report an error if a field-count word is neither `-1` nor the expected number of columns. This provides an extra check against somehow getting out of sync with the data.

## <a id="topic1__section11"></a>Examples

Copy a table to the client using the vertical bar (|) as the field delimiter:

``` pre
COPY country TO STDOUT WITH DELIMITER '|';
```

Copy data from a file into the `country` table:

``` pre
COPY country FROM '/home/usr1/sql/country_data';
```

Copy into a file just the countries whose names start with 'A':

``` pre
COPY (SELECT * FROM country WHERE country_name LIKE 'A%') TO 
'/home/usr1/sql/a_list_countries.copy';
```

Create an error table called `err_sales` to use with single row error isolation mode:

``` pre
CREATE TABLE err_sales ( cmdtime timestamptz, relname text, 
filename text, linenum int, bytenum int, errmsg text, rawdata text, rawbytes bytea ) DISTRIBUTED RANDOMLY;
```

Copy data from a file into the `sales` table using single row error isolation mode:

``` pre
COPY sales FROM '/home/usr1/sql/sales_data' LOG ERRORS INTO 
err_sales SEGMENT REJECT LIMIT 10 ROWS;
```

## <a id="topic1__section12"></a>Compatibility

There is no `COPY` statement in the SQL standard.

## <a id="topic1__section13"></a>See Also

[CREATE EXTERNAL TABLE](CREATE-EXTERNAL-TABLE.html)
