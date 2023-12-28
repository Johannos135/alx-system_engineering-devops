# Kills a process named killmenow

exec { 'pkill killmenow':
  path     => ['/usr/bin', '/usr/sbin'],
  command  => 'pkill -f killmenow',
  provider => shell,
}
