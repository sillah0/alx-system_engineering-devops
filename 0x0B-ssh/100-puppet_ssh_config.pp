# sets up a client ssh config file so that we can connect to a server with no password

$file_content = file('/etc/ssh/ssh_config')
$config = "${file_content}\
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
"
file { 'school':
    ensure => 'present'
    path => '/etc/ssh/ssh_config',
    content => $config
}
