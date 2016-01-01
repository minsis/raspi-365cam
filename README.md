# rough draft application DO NOT USE

Python script to trigger a picture on the Raspberry Pi and transfers
that file to a given server.

Adding light sensor to detect the amount of light in the room or outside
and trigger the shutter speed and exposure accordingly.

## Variables to edit
Be sure to change the variables in the script to match you system.
* local_pic_path  #path for your picture be sure to add the trailing /
* remote_server   #remote ssh server
* remote_path     #remote file path of ssh server. Be sure to add trailing /

By default the script will upload the file to a given server. Should
you want this feature turned off be sure to comment out the following
line:
* takepicdef.xferfile(final_pic, remote_server, remote_path)

```
The point of this project was to learn a little bit of python, Linux,
and git. However, this script could be useful to someone who wants
to do a 365 project with their Raspberry Pi camera.
```
