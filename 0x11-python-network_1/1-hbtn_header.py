#!/usr/bin/python3
''' This scirpt takes a URL, sends a request to the URL and
displays the value of the 'X-Request-Id' variable'''


def main():
    ''' Driver function '''
    import sys
    import urllib.request

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        page = response.info()
    print(page['X-Request-Id'])


if __name__ == '__main__':
    main()
