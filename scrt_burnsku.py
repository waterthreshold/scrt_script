#$interface="1.0"
#$language ="python"
sku_table = {
	"NA":1,
	"WW":2,
	"GR":3,
	"PR":4,
	"RU":5,
	"BZ":6,
	"IN":7,
	"KO":8,
	"JP":9,
	"AU":10,
}


def main ():
	sku_name = crt.Dialog.Prompt("SKU","sku","")
	sku_name=sku_name.upper();
	crt.Screen.Send ("burnsku {}".format(sku_table[sku_name])+"\r\n")
	crt.Screen.WaitForString ("burnsku OK",3000)
	crt.Screen.Send ("burnsku\n")
main ()