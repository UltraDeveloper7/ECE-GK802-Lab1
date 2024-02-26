import requests
from http.cookies import SimpleCookie
from datetime import datetime
from email.utils import parsedate_to_datetime

class UrlAnalyzer:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url)
        self.cookies = SimpleCookie(self.response.headers.get('Set-Cookie'))

    def print_headers(self):
        print("Κεφαλίδες απόκρισης HTTP:")
        for key, value in self.response.headers.items():
            print(f"{key}: {value}")

    def print_server_software(self):
        print(f"\nΛογισμικό εξυπηρετητή: {self.response.headers.get('Server')}")

    def print_cookies(self):
        if self.cookies:
            print("\nΗ σελίδα χρησιμοποιεί τα εξής cookies:")
            for morsel in self.cookies.values():
                if morsel['expires']:
                    expires = parsedate_to_datetime(morsel['expires'])
                    now = datetime.now(expires.tzinfo)
                    duration = expires - now
                    print(f"Όνομα: {morsel.key}, Τιμή: {morsel.value}, Διάρκεια: {duration}")
                else:
                    print(f"Όνομα: {morsel.key}, Τιμή: {morsel.value}, Διάρκεια: Δεν έχει οριστεί")
        else:
            print("\nΗ σελίδα δεν χρησιμοποιεί cookies.")

    def start(self):
        self.print_headers()
        self.print_server_software()
        self.print_cookies()
        

if __name__ == "__main__":
    url = input("Παρακαλώ εισάγετε ένα URL: ")
    analyzer = UrlAnalyzer(url)
    analyzer.start()