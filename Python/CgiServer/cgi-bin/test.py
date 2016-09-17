import cgi

form = cgi.FieldStorage()
name = form.getvalue('name')

print ("Content-type:text/html\n")
print ("<html>")
print ("<head>")
print ("<title>Hello, world!</title>")
print ("</head>")
print ("<body>")
print ("Hello, {0}!".format(name))
print ("</body>")
print ("</html>")