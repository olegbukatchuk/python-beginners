import cgi

data = cgi.FieldStorage()


city = data.getvalue('CityList')

print('Content-type:text/html\r\n\r\n')
print('<!DOCTYPE HTML>')
print('<html lang="en">')
print('<head> <meta charset="UTF-8">')
print('<title>Python Response</title> </head>')
print('<body>')
print('<h1>City:', city, '</h1>')
print('<a href="select.html">Back</a>')
print('</body>')
print('</html>')