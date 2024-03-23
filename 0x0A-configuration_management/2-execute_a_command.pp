#!/bin/bash
exec { 'killmenow':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}
