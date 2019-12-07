# API_projects
Projects that supports APIs

### 1. Blind SQL injection (MongoDB Example)
The Python program should performs a blind SQL injection to obtain the password of the user admin.
* Note that the query is passed in URL parameters and should be accessed via a GET request not a POST.
* Your program must take a single argument from the command line ```(sys.argv[1])``` that represents the IP address or name of
```<wfp2_site>``` (e.g. python3 program1.py wfp.oregonctf.org). Your program must implement a [binary search algorithm](https://www.geeksforgeeks.org/binary-search/) that uses conjunctions and regular expressions within [MongoDB](https://docs.mongodb.com/ecosystem/drivers/).
#### Consider:
```http://<wfp2_site>/mongodb/example2/?search=admin%27%20%26%26%20this.password.match(/^a/)//+%00```
assuming the password is in alphabetics:
* If entry remains, first character of password is ```a```
* Add ```a``` to test condition and move on to second character of password
* If entry disappears, move on to next candidate letter (e.g. ```b```)
#### Now, consider:
```http://<wfp2_site>/mongodb/example2/?search=admin%27%20%26%26%20this.password.match(/^[a-zA-Z]/)//+%00```
* Checks for passwords with alphanumeric first character
* If entry remains, first character is a letter
■ Split search space in half and try again
* If entry disappears, first character is not a letter
■ Search half of non-alphabetic characters
* Continue to narrow ```regexp``` until next character of password Found

### 2. Get User Name and Password.
* It is expected that when the program is run and domain provided at the command line.
* The domain is supposed to return a  response containing the password list and the username.
* The program the username list provided with the username hacker provided. If a match is found for the username hacker, the program will return the corresponding password.

### 3. Getting Random Jokes From [icanhazdadjoke](https://icanhazdadjoke.com/) website that has an open-source API
The API to this project is [here](https://icanhazdadjoke.com/search) where you get ```headers``` and ```params``` from [JSON](https://jsonapi.org/) data.
#### [Request Library](https://realpython.com/python-requests/)
This library is useful for making requests behind an API so that you can focus on interacting with services and consuming data in your application. It uses ```HTTP``` method to make requests then:
* Customizes the request headers and data, using the query string and message body,
* Inspects data from your requests and responses,
* Make authenticated requests, and
* Configures the requests to help prevent the application from backing up or slowing down.

##### NOTE: For these programs to run make sure you install pip packages below via commandline.
* ```pip``` is de facto standard package-management system used to install and manage software packages written in Python.
* For this project I only needed ```pip install requests```,```pip install pyfiglet``` and ```pip install termcolor```

* For more information about ```pip``` packages visit [here](https://pypi.org/project/pip/)
