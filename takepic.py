import exifread #need to install python-exif package
import subprocess #need to install python-subprocess package
import takepicdef

#-----BEGIN USER DEFINED VARIABLES----#
local_pic_path = "/images/" #path fo your picture besure to add the trailing /
remote_server = "remote.server.example.com" #remote ssh server
remote_path = "/usr/share/nginx/html/images/" #remote file path of ssh server. Be sure to add trailing /
#----END USER DEFINED VARIABLES----#

#shell command and process to take picture
#add whatever flags you see fit
tmp_pic = local_pic_path + "temp.jpg" #name and location of temp pic
take_picture = "raspistill -ex night -q 100 -hf -vf -e jpg -o " + tmp_pic
subprocess.call (take_picture, shell=True, stderr=subprocess.STDOUT)

#open picture for EXIF tag reading
pic_file = open(tmp_pic, 'rb')
pic_tags = exifread.process_file(pic_file)

#get the actual datetime the picture was taken
pic_date = str(pic_tags['EXIF DateTimeOriginal']).replace(":", "-", 2)

#new filename of picture with date added
final_pic = "'" + local_pic_path + "PiCam-" + pic_date.replace(" ", ":") + ".jpg'"

#shell command and process to rename picture
rename_pic = "mv %s %s" % (tmp_pic, final_pic)
subprocess.call (rename_pic, shell=True, stderr=subprocess.STDOUT)

#comment below line if you don't want to transfer the picture to a remote location
takepicdef.xferfile(final_pic, remote_server, remote_path)
