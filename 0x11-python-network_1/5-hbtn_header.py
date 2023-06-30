#!/usr/bin/python3
''' This scirpt takes a URL, sends a request to the URL and
displays the value of the 'X-Request-Id' variable'''


def main():
    ''' Driver function '''
    import requests
    import sys

    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))


if __name__ == '__main__':
    main()
