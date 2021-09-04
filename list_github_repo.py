#!/usr/bin/env python3

import requests
import sys
import logging
import argparse


def list_repo(user: str) -> str:
    ses = requests.Session()
    url = "https://api.github.com/users/{}/repos".format(user)
    result = []
    resp = ses.get(url, timeout=5)
    repos = resp.json()
    for repo in repos:
        result.append(repo["name"])

    return result


def main():
    user = None
    argp = argparse.ArgumentParser("List github repo user")
    argp.add_argument("username", type=str, help="User name")
    args = argp.parse_args()
    user = args.username
    print(list_repo(user))


if __name__ == "__main__":
    main()