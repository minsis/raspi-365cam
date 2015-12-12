import subprocess

def xferfile(local_pic, remote_server, remote_path):
	pic_name = local_pic[(local_pic.rfind('/') + 1):len(local_pic)]
	remote_location = " '" + remote_server + ":" + remote_path + pic_name
	transfer_file = "scp " + local_pic + remote_location
#	print transfer_file
	subprocess.call (transfer_file, shell=True, stderr=subprocess.STDOUT)
