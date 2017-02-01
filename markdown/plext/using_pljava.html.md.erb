---
title: Using PL/Java
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

This section provides an overview of the HAWQ PL/Java procedural language extension. 


## <a id="aboutpljava"></a>About PL/Java 

With the PL/Java extension, you can write Java methods using your favorite Java IDE and invoke the methods from PostgreSQL user-defined functions (UDFs). 

The HAWQ PL/Java package is based on the open source PL/Java 1.4.0 and provides the following features:

- PL/Java function execution with Java 1.6 or 1.7.
- Standardized mappings of Java and PostgreSQL parameters and results. Complex types as well as sets are supported.
- Two HAWQ Java languages:
	- `java` - Tusted PL/Java language
	- `javau` - Untrusted PL/Java language (superusers only)
- An embedded, high performance, JDBC driver utilizing the internal HAWQ Database Server Programming Interface (SPI).
- Metadata support for the JDBC driver. Both `DatabaseMetaData` and `ResultSetMetaData` are included.
- A standard way of passing parameters and return values. Complex types and sets are passed using the standard JDBC `ResultSet` class.
- The ability to return a `ResultSet` from a query as an alternative to building a `ResultSet` row by row.
- Full support for savepoints and exception handling.
- Transaction and Savepoint listeners enabling code execution when a transaction or savepoint is committed or rolled back.
- Integration with GNU GCJ on selected platforms.

PL/Java is optimized for performance. The Java virtual machine executes within the same process as the backend, minimizing call overhead. PL/Java brings the power of Java to the database itself, enabling the database-intensive business logic to execute as close to the actual data as possible.

Calls between the HAWQ backend and the Java VM are bridged using the standard Java Native Interface (JNI).


## <a id="abouthawqpljava"></a>About HAWQ PL/Java 

PL/Java is embedded in your HAWQ product distribution or within your HAWQ build if you chose to enable it as a build option. To use PL/Java in a HAWQ deployment, you must explicitly enable the PL/Java extension in all desired databases.

There are a few key differences between the implementation of PL/Java in standard PostgreSQL and HAWQ.

### <a id="pljavafunctions"></a>Unsupported Functions

The following functions are not supported in HAWQ:

- sqlj.install_jar()
- sqlj.install_jar()
- sqlj.replace_jar()
- sqlj.remove_jar()
- sqlj.get_classpath()
- sqlj.set_classpath()

The PL/Java classpath is handled differently in a distributed HAWQ environment than that of the PostgreSQL environment. HAWQ uses the `pljava_classpath` server configuration parameter in place of the `sqlj.set_classpath()` function.

### <a id="serverconfigparams"></a>Server Configuration Parameters 

PL/Java uses server configuration parameters to configure the classpath, Java Virtual Machine (VM), and other options. Refer to the [Server Configuration Parameter Reference](../reference/HAWQSiteConfig.html) for general information about HAWQ server configuration parameters.

The following server configuration parameters are used by HAWQ PL/Java. These parameters replace the `pljava.*` configuration parameters that are used in the standard PostgreSQL PL/Java implementation.

#### pljava\_classpath

A PL/Java user-defined function will appoint a static method in a Java class. In order for the function to execute, the appointed class must be available on the class path specified by the [`pljava_classpath`](../reference/guc/parameter_definitions.html#pljava_classpath) HAWQ server configuration parameter.

`pljava_classpath` is a colon (:) separated list of the JAR files implementing the Java classes referenced in any PL/Java user-defined functions. The JAR files must be installed in the same locations on all HAWQ hosts. When using the trusted PL/Java language handler (`java` language tag), JAR file paths must be relative to the `$GPHOME/lib/postgresql/java/` directory. Relative or absolute JAR file paths may be used with the untrusted PL/Java language handler (`javau` language tag).

#### pljava\_release\_lingering\_savepoints

[`pljava_release_lingering_savepoints`](../reference/guc/parameter_definitions.html#pljava_release_lingering_savepoints) identifies the action to perform when lingering savepoints exist after a PL/Java user-defined function exits. If TRUE, lingering savepoints are released on function exit. If FALSE, lingering savepoints are rolled back.

#### pljava\_statement\_cache\_size

[`pljava_statement_cache_size`](../reference/guc/parameter_definitions.html#pljava_statement_cache_size) sets the size (in KB) of the Most Recently Used (MRU) cache for prepared statements.

#### pljava\_vmoptions

[`pljava_vmoptions`](../reference/guc/parameter_definitions.html#pljava_vmoptions) defines the set of space-delimited start-up options for the Java VM.

### <a id="setting_serverconfigparams"></a>Setting PL/Java Configuration Parameters 

You can set PL/Java server configuration parameters at the session level, or globally across your whole cluster.

#### <a id="setsrvrcfg_global"></a>Cluster Level

You will perform different procedures to set a PL/Java server configuration parameter for your whole HAWQ cluster depending upon whether you manage your cluster from the command line or use Ambari. If you use Ambari to manage your HAWQ cluster, you must ensure that you update server configuration parameters only via the Ambari Web UI. If you manage your HAWQ cluster from the command line, you will use the `hawq config` command line utility to set PL/Java server configuration parameters.

You must reload your HAWQ cluster configuration after you set a server configuration value globally.

The following examples add a JAR file named `myclasses.jar` to the `pljava_classpath` server configuration parameter for the entire HAWQ cluster.

If you use Ambari to manage your HAWQ cluster:

1. Set the `pljava_classpath` configuration property **Key** **Value** to include `myclasses.jar` via the HAWQ service **Configs > Advanced > Custom hawq-site** drop down. 
2. Select **Service Actions > Restart All** to load the updated configuration.

If you manage your HAWQ cluster from the command line:

1.  Log in to the HAWQ master node as a HAWQ administrator and set up your HAWQ environment.

    ``` shell
    $ ssh gpadmin@master
    gpadmin@master$ source /usr/local/hawq/greenplum_path.sh
    ```

1. Use the `hawq config` utility to set `pljava_classpath`:

    ``` shell
    gpadmin@master$ hawq config -c pljava_classpath -v 'myclasses.jar'
    ```
    
    The `-c` option identifies the name of the server configuration parameter, `-v` identifies the new value.
    
2. Reload the HAWQ configuration:

    ``` shell
    gpadmin@master$ hawq stop cluster -u
    ```

#### <a id="setsrvrcfg_session"></a>Session Level 

To set a PL/Java server configuration parameter only for the *current* database session, set the parameter within the `psql` subsystem. For example:
	
``` sql
=> SET pljava_classpath='myclasses.jar';
```

## <a id="security"></a>Security 

This section describes specific security considerations when using PL/Java.

### <a id="installation"></a>Enable/Disable 

Only a database superuser can enable and disable PL/Java. You install the PL/Java utility functions with `SECURITY DEFINER` privileges; they execute with the access permissions granted to the creator of the functions.

### <a id="trustedlang"></a>Trusted/Untrusted Language 

PL/Java includes trusted and untrusted language variants.

The PL/Java trusted language is named `java`. The trusted PL/Java language cannot access the file system as stipulated by the PostgreSQL definition of a trusted language. Any database user can create and execute functions in the trusted `java` language.

The PL/Java untrusted language is named `javau`. You cannot restrict operation of functions you create with the `javau` untrusted language. Only database superusers have privileges to create untrusted PL/Java UDFs. Only database superusers and other database users explicitly `GRANT`ed the permissions can execute untrusted PL/Java UDFs.

## <a id="enablepljava"></a>Enabling and Removing PL/Java Support 

The PL/Java extension must be explicitly enabled on each database in which it will be used. To remove PL/Java support, the extension must be explicitly removed from each database in which it was used.

### <a id="pljavaprereq"></a>Prerequisites 

Before you enable PL/Java:

1. Ensure that you have installed a supported Java runtime environment and that the `$JAVA_HOME` variable is set to the same path on the master and all segment nodes.

2. Perform the following step on all nodes in your HAWQ cluster to set up the shared library cache for the installed JDK:

	``` shell
	root@hawq-node$ echo "$JAVA_HOME/jre/lib/amd64/server" > /etc/ld.so.conf.d/libjdk.conf
	root@hawq-node$ ldconfig
	```
4. Make sure that your HAWQ cluster is running, you have sourced `greenplum_path.sh` and that your `$GPHOME` environment variable is set.

    ``` shell
	$ ssh gpadmin@master
	gpadmin@master$ source /usr/local/hawq/greenplum_path.sh
	gpadmin@master$ hawq state
	```

### <a id="enablepljava"></a>Enable PL/Java and Install JAR Files 

To use PL/Java, you must:

1. Enable the language for each database.
1. Install custom JAR files on all HAWQ hosts.
1. Add the names of the JAR files to the HAWQ `pljava_classpath` server configuration parameter. This parameter value should identify a list of all installed JAR files.

#### <a id="enablepljava"></a>Enable PL/Java and Install JAR Files 

Perform the following steps as the `gpadmin` user:

1. Enable PL/Java by running the `$GPHOME/share/postgresql/pljava/install.sql` SQL script on the databases that will use PL/Java. The `install.sql` script registers both the trusted (`java`) and untrusted PL/Java (`javau`) languages. For example, the following command enables the PL/Java languages on a database named `testdb`:

	``` shell
	gpadmin@master$ psql -d testdb -f $GPHOME/share/postgresql/pljava/install.sql
	```
	
	To enable the PL/Java extension in all new HAWQ databases, run the script on the `template1` database: 

    ``` shell
    gpadmin@master$ psql -d template1 -f $GPHOME/share/postgresql/pljava/install.sql
    ```

    Use this option *only* if you are certain you want to enable both the trusted and untrusted versions of PL/Java in all newly-created databases. After you invoke this command, PL/Java will be enabled in each new database that a user creates.
	
2. Copy all custom Java JAR files to `$GPHOME/lib/postgresql/java/` on all HAWQ nodes. This example uses the `hawq scp` utility to copy the `myclasses.jar` file  to the list of hosts identified in the `hawq_hosts` file:

	``` shell
	gpadmin@master$ hawq scp -f ./hawq_hosts ./myclasses.jar =:/usr/local/hawq/lib/postgresql/java/
	```

3. Add all JAR files to the `pljava_classpath` configuration parameter. Refer to [Setting PL/Java Configuration Parameters](#setting_serverconfigparams) for the specific procedure.

5. (Optional) Your HAWQ installation includes an `examples.sql` file. This script registers sample PL/Java functions that you can use to test the PL/Java installation. Run the commands in this file to create and execute PL/Java user-defined functions that use the Java classes implemented in `examples.jar`. The database on which you run the script must have PL/Java enabled:

	``` shell
	gpadmin@master$ psql -d <dbname> -f $GPHOME/share/postgresql/pljava/examples.sql
	```

#### Configuring PL/Java VM Options

Configure PL/Java JVM options via the `pljava_vmoptions` server configuration parameter. For example, `pljava_vmoptions=-Xmx512M` sets the maximum heap size of the JVM. (The default `-Xmx` value is `64M`.)

Refer to [Setting PL/Java Configuration Parameters](#setting_serverconfigparams) for the specific procedure to set PL/Java server configuration parameters.
	
### <a id="uninstallpljava"></a>Disable PL/Java 

To disable PL/Java, you should:

1. Remove PL/Java support from each database in which it was added.
2. Uninstall/remove the Java JAR files.

#### <a id="uninstallpljavasupport"></a>Remove PL/Java Support from Databases 

Remove support for PL/Java by running the `uninstall.sql` script as the `gpadmin` user. For example, the following command disables the PL/Java languages in the specified database:

``` shell
gpadmin@master$ psql -d <dbname> -f $GPHOME/share/postgresql/pljava/uninstall.sql
```

Replace \<dbname\> with the name of the target database.


#### <a id="uninstallpljavapackage"></a>Uninstall the Java JAR files 

When no databases have PL/Java as a registered language, remove the Java JAR files.

If you use Ambari to manage your cluster:

1. Remove the `pljava_classpath` configuration property via the HAWQ service **Configs > Advanced > Custom hawq-site** drop down.

2. Remove the JAR files from the `$GPHOME/lib/postgresql/java/` directory on each HAWQ host.

3. Select **Service Actions > Restart All** to restart your HAWQ cluster.


If you manage your cluster from the command line:

1.  Log in to the HAWQ master host as a HAWQ administrator and source the file `/usr/local/hawq/greenplum_path.sh`.

    ``` shell
    gpadmin@master$ source /usr/local/hawq/greenplum_path.sh
    ```

1. Use the `hawq config` utility to remove the `pljava_classpath` setting:

    ``` shell
    gpadmin@master$ hawq config -r pljava_classpath
    ```
    
2. Remove the JAR files from the `$GPHOME/lib/postgresql/java/` directory on each HAWQ host.

3. Restart your HAWQ cluster:

    ``` shell
    gpadmin@master$ hawq restart cluster
    ```


## <a id="writingpljavafunc"></a>Writing PL/Java Functions 

This section provides information about writing functions with PL/Java.

- [SQL Declaration](#sqldeclaration)
- [Type Mapping](#typemapping)
- [NULL Handling](#nullhandling)
- [Complex Types](#complextypes)
- [Returning Complex Types](#returningcomplextypes)
- [Functions That Return Sets](#functionreturnsets)
- [Returning a SETOF \<scalar type\>](#returnsetofscalar)
- [Returning a SETOF \<complex type\>](#returnsetofcomplex)

You must have a Java SDK installed to write Java methods.

### <a id="sqldeclaration"></a>SQL Declaration 
PL/Java functions are defined using the standard SQL [CREATE FUNCTION](../reference/sql/CREATE-FUNCTION.html) syntax. A PL/Java user-defined function specifies `LANGUAGE java` (trusted) or `LANGUAGE javau` (untrusted). The function must also include `RETURNS` and `AS` clauses.

The `RETURNS` clause identifies the type of the function's return value. 

Use the `AS` clause to identify the name of a Java class and the static method on that class that HAWQ invokes when it executes the function. Any arguments to the UDF are also passed to the Java method.

The Java class is resolved using the classpath that has been defined for the schema in which the function is declared. If no classpath has been defined for that schema, the `public` schema is used. If no classpath is found in the `public` schema, an attempt is made to resolve the class using the Java system class loader.

Example: Create a UDF wrapper around the `java.lang.System` class `getProperty()` method.  `getProperty()` takes a property name string as input and returns the string value of that property:

``` sql
=> CREATE FUNCTION getsysprop_udf(VARCHAR)
     RETURNS VARCHAR
     AS 'java.lang.System.getProperty'
   LANGUAGE java;
```

Execute the `getsysprop_udf()` PL/Java UDF, passing as input the property name  `user.home`:

```sql
=> SELECT getsysprop_udf('user.home');
```

``` 
 getsysprop_udf   
----------------
 /home/gpadmin
(1 row)
```

`getsyprop_udf()` returns the value `/home/gpadmin`, the current user's (`gpadmin`) home directory.

### <a id="typemapping"></a>Type Mapping 

Scalar types are mapped between HAWQ and Java in a straightforward way. The current HAWQ to Java type mappings are listed in the table below.

**Table 1: PL/Java Data Type Mappings**

| HAWQ | Java |
|------------|------|
| bool | boolean |
| char | byte |
| int2 | short |
| int4 | int |
| int8 | long |
| varchar | java.lang.String |
| text | java.lang.String |
| bytea | byte[ ] |
| date | java.sql.Date |
| time | java.sql.Time (stored value treated as local time) |
| timetz | java.sql.Time |
| timestamp	| java.sql.Timestamp (stored value treated as local time) |
| timestampz |	java.sql.Timestamp |
| complex |	java.sql.ResultSet |
| setof complex	| java.sql.ResultSet |

All other types are mapped to `java.lang.String` and will utilize the standard textin/textout routines registered for the respective type.

### <a id="nullhandling"></a>NULL Handling 

The scalar types that map to Java primitives can not be passed as NULL values to Java methods. To pass NULL values, those types should be mapped to the Java object wrapper class that corresponds with the primitive, and must be explicitly denoted in the method reference. For example, the object wrapper class for the `integer` primitive type is `java.lang.Integer`.

Example: Handling Null Inputs

1. Create a work area for the example:

    ``` shell
    $ mkdir pljava_work
    $ cd pljava_work
    $ export PLJAVAWORK=`pwd`
    $ mkdir -p pljex/foo/fee
    $ cd pljex/foo/fee
    ```

2. Create a new file named `Fum.java`, adding the following text to create a class named `Fum` with a single method named `trueIfEvenOrNull()`. This method takes an integer as input and returns true if the integer is even or NULL, false otherwise:

    ``` shell
    $ vi Fum.java
    ```

    ``` java
    package foo.fee;
    public class Fum
    {
      static boolean trueIfEvenOrNull(Integer value)
      {
        return (value == null)
          ? true
          : (value.intValue() % 1) == 0;
      }
    }
    ```

3. Compile the `Fum` class and create a JAR file for this class named `pljex.jar`:

    ``` shell
    $ javac Fum.java
    $ cd ../..
    $ jar cf pljex.jar foo
    ```

4. Copy the JAR file to the default PL/Java classpath directory:

    ``` shell
    $ cp pljex.jar /usr/local/hawq/lib/postgresql/java/
    ```
 
5. Start the `psql` subsystem:

    ``` shell
    $ psql -d testdb
    ```

6. Add the JAR file to the session-level classpath:

    ``` sql
    => SET pljava_classpath='pljex.jar';
    ```

7. Create a trusted PL/Java UDF that invokes the `Fum` class `trueIfEvenOrNull()` method:

    ``` sql
    => CREATE FUNCTION isEvenOrNull(integer)
         RETURNS bool
         AS 'foo.fee.Fum.trueIfEvenOrNull(java.lang.Integer)'
       LANGUAGE java;
    ```
    
    Notice that the UDF input type is `integer`, while the `trueIfEvenOrNull()` Java method input is a `java.lang.Integer` object.

8. Execute the UDF twice, once with a NULL and once with an even input:

    ``` sql
    => SELECT isEvenOrNull(NULL);
    => SELECT isEvenOrNull(4);
    ```
    
    Both statements should return true.

### <a id="complextypes"></a>Complex Types 

PL/Java supports complex types. Use the `CREATE TYPE` SQL command to create the complex type. Use the `CREATE FUNCTION` SQL command to define a PL/Java UDF whose input argument is the new (complex) type.

A complex type is always passed to a Java method as a read-only `java.sql.ResultSet` with exactly one row. The values of the specific fields in the complex type are retrieved using the standard getter method associated with the data type of each field present in the `ResultSet`.

Example: Complex Input Types

1. Add the following definitions and static method to the Java `Fum` class you created in an earlier exercise. This method outputs the components of the complex type comprised of two integer fields and a timestamp field:

    ``` shell
    $ cd $PLJAVAWORK/pljex/foo/fee
    $ vi Fum.java
    ```

    ``` java
    import java.sql.ResultSet;
    import java.sql.SQLException;
    import java.sql.Timestamp;
    ```
    
    ``` java
    public static String useComplexTest(ResultSet complexTest)
    throws SQLException
    {
      int base = complexTest.getInt(1);
      int incbase = complexTest.getInt(2);
      Timestamp ctime = complexTest.getTimestamp(3);
      return "Base = \"" + base +
        "\", incbase = \"" + incbase +
        "\", ctime = \"" + ctime + "\"";
    }
    ```
    
    Add the `imports` under the `package` definition. And be sure to include the `useComplexTypes()` method within the `Fum` class `{}`s. 
    
    Notice that the `ResultSet` object is immediately referenced; a call to `next()` is not required.

2. Compile the `Fum` class, create the JAR file, and copy the JAR file to the default PL/Java classpath directory:

    ``` shell
    $ javac Fum.java
    $ cd ../..
    $ jar cf pljex.jar foo
    $ cp pljex.jar /usr/local/hawq/lib/postgresql/java/
    ```
 
5. Start the `psql` subsystem:

    ``` shell
    $ psql -d testdb
    ```

6. Add the JAR file to the session-level classpath:

    ``` sql
    => SET pljava_classpath='pljex.jar';
    ```

7. Create a custom complex type with 2 integers and a single timestamp component:

    ``` sql
    => CREATE TYPE complexTestType
         AS(base integer, incbase integer, ctime timestamptz);
    ```

7. Create a PL/Java UDF that invokes the `Fum` class `useComplexTest()` method, specifying a `complexTestType` as input:

    ```sql
    => CREATE FUNCTION useComplexTest(complexTestType)
         RETURNS VARCHAR
         AS 'foo.fee.Fum.useComplexTest'
       IMMUTABLE LANGUAGE java;
    ```

8. Execute the `useComplexTest()` UDF, providing 2 integers and a timestamp as input:

    ```sql
    => SELECT useComplexTest( '(1,2,20170101010203)' );
    ```

    ```
                           usecomplextest                       
    ------------------------------------------------------------
     Base = "1", incbase = "2", ctime = "2017-01-01 01:02:03.0"
    (1 row)
    ```
    
    Running the UDF displays the fields and values comprising the complex type.

### <a id="returningcomplextypes"></a>Returning Complex Types 

As Java does not define any way to create a `ResultSet`, returning a `ResultSet` from a Java method is not an option. The SQL-2003 draft suggests that a complex return value should be handled as an input/output argument. Conveniently, PL/Java implements a `ResultSet` that way. To declare a function that returns a complex type, you must implement a Java method with a `boolean` return type and a last input argument of type `java.sql.ResultSet`. This input/output argument will be initialized to an empty updateable `ResultSet` that contains exactly one row.

Example: Complex Return Types

1. Create the `complexTestType` type definition if you did not yet create it:

    ``` sql
    => CREATE TYPE complexTestType
         AS(base integer, incbase integer, ctime timestamptz);
    ```

2. Add the following static method to the Java class `Fum` you created in an earlier exercise. This method takes two integers as input, returning a complex type consisting of the first input integer, first input integer added to the second input integer, and a current timestamp:

    ``` shell
    $ cd $PLJAVAWORK/pljex/foo/fee
    $ vi Fum.java
    ```

    ``` java
    public static boolean complexReturn(int base, int increment, 
      ResultSet receiver)
    throws SQLException
    {
      receiver.updateInt(1, base);
      receiver.updateInt(2, base + increment);
      receiver.updateTimestamp(3, new 
        Timestamp(System.currentTimeMillis()));
      return true;
    }
    ```
    
    The return value denotes if the `receiver` should be considered as a valid tuple (true) or NULL (false).

3. Compile the `Fum` class, create the JAR file, and copy the JAR file to the default PL/Java classpath directory:

    ``` shell
    $ javac Fum.java
    $ cd ../..
    $ jar cf pljex.jar foo
    $ cp pljex.jar /usr/local/hawq/lib/postgresql/java/
    ```
 
5. Start the `psql` subsystem:

    ``` shell
    $ psql -d testdb
    ```

6. Add the JAR file to the session-level classpath:

    ``` sql
    => SET pljava_classpath='pljex.jar';
    ```

7. Create a PL/Java UDF that invokes the `Fum` class `createComplexType()` method, taking two integers as input:

    ```sql
    => CREATE FUNCTION createComplexTest(int, int)
         RETURNS complexTestType
         AS 'foo.fee.Fum.complexReturn'
       IMMUTABLE LANGUAGE java;
    ```

8. Execute the `createComplexTest()` UDF, providing 2 integers  as input:

    ```sql
    => SELECT createComplexTest(11,22);
    ```

    ```
              createcomplextest           
    --------------------------------------
     (11,33,"2016-12-31 23:04:09.388-08")
    (1 row)
    ```
    
    As described, the UDF, when executed, returns the first input integer, the sum of the first and second input integers, and the current timestamp.

### <a id="functionreturnsets"></a>Functions that Return Sets

PL/Java supports user-defined functions that return sets of both scalar and complex types. 

The HAWQ backend expects a function that `RETURNS` a `SETOF` to return one row at a time.

### <a id="returnsetofscalar"></a>Returning a SETOF &lt;Scalar Type&gt; 

To return a set of a scalar type, the Java method must return an object that implements the `java.util.Iterator` interface. 

Example: Function that returns a SETOF varchar:

1. Create a new file named `Bar.java`, adding the following text to create a class named `Bar` with a single method named `getNames()`. This method uses an `Iterator` to collect and return a list of string names:

    ``` shell
    $ cd $PLJAVAWORK/pljex/foo/fee
    $ vi Bar.java
    ```

    ``` java
    package foo.fee;
    import java.util.ArrayList;
    import java.util.Iterator;

    public class Bar
    {
        public static Iterator getNames()
        {
            ArrayList names = new ArrayList();
            names.add("Lisa");
            names.add("Bob");
            names.add("Bill");
            names.add("Sally");
            return names.iterator();
        }
    }
    ```


3. Compile the `Bar` class (ignore warnings), create the JAR file, and copy the JAR file to the default PL/Java classpath directory:

    ``` shell
    $ javac *.java
    $ cd ../..
    $ jar cf pljex.jar foo
    $ cp pljex.jar /usr/local/hawq/lib/postgresql/java/
    ```
 
5. Start the `psql` subsystem:

    ``` shell
    $ psql -d testdb
    ```

6. Add the JAR file to the session-level classpath:

    ``` sql
    => SET pljava_classpath='pljex.jar';
    ```

7. Create a PL/Java UDF that invokes the `Bar` class `getNames()` method:

    ``` sql
    => CREATE FUNCTION getListOfNames()
         RETURNS SETOF varchar
         AS 'foo.fee.Bar.getNames'
       IMMUTABLE LANGUAGE java;
    ```

8. Execute the UDF:

    ``` sql
    => SELECT getListOfNames();
    ```
    
    ```
     getlistofnames 
    ----------------
     Lisa
     Bob
     Bill
     Sally
    (4 rows)
    ```
    
    The UDF returns a list of four string names.

### <a id="returnsetofcomplex"></a>Returning a SETOF &lt;Complex Type&gt; 

A method returning a set of \<complex type\> must implement either the `org.postgresql.pljava.ResultSetProvider` interface or the `org.postgresql.pljava.ResultSetHandle` interface. The interfaces provide optimal handling for distinct use cases. Use `org.postgresql.pljava.ResultSetProvider` when you want to dynamically create each row the function returns. Use `org.postgresql.pljava.ResultSetHandle` in cases where you want to return the result of an executed query.

#### Using the ResultSetProvider Interface

The `ResultSetProvider` interface has two methods:

- `boolean assignRowValues(java.sql.ResultSet tupleBuilder, int rowNumber)`
- `void close()` 

The HAWQ query evaluator calls `assignRowValues()` repeatedly until it returns false or until the evaluator decides that it does not need any more rows. At that point, it will call `close()`.

Example: Using the `ResultSetProvider` Interface

1. Create a new file named `FumSetOfComplex.java`, adding the following text to create a class named `FumSetOfComplex` that implements the `ResultSetProvider` interface:

    ``` shell
    $ cd $PLJAVAWORK/pljex/foo/fee
    $ vi FumSetOfComplex.java
    ```

    ``` java
    package foo.fee;
    import java.sql.ResultSet;
    import java.sql.SQLException;
    import java.sql.Timestamp;
    import org.postgresql.pljava.ResultSetProvider;

    public class FumSetOfComplex implements ResultSetProvider
    {
      private final int m_base;
      private final int m_increment;
      public FumSetOfComplex(int base, int increment)
      {
        m_base = base;
        m_increment = increment;
      }
      public boolean assignRowValues(ResultSet receiver, int 
currentRow)
      throws SQLException
      {
        if(currentRow >= 12)
          return false;
        receiver.updateInt(1, m_base);
        receiver.updateInt(2, m_base + m_increment * currentRow);
        receiver.updateTimestamp(3, new 
Timestamp(System.currentTimeMillis()));
        return true;
      }
      public void close()
      {
         /* Nothing needed in this example */
      }
      public static ResultSetProvider listComplex(int base, 
int increment)
      throws SQLException
      {
        return new FumSetOfComplex(base, increment);
      }
    }
    ```

    The `listComplex()` method is called once. It will return NULL if no results are available. If results are available, `listComplex()` will return an instance of a `ResultSetProvider` interface. The Java class `FumSetOfComplex` implements this interface to return an instance of itself. `assignRowValues()` is called repeatedly until it returns false. At that time, `close()` is called.

3. Compile the `FumSetOfComplex` class, create the JAR file, and copy the JAR file to the default PL/Java classpath directory:

    ``` shell
    $ javac -classpath /usr/local/hawq/lib/postgresql/pljava.jar FumSetOfComplex.java
    $ cd ../..
    $ jar cf pljex.jar foo
    $ cp pljex.jar /usr/local/hawq/lib/postgresql/java/
    ```
 
5. Start the `psql` subsystem:

    ``` shell
    $ psql -d testdb
    ```

6. Add the JAR file to the session-level classpath:

    ``` sql
    => SET pljava_classpath='pljex.jar';
    ```

7. Create a PL/Java UDF that invokes the `FumSetOfComplex` class `listComplexTest()` method:

    ```sql
    => CREATE FUNCTION listComplexTest(int, int)
         RETURNS SETOF complexTestType
         AS 'foo.fee.FumSetOfComplex.listComplex'
       IMMUTABLE LANGUAGE java;
    ```

8. Execute the UDF:

    ``` sql
    => SELECT listComplexTest(1,2);
    ```
    
    ```
    testdb=# SELECT listComplexTest(1,2);
           listcomplextest           
    -------------------------------------
     (1,1,"2017-01-01 01:20:32.888-08")
     (1,3,"2017-01-01 01:20:32.888-08")
     (1,5,"2017-01-01 01:20:32.888-08")
     (1,7,"2017-01-01 01:20:32.888-08")
     (1,9,"2017-01-01 01:20:32.888-08")
    ...
    (12 rows)
    ```


#### Using the ResultSetHandle Interface

Classes implementing the `ResultSetHandle` interface must include a method to return a `ResultSet` named `getResultSet()`. The query evaluator will iterate over this set and deliver the `ResultSet` contents, one tuple at a time, to the caller until a call to `next()` returns false or the evaluator decides that no more rows are needed.

Example: Using the `ResultSetHandle` Interface

1. A `Users` class is defined in the Java example package `org.postgresql.example` (refer to [`example`](https://github.com/apache/incubator-hawq/blob/master/src/pl/pljava/src/java/examples/org/postgresql/example) for example source files):

    ``` java
    package org.postgresql.example;

    import java.sql.DriverManager;
    import java.sql.ResultSet;
    import java.sql.SQLException;
    import java.sql.Statement;

    import org.postgresql.pljava.ResultSetHandle;
    
    public class Users implements ResultSetHandle
    {
      private final String m_filter;
      private Statement m_statement;
      public Users(String filter)
      {
        m_filter = filter;
      }
      public ResultSet getResultSet()
      throws SQLException
      {
        m_statement = 
          DriverManager.getConnection("jdbc:default:connection").createStatement();
        return m_statement.executeQuery("SELECT * FROM pg_user 
           WHERE " + m_filter);
      }

      public void close()
      throws SQLException
      {
        m_statement.close();
      }

      public static ResultSetHandle listSupers()
      {
        return new Users("usesuper = true");
      }

      public static ResultSetHandle listNonSupers()
      {
        return new Users("usesuper = false");
      }
    }
    ```
    
    The `listSupers()` and `listNonSupers()` methods each execute a query to return a `ResultSetHandle` containing a list of those users with and without superuser privileges, respectively. 

2. Copy the `examples.jar` file to the default PL/Java classpath directory:

    ``` shell
    $ cp /usr/local/hawq/share/postgresql/pljava/examples.jar  /usr/local/hawq/lib/postgresql/java/
    ```
    
2. Start the `psql` subsystem:

    ``` shell
    $ psql -d testdb
    ```

6. Add the `examples.jar` JAR file to the session-level classpath:

    ``` sql
    => SET pljava_classpath='examples.jar';
    ```

7. Create PL/Java UDFs that execute the `listSupers()` and `listNonSupers()` methods in the `org.postgresql.example.Users` class:

    ``` sql
    => CREATE FUNCTION plistSupers()
         RETURNS SETOF pg_user
         AS 'org.postgresql.example.Users.listSupers'
       LANGUAGE java;
    => CREATE FUNCTION plistNonSupers()
         RETURNS SETOF pg_user
         AS 'org.postgresql.example.Users.listNonSupers'
       LANGUAGE java;
    ```

8. Execute the UDFs:

    ``` sql
    => SELECT plistSupers();
    ```
    
    ```
              plistsupers           
    -------------------------------
     (gpadmin,10,t,t,t,********,,)
    (1 row)
    ```
    
    ``` sql
    => SELECT plistNonSupers();
    ```
    
    ```
     plistnonsupers 
    ---------------
    (0 rows)
    ```

    
## <a id="usingjdbc"></a>Using JDBC 

PL/Java includes a JDBC driver. This driver invokes HAWQ internal SPI routines. The driver is essential; it is common for functions to make calls back to the database to fetch data. When PL/Java user-defined functions fetch data, they must use the same transactional boundaries that are used by the main function that entered the PL/Java execution context.

You can obtain a PL/Java JDBC driver connection mapping to the current transaction with the following Java statement:

``` java
Connection conn = 
  DriverManager.getConnection("jdbc:default:connection"); 
```

After obtaining a connection, you can prepare and execute statements similar to other JDBC connections. Refer to the `Users` class Java source code from the example above. 

Limitations of the PL/Java JDBC driver include the following:

- A transaction cannot be managed in any way. As such, you cannot use the following methods on the JDBC connection:
   - `commit()`
   - `rollback()`
   - `setAutoCommit()`
   - `setTransactionIsolation()`
- Savepoints are available, with some restrictions. A savepoint cannot outlive the function in which it was set, and it must be rolled back or released by that same function.
- A `ResultSet` returned from `executeQuery()` is always `FETCH_FORWARD` and `CONCUR_READ_ONLY`.
- `CallableStatement` (for stored procedures) is not implemented.
- The types `Clob` and `Blob` are not completely implemented. Use the types `byte[]` and `String` for `bytea` and `text`, respectively.

## <a id="exceptionhandling"></a>Exception Handling 

You can catch and handle an exception in the HAWQ backend just like any other exception. The backend `ErrorData` structure is exposed as a property in the `org.postgresql.pljava.internal.ServerException` class (derived from `java.sql.SQLException`), and the Java `try/catch` construct is synchronized with the backend mechanism.

**Important:** If the backend generates an exception and you have set a savepoint, the exception condition is reset when the savepoint is rolled back, allowing you to continue your execution. If the backend has generated an exception and you have *not* used a savepoint, then you cannot execute backend functions until your function propagates the error and returns.

## <a id="savepoints"></a>Savepoints 

HAWQ exposes savepoints using the `java.sql.Connection` interface. Two restrictions apply:

- A savepoint must be rolled back or released in the function in which it was set.
- A savepoint must not outlive the function from which it was set.

## <a id="logging"></a>Logging 

PL/Java uses the standard Java Logger. For example:

``` java
Logger.getAnonymousLogger().info( "Time is " + new 
    Date(System.currentTimeMillis()));
```

The logger uses a handler that maps the current setting of the HAWQ `log_min_messages` server configuration parameter to a valid Java logging level, using the HAWQ backend function `elog()` to output all messages.

**Note:** The `log_min_messages` setting is read from the database the first time a PL/Java function in a session is executed and can only be changed by restarting the HAWQ session.

The table below identifies the Java to HAWQ log level mapping:

**Table 2: PL/Java Logging Levels Mappings**

| java.util.logging.Level | HAWQ Level |
|-------------------------|------------|
| SEVERE | ERROR |
| WARNING |	WARNING |
| CONFIG |	LOG |
| INFO | INFO |
| FINE | DEBUG1 |
| FINER | DEBUG2 |
| FINEST | DEBUG3 |


## <a id="pljavaexample"></a>Example 

The following example:

1. Creates a Java class with a single method.
2. Creates a PL/Java UDF that invokes the method.
3. Executes the PL/Java UDF on a simple table.

**Note**: This example requires a Java SDK be installed on your development system.

1. Create a work area for the example:

    ``` shell
    $ mkdir -p $PLJAVAWORK/example/com/exco/app
    $ cd $PLJAVAWORK/example/com/exco/app
    ```

2. Create a new file named `SubStr.java`, adding the following text to create a class named `SubStr` with a single method named `substring()`. This method takes a text string and two index integers as input and returns the string bounded by the indexes:

    ``` shell
    $ vi SubStr.java
    ```

    ``` java
    package com.exco.app;
    import java.util.logging.Logger;
    
    public class SubStr
    {
      public static String substring(String text, int beginIndex, int endIndex)
        {
          return text.substring(beginIndex, endIndex);
        }
    }
    ```

3. Compile the `SubStr` class, create a JAR file named `exsubstr.jar`, and copy this JAR file to the default PL/Java classpath directory:

    ``` shell
    $ javac *.java
    $ cd ../../..
    $ jar cf exsubstr.jar com
    $ cp exsubstr.jar /usr/local/hawq/lib/postgresql/java/
    ```
 
5. Start the `psql` subsystem:

    ``` shell
    $ psql -d testdb
    ```

6. Add the JAR file to the session-level classpath:

    ``` sql
    => SET pljava_classpath='exsubstr.jar';
    ```

7. Create a HAWQ internal table named `extblwstrings`:

    ``` sql
    => CREATE TABLE extblwstrings (a varchar) DISTRIBUTED randomly;
    ```

8. Insert some string data into the `extblwstrings` table:

    ``` sql
    => INSERT INTO extblwstrings VALUES ('my string');
    => INSERT INTO extblwstrings VALUES ('secondstring');
    => INSERT INTO extblwstrings VALUES ('abcdefghij');
    ```

9. Create a PL/Java UDF that invokes the `com.exco.app.SubStr` class `substring()` method defined earlier:

    ``` sql
    => CREATE OR REPLACE FUNCTION ex_getsubstring(varchar, int, int) 
         RETURNS varchar AS 'com.exco.app.SubStr.substring' 
       LANGUAGE java;
    ```

8. Execute the UDF:

    ``` sql
    => SELECT ex_getsubstring( a, 3, 7) FROM extblwstrings;
    ```
    
    ```
     ex_getsubstring 
    -----------------
     stri
     onds
     defg
    (3 rows)
    ```

10. If you add each of the above SQL commands to a file, you can run the commands from the command line or the `psql` subsystem. Add the following text to a file named `/tmp/myexample.sql`:

    ``` shell
    $ vi /tmp/myexample.sql
    ```
    
    ```
    DROP TABLE IF EXISTS extblwstrings;
    SET pljava_classpath='exsubstr.jar';
    CREATE TABLE extblwstrings (a varchar) DISTRIBUTED randomly;
    INSERT INTO extblwstrings VALUES ('my string');
    INSERT INTO extblwstrings VALUES ('secondstring');
    INSERT INTO extblwstrings VALUES ('abcdefghij');
    CREATE OR REPLACE FUNCTION ex_getsubstring(varchar, int, int) 
      RETURNS varchar AS 'com.exco.app.SubStr.substring' 
    LANGUAGE java;
    SELECT ex_getsubstring( a, 3, 7) FROM extblwstrings;
    ```

11. Run the `myexample.sql` script file:

    ``` shell
    $ psql -d testdb -f /tmp/myexample.sql 
    DROP TABLE
    SET
    CREATE TABLE
    INSERT 0 1
    INSERT 0 1
    INSERT 0 1
    CREATE FUNCTION
     ex_getsubstring 
    -----------------
     stri
     onds
     defg
    (3 rows)
    ```
    
    ``` shell
    $ psql -d testdb
    ```
    
    ``` sql
    => \i /tmp/myexample.sql 
    ...
    ```
