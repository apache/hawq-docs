---
title: Using PL/Java
---

This section contains an overview of the HAWQ PL/Java language. 

<p class="note"><b>Note:</b> For details on how to install PL/Java, see <a href="/hdb/install/install_pljava.html">Installing PL/Java</a>.</p>


## About PL/Java <a id="aboutpljava"></a>

With the HAWQ PL/Java extension, you can write Java methods using your favorite Java IDE and install the JAR files that contain the methods in your HAWQ cluster.

The HAWQ PL/Java package is based on the open source PL/Java 1.4.0. HAWQ PL/Java provides the following features.

- Ability to execute PL/Java functions with Java 1.6 or higher.
- Standardized utilities (modeled after the SQL 2003 proposal) to install and maintain Java code in the database.
- Standardized mappings of parameters and result. Complex types as well as sets are supported.
- An embedded, high performance, JDBC driver utilizing the internal HAWQ Database SPI routines.
- Metadata support for the JDBC driver. Both `DatabaseMetaData` and `ResultSetMetaData` are included.
- The ability to return a `ResultSet` from a query as an alternative to building a ResultSet row by row.
- Full support for savepoints and exception handling.
- The ability to use IN, INOUT, and OUT parameters.
- Two separate HAWQ languages:
	- pljava, TRUSTED PL/Java language
	- pljavau, UNTRUSTED PL/Java language
- Transaction and Savepoint listeners enabling code execution when a transaction or savepoint is committed or rolled back.
- Integration with GNU GCJ on selected platforms.

A function in SQL will appoint a static method in a Java class. In order for the function to execute, the appointed class must available on the class path specified by the HAWQ server configuration parameter `pljava_classpath`. The PL/Java extension adds a set of functions that helps to install and maintain the Java classes. Classes are stored in normal Java archives, JAR files. A JAR file can optionally contain a deployment descriptor that in turn contains SQL commands to be executed when the JAR is deployed or undeployed. The functions are modeled after the standards proposed for SQL 2003.

PL/Java implements a standard way of passing parameters and return values. Complex types and sets are passed using the standard JDBC ResultSet class.

A JDBC driver is included in PL/Java. This driver calls HAWQ internal SPI routines. The driver is essential since it is common for functions to make calls back to the database to fetch data. When PL/Java functions fetch data, they must use the same transactional boundaries that are used by the main function that entered PL/Java execution context.

PL/Java is optimized for performance. The Java virtual machine executes within the same process as the backend to minimize call overhead. PL/Java is designed with the objective to enable the power of Java to the database itself so that database intensive business logic can execute as close to the actual data as possible.

The standard Java Native Interface (JNI) is used when bridging calls between the backend and the Java VM.


## About HAWQ PL/Java <a id="abouthawqpljava"></a>

There are a few key differences between the implementation of PL/Java in standard PostgreSQL and HAWQ.

### Functions <a id="pljavafunctions"></a>

The following functions are not supported in HAWQ. The classpath is handled differently in a distributed HAWQ environment than in the PostgreSQL environment.

- sqlj.install_jar
- sqlj.install_jar
- sqlj.replace_jar
- sqlj.remove_jar
- sqlj.get_classpath
- sqlj.set_classpath

HAWQ uses the `pljava_classpath` server configuration parameter in place of the `sqlj.set_classpath` function.

### Server Configuration Parameters <a id="serverconfigparams"></a>

The following server configuration parameters are used by PL/Java in HAWQ. These parameters replace the `pljava.*` parameters that are used in the standard PostgreSQL PL/Java implementation.

<p class="note"><b>Note:</b> See the <a href="/20/reference/hawq-reference.html">HAWQ Reference</a> for information about HAWQ server configuration parameters.</p>

#### pljava\_classpath

A colon (:) separated list of the jar files containing the Java classes used in any PL/Java functions. The jar files must be installed in the same locations on all HAWQ hosts. With the trusted PL/Java language handler, jar file paths must be relative to the `$GPHOME/lib/postgresql/java/` directory. With the untrusted language handler (javaU language tag), paths may be relative to `$GPHOME/lib/postgresql/java/` or absolute.

#### pljava\_statement\_cache\_size

Sets the size in KB of the Most Recently Used (MRU) cache for prepared statements.

#### pljava\_release\_lingering\_savepoints

If TRUE, lingering savepoints will be released on function exit. If FALSE, they will be rolled back.

#### pljava\_vmoptions

Defines the start up options for the Java VM.


## Writing PL/Java Functions <a id="writingpljavafunc"></a>

This section provides information about writing functions with PL/Java.

- [SQL Declaration](#sqldeclaration)
- [Type Mapping](#typemapping)
- [NULL Handling](#nullhandling)
- [Complex Types](#complextypes)
- [Returning Complex Types](#returningcomplextypes)
- [Functions That Return Sets](#functionreturnsets)
- [Returning a SETOF \<scalar type\>](#returnsetofscalar)
- [Returning a SETOF \<complex type\>](#returnsetofcomplex)


### SQL Declaration <a id="sqldeclaration"></a>

A Java function is declared with the name of a class and a static method on that class. The class will be resolved using the classpath that has been defined for the schema where the function is declared. If no classpath has been defined for that schema, the public schema is used. If no classpath is found there either, the class is resolved using the system classloader.

The following function can be declared to access the static method getProperty on `java.lang.System` class:

```sql
CREATE FUNCTION getsysprop(VARCHAR)
  RETURNS VARCHAR
  AS 'java.lang.System.getProperty'
  LANGUAGE java;
```

Run the following command to return the Java `user.home` property:

```sql
SELECT getsysprop('user.home');
```

### Type Mapping <a id="typemapping"></a>

Scalar types are mapped in a straightforward way. This table lists the current mappings.

***Table 1: PL/Java data type mappings***

| PostgreSQL | Java |
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

All other types are mapped to `java.lang.String` and will utilize the standard textin/textout routines registered for respective type.

### NULL Handling <a id="nullhandling"></a>

The scalar types that map to Java primitives can not be passed as NULL values. To pass NULL values, those types can have an alternative mapping. You enable this mapping by explicitly denoting it in the method reference.

```sql
CREATE FUNCTION trueIfEvenOrNull(integer)
  RETURNS bool
  AS 'foo.fee.Fum.trueIfEvenOrNull(java.lang.Integer)'
  LANGUAGE java;
```

The Java code would be similar to this:

```java
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

The following two statements both yield true:

```sql
SELECT trueIfEvenOrNull(NULL);
SELECT trueIfEvenOrNull(4);
```

In order to return NULL values from a Java method, you use the object type that corresponds to the primitive (for example, you return `java.lang.Integer` instead of `int`). The PL/Java resolve mechanism finds the method regardless. Since Java cannot have different return types for methods with the same name, this does not introduce any ambiguity.

### Complex Types <a id="complextypes"></a>

A complex type will always be passed as a read-only `java.sql.ResultSet` with exactly one row. The `ResultSet` is positioned on its row so a call to `next()` should not be made. The values of the complex type are retrieved using the standard getter methods of the `ResultSet`.

Example:

```sql
CREATE TYPE complexTest
  AS(base integer, incbase integer, ctime timestamptz);
CREATE FUNCTION useComplexTest(complexTest)
  RETURNS VARCHAR
  AS 'foo.fee.Fum.useComplexTest'
  IMMUTABLE LANGUAGE java;
```

In the Java class `Fum`, we add the following static method:

```java
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

### Returning Complex Types <a id="returningcomplextypes"></a>

Java does not stipulate any way to create a `ResultSet`. Hence, returning a ResultSet is not an option. The SQL-2003 draft suggests that a complex return value should be handled as an IN/OUT parameter. PL/Java implements a `ResultSet` that way. If you declare a function that returns a complex type, you will need to use a Java method with boolean return type with a last parameter of type `java.sql.ResultSet`. The parameter will be initialized to an empty updateable ResultSet that contains exactly one row.

Assume that the complexTest type in previous section has been created.

```sql
CREATE FUNCTION createComplexTest(int, int)
  RETURNS complexTest
  AS 'foo.fee.Fum.createComplexTest'
  IMMUTABLE LANGUAGE java;
```

The PL/Java method resolve will now find the following method in the `Fum` class:

```java
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

The return value denotes if the receiver should be considered as a valid tuple (true) or NULL (false).

### Functions that Return Sets <a id="functionreturnsets"></a>

When returning result set, you should not build a result set before returning it, because building a large result set would consume a large amount of resources. It is better to produce one row at a time. Incidentally, that is what the HAWQ backend expects a function with SETOF return to do. You can return a SETOF a scalar type such as an int, float or varchar, or you can return a SETOF a complex type.

### Returning a SETOF \<scalar type\> <a id="returnsetofscalar"></a>

In order to return a set of a scalar type, you need create a Java method that returns something that implements the `java.util.Iterator` interface. Here is an example of a method that returns a SETOF varchar:

```sql
CREATE FUNCTION javatest.getSystemProperties()
  RETURNS SETOF varchar
  AS 'foo.fee.Bar.getNames'
  IMMUTABLE LANGUAGE java;
```

This simple Java method returns an iterator:

```java
package foo.fee;
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

### Returning a SETOF \<complex type\> <a id="returnsetofcomplex"></a>

A method returning a SETOF <complex type> must use either the interface `org.postgresql.pljava.ResultSetProvider` or `org.postgresql.pljava.ResultSetHandle`. The reason for having two interfaces is that they cater for optimal handling of two distinct use cases. The former is for cases when you want to dynamically create each row that is to be returned from the SETOF function. The latter makes is in cases where you want to return the result of an executed query.

#### Using the ResultSetProvider Interface

This interface has two methods. The boolean `assignRowValues(java.sql.ResultSet tupleBuilder, int rowNumber)` and the `void close()` method. The HAWQ query evaluator will call the `assignRowValues` repeatedly until it returns false or until the evaluator decides that it does not need any more rows. Then it calls close.

You can use this interface the following way:

```sql
CREATE FUNCTION javatest.listComplexTests(int, int)
  RETURNS SETOF complexTest
  AS 'foo.fee.Fum.listComplexTest'
  IMMUTABLE LANGUAGE java;
```

The function maps to a static java method that returns an instance that implements the `ResultSetProvider` interface.

```java
public class Fum implements ResultSetProvider
{
  private final int m_base;
  private final int m_increment;
  public Fum(int base, int increment)
  {
    m_base = base;
    m_increment = increment;
  }
  public boolean assignRowValues(ResultSet receiver, int 
currentRow)
  throws SQLException
  {
    // Stop when we reach 12 rows.
    //
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
   // Nothing needed in this example
  }
  public static ResultSetProvider listComplexTests(int base, 
int increment)
  throws SQLException
  {
    return new Fum(base, increment);
  }
}
```

The `listComplextTests` method is called once. It may return NULL if no results are available or an instance of the `ResultSetProvider`. Here the Java class `Fum` implements this interface so it returns an instance of itself. The method `assignRowValues` will then be called repeatedly until it returns false. At that time, close will be called.

#### Using the ResultSetHandle Interface

This interface is similar to the `ResultSetProvider` interface in that it has a `close()` method that will be called at the end. But instead of having the evaluator call a method that builds one row at a time, this method has a method that returns a `ResultSet`. The query evaluator will iterate over this set and deliver the `ResultSet` contents, one tuple at a time, to the caller until a call to `next()` returns false or the evaluator decides that no more rows are needed.

Here is an example that executes a query using a statement that it obtained using the default connection. The SQL suitable for the deployment descriptor looks like this:

```sql
CREATE FUNCTION javatest.listSupers()
  RETURNS SETOF pg_user
  AS 'org.postgresql.pljava.example.Users.listSupers'
  LANGUAGE java;
CREATE FUNCTION javatest.listNonSupers()
  RETURNS SETOF pg_user
  AS 'org.postgresql.pljava.example.Users.listNonSupers'
  LANGUAGE java;
```

And in the Java package `org.postgresql.pljava.example` a class `Users` is added:

```java
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
      DriverManager.getConnection("jdbc:default:connection").cr
eateStatement();
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
## Using JDBC <a id="usingjdbc"></a>

PL/Java contains a JDBC driver that maps to the PostgreSQL SPI functions. A connection that maps to the current transaction can be obtained using the following statement:

```java
Connection conn = 
  DriverManager.getConnection("jdbc:default:connection"); 
```

After obtaining a connection, you can prepare and execute statements similar to other JDBC connections. These are limitations for the PL/Java JDBC driver:

- The transaction cannot be managed in any way. Thus, you cannot use methods on the connection such as:
   - `commit()`
   - `rollback()`
   - `setAutoCommit()`
   - `setTransactionIsolation()`
- Savepoints are available with some restrictions. A savepoint cannot outlive the function in which it was set and it must be rolled back or released by that same function.
- A ResultSet returned from `executeQuery()` are always `FETCH_FORWARD` and `CONCUR_READ_ONLY`.
- Meta-data is only available in PL/Java 1.1 or higher.
- `CallableStatement` (for stored procedures) is not implemented.
- The types `Clob` or `Blob` are not completely implemented, they need more work. The types `byte[]` and `String` can be used for `bytea` and `text` respectively.

## Exception Handling <a id="exceptionhandling"></a>

You can catch and handle an exception in the HAWQ backend just like any other exception. The backend `ErrorData` structure is exposed as a property in a class called `org.postgresql.pljava.ServerException` (derived from `java.sql.SQLException`) and the Java try/catch mechanism is synchronized with the backend mechanism.

**Important:** You will not be able to continue executing backend functions until your function has returned and the error has been propagated when the backend has generated an exception unless you have used a savepoint. When a savepoint is rolled back, the exceptional condition is reset and you can continue your execution.

## Savepoints <a id="savepoints"></a>

HAWQ savepoints are exposed using the `java.sql.Connection` interface. Two restrictions apply.

- A savepoint must be rolled back or released in the function where it was set.
- A savepoint must not outlive the function where it was set.

## Logging <a id="logging"></a>

PL/Java uses the standard Java Logger. Hence, you can write things like:

```java
Logger.getAnonymousLogger().info( "Time is " + new 
Date(System.currentTimeMillis()));
```

At present, the logger uses a handler that maps the current state of the HAWQ configuration setting `log_min_messages` to a valid Logger level and that outputs all messages using the HAWQ backend function `elog()`.

**Note:** The `log_min_messages` setting is read from the database the first time a PL/Java function in a session is executed. On the Java side, the setting does not change after the first PL/Java function execution in a specific session until the HAWQ session that is working with PL/Java is restarted.

The following mapping apply between the Logger levels and the HAWQ backend levels.

***Table 2: PL/Java Logging Levels Mappings***

| java.util.logging.Level | HAWQ Level |
|-------------------------|------------|
| SEVERE ERROR | ERROR |
| WARNING |	WARNING |
| CONFIG |	LOG |
| INFO | INFO |
| FINE | DEBUG1 |
| FINER | DEBUG2 |
| FINEST | DEBUG3 |

## Security <a id="security"></a>

This section describes security aspects of using PL/Java.

### Installation <a id="installation"></a>

Only a database super user can install PL/Java. The PL/Java utility functions are installed using SECURITY DEFINER so that they execute with the access permissions that where granted to the creator of the functions.

### Trusted Language <a id="trustedlang"></a>

PL/Java is a trusted language. The trusted PL/Java language has no access to the file system as stipulated by PostgreSQL definition of a trusted language. Any database user can create and access functions in a trusted language.

PL/Java also installs a language handler for the language `javau`. This version is not trusted and only a superuser can create new functions that use it. Any user can call the functions.


## Example <a id="pljavaexample"></a>

The following simple Java example creates a JAR file that contains a single method and runs the method.

<p class="note"><b>Note:</b> The example requires Java SDK to compile the Java file.</p>

The following method returns a substring.

```java
{
public static String substring(String text, int beginIndex,
  int endIndex)
    {
    return text.substring(beginIndex, endIndex);
    }
}
```

Enter the Java code in a text file `example.class`.

Contents of the file `manifest.txt`:

```plaintext
Manifest-Version: 1.0
Main-Class: Example
Specification-Title: "Example"
Specification-Version: "1.0"
Created-By: 1.6.0_35-b10-428-11M3811
Build-Date: 01/20/2013 10:09 AM
```

Compile the Java code:

```shell
$ javac *.java
```

Create a JAR archive named `analytics.jar` that contains the class file and the manifest file in the JAR.

```shell
$ jar cfm analytics.jar manifest.txt *.class
```

Upload the JAR file to the HAWQ master host.

Run the `hawq scp` utility to copy the jar file to the HAWQ Java directory. Use the `-f` option to specify the file that contains a list of the master and segment hosts.

```shell
$ hawq scp -f hawq_hosts analytics.jar =:/usr/local/hawq/lib/postgresql/java/
```

Use the `hawq config` utility to set the HAWQ `pljava_classpath` server configuration parameter. The parameter lists the installed JAR files.

```shell
$ hawq config -c pljava_classpath -v \'analytics.jar\'
```

Run the `hawq restart` utility to reload the configuration files.

```shell
$ hawq restart cluster
```

From the `psql` command line, run the following command to show the installed JAR files.

```shell
psql# show pljava_classpath
```

The following SQL commands create a table and define a Java function to test the method in the JAR file:

```sql
CREATE TABLE temp (a varchar) DISTRIBUTED randomly; 
INSERT INTO temp values ('my string'); 
--Example function 
CREATE OR REPLACE FUNCTION java_substring(varchar, int, int) 
RETURNS varchar AS 'Example.substring' LANGUAGE java; 
--Example execution 
SELECT java_substring(a, 1, 5) FROM temp;
```

You can place the contents in a file, `mysample.sql` and run the command from a psql command line:

```shell
psql# \i mysample.sql 
```

The output is similar to this:

```shell
java_substring
----------------
 y st
(1 row)
```