# Questions for client interview:

## 1 Define a class called “SSH-Connect” with following methods:
`ssh_connect.py`
- Connect()
  - Setup SSH with a remote machine. Import libraries from Python as you see fit (e.g., paramiko)

- The user name and password for the remote connection setup should be read from a configuration file - (preferably a YAML file)

- Invoke shell on the remote machine so that you can execute commands

- Send_cmd()
  - method to send a command to the remote machine (e.g., list files in the folder)

- Read()
 - Check if the session is active (note you can store the session state in a variable in the class)

- store the received buffer in the instance of the class (i.e., self)

- Close()
  - method to close the ssh client session with the server

`rpc_server.py`
## 2 Create a python script to setup an RPC server, register function to run command on command line, start the RPC server

`pcie_diagnose.py`
## 3 Write a script to diagnose the issues with the devices in the PCIe tree?

## 4 Write a script to check if the device has a yellow bang (i.e., the device driver is not installed or the device is not working properly)
