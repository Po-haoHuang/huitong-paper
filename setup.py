# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 22:05:05 2015

@author: User
"""

from distutils.core import setup
import py2exe, sys, os



sys.argv.append('py2exe')
sys.setrecursionlimit(5000)

#DATA=[('imageformats',['C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qjpeg4.dll',
#    'C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qgif4.dll',
#    'C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qico4.dll',
#    'C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qmng4.dll',
#    'C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qsvg4.dll',
#    'C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qtiff4.dll'
#    ])]

setup(
    options = {'py2exe': {'compressed': True,"includes":["sip"], 'bundle_files': 1}},
    windows = [{'script': "layoutlogic.py"}],
    zipfile = None,
#    data_files = DATA,
)