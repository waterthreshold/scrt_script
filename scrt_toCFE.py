#$interface = "1.0"
#$language ="python"

default_prompt="==++=="
def send_cmd(cmd,wait_string):
	crt.Screen.Send(cmd+"\r\n")
	result=crt.Screen.WaitForString(wait_string,10)
	return result

def change_default_prompt(default_prompt):
	cmd="PS1='{}'".format(default_prompt)
	send_cmd(cmd,default_prompt)

def main ():
	result=crt.Dialog.MessageBox("Do yo want to reboot?","Tips",BUTTON_YESNOCANCEL )
	if result!=IDYES:
		return
	command = crt.Dialog.Prompt("SKU","sku","")
	
	crt.Screen.Send("reboot"+"\r\n")
	result1=False
	result=crt.Screen.WaitForStrings(["Press any key to stop auto run","CFE for Foxconn Router"],30000)
	if result==1 or result==2:
		result1=False
	else:
		return 
	while result1==False:
		result1=send_cmd("\003","CFE>")
	if len(command) > 0:
		send_cmd(command,"CFE>")
main ()