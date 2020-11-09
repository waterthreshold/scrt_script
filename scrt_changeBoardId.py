#$interface="1.0"
#$language="python"
modal_list = {
	'R6300v1':"U12H218T00",
	'R6300v2':"U12H240T00",
	'R6400':"U12H332T00",
	'R6400v2':"U12H332T30",
	'R6700':"U12H270T10",
	'R6700v3':"U12H332T77",
	'R6900':"U12H270T11",
	'R7000':"U12H270T00",
	'R7850':"U12H315T40",
	'R7000P':"U12H270T20",
	'R7900':"U12H315T30",
	'R7900P':"U12H359T00",
	'R8000':"U12H315T00",
	'R8000P':"U12H359T00",
	'R8500':"U12H334T00",
	'RAX20':"U12H401T00",
	'RAX50':"U12H425T00",
	'RAX45':"U12H425T00",
	'RAX80':"U12H376T00",
	'XR300':"U12H332T78",
	'XR1000':"U12H425T20"
}
def send_cmd(cmd,wait_string,timeout):
	crt.Screen.Send(cmd+"\r\n")
	result=crt.Screen.WaitForString(wait_string,timeout)
	return result
	

def main ():
	modal_name = crt.Dialog.Prompt("Modal name","name","")
	modal_name=modal_name.upper().replace('V','v')
	#crt.Dialog.Prompt("Modal name {}".format(modal_name),"name","")
	try:
		board_id = modal_list[modal_name]
	except ValueError:
		print modal_name+" not Found"
		exit()
	
	board_id=board_id+"_NETGEAR"
	cmd = "nvram set board_id={boardid};burnboardid {boardid};nvram commit".format(boardid=board_id)
	crt.Screen.Send(cmd+"\r\n")


main()