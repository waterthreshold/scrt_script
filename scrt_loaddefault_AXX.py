#$language="python"
#$interface = "1.0"
default_prompt="==++=="
def send_cmd(cmd,wait_string,timeout):
	crt.Screen.Send(cmd+"\n")
	crt.Screen.WaitForString(wait_string,timeout)
	
def change_default_prompt(default_prompt):
	cmd="PS1='{}'".format(default_prompt)
	send_cmd(cmd,default_prompt,1)


	
def main ():
	result=crt.Dialog.MessageBox("Do yo want to reboot?","Tips",BUTTON_YESNOCANCEL )
	if result!=IDYES:
		return
	change_default_prompt(default_prompt)
	send_cmd("loaddefault",default_prompt,3)
	send_cmd("reboot"," Broadband Router",240)
	send_cmd("","Login: ",3)
	send_cmd("admin","Password: ",3)
	send_cmd("admin"," > ",3)
	send_cmd("sh","#",3)
	
	result=crt.Dialog.MessageBox("Do yo want to skip wizard?","Tips",BUTTON_YESNOCANCEL )
	if result!=IDYES:
		return	
	send_cmd("nvram set need_to_show_ads_page=0;nvram set router_TC_enable=1;nvram set RA_enable=1;nvram set need_to_load_basic=1","#",3)
	#send_cmd("\003",default_prompt)
	

main()