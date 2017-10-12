---
title: HAWQ packcore utility
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

## <a id="core_file_definition"></a>Core file

A core file is a disk file that records the memory image of a running process in the event the process crashes or terminates abruptly. The information in this image is useful for debugging the state of a process at the time when it was terminated.

## <a id="packcore_definition"></a>Packcore

The packcore utility helps pack a core file with its context, including the executable, application, and shared system libraries from the current environment. This information can be unpacked for later debugging on a different system. Packcore extracts the name of the binary that generated the core from the core file, then executes ldd (List Dynamic Dependencies) to create a single tar archive containing the core file information.

### <a id="using_packcore"></a>Using packcore 

The packcore utility is located under `${GPHOME}/sbin`. Run one of the following commands to pack a core file:

```shell
$ $GPHOME/sbin/packcore <core_file>
```

or

```shell
$ $GPHOME/sbin/packcore -b|--binary  $GPHOME/bin/postgres <core_file>
```

Alternatively, you can navigate to `$GPHOME/sbin` and run the following:

```shell
$ ./packcore <core_file>
```

or 

```shell
$ ./packcore -b|--binary $GPHOME/bin/postgres <core_file>
```
When processing is completed, the utility creates a tar file in the format: packcore-<core_file>.tgz. Unpack this file on another system to use it for debugging.
