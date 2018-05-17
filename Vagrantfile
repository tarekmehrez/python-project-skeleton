# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
	config.vm.hostname = "example-project"
	config.vm.box = "centos/7"

	config.vm.synced_folder ".", "/example-project"

	config.vm.provider "virtualbox" do |vb|
		vb.memory = "1024"
	end

	config.vm.provision "shell", inline: <<-SHELL

		systemctl stop firewalld
		systemctl disable firewalld

		if [ ! -e /opt/miniconda ]; then

			CONDA_INSTALLER=$(mktemp)
			curl -sL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o $CONDA_INSTALLER
			bash $CONDA_INSTALLER -b -p /opt/miniconda

		else
			echo 'Miniconda already installed'
		fi
	
		echo 'export PATH=/opt/miniconda/bin:$PATH' | tee /etc/profile.d/miniconda.sh
		chmod a+x /etc/profile.d/miniconda.sh	
		cd /example-project && pip install -r requirements.txt
	SHELL
end

