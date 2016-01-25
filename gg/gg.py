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


def encode_utf8(s):
    if type(s) == unicode:
        return s.encode('utf-8')
    else:
        return s


@click.command()
@click.version_option()
def shit():
    r = requests.get(API, auth=GithubAPIToken(TOKEN))
    content = r.json()
    if not content:
        print "No Notifications.."
    else:
        counter = 0
        for notifi in content:
            counter += 1
            print """
{}:
    pro_name: {}
    title   : {}
    -------------------
            """.format(counter,
                       encode_utf8(notifi['repository']['full_name']),
                       encode_utf8(notifi['subject']['title']))
