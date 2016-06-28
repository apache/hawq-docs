---
title: Creating and Managing Views
---

Views enable you to save frequently used or complex queries, then access them in a `SELECT` statement as if they were a table. A view is not physically materialized on disk: the query runs as a subquery when you access the view.

If a subquery is associated with a single query, consider using the `WITH` clause of the `SELECT` command instead of creating a seldom-used view.

## Creating Views <a id="topic101"></a>

The `CREATE VIEW`command defines a view of a query. For example:

``` sql
CREATE VIEW comedies AS SELECT * FROM films WHERE kind = 'comedy';
```

Views ignore `ORDER BY` and `SORT` operations stored in the view.

## Dropping Views <a id="topic102"></a>

The `DROP VIEW` command removes a view. For example:

``` sql
DROP VIEW topten;
```
