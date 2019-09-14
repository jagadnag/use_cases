# use_cases
network_automation use cases


##### Script output
```
(venv) macbook$ python ios_2900_upgrade_v3.py
Enter Device IP address: 10.1.1.1
Enter login username: admin
Password:
Source file: c2951-universalk9-mz.SPA.157-3.M4b.bin
md5: a9a129e3245993b0bc062d262a97dc02
ftp server ip: 10.10.10.1
ftp_username: ftp
ftp_password: ftp123
>>>> 2019-09-14 14:03:16.327470

Logging in to Device...


Checking the software version...

System image file is "flash0:c2951-universalk9-mz.SPA.157-3.M3.bin"
--------------------------------------------------------------------------------
Device not running on target software version. Starting Upgrade process.
--------------------------------------------------------------------------------

Initiate file transfer...
Copying file via FTP...
Destination filename [c2951-universalk9-mz.SPA.157-3.M4b.bin]? Accessing ftp://*:*@10.10.10.1/c2951-universalk9-mz.SPA.157-3.M4b.bin...
Loading c2951-universalk9-mz.SPA.157-3.M4b.bin !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[OK - 115347980/4096 bytes]

115347980 bytes copied in 190.552 secs (605336 bytes/sec)


Collecting flash details and Verifying MD5...
   11  -rw-   115347980  Sep 14 2019 18:28:38 +00:00  c2951-universalk9-mz.SPA.157-3.M4b.bin

File successfully copied. MD5 hash verified...

Changing boot statements...
config term
Enter configuration commands, one per line.  End with CNTL/Z.
ISR2951-1(config)#no boot system flash0:c2951-universalk9-mz.SPA.157-3.M3.bin
ISR2951-1(config)#boot system flash0:c2951-universalk9-mz.SPA.157-3.M4b.bin
ISR2951-1(config)#end
ISR2951-1#

Verifying boot statement...
boot system flash0:c2951-universalk9-mz.SPA.157-3.M4b.bin

Saving config...

Reloading Device...

Reload scheduled in 1 minute by admin on vty0 (10.10.1.100)
Reload reason: Reload Command
Proceed with reload? [confirm]ISR2951-1#

Waiting for device upgrade and reboot...


>>>> 2019-09-14 14:08:46.119700

>>>> 2019-09-14 14:15:46.133535

Logging in to Device...


Verifying Upgrade...
System image file is "flash0:c2951-universalk9-mz.SPA.157-3.M4b.bin"
--------------------------------------------------------------------------------
Python sucessfully upgraded the software image.
--------------------------------------------------------------------------------

>>>> Total time taken: 0:12:36.242714


(venv) (venv) macbook$ python ios_2900_upgrade_v3.py
Enter Device IP address: 10.82.142.2
Enter login username: admin
Password:
Source file: c2951-universalk9-mz.SPA.157-3.M4b.bin
md5: a9a129e3245993b0bc062d262a97dc02
ftp server ip: 10.122.153.158
ftp_username: calo
ftp_password: calo
>>>> 2019-09-14 19:22:31.629206

Logging in to Device...


Checking the software version...

System image file is "flash0:c2951-universalk9-mz.SPA.157-3.M4b.bin"
--------------------------------------------------------------------------------
Device already running on latest version. No update required.
--------------------------------------------------------------------------------
(venv) macbook$
```
