#$interface = "1.0"
#$language ="python"
def main ():
	tmp_www="/tmp/www"
	if crt.Arguments.Count >=1 :
		tmp_www="/tmp/relocate_www"
	crt.Screen.Send("killall heartbeat;nvram set www_relocation=1;test -d {path} && rm {path} -rf ;cp /www {path} -af\n".format(path=tmp_www))

main ()