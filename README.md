# API_projects
Projects that supports APIs

### 1. Blind SQL injection (MongoDB Example)
The Python program should performs a blind SQL injection to obtain the password of the user admin.
* Note that the query is passed in URL parameters and should be accessed via a GET request not a POST.
* Your program must take a single argument from the command line ```(sys.argv[1])``` that represents the IP address or name of
```<wfp2_site>``` (e.g. python3 program1.py wfp.oregonctf.org). Your program must implement a [binary search algorithm](https://www.geeksforgeeks.org/binary-search/) that uses conjunctions and regular expressions within [MongoDB](https://docs.mongodb.com/ecosystem/drivers/).
#### Consider ```http://<wfp2_site>/mongodb/example2/?search=admin%27%20%26%26%20this.password.match(/^a/)//+%00```
Assuming password alphabetic
* If entry remains, first character of password is ```a```
* Add ```a``` to test condition and move on to second character of password
* If entry disappears, move on to next candidate letter (e.g. ```b```)
#### Now, consider ```http://<wfp2_site>/mongodb/example2/?search=admin%27%20%26%26%20this.password.match(/^[a-zA-Z]/)//+%00```
* Checks for passwords with alphanumeric first character
* If entry remains, first character is a letter
■ Split search space in half and try again
* If entry disappears, first character is not a letter
■ Search half of non-alphabetic characters
* Continue to narrow regexp until next character of password Found


NOTE: For these programs to run make sure you pip intall support modules via commandline for you to be able to carry on imports e.g '

pip install requests, pip install pyfiglet, and pip install termcolor
