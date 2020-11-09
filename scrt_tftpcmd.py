#$language="python"
#$interface = "1.0"

def send_cmd(cmd,wait_string):
	crt.Screen.Send(cmd+"\r\n")
	result=crt.Screen.WaitForString(wait_string)
	return result
	
def main ():
	cmd=""
	#result=crt.Dialog.MessageBox("Do yo want to stop heartbeat?","Tips",BUTTON_YESNOCANCEL)
	#if result==IDYES:
	#	cmd += "killall heartbeat;"
	prog_name=crt.Dialog.Prompt("program name","name","httpd")
	IP=crt.Dialog.Prompt("What is Host IP?","name","192.168.1.100")
	option=""
	if prog_name!="":
		cmd1="killall {};tftp -g -l /tmp/{} -r {} {};chmod u+x /tmp/{};".format(prog_name,prog_name,prog_name,IP,prog_name)
		cmd+=cmd1
		option=crt.Dialog.Prompt("progrma OPT?","","-S -E /usr/sbin/ca.pem /usr/sbin/httpsd.pem &")
	

	if prog_name=="httpd" or prog_name=="":
		result=crt.Dialog.MessageBox("Do yo want to upload htm page?","Tips",BUTTON_YESNOCANCEL)
		if result==IDYES:
			html_page=crt.Dialog.Prompt("html page name?","","")
			cmd += "tftp -g -l /tmp/relocate_www/{} -r {} {};".format(html_page,html_page,IP)
			
	if prog_name!="":
		cmd+="/tmp/{} {}".format(prog_name,option)
	
	crt.Clipboard.Text=cmd
	result=crt.Dialog.MessageBox("Do yo want to execute cmd: {}?".format (cmd),"Tips",BUTTON_YESNOCANCEL)
	if result==IDYES:
		crt.Screen.Send(cmd+"\r\n")
	
main()