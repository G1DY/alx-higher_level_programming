<center> <h1>Python - Network #0</h1> </center>
This Project entails understanding TCP/IP transport and internet protocols. We used ``curl`` as the preferred tool to transfer data to and from a server. I learned about URL's , HTTPS, Domain & Sub-Domain names and how they work. I also digged deeper on HTTPS methods(GET, POST, PUT, DELETE, HEAD, TRACE, OPTIONS), how to write the requests and response syntax.I wrote ``Bash`` scripts to send various types of HTTP requests. Task 6 was an algorithmn challenge to find a peak in a list of unsorted integers at its lowest complexity.

---
<center> <h2>Project Tasks</h2> </center>

| Task | Description |
| ---- | ----------- |
| 0. cURL body size | Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response |
| 2. cURL Method | Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response |
| 3. cURL only methods | Write a Bash script that takes in a URL and displays all HTTP methods the server will accept. |
| 4. cURL headers | Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response |
| 5. cURL POST parameters | Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response |
| 7. Only status code | Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response. |
| 8. cURL a JSON file | Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response. |
| 9. Catch me if you can! | Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response. |

---

### Task 6
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Write a function that finds a peak in a list of unsorted integers.

Prototype: def find_peak(list_of_integers):
You are not allowed to import any module
Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
6-peak.py must contain the function
6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
Note: there may be more than one peak in the list
~~~
guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$ wc -l 6-peak.txt
2 6-peak.txt
guillaume@ubuntu:~/0x10$
~~~

### Resources
- [HTTP (HyperText Transfer Protocol)](https://intranet.alxswe.com/rltoken/rAon_EpQ6PGl8N0plySn4A)
- [HTTP Cookies](https://intranet.alxswe.com/rltoken/MhVCl_0oviQldWPn5oX-NQ)

### Learning Objective
```
What a URL is
What HTTP is
How to read a URL
The scheme for a HTTP URL
What a domain name is
What a sub-domain is
How to define a port number in a URL
What a query string is
What an HTTP request is
What an HTTP response is
What HTTP headers are
What the HTTP message body is
What an HTTP request method is
What an HTTP response status code is
What an HTTP Cookie is
How to make a request with cURL
What happens when you type google.com in your browser (Application level)
```

### Requirements
```
Allowed editors: vi, vim, emacs
- A README.md file, at the root of the folder of the project, is mandatory
All your scripts will be tested on Ubuntu 20.04 LTS
All your Bash scripts should be exactly 3 lines long (wc -l file should print 3)
All your files should end with a new line
All your files must be executable
The first line of all your bash files should be exactly #!/bin/bash
The second line of all your Bash scripts should be a comment explaining what is the script doing
All curl commands must have the option -s (silent mode)
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
The first line of all your Python files should be exactly #!/usr/bin/python3
Your code should use the pycodestyle (version 2.8.*)
All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
```
