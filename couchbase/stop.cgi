#!/usr/bin/perl
# stop.cgi
# Stop the Couchbase Server

require './couchbase-lib.pl';
&error_setup($text{'stop_err'});
$err = &stop_couchbase();
&error($err) if ($err);
&webmin_log("stop");
&redirect("");


