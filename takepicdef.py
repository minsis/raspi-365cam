import subprocess


def light_sensor():
	from TSL2561.Adafruit_TSL2561 import Adafruit_TSL2561

	#Set the lux values here with your own testing. Currently only doing
	#high, med, low ranges.
	RANGE_HIGH_UPPER = 65535
	RANGE_HIGH_LOWER = 43253
	RANGE_MED_UPPER = 43252
	RANGE_MED_LOWER = 21627
	RANGE_LOW_UPPER = 21626
	RANGE_LOW_LOWER = 0

	LightSensor = Adafruit_TSL2561()

	LightSensor.enable_auto_gain(True)
	lux = LightSensor.calculate_lux()
	if lux >= RANGE_HIGH_LOWER and lux <= RANGE_HIGH_UPPER:
		return ""
	elif lux >= RANGE_MED_LOWER and lux <= RANGE_MED_UPPER:
		return " -ss 10000"
	elif lux >= RANGE_LOW_LOWER and lux <= RANGE_LOW_UPPER:
		return " -ss 1000000"
	else:
		return ""

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
	camera_proc = camera_app()
	if options["enable_light_sensor"] == True:
		camera_proc += light_sensor()
	camera_proc += " -q 100 -hf -vf -e jpg -o " + tmp_pic
	return camera_proc
