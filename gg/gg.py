# -*- coding: utf-8 -*-

import requests
from requests.auth import AuthBase
import click

from .consts import (
    API,
    TOKEN,
    NOTIFICATIONS_FILEE
)
from .music import Music


# github api token
class GithubAPIToken(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = 'token ' + self.token
        return r


class FileObject(object):

    def __init__(self, mode):
        self.file = open(NOTIFICATIONS_FILEE, mode)

    def close(self):
        self.file.close()

    def __del__(self):
        self.close()


class WriteObject(FileObject):

    def __init__(self, mode='a'):
        super(WriteObject, self).__init__(mode)

    def __call__(self, content):
        self.file.writelines(str(content) + '\n')


class ReadObject(FileObject):

    def __init__(self, mode='r'):
        super(ReadObject, self).__init__(mode)

    def __call__(self, sizhint=0):
        print self.file.readlines(sizhint)


def encode_utf8(s):
    if type(s) == unicode:
        return s.encode('utf-8')
    else:
        return s


@click.command()
@click.version_option()
@click.option('-i', '--id', default=-1,
              help='notifications number, default: -1')
@click.option('--music', default=False, is_flag=True)
def shit(id, music):
    if music:
        music = Music()
        music.play()
    write = WriteObject()
    r = requests.get(API, auth=GithubAPIToken(TOKEN))
    content = r.json()
    if not content:
        print "No Notifications.."
    else:
        counter = 0
        for notifi in content:
            counter += 1
            text = """{}:
    pro_name: {}
    title   : {}
    -------------------""".format(counter,
                                  encode_utf8(notifi['repository']['full_name']),
                                  encode_utf8(notifi['subject']['title']))
            print text
            write(text)
