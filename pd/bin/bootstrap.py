#!/usr/bin/env python
import os
base = os.path.dirname(os.path.abspath(__file__)+'../')
os.environ['PYTHON_EGG_CACHE'] = os.path.join(base, '..', 'misc/virtenv/lib/python2.6/site-packages')
virtualenv = os.path.join(base, '..', 'misc/virtenv/bin/activate_this.py')
execfile(virtualenv, dict(__file__=virtualenv))

sys.path.append(os.path.join(base, "src"))

import server
server.main(os.environ['OPENSHIFT_DIY_IP'])
