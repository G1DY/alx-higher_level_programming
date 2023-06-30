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
