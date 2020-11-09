#$interface ="1.0"
#$language="python"
default_prompt="++===++"
import os
def cmd_send(cmd,wait_string):
	crt.Screen.Send(cmd+"\r\n")
	crt.Screen.WaitForString(wait_string)

def change_default_prompt(default_prompt):
	cmd="PS1='{}'".format(default_prompt)
	cmd_send(cmd,default_prompt)

def get_result(cmd):
	crt.Screen.Send(cmd+"\r\n")
	crt.Screen.WaitForString(cmd+"\r\n")
	szResult = crt.Screen.ReadString(default_prompt)
	return szResult
	
def main ():
	result=crt.Dialog.MessageBox("Get Firmeware update method (Yes:wget No:curl)","",ICON_QUESTION | BUTTON_YESNO)
	change_default_prompt(default_prompt)
	cert_file=get_result("nvram get cert_file")
	#current_setting=get_result("curl 127.0.0.1/currentsetting.htm")
	current_setting=get_result("nvram get system_name")
	#crt.Dialog.MessageBox(current_setting)
	info_list=current_setting.split("\n")
	#crt.Dialog.MessageBox(info_list[0],"",ICON_QUESTION | BUTTON_YESNO)
	# for str in info_list:
		# if  str.find("Model="):
			# crt.Dialog.MessageBox(str)
			# modal_list=str.split("=")
			# break
	modal=current_setting.lower().rstrip(os.linesep)
	cert_file=cert_file.rstrip(os.linesep)
	if not cert_file:
		cert_file="ca-bundle-mega.crt"
	crt.Dialog.MessageBox("wget --tries=2 --timeout=5  --ca-certificate /opt/xagent/certs/{} -O /tmp/result https://http.fw.updates1.netgear.com/sw-apps/router-analytics/{}/RAE_Policy.json &".format(cert_file[2:],modal[2:]))
	if result==IDYES:
		cmd_send("wget --tries=2 --timeout=5  --ca-certificate /opt/xagent/certs/{} -O /tmp/result https://http.fw.updates1.netgear.com/sw-apps/router-analytics/{}/RAE_Policy.json &".format(cert_file[2:],modal[2:]),default_prompt)
	elif result==IDNO:
		cmd_send("curl --retry 2 --connect-timeout 5 --cacert /opt/xagent/certs/{}  https://http.fw.updates1.netgear.com/sw-apps/router-analytics/{}/RAE_Policy.json".format(cert_file[2:],modal[2:]),default_prompt)
	
	change_default_prompt("#")
	crt.Clipboard.Text="wget --tries=2 --timeout=5  --ca-certificate /opt/xagent/certs/{} -O /tmp/result https://http.fw.updates1.netgear.com/sw-apps/router-analytics/{}/RAE_Policy.json &".format(cert_file[2:],modal[2:])

main ()


#https://documentation.help/SecureCRT/