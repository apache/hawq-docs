---
title: Using PL/R in HAWQ
---

PL/R is a procedural language. With the HAWQ PL/R extension you can write database functions in the R programming language, and use R packages that contain R functions and data sets.

<p class="note"><b>Note:</b> For details on how to install PL/R, see <a href="/hdb/install/install_plr.html">Installing PL/R</a>.</p>


## PL/R Examples <a id="plrexamples"></a>

This section contains simple PL/R examples.

### Example 1: Using PL/R for Single Row Operators <a id="example1"></a>

This function generates an array of numbers with a normal distribution using the R function `rnorm()`.

```sql
CREATE OR REPLACE FUNCTION r_norm(n integer, mean float8, 
  std_dev float8) RETURNS float8[ ] AS
$$
  x<-rnorm(n,mean,std_dev)
  return(x)
$$
LANGUAGE 'plr';
```

The following `CREATE TABLE` command uses the `r_norm` function to populate the table. The `r_norm` function creates an array of 10 numbers.

```sql
CREATE TABLE test_norm_var
  AS SELECT id, r_norm(10,0,1) as x
  FROM (SELECT generate_series(1,30:: bigint) AS ID) foo
  DISTRIBUTED BY (id);
```

### Example 2: Returning PL/R data.frames in Tabular Form <a id="example2"></a>

Assuming your PL/R function returns an R `data.frame` as its output \(unless you want to use arrays of arrays\), some work is required in order for HAWQ to see your PL/R `data.frame` as a simple SQL table:

Create a TYPE in a HAWQ with the same dimensions as your R `data.frame`:

```sql
CREATE TYPE t1 AS ...
```

Use this TYPE when defining your PL/R function:

```sql
... RETURNS SET OF t1 AS ...
```

Sample SQL for this is given in the next example.

### Example 3: Process Employee Information Using PL/R <a id="example3"></a>

The SQL below defines a TYPE and process employee information with data.frame using PL/R:

```sql
-- Create type to store employee information
DROP TYPE IF EXISTS emp_type CASCADE;
CREATE TYPE emp_type AS (name text, age int, salary numeric(10,2));

-- Create function to process employee information and return data.frame
DROP FUNCTION IF EXISTS get_emps();
CREATE OR REPLACE FUNCTION get_emps() RETURNS SETOF emp_type AS '
    names <- c("Joe","Jim","Jon")
    ages <- c(41,25,35)
    salaries <- c(250000,120000,50000)
    df <- data.frame(name = names, age = ages, salary = salaries)

    return(df)
' LANGUAGE 'plr';

-- Call the function
SELECT * FROM get_emps();
```


## Downloading and Installing R Packages <a id="downloadinstallplrlibraries"></a>

R packages are modules that contain R functions and data sets. You can install R packages to extend R and PL/R functionality in HAWQ.

<p class="note"><b>Note:</b> If you expand HAWQ and add segment hosts, you must install the R packages in the R installation of the new hosts.</p>

1. For an R package, identify all dependent R packages and each package web URL. The information can be found by selecting the given package from the following navigation page:

	[http://cran.r-project.org/web/packages/available_packages_by_name.html](http://cran.r-project.org/web/packages/available_packages_by_name.html)

	As an example, the page for the R package `arm` indicates that the package requires the following R libraries: `Matrix`, `lattice`, `lme4`, `R2WinBUGS`, `coda`, `abind`, `foreign`, and `MASS`.
	
	You can also try installing the package with `R CMD INSTALL` command to determine the dependent packages.
	
	For the R installation included with the HAWQ PL/R extension, the required R packages are installed with the PL/R extension. However, the Matrix package requires a newer version.
	
1. From the command line, use the wget utility to download the tar.gz files for the `arm` package to the HAWQ master host:

	```shell
	$ wget http://cran.r-project.org/src/contrib/Archive/arm/arm_1.5-03.tar.gz
	$ wget http://cran.r-project.org/src/contrib/Archive/Matrix/Matrix_0.9996875-1.tar.gz
	```

1. Use the `hawq scp` utility and the `hosts_all` file to copy the `tar.gz` files to the same directory on all nodes of the HAWQ cluster. The hawq_hosts file contains a list of all the HAWQ segment hosts. You might require root access to do this.

	```shell
	$ hawq scp -f hosts_all Matrix_0.9996875-1.tar.gz =:/home/gpadmin 
	$ hawq scp -f hawq_hosts arm_1.5-03.tar.gz =:/home/gpadmin
	```

1. Use the hawq ssh utility in interactive mode to log into each HAWQ segment host (`hawq ssh -f hawq_hosts`). Install the packages from the command prompt using the `R CMD INSTALL` command. Note that this may require root access. For example, this R install command installs the packages for the `arm` package.

	```shell
	$ $R_HOME/bin/R CMD INSTALL Matrix_0.9996875-1.tar.gz   arm_1.5-03.tar.gz
	```
	<p class="note"><strong>Note:</strong> Some packages require compilation. Refer to the package documentation for any system build requirements.</p>

1. Ensure that the package is installed in the `$R_HOME/library` directory on all the segments (the hawq ssh utility can be use to install the package). For example, this hawq ssh command lists the contents of the R library directory.

	```shell
	$ hawq ssh -f hawq_hosts "ls $R_HOME/library"
	```
	
1. Test if the R package can be loaded.

	This function performs a simple test to if an R package can be loaded:
	
	```sql
	CREATE OR REPLACE FUNCTION R_test_require(fname text)
	RETURNS boolean AS
	$BODY$
    	return(require(fname,character.only=T))
	$BODY$
	LANGUAGE 'plr';
	```

	This SQL command checks if the R package arm can be loaded:
	
	```sql
	SELECT R_test_require('arm');
	```

## Displaying R Library Information <a id="rlibrarydisplay"></a>

You can use the R command line to display information about the installed libraries and functions on the HAWQ host. You can also add and remove libraries from the R installation. To start the R command line on the host, log into the host as the gadmin user and run the script R from the directory `$GPHOME/ext/R-N.N.N/bin` where N.N.N corresponds to the version of R installed.

This R function lists the available R packages from the R command line:

```r
> library()
```

Display the documentation for a particular R package

```r
> library(help="package_name")
> help(package="package_name")
```

Display the help file for an R function:

```r
> help("function_name")
> ?function_name
```

To see what packages are installed, use the R command `installed.packages()`. This will return a matrix with a row for each package that has been installed. Below, we look at the first 5 rows of this matrix.

```r
> installed.packages()
```

Any package that does not appear in the installed packages matrix must be installed and loaded before its functions can be used.

An R package can be installed with `install.packages()`:

```r
> install.packages("package_name") 
> install.packages("mypkg", dependencies = TRUE, type="source")
```

Load a package from the R command line.

```r
> library(" package_name ") 
```
An R package can be removed with remove.packages

```r
> remove.packages("package_name")
```

You can use the R command `-e` option to run functions from the command line. For example, this command displays help on the R package MASS.

```shell
$ R -e 'help("MASS")'
```

## References <a id="plrreferences"></a>

[http://www.r-project.org/](http://www.r-project.org/) - The R Project home page

[https://github.com/pivotalsoftware/gp-r](https://github.com/pivotalsoftware/gp-r) - GitHub repository that contains information about using R with Pivotal software including Pivotal HDB.

[https://github.com/pivotalsoftware/PivotalR](https://github.com/pivotalsoftware/PivotalR) - GitHub repository for PivotalR, a package that provides an R interface to operate on HAWQ tables and views that is similar to the R `data.frame`. PivotalR also supports using the machine learning package MADlib directly from R.

R documentation is installed with the HAWQ R package:

```shell
$GPHOME/ext/R-N.N.N/lib64/R/doc
```

where N.N.N corresponds to the version of R installed.

### R Functions and Arguments <a id="rfunctions"></a>

See [http://www.joeconway.com/plr/doc/plr-funcs.html](http://www.joeconway.com/plr/doc/plr-funcs.html).

### Passing Data Values in R <a id="passdatavalues"></a>

See [http://www.joeconway.com/plr/doc/plr-data.html](http://www.joeconway.com/plr/doc/plr-data.html).

### Aggregate Functions in R <a id="aggregatefunctions"></a>

See [http://www.joeconway.com/plr/doc/plr-aggregate-funcs.html](http://www.joeconway.com/plr/doc/plr-aggregate-funcs.html).


