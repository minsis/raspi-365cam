import subprocess
import RPi.GPIO as GPIO

def light_sensor():
	return " -ex night"

def camera_app():
	return "raspistill"

def xferfile(local_pic, remote_server, remote_path):
	#relies on having ssh keys setup between your RasPi and remote server
	pic_name = local_pic[(local_pic.rfind('/') + 1):len(local_pic)]
	remote_location = " '" + remote_server + ":" + remote_path + pic_name
	transfer_file = "scp " + local_pic + remote_location
#	print transfer_file
	subprocess.call (transfer_file, shell=True, stderr=subprocess.STDOUT)

def take_picture(options,tmp_pic):
	#crude function, better one coming later
	on = 1; off = 0
	camera_proc = camera_app()
	if options["enable_light_sensor"] = on:
		camera_proc += light_sensor()
	camera_proc += " -q 100 -hf -vf -e jpg -o " + tmp_pic
