---
title: Data Types
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

This topic provides a reference of the data types supported in HAWQ.

HAWQ has a rich set of native data types available to users. Users may also define new data types using the `CREATE TYPE` command. This reference shows all of the built-in data types. In addition to the types listed here, there are also some internally used data types, such as **oid** (object identifier), but those are not documented in this guide.

The following data types are specified by SQL:

-   array (*)
-   bit
-   bit varying
-   boolean
-   character varying
-   char
-   character
-   date
-   decimal
-   double precision
-   integer
-   interval
-   numeric
-   real
-   smallint
-   time (with or without time zone)
-   timestamp (with or without time zone)
-   varchar

**Note**(\*): HAWQ supports the array data type for append-only tables; parquet table storage does *not* support the array type. 

Each data type has an external representation determined by its input and output functions. Many of the built-in types have obvious external formats. However, several types are unique to HAWQ, such as geometric paths, or have several possibilities for formats, such as the date and time types. Some of the input and output functions are not invertible. That is, the result of an output function may lose accuracy when compared to the original input.

 
 <span class="tablecap">Table 1. HAWQ Built-in Data Types</span>
=======
 

| Name                                       | Alias               | Size                  | Range                                       | Description                                                                       |
|--------------------------------------------|---------------------|-----------------------|---------------------------------------------|-----------------------------------------------------------------------------------|
| array                                     |          [ ]       |    variable (ignored)    | multi-dimensional |   any built-in or user-defined base type, enum type, or composite type                                                               |
| bigint                                     | int8                | 8 bytes               | -9223372036854775808 to 9223372036854775807 | large range integer                                                               |
| bigserial                                  | serial8             | 8 bytes               | 1 to 9223372036854775807                    | large autoincrementing integer                                                    |
| bit \[ (n) \]                              |                     | n bits                | bit string constant                         | fixed-length bit string                                                           |
| bit varying \[ (n) \]                      | varbit              | actual number of bits | bit string constant                         | variable-length bit string                                                        |
| boolean                                    | bool                | 1 byte                | true/false, t/f, yes/no, y/n, 1/0           | logical Boolean (true/false)                                                      |
| box                                        |                     | 32 bytes              | ((x1,y1),(x2,y2))                           | rectangular box in the plane - not allowed in distribution key columns.           |
| bytea                                      |                     | 1 byte + binarystring | sequence of octets                          | variable-length binary string                                                     |
| character \[ (n) \]                        | char  \[ (n) \]     | 1 byte + n            | strings up to n characters in length        | fixed-length, blank padded                                                        |
| character varying \[ (n) \]                | varchar  \[ (n) \]  | 1 byte + binarystring | strings up to n characters in length        | variable-length  with limit                                                       |
| cidr                                       |                     | 12 or 24 bytes        |                                             | IPv4 networks                                                                     |
| circle                                     |                     | 24 bytes              | &lt;(x,y),r&gt; (center and radius)         | circle in the plane - not allowed in distribution key columns.                    |
| date                                       |                     | 4 bytes               | 4713 BC - 294,277 AD                        |  calendar date (year, month, day)                                                 |
| decimal \[ (p, s) \]                       | numeric \[ (p,s) \] | variable              | no limit                                    | user-specified, inexact                                                           |
| double precision                           | float8 float        | 8 bytes               | 15 decimal digits precision                 | variable-precision, inexact                                                       |
| inet                                       |                     | 12 or 24 bytes        |                                             |  IPv4 hosts and networks                                                          |
| integer                                    | int, int4           | 4 bytes               | -2147483648 to +2147483647                  | usual choice for integer                                                          |
| interval \[ (p) \]                         |                     | 12 bytes              | -178000000 years - 178000000 years          | time span                                                                         |
| lseg                                       |                     | 32 bytes              | ((x1,y1),(x2,y2))                           | line segment in the plane - not allowed in distribution key columns.              |
| macaddr                                    |                     | 6 bytes               |                                             | MAC addresses                                                                     |
| money                                      |                     | 4 bytes               | -21474836.48 to +21474836.47                | currency amount                                                                   |
| path                                       |                     | 16+16n bytes          | \[(x1,y1),...\]                             | geometric path in the plane - not allowed in distribution key columns.            |
| point                                      |                     | 16 bytes              | (x, y)                                      | geometric path in the plane - not allowed in distribution key columns.            |
| polygon                                    |                     | 40+16n bytes          |  \[(x1,y1),...\]                            | closed geometric path in the plane - not allowed in the distribution key columns. |
| real                                       | float4              | 4 bytes               | 6 decimal digits precision                  |  variable-precision, inexact                                                      |
| serial                                     | serial4             | 4 bytes               | 1 to 2147483647                             | autoincrementing integer                                                          |
| smallint                                   | int2                | 2 bytes               | -32768 to +32767                            | small range integer                                                               |
| text                                       |                     | 1 byte + string size  | strings of any length                       | variable unlimited length                                                         |
| time \[ (p) \] \[ without time zone \]     |                     | 8 bytes               | 00:00:00\[.000000\] - 24:00:00\[.000000\]   | time of day only                                                                  |
| time \[ (p) \] with time zone              | timetz              | 12 bytes              | 00:00:00+1359 - 24:00:00-1359               | time of day only, with time zone                                                  |
| timestamp \[ (p) \] \[without time zone \] |                     | 8 bytes               | 4713 BC - 294,277 AD                        | both date and time                                                                |
| timestamp \[ (p) \] with time zone         | timestamptz         | 8 bytes               | 4713 BC - 294,277 AD                        | both date and time, with time zone                                                |
| xml                                        |                     | 1 byte + xml size     | xml of any length                           | variable unlimited length                                                         |

 
For variable length data types (such as char, varchar, text, xml, etc.) if the data is greater than or equal to 127 bytes, the storage overhead is 4 bytes instead of 1.

**Note**: Use these documented built-in types when creating user tables.  Any other data types that might be visible in the source code are for internal use only.

## <a id="timezones"></a>Time Zones

Time zones, and time-zone conventions, are influenced by political decisions, not just earth geometry. Time zones around the world became somewhat standardized during the 1900's, but continue to be prone to arbitrary changes, particularly with respect to daylight-savings rules. HAWQ uses the widely-used zoneinfo time zone database for information about historical time zone rules. For times in the future, the assumption is that the latest known rules for a given time zone will continue to be observed indefinitely far into the future.

HAWQ is compatible with the SQL standard definitions for typical usage. However, the SQL standard has an odd mix of date and time types and capabilities. Two obvious problems are:

-   Although the date type cannot have an associated time zone, the time type can. Time zones in the real world have little meaning unless associated with a date as well as a time, since the offset can vary through the year with daylight-saving time boundaries.
-   The default time zone is specified as a constant numeric offset from UTC. It is therefore impossible to adapt to daylight-saving time when doing date/time arithmetic across DST boundaries.

To address these difficulties, use date/time types that contain both date and time when using time zones. Do not use the type time with time zone (although HAWQ supports this for legacy applications and for compliance with the SQL standard). HAWQ assumes your local time zone for any type containing only date or time.

All timezone-aware dates and times are stored internally in UTC. They are converted to local time in the zone specified by the timezone configuration parameter before being displayed to the client.

HAWQ allows you to specify time zones in three different forms:

-   A full time zone name, for example America/New\_York. HAWQ uses the widely-used zoneinfo time zone data for this purpose, so the same names are also recognized by much other software.
-   A time zone abbreviation, for example PST. Such a specification merely defines a particular offset from UTC, in contrast to full time zone names which can imply a set of daylight savings transition-date rules as well. You cannot set the configuration parameters timezone or log\_timezone to a time zone abbreviation, but you can use abbreviations in date/time input values and with the AT TIME ZONE operator.
-   In addition to the timezone names and abbreviations, HAWQ /&gt; accepts POSIX-style time zone specifications of the form STDoffset or STDoffsetDST, where STD is a zone abbreviation, offset is a numeric offset in hours west from UTC, and DST is an optional daylight-savings zone abbreviation, assumed to stand for one hour ahead of the given offset. For example, if EST5EDT were not already a recognized zone name, it would be accepted and would be functionally equivalent to United States East Coast time. When a daylight-savings zone name is present, it is assumed to be used according to the same daylight-savings transition rules used in the zoneinfo time zone database's posixrules entry. In a standard HAWQ installation, posixrules is the same as US/Eastern, so that POSIX-style time zone specifications follow USA daylight-savings rules. If needed, you can adjust this behavior by replacing the posixrules file.

In short, this is the difference between abbreviations and full names: abbreviations always represent a fixed offset from UTC, whereas most of the full names imply a local daylight-savings time rule, and so have two possible UTC offsets.

One should be wary that the POSIX-style time zone feature can lead to silently accepting bogus input, since there is no check on the reasonableness of the zone abbreviations. For example, SET TIMEZONE TO FOOBAR0 will work, leaving the system effectively using a rather peculiar abbreviation for UTC. Another issue to keep in mind is that in POSIX time zone names, positive offsets are used for locations west of Greenwich. Everywhere else, PostgreSQL follows the ISO-8601 convention that positive timezone offsets are east of Greenwich.

In all cases, timezone names are recognized case-insensitively. 

Neither full names nor abbreviations are hard-wired into the server, see [Date and Time Configuration Files](#dateandtimeconfigurationfiles).

The timezone configuration parameter can be set in the file `hawq-site.xml`. There are also several special ways to set it:

-   If timezone is not specified in `hawq-site.xml` or as a server command-line option, the server attempts to use the value of the TZ environment variable as the default time zone. If TZ is not defined or is not any of the time zone names known to PostgreSQL, the server attempts to determine the operating system's default time zone by checking the behavior of the C library function localtime(). The default time zone is selected as the closest match from the known time zones. 
-   The SQL command SET TIME ZONE sets the time zone for the session. This is an alternative spelling of SET TIMEZONE TO with a more SQL-spec-compatible syntax.
-   The PGTZ environment variable is used by libpq clients to send a SET TIME ZONE command to the server upon connection.

## <a id="dateandtimeconfigurationfiles"></a>Date and Time Configuration Files

Since timezone abbreviations are not well standardized, HAWQ /&gt; provides a means to customize the set of abbreviations accepted by the server. The timezone\_abbreviations run-time parameter determines the active set of abbreviations. While this parameter can be altered by any database user, the possible values for it are under the control of the database administrator — they are in fact names of configuration files stored in .../share/timezonesets/ of the installation directory. By adding or altering files in that directory, the administrator can set local policy for timezone abbreviations.

timezone\_abbreviations can be set to any file name found in .../share/timezonesets/, if the file's name is entirely alphabetic. (The prohibition against non-alphabetic characters in timezone\_abbreviations prevents reading files outside the intended directory, as well as reading editor backup files and other extraneous files.)

A timezone abbreviation file can contain blank lines and comments beginning with \#. Non-comment lines must have one of these formats:

``` pre
time_zone_nameoffsettime_zone_nameoffset D
@INCLUDE file_name
@OVERRIDE
```

A time\_zone\_name is just the abbreviation being defined. The offset is the zone's offset in seconds from UTC, positive being east from Greenwich and negative being west. For example, -18000 would be five hours west of Greenwich, or North American east coast standard time. D indicates that the zone name represents local daylight-savings time rather than standard time. Since all known time zone offsets are on 15 minute boundaries, the number of seconds has to be a multiple of 900.

The @INCLUDE syntax allows inclusion of another file in the .../share/timezonesets/ directory. Inclusion can be nested, to a limited depth.

The @OVERRIDE syntax indicates that subsequent entries in the file can override previous entries (i.e., entries obtained from included files). Without this, conflicting definitions of the same timezone abbreviation are considered an error.

In an unmodified installation, the file Default contains all the non-conflicting time zone abbreviations for most of the world. Additional files Australia and India are provided for those regions: these files first include the Default file and then add or modify timezones as needed.

For reference purposes, a standard installation also contains files Africa.txt, America.txt, etc, containing information about every time zone abbreviation known to be in use according to the zoneinfo timezone database. The zone name definitions found in these files can be copied and pasted into a custom configuration file as needed.

**Note:** These files cannot be directly referenced as timezone\_abbreviations settings, because of the dot embedded in their names.

## <a id="polymorphictypes"></a>Polymorphic Types 

Two pseudo-types of special interest are `anyelement` and `anyarray`, which are collectively called *polymorphic types*. Any function declared using these types is said to be a *polymorphic function*. A polymorphic function can operate on many different data types, with the specific data type(s) being determined by the data types actually passed to it in a particular call.

Polymorphic arguments and results are tied to each other and are resolved to a specific data type when a query calling a polymorphic function is parsed. Each position (either argument or return value) declared as `anyelement` is allowed to have any specific actual data type, but in any given call they must all be the same actual type. Each position declared as `anyarray` can have any array data type, but similarly they must all be the same type. If there are positions declared `anyarray` and others declared `anyelement`, the actual array type in the `anyarray` positions must be an array whose elements are the same type appearing in the `anyelement` positions.

Thus, when more than one argument position is declared with a polymorphic type, the net effect is that only certain combinations of actual argument types are allowed. For example, a function declared as `equal(anyelement, anyelement)` will take any two input values, so long as they are of the same data type.

When the return value of a function is declared as a polymorphic type, there must be at least one argument position that is also polymorphic, and the actual data type supplied as the argument determines the actual result type for that call. For example, if there were not already an array subscripting mechanism, one could define a function that implements subscripting as `subscript(anyarray, integer) returns anyelement`. This declaration constrains the actual first argument to be an array type, and allows the parser to infer the correct result type from the actual first argument's type. 

