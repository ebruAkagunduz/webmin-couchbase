#!/usr/bin/perl
# index.cgi

require './couchbase-lib.pl';
&ReadParse();

ui_print_header(undef, $module_info{'desc'}, "", undef, 1, 1);
print "<form action=start.cgi>\n";
print "<table width=100%><tr><td>\n";
print "<input type=submit ", "value=\"$text{'index_start'}\"></td>\n";
print "<td>",&text('index_startmsg',
                   "<tt>$config{'start_cmd'}</tt>"),"</td> </tr></table>\n";
print "</form>\n";

