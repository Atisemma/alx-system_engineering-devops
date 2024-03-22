#!/bin/bash
exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => ['/usr/bin', '/bin'],
  refreshonly => true,
}
