# Multichain Ansible Automation
This project can be used to deploy and configure the distributed ledger Multichain based on the Bitcoin technology on as many hosts as required using the configuration engine Ansible.

## Requirements
In order to deploy the multichain only the configurations hosts public SSH key has to be copied to the hosts root directory using the command:
```bash
ssh-copy-id root@<host_address>
``` 
and the inventory has to be adjusted according to the developers needs.

Therafer using the command 
```bash
ansible-playbook deploy.yml -i inventory
```
installs, starts and permissions the blockchain on all nodes.

In Case the *ansible_hosts* are already set up and only the software needs to be installed, executing the following playbook like so:
```bash
ansible-playbook redeploy.yml -i inventory
```
will do the job in a faster manner.

## Configuration
Some basic configuration of the node setup can be done by modifying the **host_vars/all.yml** file:

```bash
---
blockchainName: "supplyChain"
networkPort: 7700
rpcPort: 7755
explorerPort: 4444
``` 

## The Inventory
In the Inventory there are 6 groups used to diffrentiate between the hosts.
1. For security reasons, only the configuration of the network interface and the user configuration are done using the root user, neccecitating in the **roottotal** group. This group includes the root user aswell as the IP-Addresses of all hosts taking part in the distributed ledger.
2. The **contractor** group can only include one host, since a blockchain can only be created at one place, with the other nodes joining the network later.
3. The **readers** group are members of the Blockchain network, who can only read from the blockchain, not write or issue assets.
4. The **writers** group includes all members, who can read, write and issue assets on the blockchain
5. The **partners** group simply is the combination if readers and writers
6. The **total** group includes all hosts taking part in the network

## The Roles

| roles              | desription                                            | target hosts |
|--------------------|-------------------------------------------------------|--------------|
| user-add           | adds ansible user and passwordless sudo               | roottotal    |
| network            | configures the network interfaces                     | roottotal    |
| yum-update         | updates all packages and repositories                 | total        |
| hostname-set       | sets hostname to be equal to inventory name           | total        |
| time-set           | sets central european time zone                       | total        |
| multichain-install | installs and configures the servers to run multichain | total        |
| multichain-deploy  | creates genesis block, starts blockchain & explorer   | contractor   |
| multichain-attach  | connects the **partner** servers and permissions them | partners     |

## Tools

### cleanup.yml
This tool uninstalls multichain from the participating nodes, removes the **@reboot** cronjobs, installation and blockchain data, then reboots the system to stop the processes.
The tool can be run using 
```bash
ansible-playbook cleanup.yml -i inventory
```

### multichain explorer
Included in the role multichain-deploy is also the installation of the multichain explorer 2.
This is a webaplication used to display broad metrics about the distributed ledger. It can be accessed at the contractors address: **<server_ip>:{{ explorerPort }}**

### getting_started.py
At the end of the Ansible Playbook run **deploy.yml** a pythonscript in the projects root directory is created containing an import of a [python module](https://github.com/coblo/mcrpc) and the connection details to the contractor node.
With this script you can start developing your multichain solution right away.
