<center><h1>JavaScript - Web jQuery</h1></center>

In this project i covered jquery and how to use the API to get(), Post(), append(), prepend() etc.

<center><h2>Project task</h2></center>

| Task | Description |
| ---- | ----------- |
| 0. No JQuery | a JavaScript script that updates the text color of the <header> element to red (#FF0000): using document.queryselector |
| 1. With JQuery | a JavaScript script that updates the text color of the <header> element to red (#FF0000 using jquery API |
| 2. Click and turn red | a JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header using jquery API |
| 3. Add `.red` class | a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header using jquery |
| 4. Toggle classes |  a JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header, The <header> element must always have one class: red or green, never both in the same time and never empty., If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse., |
| 5. List of elements | a JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item, The new element must be: <li>Item</li>, The new element must be added to UL.my_list, |
| 6. Change the text | a JavaScript script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header |
| 7. Star wars character | a JavaScript script that fetches the character name from this URL: `https://swapi-api.alx-tools.com/api/people/5/?format=json, The name must be displayed in the HTML tag DIV#character |
| 8. Star Wars movies | a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json, All movie titles must be list in the HTML tag UL#list_movies |
| 9. Say Hello! | a JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello., The translation of “hello” must be displayed in the HTML tag DIV#hello |
| 10. No jQuery - document loaded | a JavaScript script that updates the text color of the <header> element to red (#FF0000):, You must use document.querySelector to select the HTML tag |
| 11. List, add, remove | a JavaScript script that adds, removes and clears LI elements from a list when the user clicks:, The new element must be: <li>Item</li>, The new element must be added to UL.my_list, When the user clicks on DIV#add_item: a new element is added to the list, When the user clicks on DIV#remove_item: the last element is removed from the list, When the user clicks on DIV#clear_list: all elements of the list are removed |
| 12. Say hello to everybody! | a JavaScript script that fetches and prints how to say “Hello” depending on the language, You should use this API service: https://www.fourtonfish.com/hellosalut/hello/, The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.), The translation must be fetched when the user clicks on INPUT#btn_translate, The translation of “Hello” must be displayed in the HTML tag DIV#hello |
| 13. And press ENTER | a JavaScript script that fetches and prints how to say “Hello” depending on the language, You should use this API service: https://www.fourtonfish.com/hellosalut/hello/, The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.), The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code, he translation of “Hello” must be displayed in the HTML tag DIV#hello |

### **Resources**

- [What is JavaScript?](https://intranet.alxswe.com/rltoken/NJ5XM_fzjlBKERHTkdF-uA)
- [Selector](https://intranet.alxswe.com/rltoken/wsnVUxEcAzzlCx6ES1qc7g)
- [Get and set content](https://intranet.alxswe.com/rltoken/rwtc96sn2_LHToBAd0MIhQ)
- [Manipulate CSS classes](https://intranet.alxswe.com/rltoken/IcM5kKVzssU0ibdUo-2gKQ)
- [Manipulate DOM elements](https://intranet.alxswe.com/rltoken/ve8UKsZLVw2t27PtWscZfQ)
- [API](https://intranet.alxswe.com/rltoken/vKc7XmiHG7HIh3N0Kl_VQw)
- [Introduction](https://intranet.alxswe.com/rltoken/QiUwuS_9TXE49D5IVL-ocg)
- [GET & POST request](https://intranet.alxswe.com/rltoken/Mbe7uoy0iMAfTVs2Tn4Pzg)
- [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://intranet.alxswe.com/rltoken/gMwyXisSLu-kZicmGA0-LQ)
- [What went wrong? Troubleshooting JavaScript](https://intranet.alxswe.com/rltoken/4eYyJr72PO-cohImk93M3w)
- [JQuery](https://intranet.alxswe.com/rltoken/HnjBq6jf84S9S-C15Qi0vw)
- [JQuery API](https://intranet.alxswe.com/rltoken/jvibhq-8VEdQHNUWKTCI7w)
- [JQuery Ajax](https://intranet.alxswe.com/rltoken/rBZyrXxuRuISDfPBzO9Y7Q)

#### **Learning Objectives**


```
General
Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
How to select HTML elements in JavaScript
How to select HTML elements with JQuery
What are differences between ID, class and tag name selectors
How to modify an HTML element style
How to get and update an HTML element content
How to modify the DOM
How to make a GET request with JQuery Ajax
How to make a POST request with JQuery Ajax
How to listen/bind to DOM events

```
#### **How to listen/bind to user events**

```
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Chrome (version 57.0)
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should be semistandard compliant with the flag --global $: semistandard *.js --global $
You must use JQuery version 3.x
You are not allowed to use var
HTML should not reload for each action: DOM manipulation, update values, fetch data…
More Info
Import JQuery
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```