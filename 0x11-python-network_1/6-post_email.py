#!/usr/bin/python3
''' This scirpt takes a URL and an email,
    sends a POST request to the URL with the email as a parameter
'''


def main():
    ''' Driver function '''
    import sys
    import requests

    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    res = requests.post(url, data=value)
    print(res.text)

if __name__ == '__main__':
    main()
