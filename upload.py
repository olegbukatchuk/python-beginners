import cgi , os

data = cgi.FieldStorage()

upload = data['filename']
filename = os.path.basename(upload.filename)