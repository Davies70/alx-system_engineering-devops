# execute a command

exec { 'pkill killmenow':
  command => 'pkill killmenow',
  path    => '/bin',
}
