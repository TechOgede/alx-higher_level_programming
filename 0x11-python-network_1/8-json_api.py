#!/usr/bin/python3
''' This script sends a POST request and checks for JSON response '''


def main():
    ''' Driver function'''
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    res = requests.post(url, data=data)
    try:
        dict_ = res.json()
    except Exception:
        print('Not a valid JSON')
    else:
        if dict_:
            print(f'[{dict_.get("id")}] {dict_.get("name")}')
        else:
            print('No result')


if __name__ == '__main__':
    main()
