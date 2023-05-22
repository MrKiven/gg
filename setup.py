# -*- coding: utf-8 -*-

import os
import re
from setuptools import setup, find_packages


def _get_version():
    v_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'gg', '__init__.py')
    ver_info_str = re.compile(r".*version_info = \((.*?)\)", re.S). \
        match(open(v_file_path).read()).group(1)
    return re.sub(r'(\'|"|\s+)', '', ver_info_str).replace(',', '.')

entry_points = [
    'shit = gg.gg:shit'
]

setup(
    name='shit',
    version=_get_version(),
    description="For Github Notifications",
    long_description=open('README.md').read(),
    author='kiven',
    author_email='kiven.mr@gmail.com',
    packages=find_packages(),
    url='https://github.com/MrKiven/gg/',
    entry_points={'console_scripts': entry_points},
    install_requires=[
        'requests==2.31.0'
    ],
)
