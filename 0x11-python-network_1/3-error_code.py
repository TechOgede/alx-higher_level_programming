#!/usr/bin/python3
''' This scirpt takes a URL, sends a request to the URL and
displays the value of the 'X-Request-Id' variable or
the error code, if any'''


def main():
    ''' Driver function '''
    import sys
    import urllib.request
    import urllib.error

    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')


if __name__ == '__main__':
    main()
