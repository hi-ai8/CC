#KVM
Step 1: 
Sudo apt-get update 
Step 2: kvm 
egrep -c ‘(vmx|svm)’ /proc/cpuinfo 
Step 3 : 
kvm-ok 
Step 4: 
Sudo apt install -y cpu-checker
Step 5: 
sudo apt-get install -y qemu-kvm virt-manager libvirt-daemon-system 
virtinstlibvirt-clients bridge-utils 
Step 6: 
sudosystemctl enable –now libvirtd


#OPENSTACK

Steps to perform: 
1. sudo apt update 
2. Sudo apt upgrade 
Step 1: sudo snap install microstack --beta
Step 2: snap list microstack
Step 3: sudo microstack init --auto --control
Step 4: microstack.openstack --version
Step 5: sudo snap get microstack config.credentials.keystone-password
Step 6: ip a


#FOSS
Step 21: Add following command in front of localhost fc-node-configuration –n demo-system –password admin
Step 22: Type ifconfig command to get inet of the device.