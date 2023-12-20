import subprocess

subprocess.call(['sudo', 'apt', 'update'])
subprocess.call(['sudo', 'apt', 'install', 'apache2'])
subprocess.call(['sudo', 'apt-get', 'upgrade'])
subprocess.call(['sudo', 'apt-get', 'install', 'openssh-client'])
subprocess.call(['sudo', 'apt', 'autoremove'])
