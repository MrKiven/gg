# -*- coding: utf-8 -*-

import requests
from requests.auth import AuthBase
import click

from .consts import (
    API,
    TOKEN,
)


# github api token
class GithubAPIToken(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = 'token ' + self.token
        return r


@click.command()
@click.version_option()
@click.option('--token', default=False, is_flag=True,
              help='if need token(default: False)')
def gg(token):
    if token:
        r = requests.get(API, auth=GithubAPIToken(TOKEN))
    else:
        r = requests.get(API)
    return r.text
