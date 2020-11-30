#$interface="1.0"
#$language="python"

import os 
def send_cmd(cmd,wait_string,timeout):
	crt.Screen.Send(cmd+"\n")
	crt.Screen.WaitForString(cmd)
	result=crt.Screen.ReadString(wait_string,timeout)
	return result


def nvram_get (key):
	res=send_cmd("nvram get {}".format(key),"#",2000)
	return res

def nvram_set (key,value):
	res=send_cmd("nvram set {}={}".format(key,value),"#",2000)
	return res
	
def nvram_show(key): 
	res=send_cmd("nvram show | grep {}".format(key),"#",2000)
	return res
	
def main ():
	Key=crt.Dialog.Prompt("nvram Key","Key","http_passwd")
	if not Key: 
		return
	
	if crt.Arguments.Count  < 1:
		value=nvram_get(Key)
	elif crt.Arguments[0] == "show" :
		value=nvram_show(Key)
	elif crt.Arguments[0] == "set" :
		keyvalue=crt.Dialog.Prompt("nvram value","value","")
		valuen=nvram_set(Key,keyvalue)
	# value=send_cmd("nvram get {}".format(Key),"#",2000)
	# value=value.replace("\r\n","")
	# if len(value) > 0:
		# crt.Dialog.MessageBox(value)
		# crt.Clipboard.Text=value
		
	#crt.Dialog.MessageBox("{}".format(len(value)))
main()
