# Apache HAWQ (incubating) End-User Documentation

This repository provides the full source for Apache HAWQ (incubating) end-user documentation in MarkDown format. You can build the source files into HTML by using [Bookbinder](https://github.com/cloudfoundry-incubator/bookbinder) or other MarkDown tools.

Bookbinder is a Ruby gem that binds together a unified documentation web application from markdown, html, and/or DITA source material. The source material for bookbinder must be stored either in local directories or in GitHub repositories. Bookbinder runs [middleman](http://middlemanapp.com/) to produce a Rackup app that can be deployed locally or as a Web application.

This document contains instructions for building the local Apache HAWQ (incubating) documentation. It contains the sections:

* [Bookbinder Usage](#usage)
* [Prerequisites](#prereq)
* [Building the Documentation](#building)
* [Publishing the Documentation](#publishing)
* [Getting More Information](#moreinfo)

<a name="usage"></a>
## Bookbinder Usage

Bookbinder is meant to be used from within a project called a **book**. The book includes a configuration file that describes which documentation repositories to use as source materials. Bookbinder provides a set of scripts to aggregate those repositories and publish them to various locations in your final web application.

For Apache HAWQ (incubating), a preconfigured **book** is provided in the `/book` directory of this repo.  You can use this configuration to build the HTML for HAWQ on your local system.

<a name="prereq"></a>
## Prerequisites

* Ruby version 2.3.0 or higher.
* Ruby [bundler](http://bundler.io/) installed for gem package management.

<a name="building"></a>
## Building the Documentation

1. Change to the `book` directory of this repo.

2. Install bookbinder and its dependent gems. Make sure you are in the `book` directory and enter:

    ``` bash
    $ bundle install
    ```

3. The installed `config.yml` file configures the book for building from your local HAWQ source files.  Build the output HTML files by executing the command:

    ``` bash
    $ bundle exec bookbinder bind local
    ```

   Bookbinder converts the XML source into HTML, and puts the final output in the `final_app` directory.
  
5. The `final_app` directory stages the HTML into a web application that you can view using the rack gem. To view the documentation build:

    ``` bash
    $ cd final_app
    $ bundle install
    $ rackup
    ```

   Your local documentation is now available for viewing at[http://localhost:9292](http://localhost:9292)

<a name="moreinfo"></a>  
## Getting More Information

Bookbinder provides additional functionality to construct books from multiple Github repos, to perform variable substitution, and also to automatically build documentation in a continuous integration pipeline.  For more information, see [https://github.com/cloudfoundry-incubator/bookbinder](https://github.com/cloudfoundry-incubator/bookbinder).

