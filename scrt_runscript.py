#$language="python"
#$interface = "1.0"
DEFAULT_PROMPT="+=+=+="
path="C:\\Users\\ERIC2\\Desktop\\vlan.sh"
import os
import re
def send_cmd(cmd,wait_string,timeout):
	crt.Screen.Send(cmd+"\r\n")
	result=crt.Screen.WaitForString(wait_string,timeout)
	return result

def set_defaultpromt (prompt):
	send_cmd("export PS1='{}'".format(prompt)+"\n",prompt,1000)
def run_script (file_path,prompt):
	set_defaultpromt(prompt)
	f = file(file_path, 'r')
	cmd=f.readline()
	# crt.Dialog.MessageBox(cmd)
	while cmd:
		send_cmd(cmd,prompt,1000)
		cmd=f.readline()
	f.close()
	set_defaultpromt("#")
	
def main ():
	if os.path.exists(path):
		run_script(path,DEFAULT_PROMPT)
main()