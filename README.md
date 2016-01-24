Python script to trigger a picture on the Raspberry Pi and transfers
that file to a given server.

Adding light sensor to detect the amount of light in the room or outside
and trigger the shutter speed and/or exposure accordingly. You may have to
experiment with the shutter speeds for your area. The script is currently using
the TSL2561 sensor and breakout board from Adafruit. This sensor uses the I2C
bus and requires you to enable hardware and driver on the RasPi. If using other
sensors you may need to experiment with it.

[Sensor](https://www.adafruit.com/products/439)  
[TSL2561 Python Library](https://github.com/IainColledge/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_TSL2561)  
[Adafruit I2C Library](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_I2C)  

There's also a new options section to toggle if you want certain settings
to be used with the raspistill application. Right now its pretty crude and
will probably change it to an interactive config manager in the future.

###### Variables to edit
Be sure to change the variables in the script to match you system.
* local_pic_path  #path for your picture be sure to add the trailing /
* remote_server   #remote ssh server
* remote_path     #remote file path of ssh server. Be sure to add trailing /

By default the script will upload the file to a given server. Should
you want this feature turned off be sure to comment out the following
line:
* takepicdef.xferfile(final_pic, remote_server, remote_path)

###### Toggle options
Toggle on whatever options you'd like using on or off:
* enable_light_sensor

```
The point of this project was to learn a little bit of python, Linux,
and git. However, this script could be useful to someone who wants
to do a 365 project with their Raspberry Pi camera.
```
