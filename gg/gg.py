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
                       notifi['repository']['full_name'],
                       notifi['subject']['title'])
