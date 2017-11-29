import cgi , os

data = cgi.FieldStorage()

upload = data['filename']
filename = os.path.basename(upload.filename)

with open(filename, 'wb') as copy:
    copy.write(upload.file.read())