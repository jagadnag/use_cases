#!/usr/bin/env python

"""

Author: Jag
email: jagadnag@gmail.com
Purpose: Script to upgrade Cisco IOS routers.
Requirements:
python3 
virtualenv
netmiko
Status: WIP, need to add more error handling and argparse

"""

from __future__ import print_function
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler, FileTransfer
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import time
import sys

def main():
    # Collect input details
    ip_addr = input("Enter Device IP address: ")
    user = input("Enter login username: ")     
    my_pass = getpass()
    source_file = input("Source file: ")
    md5 = input("md5: ")
    ftp = input("ftp server ip: ")
    ftp_user = input("ftp_username: ")
    ftp_pass = input("ftp_password: ")
    dest_file = source_file

    start_time = datetime.now()
    print(">>>> {}".format(start_time))

    net_device = {
        "device_type": "cisco_ios",
        "ip": ip_addr,
        "username": user,
        "password": my_pass,
        "secret": my_pass,
        "port": 22,
    }
    
    # Initiate Netmiko Connection
    print("\nLogging in to Device...")
    try:
        ssh_conn = ConnectHandler(**net_device)
    except (AuthenticationException):
        print ('Authentication failure: ' + ip_addr)
        sys.exit(1)
    except (NetMikoTimeoutException):
        print ('Timeout to device: ' + ip_addr)
        sys.exit(1)
    except (EOFError):
        print ("End of file while attempting device " + ip_addr)
        sys.exit(1)
    except (SSHException):
        print ('SSH Issue. Are you sure SSH is enabled? ' + ip_addr)
        sys.exit(1)
    except Exception as unknown_error:
        print ('Some other error: ' + str(unknown_error))
        sys.exit(1)

    # Check current software version
    print("\nChecking the current software version...\n")
    current_version = ssh_conn.send_command("sh version | in System image")
    print(current_version)


    # Check whether software upgrade required or not
    if source_file in current_version:
        print("-" * 80)
        print("Device already running on latest version. No update required.")
        print("-" * 80)

    else:
        print("-" * 80)
        print("Device not running on target software version. Starting Upgrade process.")
        print("-" * 80)    
        print("\nInitiate file transfer...")
        output = ssh_conn.send_command("dir | in {}".format(source_file))

        # Check whether upgrade image already exists in filesystem
        if source_file in output:
            print("File already exists. No file transfer required.")
        else:
            # Identify file_system details flash or disk0 or bootflash
            dir_output = ssh_conn.send_command("dir | in Directory")
            dir_output = dir_output.strip().split()
            file_system = dir_output[2]
            file_system = file_system[:-1]
            print("Identifying file_system: {}".format(file_system))

            # Initiate file transfer via FTP
            print("Copying file via FTP...")    
            cmd = "copy ftp://{}:{}@{}/{} {}".format(ftp_user,ftp_pass,ftp,source_file, file_system)
            output = ssh_conn.send_command(cmd, expect_string =r'Destination filename')
            output += ssh_conn.send_command('\n',expect_string=r'#', delay_factor=2)
            print(output)
        
        # Verify file properly copied and MD5 hash
        print("\nCollecting flash details and Verifying MD5...")
        output = ssh_conn.send_command("dir | in {}".format(source_file))
        print(output)
        hash_output = ssh_conn.send_command("verify /md5 {}{} {}".format(file_system, source_file, md5),    delay_factor=2)
    
        if source_file in output and "Verified" in hash_output:
            print("\nFile successfully copied. MD5 hash verified...")
            
            # Change boot statement commands
            print("\nChanging boot statements...")
            output = ssh_conn.send_command("sh run | in boot system ")
            boot_cmd = ['no ' + output, 
                        'boot system flash0:' + source_file,
                        ]
            output = ssh_conn.send_config_set(boot_cmd)
            print(output)
            
            # Change boot statement properly configured
            print("\nVerifying boot statement...")
            output = ssh_conn.send_command("sh run | in boot system")
            print(output)
            
            # Save config
            ssh_conn.save_config()
            print("\nSaving config...")
            
            # Reload device and sleep for 7mins
            print("\nReloading Device...\n")
            request_reload = ssh_conn.send_command("reload in 1\n", expect_string =r'Proceed with reload?')
            request_reload += ssh_conn.send_command('y\n', expect_string =r'#')
            print(request_reload)
            print("\nWaiting for device upgrade and reboot...\n")
            print("\n>>>> {}".format(datetime.now()))
            time.sleep(420)
            print("\n>>>> {}".format(datetime.now()))

            # Login into device again and verify current software version
            print("\nLogging in to Device...")
            ssh_conn = ConnectHandler(**net_device)
            print()
            print("\nVerifying Upgrade...")
            output = ssh_conn.send_command("sh version | in System image")
            print(output)
            
            # If device running on updated version, print message
            if source_file in output:
                print("-" * 80)
                print("Python sucessfully upgraded the software image.")
                print("-" * 80)
    
        else:
            print("Upgrade failed")    
    
        print("\n>>>> Total time taken: {}".format(datetime.now() - start_time))
        print()

if __name__ == "__main__":
    main()