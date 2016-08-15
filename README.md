# Apache HAWQ (incubating) End-User Documentation

This repository provides the full source for Apache HAWQ (incubating) end-user documentation in MarkDown format. The source files can be built into HTML output using [Bookbinder](https://github.com/cloudfoundry-incubator/bookbinder) or other MarkDown tools.

Bookbinder is a gem that binds together a unified documentation web application from markdown, html, and/or DITA source material. The source material for bookbinder must be stored either in local directories or in GitHub repositories. Bookbinder runs [middleman](http://middlemanapp.com/) to produce a Rackup app that can be deployed locally or as a Web application.

This document contains instructions for building the local Apache HAWQ (incubating) documentation. It contains the sections:

* [Bookbinder Usage](#usage)
* [Prerequisites](#prereq)
* [Building the Documentation](#building)
* [Publishing the Documentation](#publishing)
* [Getting More Information](#moreinfo)

<a name="usage"></a>
## Bookbinder Usage

Bookbinder is meant to be used from within a project called a **book**. The book includes a configuration file that describes which documentation repositories to use as source materials. Bookbinder provides a set of scripts to aggregate those repositories and publish them to various locations.

For Apache HAWQ (incubating), a preconfigured **book** is provided in the directory `/hawq-book`.  You can use this configuration to build HTML for Apache HAWQ (incubating) on your local system.

<a name="prereq"></a>
## Prerequisites

* Bookbinder requires Ruby version 2.0.0-p195 or higher.

<a name="building"></a>
## Building the Documentation

1. Begin by moving or copying the `/hawq-book directory` to a directory that is parallel to `incubator-hawq/docs-apache-hawq-md`. For example:

        $ cd /repos/incubator-hawq/docs-apache-hawq-md
        $ cp -r hawq-book ..
        $ cd ../hawq-book

2. The GemFile in the book directory already defines the `gem "bookbindery"` dependency. Make sure you are in the relocated book directory and enter:

        $ bundle install
     
3. The installed `config.yml` file configures the Apache HAWQ (incubating) book for building locally.  Build the files with the command:

        $ bundle exec bookbinder bind local
    
  Bookbinder converts the XML source into HTML, putting the final output in the `final_app` directory.
  
5. Because the `final_app` directory contains the full output of the HTML conversion process, you can easily publish this directory as a hosted Web application. `final_app` contains a default configuration to serve the local files using the Rack web server:

        $ cd final_app
        $ bundle install
        $ rackup
    
  You can now view the local documentation at [http://localhost:9292](http://localhost:9292)