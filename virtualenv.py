import requests

print(requests.__version__)

r = requests.get("http://www.google.com")
print(r.text)

myCode = requests.get("https://raw.githubusercontent.com/Jdvdb/lab1/main/virtualenv.py")
print(myCode.text)
