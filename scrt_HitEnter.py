#$interface = "1.0"
#$language ="python"
DEFAULT_PROMPT="+=+=+="
path="C:\\Users\\ERIC2\\Desktop\\vlan.sh"
import os 
def send_cmd(cmd,wait_string,timeout):
	crt.Screen.Send(cmd+"\r\n")
	result=crt.Screen.WaitForString(wait_string,timeout)
	return result


def set_defaultpromt (prompt):
	send_cmd("export PS1='{}'".format(prompt)+"\n",prompt,1000)
	
def set_interface (prompt):
	send_cmd("ifconfig eth0 up;ifconfig eth1 up;ifconfig eht2 up;ifconfig wl0.1 up ;ifconfig wl1.1 up\r\n",prompt,3000)
	send_cmd("brctl addbr br0;brctl addif br0 eth1;brctl addif br0 eth2;brctl addif br0 wl0.1;brctl addif br0 wl1.1\r\n",prompt,3000)
	send_cmd("ifconfig br0 192.168.1.1 netmask 255.255.255.0",prompt,3000)
	
def run_script (file_path,prompt):
	set_defaultpromt(prompt)
	f = file(file_path, 'r')
	cmd=f.readline()
	while cmd:
		crt.Dialog.MessageBox(cmd)
		send_cmd(cmd,prompt,1000)
		cmd=f.readline()
	f.close()
	set_defaultpromt("#")
	
def main  ():
	send_cmd("reboot","Hit enter to continue...",70000)
	crt.Screen.Send ("\nifconfig\r\n")
	run_script(path,DEFAULT_PROMPT)
	#set_defaultpromt(DEFAULT_PROMPT)
	#set_interface(DEFAULT_PROMPT)
	#set_defaultpromt("#")
main ()