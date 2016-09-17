import cgi
import json

form = cgi.FieldStorage()
key = form.getvalue('key')
value = form.getvalue('value')
data = {key:value}

print ("Content-type:application/json\n")
print(json.dumps(data, indent = 1))