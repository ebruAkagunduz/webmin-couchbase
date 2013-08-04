#!/usr/bin/perl
# start.cgi
# Start the Couchbase server

require './couchbase-lib.pl';
&error_setup($text{'start_err'});
$err = &start_couchbase();
&error($err) if ($err);
sleep(3);
&webmin_log("start");
&redirect("");

