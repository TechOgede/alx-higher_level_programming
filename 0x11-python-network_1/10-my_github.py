#!/usr/bin/python3
''' This script takes GitHub credentials and uses the GitHub
API to display id
'''


def main():
    ''' Driver function '''
    import sys
    import requests

    user = sys.argv[1]
    pwd = sys.argv[2]

    url = f'https://api.github.com/{user}'
    headers = {'Accept': 'application/vnd.github+json',
               'Authorization': f'Bearer {pwd}',
               'X-GitHub-Api-Version': '2022-11-28'}
    res = requests.get(url, headers=headers)
    data = res.json()
    print(data.get('id'))


if __name__ == '__main__':
    main()
