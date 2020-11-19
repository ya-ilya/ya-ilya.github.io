#!/usr/bin/env python3
import cgi
import requests

lol = requests.get("https://2b2t.io/api/queue").text
if lol[15] != 0:
    online = lol[13] + lol[14] + lol[15]
else:
    if lol[14] != 0:
        online = lol[13] + lol[14]
    else:
        online = lol[13]

form = cgi.FieldStorage()
text1 = form.getfirst("Queue", online)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>lolkek</title>
        </head>
        <body>""")

print("<h1>2b2t queue</h1>")
print("<p>Queue: {}</p>".format(text1))

print("""</body>
        </html>""")
