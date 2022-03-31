import requests

response = requests.get('http://183.6.94.28/drcom/login?callback=dr1003&DDDDD=202050731024%40GZARTS.GZ&upass=1118661X&0MKKey=123456&R1=0&R3=0&R6=1&para=00&v6ip=&v=7242') #填入login_URL

print(response.headers)