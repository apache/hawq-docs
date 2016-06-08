---
title: Using Procedural Languages in HAWQ
---

HAWQ allows user-defined functions to be written in other languages besides SQL and C. These other languages are generically called *procedural languages* (PLs).

For a function written in a procedural language, the database server has no built-in knowledge about how to interpret the function's source text. Instead, the task is passed to a special handler that knows the details of the language. The handler could either do all the work of parsing, syntax analysis, execution, and so on itself, or it could serve as "glue" between HAWQ and an existing implementation of a programming language. The handler itself is a C language function compiled into a shared object and loaded on demand, just like any other C function.

This chapter describes the following:

-   <a href="using_pljava.html">Using PL/Java</a>
-   <a href="using_plpgsql.html">Using PL/pgSQL</a>
-   <a href="using_plr.html">Using PL/R</a>




