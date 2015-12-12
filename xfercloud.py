import subprocess

def xferfile(new_pic):
	picname = new_pic[(new_pic.rfind('/') + 1):len(new_pic)]
	remoteurl = " 'picloud.dwhitney.net:"
	remoteloc = remoteurl + "/usr/share/nginx/html/images/" + picname
	localloc = "'/images/" + picname
	xfercmd = "scp " + localloc + remoteloc
#	print xfercmd
	subprocess.call (xfercmd, shell=True, stderr=subprocess.STDOUT)
