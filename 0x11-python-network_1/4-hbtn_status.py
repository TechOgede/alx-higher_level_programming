#!/usr/bin/python3
''' This scirpt fetches https://alx-intranet.hbtn/io/status'''


def main():
    ''' Driver function '''
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    print('Body response:')
    print(f'\t- type: {type(res.text)}')
    print(f'\t- content: {res.text}')


if __name__ == '__main__':
    main()
