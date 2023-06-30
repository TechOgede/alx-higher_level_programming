#!/usr/bin/python3
''' This scirpt fetches https://alx-intranet.hbtn/io/status'''


def main():
    ''' Driver function '''
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        page = response.read()
    print('Body response:')
    print(f'\t- type: {type(page)}')
    print(f'\t- content: {page}')
    print(f'\t- utf8 content: {page.decode("utf-8")}')


if __name__ == '__main__':
    main()
