use WebminCore;
&init_config();

sub start_couchbase{
local $temp_file = &transname();
local $cmd = &system_logged("($config{'start_cmd'}) >$temp_file 2>&1");
local $out = `cat $temp_file`; unlink($temp_file);
if ($out =~ /failed/i) {
        return "<pre>$out</pre>";
        }
return undef;
}

