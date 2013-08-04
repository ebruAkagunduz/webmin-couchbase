use WebminCore;
init_config();

sub start_couchbase{
local $temp = &transname();
local $rv = &system_logged("($config{'start_cmd'}) >$temp 2>&1");
local $out = `cat $temp`; unlink($temp);
if ($rv || $out =~ /failed/i) {
        return "<pre>$out</pre>";
        }
return undef;
}

