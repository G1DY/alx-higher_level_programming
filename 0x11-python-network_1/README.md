<center><h1>Python - Network #1</h1></center>
In this Project we used the URLLIB python module and the python requests package to fetch and send requests to the server over the HTTP protocol. We also learnt how to manipulate data using HTTP requests methods and how to fetch json resources. I wrote scripts on urllib.request functions. Task 10 was an interview challenge to test our understanding on the project.

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

