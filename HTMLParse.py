import string

# Rquest looks like this
# first line usually looks like this
# POST / HTTP/1.1 
# GET /background.png HTTP/1.0
# the first line contains method then url then the http version 
# 
msg = """HTTP/1.1 200 OK
Date: Mon, 09 May 2022 13:05:18 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2022-05-09-13; expires=Wed, 08-Jun-2022 13:05:18 GMT; path=/; domain=.google.com; Secure 
Set-Cookie: AEC=AakniGOObrtwHmtvcs6s6AM_34piSjf2j6mrmu24RiLKdDxU2KtmybmyhA; expires=Sat, 05-Nov-2022 13:05:18 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax
Set-Cookie: NID=511=G1tgcKjUjUcYqueLQ3QSn5zhBHuV9VEthTtJkU_an0LaVeLwYiGaCgYHZS2rikjTnmi8C28WMJycTOTUlNm5XymKSeQYOir1HabDVeDNckKQJcEFuqMzYWrlPPqLg9-MK6Gi50z5TSrRrTgvGfc9PPP973NiTDZnKkqvS18Gakw; expires=Tue, 08-Nov-2022 13:05:18 GMT; path=/; domain=.google.com; HttpOnly
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

534f
<!doctype html><html dir="rtl" itemscope="" itemtype="http://schema.org/WebPage" lang="ar"><head><meta content="""


def splitResponse(HTMLrequest:string):
 parsedRequest = HTMLrequest.split('\r\n')
 parsedRequest[0] = parsedRequest[0].split(' ')
 
 
 return parsedRequest 

if __name__ == "__main__":
 msg = splitResponse(msg)
 if msg[0][2] == "OK":
  print(msg[-1])