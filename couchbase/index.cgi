#!/usr/bin/perl
# index.cgi

require './couchbase-lib.pl';
&ReadParse();

&ui_print_header(undef, $module_info{'desc'}, "", undef, 1, 1);
print &ui_buttons_row("start.cgi", $text{'index_start'}, $text{'index_startmsg'});
print &ui_buttons_row("stop.cgi", $text{'index_stop'}, $text{'index_stopmsg'});
