import requests

print(requests.__version__)

r = requests.get("http://www.google.com")
print(r.text)


"""
1. What is your github URL?
https://github.com/Jdvdb

2. What version is the requests library installed on the system?
2.28.1

3. What version is the requests library installed in the virtualenv?
2.28.1 by default. However, I can specify to install 2.28.0 instead
and it says that.

4. What is the difference between the virtual environment and the not virtual
    environment in python?
They are the same in my case since I installed the same version of the
library. However, the directories shown when running 'which python' are
different in the virtual environment and non-virtual environment.

After I specifically installed 2.28.0 in the virtual environment, the 
one in the new terminal window said 2.28.1 still but the virtualenv one
is 2.28.0.

5. What status code is returned for http://google.com? What URL must you
    visit to get a 200 status code?
You get the code '301' which means it has moved permanently.
You need to curl http://www.google.com/

6. What status code is returned for http://google.com/teapot? Is it the
    one returned by curl -i or curl -iL? What happens when you curl http://www.google.com/teapot?
If you use 'curl' or 'curl -i' then you get the 301 code.
If you use 'curl -iL' you get the code 418 which means I'm a teapot. 

7. What changed in the output of https://webdocs.cs.ualberta.ca/~hindle1/1.py
    when you used -X POST? What is this method useful for?

2c2
< Date: Tue, 10 Jan 2023 00:20:33 GMT
---
> Date: Tue, 10 Jan 2023 00:20:25 GMT
19d18
< <P>No form fields.
20a20,21
> <DT>X: <i>&lt;type 'instance'&gt;</i>
> <DD>MiniFieldStorage('X', 'Y')
25a27,28
> <DT> CONTENT_LENGTH <DD> 3
> <DT> CONTENT_TYPE <DD> application/x-www-form-urlencoded
37,38c40,41
< <DT> REMOTE_PORT <DD> 30738
< <DT> REQUEST_METHOD <DD> GET
---
> <DT> REMOTE_PORT <DD> 26132
> <DT> REQUEST_METHOD <DD> POST
52c55
< <DT> UNIQUE_ID <DD> Y7yvUelNh-OBjlhT8H1MfwAAAAo
---
> <DT> UNIQUE_ID <DD> Y7yvSStZVhcjWXSR6f@4NQAAAAc
127a131,132
> <DT> CONTENT_LENGTH <DD> 3
> <DT> CONTENT_TYPE <DD> application/x-www-form-urlencoded
139,140c144,145
< <DT> REMOTE_PORT <DD> 30738
< <DT> REQUEST_METHOD <DD> GET
---
> <DT> REMOTE_PORT <DD> 26132
> <DT> REQUEST_METHOD <DD> POST
154c159
< <DT> UNIQUE_ID <DD> Y7yvUelNh-OBjlhT8H1MfwAAAAo
---
> <DT> UNIQUE_ID <DD> Y7yvSStZVhcjWXSR6f@4NQAAAAc

POST is useful for sending data to a server.

"""