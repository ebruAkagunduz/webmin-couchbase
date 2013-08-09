use WebminCore;
&init_config();

sub start_couchbase{
  local $out;
  $out = &backquote_logged("$config{'start_cmd'} 2>&1");
  
  if ($out =~ /failed/i) {
    return "<pre>$out</pre>";
  }
  return undef;
}

sub stop_couchbase{
  local $out;
  $out = &backquote_logged("$config{'stop_cmd'} 2>&1");
  
  if ($out =~ /failed/i) {
    return "<pre>$out</pre>";
  }
  return undef;

}
