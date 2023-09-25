import requests

r = requests.get('http://172.25.0.29')

web_headers = r.headers
print("Headers Returened:")
print(web_headers)

web_html = r.text
print("HTML Returned:")
print(web_html)

web_status_code = r.status_code
print("HTTP Status Code Returned:")
print(web_status_code)

web_cookies = r.cookies
print("Cookies Returned:")
print(web_cookies)