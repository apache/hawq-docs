---
title: gplogfilter
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

Searches through HAWQ log files for specified entries.

## <a id="topic1__section2"></a>Synopsis

``` pre
gplogfilter [<timestamp_options>] [<pattern_matching_options>] 
     [<output_options>] [<input_options>]  

gplogfilter --help 

gplogfilter --version
```
where:

``` pre
<timestamp_options> =
     [-b <datetime> | --begin <datetime>]
     [-e <datetime> | --end <datetime>]
     [-d <time> | --duration <time>]

<pattern_matching_options> =
     [-c i[gnore] | r[espect] | --case i[gnore] | r[espect]]
     [-C '<string>'  | --columns '<string>']
     [-f '<string>' | --find '<string>']
     [-F '<string> | --nofind '<string>']
     [-m <regex> | --match <regex>]
     [-M <regex>] | --nomatch <regex>]
     [-t | --trouble]
     
<output_options> =
     [-n <integer> |  --tail <integer>]
     [-s <offset> [<limit>] | --slice <offset> [<limit>]]
     [-o <output_file> | --out <output_file>]   
     [-z <0..9> | --zip <0..9>]
     [-a | --append]
     
<input_options> =
     [<input_file> [-u | --unzip]]       
```


## <a id="topic1__section3"></a>Description

The `gplogfilter` utility can be used to search through a HAWQ log file for entries matching the specified criteria. To read from standard input, use a dash (`-`) as the input file name. Input files may be compressed using `gzip`. In an input file, a log entry is identified by its timestamp in `YYYY-MM-DD [hh:mm[:ss]]` format.

You can also use `gplogfilter` to search through all segment log files at once by running it through the [hawq ssh](hawqssh.html#topic1) utility. For example, to display the last three lines of each segment log file:

``` shell
$ hawq ssh -f seg_hostfile_hawqssh
=> source /usr/local/hawq/greenplum_path.sh
=> gplogfilter -n 3 /data/hawq-install-path/segmentdd/pg_log/hawq*.csv
```

By default, the output of `gplogfilter` is sent to standard output. Use the `-o` option to send the output to a file or a directory. If you supply an output file name ending in `.gz`, the output file will be compressed by default using maximum compression. If the output destination is a directory, the output file is given the same name as the input file.

## <a id="topic1__section4"></a>Options


**\<input_options\>**

<dt>\<input\_file\></dt>
<dd>The name of the input log file(s) to search through. To read from standard input, use a dash (`-`) as the input file name.</dd>

<dt>-u, -\\\-unzip  </dt>
<dd>Uncompress the input file using `gunzip`. If the input file name ends in `.gz`, it will be uncompressed by default.</dd>

**\<output_options\>**

<dt>-n, -\\\-tail \<integer\>  </dt>
<dd>Limits the output to the last \<integer\> of qualifying log entries found.</dd>

<dt>-s,  -\\\-slice \<offset\> \[\<limit\>\] </dt>
<dd>From the list of qualifying log entries, returns the \<limit\> number of entries starting at the \<offset\> entry number, where an \<offset\> of zero (`0`) denotes the first entry in the result set and an \<offset\> of any number greater than zero counts back from the end of the result set.</dd>

<dt>-o, -\\\-out \<output\_file\> </dt>
<dd>Writes the output to the specified file or directory location instead of `STDOUT`.</dd>

<dt>-z, -\\\-zip \<0..9\>  </dt>
<dd>Compresses the output file to the specified compression level using `gzip`, where `0` is no compression and `9` is maximum compression. If you supply an output file name ending in `.gz`, the output file will be compressed by default using maximum compression.</dd>

<dt>-a, -\\\-append  </dt>
<dd>If the output file already exists, appends to the file instead of overwriting it.</dd>


**\<pattern\_matching\_options\>**

<dt>-c, -\\\-case i\[gnore\] | r\[espect\]  </dt>
<dd>Matching of alphabetic characters is case sensitive by default unless proceeded by the `--case=ignore` option.</dd>

<dt>-C, -\\\-columns '\<string\>'  </dt>
<dd>Selects specific columns from the log file. Specify the desired columns as a comma-delimited string of column numbers beginning with 1, where the second column from left is 2, the third is 3, and so on.</dd>

<dt>-f, -\\\-find '\<string\>'  </dt>
<dd>Finds the log entries containing the specified string.</dd>

<dt>-F, -\\\-nofind '\<string\>'  </dt>
<dd>Rejects the log entries containing the specified string.</dd>

<dt>-m, -\\\-match \<regex\>  </dt>
<dd>Finds log entries that match the specified Python regular expression. See [http://docs.python.org/library/re.html](http://docs.python.org/library/re.html) for Python regular expression syntax.</dd>

<dt>-M, -\\\-nomatch \<regex\> </dt>
<dd>Rejects log entries that match the specified Python regular expression. See [http://docs.python.org/library/re.html](http://docs.python.org/library/re.html) for Python regular expression syntax.</dd>

<dt>-t, -\\\-trouble  </dt>
<dd>Finds only the log entries that have `ERROR:`, `FATAL:`, or `PANIC:` in the first line.</dd>

**\<timestamp_options\>**

<dt>-b, -\\\-begin \<datetime\>  </dt>
<dd>Specifies a starting date and time to begin searching for log entries in the format of `YYYY-MM-DD [hh:mm[:ss]]`.

If a time is specified, the date and time must be enclosed in either single or double quotes. This example encloses the date and time in single quotes:

``` shell
$ gplogfilter -b '2016-02-13 14:23'
```
</dd>

<dt>-e, -\\\-end \<datetime\>  </dt>
<dd>Specifies an ending date and time to stop searching for log entries in the format of `YYYY-MM-DD [hh:mm[:ss]]`.

If a time is specified, the date and time must be enclosed in either single or double quotes. This example encloses the date and time in single quotes:

``` shell
$ gplogfilter -e '2016-02-13 14:23' 
```
</dd>

<dt>-d, -\\\-duration \<time\>  </dt>
<dd>Specifies a time duration to search for log entries in the format of `[hh][:mm[:ss]]`. If used without either the `-b` or `-e` option, will use the current time as a basis.</dd>

**Other Options**

<dt>-\\\-help  </dt>
<dd>Displays the online help.</dd>

<dt>-\\\-version  </dt>
<dd>Displays the version of this utility.</dd>

## <a id="topic1__section9"></a>Examples

Display the last three error messages in the identified log file:

``` shell
$ gplogfilter -t -n 3 "/data/hawq/master/pg_log/hawq-2016-09-01_134934.csv"
```

Display the last five error messages in a date-specified log file:

``` shell
$ gplogfilter -t -n 5 "/data/hawq-file-path/hawq-yyyy-mm-dd*.csv"
```

Display all log messages in the date-specified log file timestamped in the last 10 minutes:

``` shell
$ gplogfilter -d :10 "/data/hawq-file-path/hawq-yyyy-mm-dd*.csv"
```

Display log messages in the identified log file containing the string `|con6 cmd11|`:

``` shell
$ gplogfilter -f '|con6 cmd11|' "/data/hawq/master/pg_log/hawq-2016-09-01_134934.csv"
```

Using [hawq ssh](hawqssh.html#topic1), run `gplogfilter` on the segment hosts and search for log messages in the segment log files containing the string `con6` and save output to a file.

``` shell
$ hawq ssh -f /data/hawq-2.x/segmentdd/pg_hba.conf -e 'source /usr/local/hawq/greenplum_path.sh ; 
gplogfilter -f con6 /data/hawq-2.x/pg_log/hawq*.csv' > seglog.out
```

## <a id="topic1__section10"></a>See Also

[hawq ssh](hawqssh.html#topic1)
