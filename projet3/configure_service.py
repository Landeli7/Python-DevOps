import os

def configure_apache():
	with open('/etc/apache2/apache2.conf', 'a') as apache_conf:
		apache_conf.write('ServerName localhost\n')

	os.system('sudo systemctl restart apache2')

def configure_ssh():
	with open('/etc/ssh/sshd_config', 'a') as ssh_config:
		ssh_config.write('PermitRootLogin no\n')
		ssh_config.write('PasswordAuthentication no\n')

	os.system('sudo systemctl restart ssh')

if __name__ == '__main__':
	configure_apache()
	configure_ssh()
