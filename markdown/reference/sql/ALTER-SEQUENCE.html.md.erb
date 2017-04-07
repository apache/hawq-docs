---
title: ALTER SEQUENCE
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

Change the definition of a sequence generator.

## <a id="topic1__section2"></a>Synopsis

``` pre
ALTER SEQUENCE <name>
       [INCREMENT [BY] <value>]
       [MINVALUE <minvalue> | NO MINVALUE]
       [MAXVALUE <maxvalue> | NO MAXVALUE]
       [RESTART [ WITH ] <start>]
       [CACHE <cache>]
       [[NO] CYCLE]
       [OWNED BY { <table>.<column> | NONE }]
```

## <a id="topic1__section3"></a>Description

`ALTER SEQUENCE` changes the parameters of an existing sequence generator. Any parameters not specifically set in the `ALTER SEQUENCE` command retain their prior setting.

You must own the sequence to use `ALTER SEQUENCE`. 


## <a id="topic1__section4"></a>Parameters

<dt> \<name\>  </dt>
<dd>The name (optionally schema-qualified) of the sequence to be altered.</dd>

<dt> \<increment\>  </dt>
<dd>Specifies which value is added to the current sequence value to create a new value. A positive value will make an ascending sequence, a negative one a descending sequence. The default value is 1.</dd>

<dt> \<minvalue\>  
NO MINVALUE  </dt>
<dd>Determines the minimum value a sequence can generate. If this clause is not supplied or `NO MINVALUE` is specified, then defaults will be used. The defaults are 1 and -2<sup>63</sup>-1 for ascending and descending sequences, respectively.</dd>

<dt> \<maxvalue\>  
NO MAXVALUE  </dt>
<dd>Determines the maximum value for the sequence. If this clause is not supplied or `NO MAXVALUE` is specified, then default values will be used. The defaults are 2<sup>63</sup>-1 and -1 for ascending and descending sequences, respectively.</dd>

<dt> \<start\>  </dt>
<dd>The new current value of the sequence.</dd>

<dt> \<cache\>  </dt>
<dd>Specifies how many sequence numbers are to be preallocated and stored in memory for faster access. The minimum (and default) value is 1 (no cache).</dd>

<dt>CYCLE  
NO CYCLE  </dt>
<dd>Allows the sequence to wrap around when the \<maxvalue\> (for ascending) or \<minvalue\> (for descending) has been reached. If the limit is reached, the next number generated will be the \<minvalue\> (for ascending) or \<maxvalue\> (for descending). If `NO CYCLE` is specified, any calls to `nextval()` after the sequence has reached its maximum value will return an error. If not specified, `NO CYCLE` is the default.</dd>

<dt>OWNED BY \<table\>.\<column\>  
OWNED BY NONE  </dt>
<dd>Causes the sequence to be associated with a specific table column, such that if that column (or its whole table) is dropped, the sequence will be automatically dropped as well. If specified, this association replaces any previously specified assocation for the sequence. The specified table must have the same owner and be in the same schema as the sequence. `OWNED BY NONE` removes any existing association.</dd>

## <a id="topic1__section5"></a>Notes

`ALTER SEQUENCE` will not immediately affect `nextval()` results in backends, other than the current one, that have preallocated (cached) sequence values. They will use up all cached values prior to noticing the changed sequence generation parameters. The current backend will be affected immediately.

Some variants of `ALTER TABLE` can be used with sequences as well; for example, to rename a sequence use `ALTER TABLE RENAME`.

## <a id="topic1__section6"></a>Examples

Restart the sequence named `myseq`:

``` pre
ALTER SEQUENCE myseq RESTART WITH 111;
```

Change the increment value for the sequence named `myseq`:

``` pre
ALTER SEQUENCE myseq INCREMENT BY 3;
```

## <a id="topic1__section7"></a>Compatibility

`CREATE SEQUENCE` conforms to the SQL standard, with the exception that the `OWNED BY` clause is a HAWQ extension.

## <a id="topic1__section8"></a>See Also

[CREATE SEQUENCE](CREATE-SEQUENCE.html), [DROP SEQUENCE](DROP-SEQUENCE.html)
