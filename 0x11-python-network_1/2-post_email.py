#!/usr/bin/python3
''' This scirpt takes a URL and an email,
    sends a POST request to the URL with the email as a parameter,
    and displays the value of the 'X-Request-Id' variable'''


def main():
    ''' Driver function '''
    import sys
    import urllib.request

    url = sys.argv[1]
    value = {email: sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read()

    print(page.decode('utf-8')


if __name__ == '__main__':
    main()
