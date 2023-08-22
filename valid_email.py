import re 
string="new@thundersoft.com"
pattern = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
res=re.findall( pattern,string)
print(res)
