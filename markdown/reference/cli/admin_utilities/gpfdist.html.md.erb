---
title: gpfdist
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

Serves data files to or writes data files out from HAWQ segments.

## <a id="topic1__section2"></a>Synopsis

``` pre
gpfdist [-d <directory>] [-p <http_port>] [-l <log_file>] [-t <timeout>] 
   [-S] [-w <time>] [-v | -V] [-s] [-m <max_length>] [--ssl <certificate_path>]

gpfdist -? | --help 

gpfdist --version
```

## <a id="topic1__section3"></a>Description

`gpfdist` is HAWQ parallel file distribution program. It is used by readable external tables and `hawq load` to serve external table files to all HAWQ segments in parallel. It is used by writable external tables to accept output streams from HAWQ segments in parallel and write them out to a file.

In order for `gpfdist` to be used by an external table, the `LOCATION` clause of the external table definition must specify the external table data using the `gpfdist://` protocol (see the HAWQ command `CREATE EXTERNAL TABLE`).

**Note:** If the `--ssl` option is specified to enable SSL security, create the external table with the `gpfdists://` protocol.

The benefit of using `gpfdist` is that you are guaranteed maximum parallelism while reading from or writing to external tables, thereby offering the best performance as well as easier administration of external tables.

For readable external tables, `gpfdist` parses and serves data files evenly to all the segment instances in the HAWQ system when users `SELECT` from the external table. For writable external tables, `gpfdist` accepts parallel output streams from the segments when users `INSERT` into the external table, and writes to an output file.

For readable external tables, if load files are compressed using `gzip` or `bzip2` (have a `.gz` or `.bz2` file extension), `gpfdist` uncompresses the files automatically before loading provided that `gunzip` or `bunzip2` is in your path.

**Note:** Currently, readable external tables do not support compression on Windows platforms, and writable external tables do not support compression on any platforms.

To run `gpfdist` on your ETL machines, refer to [Client-Based HAWQ Load Tools](../../../datamgmt/load/client-loadtools.html) for more information.

**Note:** When using IPv6, always enclose the numeric IP address in brackets.

You can also run `gpfdist` as a Windows Service. See [Running gpfdist as a Windows Service](#topic1__section5) for more details.

## <a id="topic1__section4"></a>Options

<dt>-d \<directory\>  </dt>
<dd>The directory from which `gpfdist` will serve files for readable external tables or create output files for writable external tables. If not specified, defaults to the current directory.</dd>

<dt>-l \<log\_file\>  </dt>
<dd>The fully qualified path and log file name where standard output messages are to be logged.</dd>

<dt>-p \<http\_port\>  </dt>
<dd>The HTTP port on which `gpfdist` will serve files. Defaults to 8080.</dd>

<dt>-t \<timeout\>  </dt>
<dd>Sets the time allowed for HAWQ to establish a connection to a `gpfdist` process. Default is 5 seconds. Allowed values are 2 to 600 seconds. May need to be increased on systems with a lot of network traffic.</dd>

<dt>-m \<max\_length\>  </dt>
<dd>Sets the maximum allowed data row length in bytes. Default is 32768. Should be used when user data includes very wide rows (or when `line too long` error message occurs). Should not be used otherwise as it increases resource allocation. Valid range is 32K to 256MB. (The upper limit is 1MB on Windows systems.)</dd>

<dt>-s  </dt>
<dd>Enables simplified logging. When this option is specified, only messages with `WARN` level and higher are written to the `gpfdist` log file. `INFO` level messages are not written to the log file. If this option is not specified, all `gpfdist` messages are written to the log file.

You can specify this option to reduce the information written to the log file.</dd>

<dt>-S (use O\_SYNC)  </dt>
<dd>Opens the file for synchronous I/O with the `O_SYNC` flag. Any writes to the resulting file descriptor block `gpfdist` until the data is physically written to the underlying hardware.</dd>

<dt>-w \<time\>  </dt>
<dd>Sets the number of seconds that HAWQ delays before closing a target file such as a named pipe. The default value is 0, no delay. The maximum value is 600 seconds, 10 minutes.

For a HAWQ with multiple segments, there might be a delay between segments when writing data from different segments to the file. You can specify a time to wait before HAWQ closes the file to ensure all the data is written to the file.</dd>

<dt>-\\\-ssl \<certificate\_path\>  </dt>
<dd>Adds SSL encryption to data transferred with `gpfdist`. After executing `gpfdist` with the `--ssl <certificate_path>` option, the only way to load data from this file server is with the `gpfdist://` protocol.

The location specified in \<certificate\_path\> must contain the following files:

-   The server certificate file, `server.crt`
-   The server private key file, `server.key`
-   The trusted certificate authorities, `root.crt`

The root directory (`/`) cannot be specified as \<certificate\_path\>.</dd>

<dt>-v (verbose)  </dt>
<dd>Verbose mode shows progress and status messages.</dd>

<dt>-V (very verbose)  </dt>
<dd>Verbose mode shows all output messages generated by this utility.</dd>

<dt>-? (help)  </dt>
<dd>Displays the online help.</dd>

<dt>-\\\-version  </dt>
<dd>Displays the version of this utility.</dd>

## <a id="topic1__section5"></a>Running gpfdist as a Windows Service

HAWQ Loaders allow `gpfdist` to run as a Windows Service.

Follow the instructions below to download, register and activate `gpfdist` as a service:

1.  Update your HAWQ Loaders for Windows package to the latest version. See [HAWQ Loader Tools for Windows](../../../datamgmt/load/client-loadtools.html#installloadrunwin) for install and configuration information.
    
2.  Register `gpfdist` as a Windows service:
    1.  Open a Windows command window
    2.  Run the following command:

        ``` pre
        sc create gpfdist binpath= "<loader_install_dir>\bin\gpfdist.exe -p 8081 -d \"<external_load_files_path>\" -l \"<log_file_path>\""
        ```

        You can create multiple instances of `gpfdist` by running the same command again, with a unique name and port number for each instance:

        ``` pre
        sc create gpfdistN binpath= "<loader_install_dir>\bin\gpfdist.exe -p 8082 -d \"<external_load_files_path>\" -l \"<log_file_path>\""
        ```

3.  Activate the `gpfdist` service:
    1.  Open the Windows Control Panel and select **Administrative Tools &gt; Services**.
    2.  Highlight then right-click on the `gpfdist` service in the list of services.
    3.  Select **Properties** from the right-click menu, the Service Properties window opens.

        Note that you can also stop this service from the Service Properties window.

    4.  Optional: Change the **Startup Type** to **Automatic** (after a system restart, this service will be running), then under **Service** status, click **Start**.
    5.  Click **OK**.

Repeat the above steps for each instance of `gpfdist` that you created.

## <a id="topic1__section6"></a>Examples

To serve files from a specified directory using port 8081 (and start `gpfdist` in the background):

``` shell
$ gpfdist -d /var/load_files -p 8081 &
```

To start `gpfdist` in the background and redirect output and errors to a log file:

``` shell
$ gpfdist -d /var/load_files -p 8081 -l /home/gpadmin/log &
```

To stop `gpfdist` when it is running in the background:

--First find its process id:

``` shell
$ ps ax | grep gpfdist
```

--Then kill the process, for example:

``` shell
$ kill 3456
```

## <a id="topic1__section7"></a>See Also

[hawq load](hawqload.html#topic1), [CREATE EXTERNAL TABLE](../../sql/CREATE-EXTERNAL-TABLE.html)
