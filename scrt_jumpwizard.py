#$interface = "1.0"
#$language ="python"
def goto_ac():
	cmd="nvram set blank_state=0"
	crt.Screen.Send(cmd+"\r\n")
def goto_ax():
	cmd="nvram set need_to_show_ads_page=0;nvram set RA_enable=1;nvram set auto_update_enable=1;nvram set router_TC_enable=1;nvram set blank_state=0;nvram set weak_passwd_neverRemind=1"
	crt.Screen.Send(cmd+"\r\n")
def main ():
	
	if crt.Arguments.Count  < 1:
		goto_ac()
	elif  crt.Arguments[0] == "AX":
		goto_ax()
	return 
		

main ()