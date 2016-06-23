---
title: Using PL/Python in HAWQ
---

This section contains an overview of the HAWQ PL/Python Language.

## About HAWQ PL/Python <a id="abouthawqplpython"></a>

PL/Python is a loadable procedural language. With the HAWQ PL/Python extension, you can write a HAWQ user-defined functions in Python that take advantage of Python features and modules to quickly build robust database applications.

The HAWQ PL/Python extension is installed by default with HAWQ. HAWQ installs a version of Python and PL/Python. HAWQ uses the following Python installation:

```shell
$GPHOME/ext/python/
```

**Note:** HAWQ uses Python version 2.6.6.

### HAWQ PL/Python Limitations <a id="hawqlimitations"></a>

- HAWQ does not support PL/Python triggers.
- PL/Python is available only as a HAWQ untrusted language.
 
## Enabling and Removing PL/Python Support <a id="enableplpython"></a>

The PL/Python language is installed with HAWQ. To create and run a PL/Python user-defined function (UDF) in a database, you must register the PL/Python language with the database.

On every database where you want to install and enable PL/Python, connect to the database using the psql client.

```shell
$ psql -d <dbname>
```

Replace \<dbname\> with the name of the target database.

Then, run the following SQL command:

```shell
psql# CREATE LANGUAGE plpythonu;
```

Note that `plpythonu` is installed as an “untrusted” language, meaning it does not offer any way of restricting what users can do in it.

To remove support for plpythonu from a database, run the following SQL command:

```shell
psql# DROP LANGUAGE plpythonu;
```

## Developing Functions with PL/Python <a id="developfunctions"></a>

The body of a PL/Python user-defined function is a Python script. When the function is called, its arguments are passed as elements of the array `args[]`. Named arguments are also passed as ordinary variables to the Python script. The result is returned from the PL/Python function with return statement, or yield statement in case of a result-set statement.

The HAWQ PL/Python language module imports the Python module `plpy`. The module plpy implements these functions:

- Functions to execute SQL queries and prepare execution plans for queries.
   - `plpy.execute`
   - `plpy.prepare`
   
- Functions to manage errors and messages.
   - `plpy.debug`
   - `plpy.log`
   - `plpy.info`
   - `plpy.notice`
   - `plpy.warning`
   - `plpy.error`
   - `plpy.fatal`
   - `plpy.debug`
   
## Executing and Preparing SQL Queries <a id="executepreparesql"></a>

The PL/Python `plpy` module provides two Python functions to execute an SQL query and prepare an execution plan for a query, `plpy.execute` and `plpy.prepare`. Preparing the execution plan for a query is useful if you run the query from multiple Python functions.

### plpy.execute <a id="plpyexecute"></a>

Calling `plpy.execute` with a query string and an optional limit argument causes the query to be run and the result to be returned in a Python result object. The result object emulates a list or dictionary object. The rows returned in the result object can be accessed by row number and column name. The result set row numbering starts with 0 (zero). The result object can be modified. The result object has these additional methods:

- `nrows` that returns the number of rows returned by the query.
- `status` which is the `SPI_execute()` return value.

For example, this Python statement in a PL/Python user-defined function executes a query.

```python
rv = plpy.execute("SELECT * FROM my_table", 5)
```

The `plpy.execute` function returns up to 5 rows from `my_table`. The result set is stored in the `rv` object. If `my_table` has a column `my_column`, it would be accessed as:

```python
my_col_data = rv[i]["my_column"]
```

Since the function returns a maximum of 5 rows, the index `i` can be an integer between 0 and 4.

### plpy.prepare <a id="plpyprepare"></a>

The function `plpy.prepare` prepares the execution plan for a query. It is called with a query string and a list of parameter types, if you have parameter references in the query. For example, this statement can be in a PL/Python user-defined function:

```python
plan = plpy.prepare("SELECT last_name FROM my_users WHERE 
  first_name = $1", [ "text" ])
```

The string text is the data type of the variable that is passed for the variable `$1`. After preparing a statement, you use the function `plpy.execute` to run it:

```python
rv = plpy.execute(plan, [ "Fred" ], 5)
```

The third argument is the limit for the number of rows returned and is optional.

When you prepare an execution plan using the PL/Python module the plan is automatically saved. See the Postgres Server Programming Interface (SPI) documentation for information about the execution plans [http://www.postgresql.org/docs/8.2/static/spi.html](http://www.postgresql.org/docs/8.2/static/spi.html).

To make effective use of saved plans across function calls you use one of the Python persistent storage dictionaries SD or GD.

The global dictionary SD is available to store data between function calls. This variable is private static data. The global dictionary GD is public data, available to all Python functions within a session. Use GD with care.

Each function gets its own execution environment in the Python interpreter, so that global data and function arguments from myfunc are not available to `myfunc2`. The exception is the data in the GD dictionary, as mentioned previously.

This example uses the SD dictionary:

```sql
CREATE FUNCTION usesavedplan() RETURNS trigger AS $$
  if SD.has_key("plan"):
    plan = SD["plan"]
  else:
    plan = plpy.prepare("SELECT 1")
    SD["plan"] = plan

  # rest of function

$$ LANGUAGE plpythonu;
```

## Handling Python Errors and Messages <a id="pythonerrors"></a>

The message functions `plpy.error` and `plpy.fatal` raise a Python exception which, if uncaught, propagates out to the calling query, causing the current transaction or subtransaction to be aborted. The functions raise `plpy.ERROR(msg)` and raise `plpy.FATAL(msg)` are equivalent to calling `plpy.error` and `plpy.fatal`, respectively. The other message functions only generate messages of different priority levels.

Whether messages of a particular priority are reported to the client, written to the server log, or both is controlled by the HAWQ server configuration parameters `log_min_messages` and `client_min_messages`. For information about the parameters, see the [Server Configuration Parameter Reference](../reference/HAWQSiteConfig.html).

## Using the Dictionary GD to Improve PL/Python Performance <a id="dictionarygd"></a>

In terms of performance, importing a Python module is an expensive operation and can affect performance. If you are importing the same module frequently, you can use Python global variables to load the module on the first invocation and not require importing the module on subsequent calls. The following PL/Python function uses the GD persistent storage dictionary to avoid importing a module if it has already been imported and is in the GD.

```sql
psql=#
   CREATE FUNCTION pytest() returns text as $$ 
      if 'mymodule' not in GD:
        import mymodule
        GD['mymodule'] = mymodule
    return GD['mymodule'].sumd([1,2,3])
$$;
```

## Installing Python Modules <a id="installpythonmodules"></a>

When you install a Python module on HAWQ, the HAWQ Python environment must have the module added to it across all segment hosts in the cluster. When expanding HAWQ, you must add the Python modules to the new segment hosts. You can use the HAWQ utilities `hawq ssh` and `hawq scp` run commands on HAWQ hosts and copy files to the hosts. For information about the utilities, see the [HAWQ Management Tools Reference](../reference/cli/management_tools.html).

As part of the HAWQ installation, the `gpadmin` user environment is configured to use Python that is installed with HAWQ.

To check which Python is being used in your environment, use the `which` command:

```bash
$ which python
```

The command returns the location of the Python installation. The Python installed with HAWQ is in the HAWQ `ext/python` directory.

```bash
/$GPHOME/ext/python/bin/python
```

If you are building a Python module, you must ensure that the build creates the correct executable. For example on a Linux system, the build should create a 64-bit executable.

Before building a Python module prior to installation, ensure that the appropriate software to build the module is installed and properly configured. The build environment is required only on the host where you build the module.

These are examples of installing and testing Python modules:

- Simple Python Module Installation Example (setuptools)
- Complex Python Installation Example (NumPy)
- Testing Installed Python Modules

### Simple Python Module Installation Example (setuptools) <a id="simpleinstall"></a>

This example manually installs the Python `setuptools` module from the Python Package Index repository. The module lets you easily download, build, install, upgrade, and uninstall Python packages.

This example first builds the module from a package and installs the module on a single host. Then the module is built and installed on segment hosts.

Get the module package from the Python Package Index site. For example, run this `wget` command on a HAWQ host as the gpadmin user to get the tar.gz file.

```bash
$ wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-18.4.tar.gz
```

Extract the files from the tar.gz file.

```bash
$ tar -xzvf setuptools-18.4.tar.gz
```

Go to the directory that contains the package files, and run the Python scripts to build and install the Python package.

```bash
$ cd setuptools-18.4
$ python setup.py build && python setup.py install
```

The following Python command returns no errors if the module is available to Python.

```bash
$ python -c "import setuptools"
```

Copy the package to the HAWQ hosts with the `hawq scp` utility. For example, this command copies the tar.gz file from the current host to the host systems listed in the file `hawq-hosts`.

```bash
$ hawq scp -f hawq-hosts setuptools-18.4.tar.gz =:/home/gpadmin
```

Run the commands to build, install, and test the package with `hawq ssh` utility on the hosts listed in the file `hawq-hosts`. The file `hawq-hosts` lists all the remote HAWQ segment hosts:

```bash
$ hawq ssh -f hawq-hosts
>>> tar -xzvf setuptools-18.4.tar.gz
>>> cd setuptools-18.4
>>> python setup.py build && python setup.py install
>>> python -c "import setuptools"
>>> exit
```

The `setuptools` package installs the `easy_install` utility that lets you install Python packages from the Python Package Index repository. For example, this command installs Python PIP utility from the Python Package Index site.

```shell
$ easy_install pip
```

You can use the `hawq ssh` utility to run the `easy_install` command on all the HAWQ segment hosts.

### Complex Python Installation Example (NumPy) <a id="complexinstall"></a>

This example builds and installs the Python module NumPy. NumPy is a module for scientific computing with Python. For information about NumPy, see [http://www.numpy.org/](http://www.numpy.org/).

Building the NumPy package requires this software:
- OpenBLAS libraries, an open source implementation of BLAS (Basic Linear Algebra Subprograms).
- The gcc compilers: gcc, gcc-gfortran, and gcc-c++. The compilers are required to build the OpenBLAS libraries. See [OpenBLAS Prerequisites](#openblasprereq).

This example process assumes `yum` is installed on all HAWQ segment hosts and the `gpadmin` user is a member of `sudoers` with `root` privileges on the hosts.

Download the OpenBLAS and NumPy source files. For example, these `wget` commands download tar.gz files into the directory packages:

```bash
$ wget --directory-prefix=packages http://github.com/xianyi/OpenBLAS/tarball/v0.2.8
$ wget --directory-prefix=packages http://sourceforge.net/projects/numpy/files/NumPy/1.8.0/numpy-1.8.0.tar.gz/download
```

Distribute the software to the HAWQ hosts. For example, if you download the software to `/home/gpadmin/packages`, these commands create the directory on the hosts and copies the software to hosts for the hosts listed in the `hawq-hosts` file.

```bash
$ hawq ssh -f hawq-hosts mkdir packages 
$ hawq scp -f hawq-hosts packages/* =:/home/gpadmin/packages
```

#### OpenBLAS Prerequisites <a id="openblasprereq"></a>

1. If needed, use `yum` to install gcc compilers from system repositories. The compilers are required on all hosts where you compile OpenBLAS:

	```bash
	$ sudo yum -y install gcc gcc-gfortran gcc-c++
	```

	**Note:** If you cannot install the correct compiler versions with `yum`, you can download the gcc compilers, including gfortran, from source and install them.

	These two commands download and install the compilers:

	```bash
	$ wget http://gfortran.com/download/x86_64/snapshots/gcc-4.4.tar.xz
	$ tar xf gcc-4.4.tar.xz -C /usr/local/
	```

	If you installed `gcc` manually from a tar file, add the new `gcc` binaries to `PATH` and `LD_LIBRARY_PATH`:

	```bash
	$ export PATH=$PATH:/usr/local/gcc-4.4/bin
	$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/gcc-4.4/lib
	```

2. Create a symbolic link to `g++` and call it `gxx`:

	```bash
	$ sudo ln -s /usr/bin/g++ /usr/bin/gxx
	```

3. You might also need to create symbolic links to any libraries that have different versions available for example `libppl_c.so.4` to `libppl_c.so.2`.

4. If needed, you can use the `hawq scp` utility to copy files to HAWQ hosts and the `hawq ssh` utility to run commands on the hosts.

#### Build and Install OpenBLAS Libraries <a id="buildopenblas"></a>

Before build and install the NumPy module, you install the OpenBLAS libraries. This section describes how to build and install the libraries on a single host.

1. Extract the OpenBLAS files from the file. These commands extract the files from the OpenBLAS tar file and simplify the directory name that contains the OpenBLAS files.

	```bash
	$ tar -xzf packages/v0.2.8 -C /home/gpadmin/packages
	$ mv /home/gpadmin/packages/xianyi-OpenBLAS-9c51cdf /home/gpadmin/packages/	OpenBLAS
	```

2. Compile OpenBLAS. These commands set the LIBRARY_PATH environment variable and run the make command to build OpenBLAS libraries.

	```bash
	$ cd /home/gpadmin/packages/OpenBLAS
	$ export LIBRARY_PATH=$LD_LIBRARY_PATH
	$ make FC=gfortran USE_THREAD=0
	```

3. Use these commands to install the OpenBLAS libraries in `/usr/local` as `root`, and then change the owner of the files to `gpadmin`.

	```bash
	$ cd /home/gpadmin/packages/OpenBLAS/
	$ sudo make PREFIX=/usr/local install
	$ sudo ldconfig
	$ sudo chown -R gpadmin /usr/local/lib
	```

	The following libraries are installed, along with symbolic links:

	```bash
	libopenblas.a -> libopenblas_sandybridge-r0.2.8.a
	libopenblas_sandybridge-r0.2.8.a
	libopenblas_sandybridge-r0.2.8.so
	libopenblas.so -> libopenblas_sandybridge-r0.2.8.so
	libopenblas.so.0 -> libopenblas_sandybridge-r0.2.8.so
	```

4. You can use the `hawq ssh` utility to build and install the OpenBLAS libraries on multiple hosts.

	All HAWQ hosts (master and segment hosts) have identical configurations. You can copy the OpenBLAS libraries from the system where they were built instead of building the OpenBlas libraries on all the hosts. For example, these `hawq ssh` and `hawq scp commands copy and install the OpenBLAS libraries on the hosts listed in the hawq-hosts file.

```bash
$ hawq ssh -f hawq-hosts -e 'sudo yum -y install gcc gcc-gfortran gcc-c++'
$ hawq ssh -f hawq-hosts -e 'ln -s /usr/bin/g++ /usr/bin/gxx'
$ hawq ssh -f hawq-hosts -e sudo chown gpadmin /usr/local/lib
$ hawq scp -f hawq-hosts /usr/local/lib/libopen*sandy* =:/usr/local/lib
```
```bash
$ hawq ssh -f hawq-hosts
>>> cd /usr/local/lib
>>> ln -s libopenblas_sandybridge-r0.2.8.a libopenblas.a
>>> ln -s libopenblas_sandybridge-r0.2.8.so libopenblas.so
>>> ln -s libopenblas_sandybridge-r0.2.8.so libopenblas.so.0
>>> sudo ldconfig
```

#### Build and Install NumPy <a name="buildinstallnumpy"></a>

After you have installed the OpenBLAS libraries, you can build and install NumPy module. These steps install the NumPy module on a single host. You can use the hawq ssh utility to build and install the NumPy module on multiple hosts.

1. Go to the packages subdirectory and get the NumPy module source and extract the files.

	```bash
	$ cd /home/gpadmin/packages
	$ tar -xzf numpy-1.8.0.tar.gz
	```

2. Set up the environment for building and installing NumPy.

	```bash
	$ export BLAS=/usr/local/lib/libopenblas.a
	$ export LAPACK=/usr/local/lib/libopenblas.a
	$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib/
	$ export LIBRARY_PATH=$LD_LIBRARY_PATH
	```

3. Go to the NumPy directory and build and install NumPy. Building the NumPy package might take some time.

	```bash
	$ cd numpy-1.8.0
	$ python setup.py build
	$ python setup.py install
	```

	**Note:** If the NumPy module did not successfully build, the NumPy build process might need a site.cfg that specifies the location of the OpenBLAS libraries. Create the file `site.cfg` in the NumPy package directory:

	```bash
	$ cd ~/packages/numpy-1.8.0
	$ touch site.cfg
	```

	Add the following to the `site.cfg` file and run the NumPy build command again:

	<pre>
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
	</pre>

4. The following Python command ensures that the module is available for import by Python on a host system.

	```bash
	$ python -c "import numpy"
	```

5. Similar to the simple module installation, use the `hawq ssh` utility to build, install, and test the module on HAWQ segment hosts.

5. The environment variables that are require to build the NumPy module are also required in the gpadmin user environment when running Python NumPy functions. You can use the `hawq ssh` utility with the `echo` command to add the environment variables to the `.bashrc` file. For example, these echo commands add the environment variables to the `.bashrc` file in the user home directory.

	```bash
	$ echo -e '\n#Needed for NumPy' >> ~/.bashrc
	$ echo -e 'export BLAS=/usr/local/lib/libopenblas.a' >> ~/.bashrc
	$ echo -e 'export LAPACK=/usr/local/lib/libopenblas.a' >> ~/.bashrc
	$ echo -e 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib' >> ~/.bashrc
	$ echo -e 'export LIBRARY_PATH=$LD_LIBRARY_PATH' >> ~/.bashrc
	```

## Testing Installed Python Modules <a id="testingpythonmodules"></a>

You can create a simple PL/Python user-defined function (UDF) to validate that Python a module is available in HAWQ. This example tests the NumPy module.

This PL/Python UDF imports the NumPy module. The function returns SUCCESS if the module is imported, and FAILURE if an import error occurs.

```sql
CREATE OR REPLACE FUNCTION plpy_test(x int)
returns text
as $$
  try:
      from numpy import *
      return 'SUCCESS'
  except ImportError, e:
      return 'FAILURE'
$$ language plpythonu;
```

Create a table that contains data on each HAWQ segment instance. Depending on the size of your HAWQ installation, you might need to generate more data to ensure data is distributed to all segment instances.

```sql
CREATE TABLE DIST AS (SELECT x FROM generate_series(1,50) x ) DISTRIBUTED RANDOMLY ;
```

This SELECT command runs the UDF on the segment hosts where data is stored in the primary segment instances.

```sql
SELECT gp_segment_id, plpy_test(x) AS status
  FROM dist
  GROUP BY gp_segment_id, status
  ORDER BY gp_segment_id, status;
```

The SELECT command returns SUCCESS if the UDF imported the Python module on the HAWQ segment instance. If the SELECT command returns FAILURE, you can find the segment host of the segment instance host. The HAWQ system table `gp_segment_configuration` contains information about segment configuration. This command returns the host name for a segment ID.

```sql
SELECT hostname, content AS seg_ID FROM gp_segment_configuration
  WHERE content = seg_id ;
```

If FAILURE is returned, these are some possible causes:

- A problem accessing required libraries. For the NumPy example, HAWQ might have a problem accessing the OpenBLAS libraries or the Python libraries on a segment host.

	Make sure you get no errors when running command on the segment host as the gpadmin user. This hawq ssh command tests importing the NumPy module on the segment host mdw1.

	```shell
	$ hawq ssh -h mdw1 python -c "import numpy"
	```

- If the Python import command does not return an error, environment variables might not be configured in the HAWQ environment. For example, the variables are not in the `.bashrc` file, or HAWQ might not have been restarted after adding the environment variables to the `.bashrc` file.

	Ensure sure that the environment variables are properly set and then restart HAWQ. For the NumPy example, ensure the environment variables listed at the end of the section [Build and Install NumPy](#buildinstallnumpy) are defined in the `.bashrc` file for the gpadmin user on the master and segment hosts.

	**Note:** On HAWQ master and segment hosts, the `.bashrc` file for the gpadmin user must source the file `$GPHOME/greenplum_path.sh`.

## Examples <a id="examples"></a>

This PL/Python UDF returns the maximum of two integers:

```sql
CREATE FUNCTION pymax (a integer, b integer)
  RETURNS integer
AS $$
  if (a is None) or (b is None):
      return None
  if a > b:
     return a
  return b
$$ LANGUAGE plpythonu;
```

You can use the STRICT property to perform the null handling instead of using the two conditional statements.

```sql
CREATE FUNCTION pymax (a integer, b integer) 
  RETURNS integer AS $$ 
return max(a,b) 
$$ LANGUAGE plpythonu STRICT ;
```

You can run the user-defined function pymax with SELECT command. This example runs the UDF and shows the output.

```sql
SELECT ( pymax(123, 43));
column1
---------
     123
(1 row)
```

This example that returns data from an SQL query that is run against a table. These two commands create a simple table and add data to the table.

```sql
CREATE TABLE sales (id int, year int, qtr int, day int, region text)
  DISTRIBUTED BY (id) ;

INSERT INTO sales VALUES
 (1, 2014, 1,1, 'usa'),
 (2, 2002, 2,2, 'europe'),
 (3, 2014, 3,3, 'asia'),
 (4, 2014, 4,4, 'usa'),
 (5, 2014, 1,5, 'europe'),
 (6, 2014, 2,6, 'asia'),
 (7, 2002, 3,7, 'usa') ;
```

This PL/Python UDF executes a SELECT command that returns 5 rows from the table. The Python function returns the REGION value from the row specified by the input value. In the Python function, the row numbering starts from 0. Valid input for the function is an integer between 0 and 4.

```sql
CREATE OR REPLACE FUNCTION mypytest(a integer) 
  RETURNS text 
AS $$ 
  rv = plpy.execute("SELECT * FROM sales ORDER BY id", 5)
  region = rv[a]["region"]
  return region
$$ language plpythonu;
```

Running this SELECT statement returns the REGION column value from the third row of the result set.

```sql
SELECT mypytest(2) ;
```

This command deletes the UDF from the database.

```sql
DROP FUNCTION mypytest(integer) ;
```

## References <a id="references"></a>

This section lists references for using PL/Python.

### Technical References <a id="technicalreferences"></a>

For information about PL/Python see the PostgreSQL documentation at [http://www.postgresql.org/docs/8.2/static/plpython.html](http://www.postgresql.org/docs/8.2/static/plpython.html).

For information about Python Package Index (PyPI), see [https://pypi.python.org/pypi](https://pypi.python.org/pypi).

These are some Python modules that can be downloaded:

- SciPy library provides user-friendly and efficient numerical routines such as routines for numerical integration and optimization [http://www.scipy.org/scipylib/index.html](http://www.scipy.org/scipylib/index.html). This wget command downloads the SciPy package tar file.

 ```shell
$ wget http://sourceforge.net/projects/scipy/files/scipy/0.10.1/ scipy-0.10.1.tar.gz/download
```

- Natural Language Toolkit (nltk) is a platform for building Python programs to work with human language data http://www.nltk.org/. This wget command downloads the nltk package tar file.

 ```shell
$ wget http://pypi.python.org/packages/source/n/nltk/nltk-2.0.2.tar.gz#md5=6e714ff74c3398e88be084748df4e657
 ```

 **Note:** The Python package Distribute [https://pypi.python.org/pypi/](https://pypi.python.org/pypi/) distribute is required for `nltk`. The Distribute module should be installed before the `ntlk` package. This wget command downloads the Distribute package tar file.

```shell
$ wget http://pypi.python.org/packages/source/d/distribute/distribute-0.6.21.tar.gz
```

### Useful Reading <a id="usefulreading"></a>

For information about the Python language, see [http://www.python.org/](http://www.python.org/).

A set of slides that were used in a talk about how the Pivotal Data Science team uses the PyData stack in the Pivotal MPP databases and on Pivotal Cloud Foundry [http://www.slideshare.net/SrivatsanRamanujam/all-thingspythonpivotal](http://www.slideshare.net/SrivatsanRamanujam/all-thingspythonpivotal).

