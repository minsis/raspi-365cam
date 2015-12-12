import exifread
import subprocess
import xfercloud

oldpic = "/images/temp.jpg" #name of temp pic

#shell command and process to take picture
takepic = "raspistill -ex night -q 100 -hf -vf -e jpg -o " + oldpic
subprocess.call (takepic, shell=True, stderr=subprocess.STDOUT)

#open picture for EXIF tag reading
f = open(oldpic, 'rb')
tags = exifread.process_file(f)

#get the actual datetime the picture was taken
picdate = str(tags['EXIF DateTimeOriginal']).replace(":", "-", 2)

#append datetime to new name of picture
newpic = "'/images/PiCam-" + picdate.replace(" ", ":") + ".jpg'"

#shell command and process to rename picture
renamepic = "mv %s %s" % (oldpic, newpic)
subprocess.call (renamepic, shell=True, stderr=subprocess.STDOUT)

xfercloud.xferfile(newpic)
