#$language = "Python"
#$interface = "1.0"
default_prompt="#*&^#"
import time 
import os 
path="C:\\Users\\ERIC2\\Desktop\\vmlinux_Test.txt"
def write2file (path,str):
	f = file(path, 'w')
	f.write(str)
	f.close()


def main ():
	
	crt.Screen.Send ("reboot\r\n")
	
	str=""
	if 0:	
		crt.Screen.WaitForString("Hit enter to continue...")
		crt.Screen.Send ("\r\nexport PS1='{}'\r\n".format(default_prompt))
		crt.Screen.WaitForString(default_prompt)
		
		crt.Screen.send ("nvram set boot_wait=on\r\n")
		crt.Screen.WaitForString(default_prompt)
		crt.Screen.Send ("reboot")
		
	for i in range(10):
		
		crt.Screen.WaitForString("Loader:raw Filesys:tftp Dev:")
		start =time.time()
		crt.Screen.WaitForString("Entry at 0x00008000")
		end = time.time()
		execu_time = end - start 
		str += "{} time execute {} secs\n".format(i+1,execu_time)
		crt.Screen.WaitForString("Hit enter to continue...")
		crt.Screen.Send ("\r\nreboot\r\n")
	write2file(path,str)
main()