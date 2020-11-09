#$language="python"
#$interface = "1.0"
default_prompt="==++=="
def send_cmd(cmd,wait_string):
	crt.Screen.Send(cmd+"\r\n")
	crt.Screen.WaitForString(wait_string)
	
def change_default_prompt(default_prompt):
	cmd="PS1='{}'".format(default_prompt)
	send_cmd(cmd,default_prompt)


	
def main ():
	result=crt.Dialog.MessageBox("Do yo want to reboot?","Tips",BUTTON_YESNOCANCEL )
	if result!=IDYES:
		return
	change_default_prompt(default_prompt)
	send_cmd("nvram loaddefault",default_prompt)
	send_cmd("reboot",default_prompt)
	#send_cmd("\003",default_prompt)
	

main()