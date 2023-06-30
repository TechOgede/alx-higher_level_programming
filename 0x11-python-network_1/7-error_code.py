#!/usr/bin/python3
''' This scirpt takes a URL, sends a request to the URL and
displays the value of the 'X-Request-Id' variable or
the error code, if any'''


def main():
    ''' Driver function '''
    import sys
    import requests

    url = sys.argv[1]

    res = requests.get(url)
    if res.status_code >= 400:
        print(f'Error code: {res.status_code}')
    else:
        print(res.text)


if __name__ == '__main__':
    main()
