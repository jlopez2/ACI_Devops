#!/usr/bin/env python

import sys

from cobra.mit.session import LoginSession 
from cobra.mit.access import MoDirectory 
from cobra.mit.request import ConfigRequest 
from cobra.model.fv import Tenant
from cobra.internal.codec.xmlcodec import toXMLStr

def apic_login(hostname, username, password): 
    url = "http://" + hostname
    sess = LoginSession(url, username, password) modir = MoDirectory(sess)
    try:
        modir.login()
    except:
        print 'Login error'
        exit(1)
    return modir
pass

