# Multichain Ansible Automation
This project can be used to start the distributed ledger Multichain based on the Bitcoin technology on as many hosts as required using the configuration engine Ansible.

## Requirements
In order to deploy the multichain only the configurations hosts public SSH key has to be copied to the hosts root directory using the command:
```bash
ssh-copy-id root@<host_address>
``` 
and the inventory has to be adjusted according to the developers needs.

## The Inventory
In the Inventory there are 6 groups used to diffrentiate between the hosts.
1. For security reasons, only the configuration of the network interface and the user configuration are done using the root user, neccecitating in the **roottotal** group. This group includes the root user aswell as the IP-Addresses of all hosts taking part in the distributed ledger.
2. The **contractor** group can only include one host, since a blockchain can only be created at one place, with the other nodes joining the network later.
3. The **readers** group are members of the Blockchain network, who can only read from the blockchain, not write or issue assets.
4. The **writers** group includes all members, who can read, write and issue assets on the blockchain
5. The **partners** group simply is the combination if readers and writers
6. The **total** group includes all hosts taking part in the network


