---
title: Using PL/Python in HAWQ
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

This section provides an overview of the HAWQ PL/Python procedural language extension.

## <a id="abouthawqplpython"></a>About HAWQ PL/Python 

PL/Python is embedded in your HAWQ product distribution or within your HAWQ build if you chose to enable it as a build option. 

With the HAWQ PL/Python extension, you can write user-defined functions in Python that take advantage of Python features and modules, enabling you to quickly build robust HAWQ database applications.

HAWQ uses the system Python installation.

### <a id="hawqlimitations"></a>HAWQ PL/Python Limitations 

- HAWQ does not support PL/Python trigger functions.
- PL/Python is available only as a HAWQ untrusted language.
 
## <a id="enableplpython"></a>Enabling and Removing PL/Python Support 

To use PL/Python in HAWQ, you must either install a binary version of HAWQ that includes PL/Python or specify PL/Python as a build option when you compile HAWQ from source.

You must register the PL/Python language with a database before you can create and execute a PL/Python UDF on that database. You must be a database superuser to register and remove new languages in HAWQ databases.

On every database to which you want to install and enable PL/Python:

1. Connect to the database using the `psql` client:

    ``` shell
    gpadmin@hawq-node$ psql -d <dbname>
    ```

    Replace \<dbname\> with the name of the target database.

2. Run the following SQL command to register the PL/Python procedural language:

    ``` sql
    dbname=# CREATE LANGUAGE plpythonu;
    ```

    **Note**: `plpythonu` is installed as an *untrusted* language; it offers no way of restricting what you can program in UDFs created with the language. Creating and executing PL/Python UDFs is permitted only by database superusers and other database users explicitly `GRANT`ed the permissions.

To remove support for `plpythonu` from a database, run the following SQL command; you must be a database superuser to remove a registered procedural language:

``` sql
dbname=# DROP LANGUAGE plpythonu;
```

## <a id="developfunctions"></a>Developing Functions with PL/Python 

PL/Python functions are defined using the standard SQL [CREATE FUNCTION](../reference/sql/CREATE-FUNCTION.html) syntax.

The body of a PL/Python user-defined function is a Python script. When the function is called, its arguments are passed as elements of the array `args[]`. You can also pass named arguments as ordinary variables to the Python script. 

PL/Python function results are returned with a `return` statement, or a `yield` statement in the case of a result-set statement.

The following PL/Python function computes and returns the maximum of two integers:

``` sql
=# CREATE FUNCTION mypymax (a integer, b integer)
     RETURNS integer
   AS $$
     if (a is None) or (b is None):
       return None
     if a > b:
       return a
     return b
   $$ LANGUAGE plpythonu;
```

To execute the `mypymax` function:

``` sql
=# SELECT mypymax(5, 7);
 mypymax 
---------
       7
(1 row)
```

Adding the `STRICT` keyword to the `LANGUAGE` subclause instructs HAWQ to return null when any of the input arguments are null. When created as `STRICT`, the function itself need not perform null checks.

The following example uses an unnamed argument, the built-in Python `max()` function, and the `STRICT` keyword to create a UDF named `mypymax2`:

``` sql
=# CREATE FUNCTION mypymax2 (a integer, integer)
     RETURNS integer AS $$ 
   return max(a, args[0]) 
   $$ LANGUAGE plpythonu STRICT;
=# SELECT mypymax(5, 3);
 mypymax2
----------
        5
(1 row)
=# SELECT mypymax(5, null);
 mypymax2
----------
       
(1 row)
```

## <a id="example_createtbl"></a>Creating the Sample Data

Perform the following steps to create, and insert data into, a simple table. This table will be used in later exercises.

1. Create a database named `testdb`:

    ``` shell
    gpadmin@hawq-node$ createdb testdb
    ```

1. Create a table named `sales`:

    ``` shell
    gpadmin@hawq-node$ psql -d testdb
    ```
    ``` sql
    testdb=> CREATE TABLE sales (id int, year int, qtr int, day int, region text)
               DISTRIBUTED BY (id);
    ```

2. Insert data into the table:

    ``` sql
    testdb=> INSERT INTO sales VALUES
     (1, 2014, 1,1, 'usa'),
     (2, 2002, 2,2, 'europe'),
     (3, 2014, 3,3, 'asia'),
     (4, 2014, 4,4, 'usa'),
     (5, 2014, 1,5, 'europe'),
     (6, 2014, 2,6, 'asia'),
     (7, 2002, 3,7, 'usa') ;
    ```

## <a id="pymod_intro"></a>Python Modules 
A Python module is a text file containing Python statements and definitions. Python modules are named, with the file name for a module following the `<python-module-name>.py` naming convention.

Should you need to build a Python module, ensure that the appropriate software is installed on the build system. Also be sure that you are building for the correct deployment architecture, i.e. 64-bit.

### <a id="pymod_intro_hawq"></a>HAWQ Considerations 

When installing a Python module in HAWQ, you must add the module to all segment nodes in the cluster. You must also add all Python modules to any new segment hosts when you expand your HAWQ cluster.

PL/Python supports the built-in HAWQ Python module named `plpy`.  You can also install 3rd party Python modules.


## <a id="modules_plpy"></a>plpy Module 

The HAWQ PL/Python procedural language extension automatically imports the Python module `plpy`. `plpy` implements functions to execute SQL queries and prepare execution plans for queries.  The `plpy` module also includes functions to manage errors and messages.
   
### <a id="executepreparesql"></a>Executing and Preparing SQL Queries 

Use the PL/Python `plpy` module `plpy.execute()` function to execute a SQL query. Use the `plpy.prepare()` function to prepare an execution plan for a query. Preparing the execution plan for a query is useful if you want to run the query from multiple Python functions.

#### <a id="plpyexecute"></a>plpy.execute() 

Invoking `plpy.execute()` with a query string and an optional limit argument runs the query, returning the result in a Python result object. This result object:

- emulates a list or dictionary object
- returns rows that can be accessed by row number and column name; row numbering starts with 0 (zero)
- can be modified
- includes an `nrows()` method that returns the number of rows returned by the query
- includes a `status()` method that returns the `SPI_execute()` return value

For example, the following Python statement when present in a PL/Python user-defined function will execute a `SELECT * FROM mytable` query:

``` python
rv = plpy.execute("SELECT * FROM my_table", 3)
```

As instructed by the limit argument `3`, the `plpy.execute` function will return up to 3 rows from `my_table`. The result set is stored in the `rv` object.

Access specific columns in the table by name. For example, if `my_table` has a column named `my_column`:

``` python
my_col_data = rv[i]["my_column"]
```

You specified that the function return a maximum of 3 rows in the `plpy.execute()` command above. As such, the index `i` used to access the result value `rv` must specify an integer between 0 and 2, inclusive.

##### <a id="plpyexecute_example"></a>Example: plpy.execute()

Example: Use `plpy.execute()` to run a similar query on the `sales` table you created in an earlier section:

1. Define a PL/Python UDF that executes a query to return at most 5 rows from the `sales` table:

    ``` sql
    =# CREATE OR REPLACE FUNCTION mypytest(a integer) 
         RETURNS text 
       AS $$ 
         rv = plpy.execute("SELECT * FROM sales ORDER BY id", 5)
         region = rv[a-1]["region"]
         return region
       $$ LANGUAGE plpythonu;
    ```

    When executed, this UDF returns the `region` value from the `id` identified by the input value `a`. Since row numbering of the result set starts at 0, you must access the result set with index `a - 1`. 
    
    Specifying the `ORDER BY id` clause in the `SELECT` statement ensures that subsequent invocations of `mypytest` with the same input argument will return identical result sets.

3. Run `mypytest` with an argument identifying `id` `3`:

    ```sql
    =# SELECT mypytest(3);
     mypytest 
    ----------
     asia
    (1 row)
    ```
    
    Recall that the row numbering starts from 0 in a Python returned result set. The valid input argument for the `mypytest2` function is an integer between 0 and 4, inclusive.

    The query returns the `region` from the row with `id = 3`, `asia`.
    
Note: This example demonstrates some of the concepts discussed previously. It may not be the ideal way to return a specific column value.

#### <a id="plpyprepare"></a>plpy.prepare() 

The function `plpy.prepare()` prepares the execution plan for a query. Preparing the execution plan for a query is useful if you plan to run the query from multiple Python functions.

You invoke `plpy.prepare()` with a query string. Also include a list of parameter types if you are using parameter references in the query. For example, the following statement in a PL/Python user-defined function returns the execution plan for a query:

``` python
plan = plpy.prepare("SELECT * FROM sales ORDER BY id WHERE 
  region = $1", [ "text" ])
```

The string `text` identifies the data type of the variable `$1`. 

After preparing an execution plan, you use the function `plpy.execute()` to run it.  For example:

``` python
rv = plpy.execute(plan, [ "usa" ])
```

When executed, `rv` will include all rows in the `sales` table where `region = usa`.

Read on for a description of how one passes data between PL/Python function calls.

##### <a id="plpyprepare_dictionaries"></a>Saving Execution Plans

When you prepare an execution plan using the PL/Python module, the plan is automatically saved. See the [Postgres Server Programming Interface (SPI)](http://www.postgresql.org/docs/8.2/static/spi.html) documentation for information about execution plans.

To make effective use of saved plans across function calls, you use one of the Python persistent storage dictionaries, SD or GD.

The global dictionary SD is available to store data between function calls. This variable is private static data. The global dictionary GD is public data, and is available to all Python functions within a session. *Use GD with care*.

Each function gets its own execution environment in the Python interpreter, so that global data and function arguments from `myfunc1` are not available to `myfunc2`. The exception is the data in the GD dictionary, as mentioned previously.

This example saves an execution plan to the SD dictionary and then executes the plan:

```sql
=# CREATE FUNCTION usesavedplan() RETURNS text AS $$
     select1plan = plpy.prepare("SELECT region FROM sales WHERE id=1")
     SD["s1plan"] = select1plan
     # other function processing
     # execute the saved plan
     rv = plpy.execute(SD["s1plan"])
     return rv[0]["region"]
   $$ LANGUAGE plpythonu;
=# SELECT usesavedplan();
```

##### <a id="plpyprepare_example"></a>Example: plpy.prepare()

Example: Use `plpy.prepare()` and `plpy.execute()` to prepare and run an execution plan using the GD dictionary:

1. Define a PL/Python UDF to prepare and save an execution plan to the GD. Also  return the name of the plan:

    ``` sql
    =# CREATE OR REPLACE FUNCTION mypy_prepplan() 
         RETURNS text 
       AS $$ 
         plan = plpy.prepare("SELECT * FROM sales WHERE region = $1 ORDER BY id", [ "text" ])
         GD["getregionplan"] = plan
         return "getregionplan"
       $$ LANGUAGE plpythonu;
    ```

    This UDF, when run, will return the name (key) of the execution plan generated from the `plpy.prepare()` call.

1. Define a PL/Python UDF to run the execution plan; this function will take the plan name and `region` name as an input:

    ``` sql
    =# CREATE OR REPLACE FUNCTION mypy_execplan(planname text, regionname text)
         RETURNS integer 
       AS $$ 
         rv = plpy.execute(GD[planname], [ regionname ], 5)
         year = rv[0]["year"]
         return year
       $$ LANGUAGE plpythonu STRICT;
    ```

    This UDF executes the `planname` plan that was previously saved to the GD. You will call `mypy_execplan()` with the `planname` returned from the `plpy.prepare()` call.

3. Execute the `mypy_prepplan()` and `mypy_execplan()` UDFs, passing `region` `usa`:

    ``` sql
    =# SELECT mypy_execplan( mypy_prepplan(), 'usa' );
     mypy_execplan
    ---------------
         2014
    (1 row)
    ```

### <a id="pythonerrors"></a>Handling Python Errors and Messages 

The `plpy` module implements the following message- and error-related functions, each of which takes a message string as an argument:

- `plpy.debug(msg)`
- `plpy.log(msg)`
- `plpy.info(msg)`
- `plpy.notice(msg)`
- `plpy.warning(msg)`
- `plpy.error(msg)`
- `plpy.fatal(msg)`

`plpy.error()` and `plpy.fatal()` raise a Python exception which, if uncaught, propagates out to the calling query, possibly aborting the current transaction or subtransaction. `raise plpy.ERROR(msg)` and `raise plpy.FATAL(msg)` are equivalent to calling `plpy.error()` and `plpy.fatal()`, respectively. Use the other message functions to generate messages of different priority levels.

Messages may be reported to the client and/or written to the HAWQ server log file.  The HAWQ server configuration parameters [`log_min_messages`](../reference/guc/parameter_definitions.html#log_min_messages) and [`client_min_messages`](../reference/guc/parameter_definitions.html#client_min_messages) control where messages are reported.

#### <a id="plpymessages_example"></a>Example: Generating Messages

In this example, you will create a PL/Python UDF that includes some debug log messages. You will also configure your `psql` session to enable debug-level client logging.

1. Define a PL/Python UDF that executes a query that will return at most 5 rows from the `sales` table. Invoke the `plpy.debug()` method to display some additional information:

    ``` sql
    =# CREATE OR REPLACE FUNCTION mypytest_debug(a integer) 
         RETURNS text 
       AS $$ 
         plpy.debug('mypytest_debug executing query:  SELECT * FROM sales ORDER BY id')
         rv = plpy.execute("SELECT * FROM sales ORDER BY id", 5)
         plpy.debug('mypytest_debug: query returned ' + str(rv.nrows()) + ' rows')
         region = rv[a]["region"]
         return region
       $$ LANGUAGE plpythonu;
    ```

2. Execute the `mypytest_debug()` UDF, passing the integer `2` as an argument:

    ```sql
    =# SELECT mypytest_debug(2);
     mypytest_debug 
    ----------------
     asia
    (1 row)
    ```

3. Enable `DEBUG2` level client logging:

    ``` sql
    =# SET client_min_messages=DEBUG2;
    ```
    
2. Execute the `mypytest_debug()` UDF again:

    ```sql
    =# SELECT mypytest_debug(2);
    ...
    DEBUG2:  mypytest_debug executing query:  SELECT * FROM sales ORDER BY id
    ...
    DEBUG2:  mypytest_debug: query returned 5 rows
    ...
    ```

    Debug output is very verbose. You will parse a lot of output to find the `mypytest_debug` messages. *Hint*: look both near the start and end of the output.
    
6. Turn off client-level debug logging:

    ```sql
    =# SET client_min_messages=NOTICE;
    ```

## <a id="pythonmodules-3rdparty"></a>3rd-Party Python Modules 

PL/Python supports installation and use of 3rd-party Python Modules. This section includes examples for installing the `setuptools` and NumPy Python modules.

**Note**: You must have superuser privileges to install Python modules to the system Python directories.

### <a id="simpleinstall"></a>Example: Installing setuptools 

In this example, you will manually install the Python `setuptools` module from the Python Package Index repository. `setuptools` enables you to easily download, build, install, upgrade, and uninstall Python packages.

You will first build the module from the downloaded package, installing it on a single host. You will then build and install the module on all segment nodes in your HAWQ cluster.

1. Download the `setuptools` module package from the Python Package Index site. For example, run this `wget` command on a HAWQ node as the `gpadmin` user:

    ``` shell
    $ ssh gpadmin@<hawq-node>
    gpadmin@hawq-node$ . /usr/local/hawq/greenplum_path.sh
    gpadmin@hawq-node$ mkdir plpython_pkgs
    gpadmin@hawq-node$ cd plpython_pkgs
    gpadmin@hawq-node$ export PLPYPKGDIR=`pwd`
    gpadmin@hawq-node$ wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-18.4.tar.gz
    ```

2. Extract the files from the `tar.gz` package:

    ``` shell
    gpadmin@hawq-node$ tar -xzvf setuptools-18.4.tar.gz
    ```

3. Run the Python scripts to build and install the Python package; you must have superuser privileges to install Python modules to the system Python installation:

    ``` shell
    gpadmin@hawq-node$ cd setuptools-18.4
    gpadmin@hawq-node$ python setup.py build 
    gpadmin@hawq-node$ sudo python setup.py install
    ```

4. Run the following command to verify the module is available to Python:

    ``` shell
    gpadmin@hawq-node$ python -c "import setuptools"
    ```
    
    If no error is returned, the `setuptools` module was successfully imported.

5. The `setuptools` package installs the `easy_install` utility. This utility enables you to install Python packages from the Python Package Index repository. For example, this command installs the Python `pip` utility from the Python Package Index site:

    ``` shell
    gpadmin@hawq-node$ sudo easy_install pip
    ```

5. Copy the `setuptools` package to all HAWQ nodes in your cluster. For example, this command copies the `tar.gz` file from the current host to the host systems listed in the file `hawq-hosts`:

    ``` shell
    gpadmin@hawq-node$ cd $PLPYPKGDIR
    gpadmin@hawq-node$ hawq scp -f hawq-hosts setuptools-18.4.tar.gz =:/home/gpadmin
    ```

6. Run the commands to build, install, and test the `setuptools` package you just copied to all hosts in your HAWQ cluster. For example:

    ``` shell
    gpadmin@hawq-node$ hawq ssh -f hawq-hosts
    >>> mkdir plpython_pkgs
    >>> cd plpython_pkgs
    >>> tar -xzvf ../setuptools-18.4.tar.gz
    >>> cd setuptools-18.4
    >>> python setup.py build 
    >>> sudo python setup.py install
    >>> python -c "import setuptools"
    >>> exit
    ```

### <a id="complexinstall"></a>Example: Installing NumPy 

In this example, you will build and install the Python module NumPy. NumPy is a module for scientific computing with Python. For additional information about NumPy, refer to [http://www.numpy.org/](http://www.numpy.org/).

This example assumes `yum` is installed on all HAWQ segment nodes and that the `gpadmin` user is a member of `sudoers` with `root` privileges on the nodes.

#### <a id="complexinstall_prereq"></a>Prerequisites
Building the NumPy package requires the following software:

- OpenBLAS libraries - an open source implementation of BLAS (Basic Linear Algebra Subprograms)
- Python development packages - python-devel
- gcc compilers - gcc, gcc-gfortran, and gcc-c++

Perform the following steps to set up the OpenBLAS compilation environment on each HAWQ node:

1. Use `yum` to install gcc compilers from system repositories. The compilers are required on all hosts where you compile OpenBLAS.  For example:

	``` shell
	root@hawq-node$ yum -y install gcc gcc-gfortran gcc-c++ python-devel
	```

2. (Optionally required) If you cannot install the correct compiler versions with `yum`, you have the option to download the gcc compilers, including `gfortran`, from source and build and install them manually. Refer to [Building gfortran from Source](https://gcc.gnu.org/wiki/GFortranBinaries#FromSource) for `gfortran` build and install information.

2. Create a symbolic link to `g++`, naming it `gxx`:

	``` bash
	root@hawq-node$ ln -s /usr/bin/g++ /usr/bin/gxx
	```

3. You may also need to create symbolic links to any libraries that have different versions available; for example, linking `libppl_c.so.4` to `libppl_c.so.2`.

4. You can use the `hawq scp` utility to copy files to HAWQ hosts and the `hawq ssh` utility to run commands on those hosts.


#### <a id="complexinstall_downdist"></a>Obtaining Packages

Perform the following steps to download and distribute the OpenBLAS and NumPy source packages:

1. Download the OpenBLAS and NumPy source files. For example, these `wget` commands download `tar.gz` files into a `packages` directory in the current working directory:

    ``` shell
    $ ssh gpadmin@<hawq-node>
    gpadmin@hawq-node$ wget --directory-prefix=packages http://github.com/xianyi/OpenBLAS/tarball/v0.2.8
    gpadmin@hawq-node$ wget --directory-prefix=packages http://sourceforge.net/projects/numpy/files/NumPy/1.8.0/numpy-1.8.0.tar.gz/download
    ```

2. Distribute the software to all nodes in your HAWQ cluster. For example, if you downloaded the software to `/home/gpadmin/packages`, these commands create the `packages` directory on all nodes and copies the software to the nodes listed in the `hawq-hosts` file:

    ``` shell
    gpadmin@hawq-node$ hawq ssh -f hawq-hosts mkdir packages 
    gpadmin@hawq-node$ hawq scp -f hawq-hosts packages/* =:/home/gpadmin/packages
    ```

#### <a id="buildopenblas"></a>Build and Install OpenBLAS Libraries 

Before building and installing the NumPy module, you must first build and install the OpenBLAS libraries. This section describes how to build and install the libraries on a single HAWQ node.

1. Extract the OpenBLAS files from the file:

	``` shell
	$ ssh gpadmin@<hawq-node>
	gpadmin@hawq-node$ cd packages
	gpadmin@hawq-node$ tar xzf v0.2.8 -C /home/gpadmin/packages
	gpadmin@hawq-node$ mv /home/gpadmin/packages/xianyi-OpenBLAS-9c51cdf /home/gpadmin/packages/OpenBLAS
	```
	
	These commands extract the OpenBLAS tar file and simplify the unpacked directory name.

2. Compile OpenBLAS. You must set the `LIBRARY_PATH` environment variable to the current `$LD_LIBRARY_PATH`. For example:

	``` shell
	gpadmin@hawq-node$ cd OpenBLAS
	gpadmin@hawq-node$ export LIBRARY_PATH=$LD_LIBRARY_PATH
	gpadmin@hawq-node$ make FC=gfortran USE_THREAD=0 TARGET=SANDYBRIDGE
	```
	
	Replace the `TARGET` argument with the target appropriate for your hardware. The `TargetList.txt` file identifies the list of supported OpenBLAS targets.
	
	Compiling OpenBLAS make take some time.

3. Install the OpenBLAS libraries in `/usr/local` and then change the owner of the files to `gpadmin`. You must have `root` privileges. For example:

	``` shell
	gpadmin@hawq-node$ sudo make PREFIX=/usr/local install
	gpadmin@hawq-node$ sudo ldconfig
	gpadmin@hawq-node$ sudo chown -R gpadmin /usr/local/lib
	```

	The following libraries are installed to `/usr/local/lib`, along with symbolic links:

	``` shell
	gpadmin@hawq-node$ ls -l gpadmin@hawq-node$
	    ...
	    libopenblas.a -> libopenblas_sandybridge-r0.2.8.a
	    libopenblas_sandybridge-r0.2.8.a
	    libopenblas_sandybridge-r0.2.8.so
	    libopenblas.so -> libopenblas_sandybridge-r0.2.8.so
	    libopenblas.so.0 -> libopenblas_sandybridge-r0.2.8.so
	    ...
	```

4. Install the OpenBLAS libraries on all nodes in your HAWQ cluster. You can use the `hawq ssh` utility to similarly build and install the OpenBLAS libraries on each of the nodes. 

    Or, you may choose to copy the OpenBLAS libraries you just built to all of the HAWQ cluster nodes. For example, these `hawq ssh` and `hawq scp` commands install prerequisite packages, and copy and install the OpenBLAS libraries on the hosts listed in the `hawq-hosts` file.

    ``` shell
    $ hawq ssh -f hawq-hosts -e 'sudo yum -y install gcc gcc-gfortran gcc-c++ python-devel'
    $ hawq ssh -f hawq-hosts -e 'ln -s /usr/bin/g++ /usr/bin/gxx'
    $ hawq ssh -f hawq-hosts -e sudo chown gpadmin /usr/local/lib
    $ hawq scp -f hawq-hosts /usr/local/lib/libopen*sandy* =:/usr/local/lib
    ```
    ``` shell
    $ hawq ssh -f hawq-hosts
    >>> cd /usr/local/lib
    >>> ln -s libopenblas_sandybridge-r0.2.8.a libopenblas.a
    >>> ln -s libopenblas_sandybridge-r0.2.8.so libopenblas.so
    >>> ln -s libopenblas_sandybridge-r0.2.8.so libopenblas.so.0
    >>> sudo ldconfig
   ```

#### Build and Install NumPy <a name="buildinstallnumpy"></a>

After you have installed the OpenBLAS libraries, you can build and install NumPy module. These steps install the NumPy module on a single host. You can use the `hawq ssh` utility to build and install the NumPy module on multiple hosts.

1. Extract the NumPy module source files:

	``` shell
	gpadmin@hawq-node$ cd /home/gpadmin/packages
	gpadmin@hawq-node$ tar xzf numpy-1.8.0.tar.gz
	```
	
	Unpacking the `numpy-1.8.0.tar.gz` file creates a directory named `numpy-1.8.0` in the current directory.

2. Set up the environment for building and installing NumPy:

	``` shell
	gpadmin@hawq-node$ export BLAS=/usr/local/lib/libopenblas.a
	gpadmin@hawq-node$ export LAPACK=/usr/local/lib/libopenblas.a
	gpadmin@hawq-node$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib/
	gpadmin@hawq-node$ export LIBRARY_PATH=$LD_LIBRARY_PATH
	```

3. Build and install NumPy. (Building the NumPy package might take some time.)

	``` shell
	gpadmin@hawq-node$ cd numpy-1.8.0
	gpadmin@hawq-node$ python setup.py build
	gpadmin@hawq-node$ sudo python setup.py install
	```

	**Note:** If the NumPy module did not successfully build, the NumPy build process might need a `site.cfg` file that specifies the location of the OpenBLAS libraries. Create the `site.cfg` file in the NumPy package directory:

	``` shell
	gpadmin@hawq-node$ touch site.cfg
	```

	Add the following to the `site.cfg` file and run the NumPy build command again:

	``` pre
	[default]
	library_dirs = /usr/local/lib

	[atlas]
	atlas_libs = openblas
	library_dirs = /usr/local/lib

	[lapack]
	lapack_libs = openblas
	library_dirs = /usr/local/lib

	# added for scikit-learn 
	[openblas]
	libraries = openblas
	library_dirs = /usr/local/lib
	include_dirs = /usr/local/include
	```

4. Verify that the NumPy module is available for import by Python:

	``` shell
	gpadmin@hawq-node$ cd $HOME
	gpadmin@hawq-node$ python -c "import numpy"
	```
	
	If no error is returned, the NumPy module was successfully imported.

5. As performed in the `setuptools` Python module installation, use the `hawq ssh` utility to build, install, and test the NumPy module on all HAWQ nodes.

5. The environment variables that were required to build the NumPy module are also required in the `gpadmin` runtime environment to run Python NumPy functions. You can use the `echo` command to add the environment variables to `gpadmin`'s `.bashrc` file. For example, the following `echo` commands add the environment variables to the `.bashrc` file in `gpadmin`'s home directory:

	``` shell
	$ echo -e '\n#Needed for NumPy' >> ~/.bashrc
	$ echo -e 'export BLAS=/usr/local/lib/libopenblas.a' >> ~/.bashrc
	$ echo -e 'export LAPACK=/usr/local/lib/libopenblas.a' >> ~/.bashrc
	$ echo -e 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib' >> ~/.bashrc
	$ echo -e 'export LIBRARY_PATH=$LD_LIBRARY_PATH' >> ~/.bashrc
	```

    You can use the `hawq ssh` utility with these `echo` commands to add the environment variables to the `.bashrc` file on all nodes in your HAWQ cluster.

### <a id="testingpythonmodules"></a>Testing Installed Python Modules 

You can create a simple PL/Python user-defined function (UDF) to validate that a Python module is available in HAWQ. This example tests the NumPy module.

1. Create a PL/Python UDF that imports the NumPy module:

    ``` shell
    gpadmin@hawq_node$ psql -d testdb
    ```
    ``` sql
    =# CREATE OR REPLACE FUNCTION test_importnumpy(x int)
       RETURNS text
       AS $$
         try:
             from numpy import *
             return 'SUCCESS'
         except ImportError, e:
             return 'FAILURE'
       $$ LANGUAGE plpythonu;
    ```

    The function returns SUCCESS if the module is imported, and FAILURE if an import error occurs.

2. Create a table that loads data on each HAWQ segment instance:

    ``` sql
    => CREATE TABLE disttbl AS (SELECT x FROM generate_series(1,50) x ) DISTRIBUTED BY (x);
    ```
    
    Depending upon the size of your HAWQ installation, you may need to generate a larger series to ensure data is distributed to all segment instances.

3. Run the UDF on the segment nodes where data is stored in the primary segment instances.

    ``` sql
    =# SELECT gp_segment_id, test_importnumpy(1) AS status
         FROM disttbl
         GROUP BY gp_segment_id, status
         ORDER BY gp_segment_id, status;
    ```

    The `SELECT` command returns SUCCESS if the UDF imported the Python module on the HAWQ segment instance. FAILURE is returned if the Python module could not be imported.
   

#### <a id="testingpythonmodules"></a>Troubleshooting Python Module Import Failures

Possible causes of a Python module import failure include:

- A problem accessing required libraries. For the NumPy example, HAWQ might have a problem accessing the OpenBLAS libraries or the Python libraries on a segment host.

	*Try*: Test importing the module on the segment host. This `hawq ssh` command tests importing the NumPy module on the segment host named mdw1.

	``` shell
	gpadmin@hawq-node$ hawq ssh -h mdw1 python -c "import numpy"
	```

- Environment variables may not be configured in the HAWQ environment. The Python import command may not return an error in this case.

	*Try*: Ensure that the environment variables are properly set. For the NumPy example, ensure that the environment variables listed at the end of the section [Build and Install NumPy](#buildinstallnumpy) are defined in the `.bashrc` file for the `gpadmin` user on the master and all segment nodes.
	
	**Note:** The `.bashrc` file for the `gpadmin` user on the HAWQ master and all segment nodes must source the `greenplum_path.sh` file.

	
- HAWQ might not have been restarted after adding environment variable settings to the `.bashrc` file. Again, the Python import command may not return an error in this case.

	*Try*: Ensure that you have restarted HAWQ.
	
	``` shell
	gpadmin@master$ hawq restart cluster
	```

## <a id="dictionarygd"></a>Using the GD Dictionary to Improve PL/Python Performance 

Importing a Python module is an expensive operation that can adversely affect performance. If you are importing the same module frequently, you can use Python global variables to import the module on the first invocation and forego loading the module on subsequent imports. 

The following PL/Python function uses the GD persistent storage dictionary to avoid importing the module NumPy if it has already been imported in the GD. The UDF includes a call to `plpy.notice()` to display a message when importing the module.

``` sql
=# CREATE FUNCTION mypy_import2gd() RETURNS text AS $$ 
     if 'numpy' not in GD:
       plpy.notice('mypy_import2gd: importing module numpy')
       import numpy
       GD['numpy'] = numpy
     return 'numpy'
   $$ LANGUAGE plpythonu;
```
``` sql
=# SELECT mypy_import2gd();
NOTICE:  mypy_import2gd: importing module numpy
CONTEXT:  PL/Python function "mypy_import2gd"
 mypy_import2gd 
----------------
 numpy
(1 row)
```
``` sql
=# SELECT mypy_import2gd();
 mypy_import2gd 
----------------
 numpy
(1 row)
```

The second `SELECT` call does not include the `NOTICE` message, indicating that the module was obtained from the GD.

## <a id="references"></a>References 

This section lists references for using PL/Python.

### <a id="technicalreferences"></a>Technical References 

For information about PL/Python in HAWQ, see the [PL/Python - Python Procedural Language](http://www.postgresql.org/docs/8.2/static/plpython.html) PostgreSQL documentation.

For information about Python Package Index (PyPI), refer to [PyPI - the Python Package Index](https://pypi.python.org/pypi).

The following Python modules may be of interest:

- [SciPy library](http://www.scipy.org/scipylib/index.html) provides user-friendly and efficient numerical routines including those for numerical integration and optimization. To download the SciPy package tar file:

    ``` shell
    hawq-node$ wget http://sourceforge.net/projects/scipy/files/scipy/0.10.1/scipy-0.10.1.tar.gz
    ```

- [Natural Language Toolkit](http://www.nltk.org/) (`nltk`) is a platform for building Python programs to work with human language data. 

    The Python [`distribute`](https://pypi.python.org/pypi/distribute/0.6.21) package is required for `nltk`. The `distribute` package should be installed before installing `ntlk`. To download the `distribute` package tar file:

    ``` shell
    hawq-node$ wget http://pypi.python.org/packages/source/d/distribute/distribute-0.6.21.tar.gz
    ```

    To download the `nltk` package tar file:

    ``` shell
    hawq-node$ wget http://pypi.python.org/packages/source/n/nltk/nltk-2.0.2.tar.gz#md5=6e714ff74c3398e88be084748df4e657
    ```

### <a id="usefulreading"></a>Useful Reading 

For information about the Python language, see [http://www.python.org/](http://www.python.org/).

A set of slides that were used in a talk about how the Pivotal Data Science team uses the PyData stack in the Pivotal MPP databases and on Pivotal Cloud Foundry [http://www.slideshare.net/SrivatsanRamanujam/all-thingspythonpivotal](http://www.slideshare.net/SrivatsanRamanujam/all-thingspythonpivotal).

