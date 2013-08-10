#!/usr/bin/perl
# index.cgi

require './couchbase-lib.pl';
&ReadParse();

&ui_print_header(undef, $module_info{'desc'}, "", undef, 1, 1);

if (-e $config{'couchbase_init_file'}) {
  print &ui_buttons_start();
  print &ui_buttons_row("start.cgi", $text{'index_start'}, $text{'index_startmsg'});
  print &ui_buttons_row("stop.cgi", $text{'index_stop'}, $text{'index_stopmsg'});
  print &ui_buttons_end();
}
else {
  print "<p> <b>$text{'cb_not_loaded'}</b> <p>\n";
  print "You can install from <a href=\"http://www.couchbase.com/downloads-all\">here</a>"
}

