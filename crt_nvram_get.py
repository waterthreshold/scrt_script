#$interface="1.0"
#$language="python"

import os 
def send_cmd(cmd,wait_string,timeout):
	crt.Screen.Send(cmd+"\n")
	crt.Screen.WaitForString(cmd)
	result=crt.Screen.ReadString(wait_string,timeout)
	return result

def main ():
	Key=crt.Dialog.Prompt("nvram Key","Key","http_passwd")
	if not Key: 
		return
	
	value=send_cmd("nvram get {}".format(Key),"#",2000)
	value=value.replace("\r\n","")
	if len(value) > 0:
		crt.Dialog.MessageBox(value)
		# crt.Clipboard.Text=value
		
	#crt.Dialog.MessageBox("{}".format(len(value)))
main()
