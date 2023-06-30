#!/usr/bin/python3
''' This script takes GitHub credentials and uses the GitHub
API to display 10 most recent commits to a repo passaed as CL argument
'''


def main():
    ''' Driver function '''
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits?per_page=10'
    headers = {'Accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28'}
    res = requests.get(url, headers=headers)
    commits = res.json()
    for commit in commits:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f'{sha}: {author}')


if __name__ == '__main__':
    main()
