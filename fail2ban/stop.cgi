#!/usr/local/bin/perl
# stop.cgi
# Stop the running fail2ban process

require './fail2ban-lib.pl';
&ReadParse();
$access{'stop'} || &error($text{'stop_ecannot'});
&error_setup($text{'stop_err'});
$err = &stop_sendmail();
&error($err) if ($err);
&webmin_log("stop");
&redirect("");

