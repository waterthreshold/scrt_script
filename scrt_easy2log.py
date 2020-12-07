#$language = "Python"
#$interface = "1.0"
import datetime
import sys
import os 
#crt.Dialog.MessageBox(crt.Screen.Selection)
def main ():
	message=crt.Screen.Selection
	if not message:
		crt.Dialog.MessageBox("Please Enter Filename:")
		return
		
	name = crt.Dialog.Prompt ("Enter file name:","Enter file name:","",False)
	datetime_dt = datetime.datetime.today()
	date=datetime_dt.strftime("%Y%m%d_%H%M%S")
	filename = name + "_" + date
	#log = crt.Session.LogFileName(filename)
	path="C:\\Users\\ERIC2\\Desktop\\CRT_LOG\\"
	if not os.path.exists(path):
		os.makedirs( path, 0755 );
	path+=filename
	write2file (path,message)

def write2file (path,message):
	f = file(path, 'w')
	f.write(message)
	f.close()


main ()
#crt.Dialog.MessageBox (filename)