---
title: Using PL/Perl
---

This section contains an overview of the HAWQ PL/Perl language extension.

## <a id="enableplperl"></a>Enabling PL/Perl

If PL/Perl is enabled during HAWQ build time, HAWQ installs the PL/Perl language extension automatically. To use PL/Perl, you must enable it on specific databases.

On every database where you want to enable PL/Perl, connect to the database using the psql client.

``` shell
$ psql -d <dbname>
```

Replace \<dbname\> with the name of the target database.

Then, run the following SQL command:

``` shell
psql# CREATE LANGUAGE plperl;
```

## <a id="references"></a>References 

For more information on using PL/Perl, see the PostgreSQL PL/Perl documentation at [https://www.postgresql.org/docs/8.2/static/plperl.html](https://www.postgresql.org/docs/8.2/static/plperl.html).