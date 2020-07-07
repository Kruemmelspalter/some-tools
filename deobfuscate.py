s = input(": ")
fc=""
offset=0

def escape(s:str):
	if s in ['\\', '\'', '\"']:
		s='\\'+s
	if s=='\n': s='\\n'
	if s=='\t': s='\\t'
	return s


for i in range(0, len(s)):
	if offset != 0:
		offset -= 1
		continue
	if s[i] == "\\" and s[i+1]=="x":
		fc+=escape(chr(int(s[i+2]+s[i+3], 16)))
		offset = 3
	else:
		fc+=s[i]
print("\n\n\n")
print(fc)