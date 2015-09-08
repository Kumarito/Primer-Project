#!/usr/bin/python
import cgi

form = cgi.FieldStorage()
wish = form.getvalue('wish')
print "Content-type: text/html"
print
print "<br/>"
print "<center>"
print "<h1> Wish Master</h1>"
print "</center>"
print "<br/>"
print "<h4>Your wish for ( %s ) shall not be granted. Life isn't fair! </h4/>" %(wish)
print "<HTML>"
print "<img src=http://blogs-images.forbes.com/mikemyatt/files/2012/12/Forbes-Image-21.jpg>"
print "</img>"
print "<br/>"
print "<br/>"
print "<form method=get action=https://www.google.com/search>"
print "<label> Feel free to do a Google Search for your wish: <input type=text name=q></label>"
print "<input type=submit value=Submit>"
print "<br/>"
print "<label>WARNING: If you are not able to find your wish or buy it, too bad, get glad!</label>"
print "<br/>"
print "<br/>"
print "<label> If you would like to try to enter a wish again,or if you would like to read about the person who didn't grant your wish, please click nowhere. Mwuahaha!\
</label>"
print "</HTML>"
