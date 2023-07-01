<center><h1>Python - Network #1</h1></center>
In this Project we used the `URLLIB` python module and the python `requests` package to fetch and send requests to the server over the HTTP protocol. We also learnt how to manipulate data using HTTP requests methods and how to fetch json resources. I wrote scripts on `urllib.request` using `with` statements and packages `requests` & `sys`. Task 10 was an interview challenge to test our understanding on the project.

---

<center><h2>Project Tasks</h2></center>

| Task | Description |
| ---- | ----------- |
| 0. What's my status? #0 | Write a Python script that fetches `https://alx-intranet.hbtn.io/status`: use package `urllib` and `with` statement |
| 1. Response header value #0 | Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response. |
| 2. POST an email #0 | Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`) |
| 3. Error code #0 | Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`): manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code |
| 4. What's my status? #1 | Write a Python script that fetches `https://alx-intranet.hbtn.io/status`: use the package `requests` |
| 5. Response header value #1 | Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header: use the packages `requests` and `sys` |
| 6. POST an email #1 | Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response: use packages `requests` and `sys` |
| 7. Error code #1 | Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response: f the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code, use packages `requests` and `sys` |
| 8. Search API | Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter: The letter must be sent in the variable `q`, If no argument is given, set `q=""`, If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>]` `<name>`, Otherwise: Display `Not a valid JSON` if the JSON is invalid, Display `No result` if the JSON is empty use package `requests` and `sys` |
| 9. My GitHub! | Write a Python script that takes your GitHub credentials (username and password) and uses the [GitHub API](https://intranet.alxswe.com/rltoken/LjPfW9hW_55YwijGVofyTQ) to display your `id`: You must use [Basic Authentication](https://intranet.alxswe.com/rltoken/_UgCj47xv8jzRRVcOG7V4w) with a [personal access token as password](https://intranet.alxswe.com/rltoken/Kz4UM-V_bcwrcWajaCAVtQ) to access to your information (only `read:user` permission is needed), sys.argv[1]=username and sys.argv[2]=password |

### 10. Time for an interview!
The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:
```
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
```
Write a Python script that takes 2 arguments in order to solve this challenge.
> The first argument will be the repository name
> The second argument will be the owner name
> You must use the packages requests and sys
> You are not allowed to import packages other than requests and sys
> You don’t need to check arguments passed to the script (number or type)

***test***
~~~
guillaume@ubuntu:~/0x11$ ./100-github_commits.py rails rails
3b5a6dfb18f33c373a89760c60d741f34206f23b: Jon Moss
f785ad786ae49dd6f7a2f1d77c44ea17008c6656: Jon Moss
bb13c37fefdc8b5699918b38eff84751c2899ad5: Rafael França
f5d880866917724217eae9785a3ccd3f806c5aaf: Rafael França
0da696a5e3cee87a996a020b664caa1eabd66220: Ryuta Kamizono
24eb450d7599bab1f5863e0578a21c65ca42a915: Matthew Draper
668f8691f1017042e238497d1a5b7b8bf1c43819: Matthew Draper
a76f5189f6cec4b3e6d9035e2b55dcda6050dfdb: Ryuta Kamizono
28079868d0e70bdac80c76cf806afd517edfe1e7: Rafael França
8f0d8551893789f26e5d6b82ccef00779296818f: Rafael Mendonça França
guillaume@ubuntu:~/0x11$
~~~

### Resources
- [HOWTO Fetch Internet Resources Using urllib Package](https://intranet.alxswe.com/rltoken/KoRrs5dVWsb-B82e-M1TQQ)
- [Quickstart with Requests package](https://intranet.alxswe.com/rltoken/OGcRGPr7TSWtzypDd0ZibQ)
- [Requests package](https://intranet.alxswe.com/rltoken/dUNaNQrV2bMSstILitQbXQ)

### Learning Objectives
~~~
How to fetch internet resources with the Python package urllib
How to decode urllib body response
How to use the Python package requests #requestsiswaysimplerthanurllib
How to make HTTP GET request
How to make HTTP POST/PUT/etc. request
How to fetch JSON resources
How to manipulate data from an external service
~~~

### Requirements
~~~
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the repo, containing a description of the repository
A README.md file, at the root of the folder of this project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Your code should not be executed when imported (by using if __name__ == "__main__":)
~~~
