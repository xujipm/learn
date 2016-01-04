# /usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

debug_handler = urllib.request.HTTPHandler(debuglevel=1)
# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = "120.36.131.66:1723"
password_mgr.add_password(None, top_level_url, 'bandeng@vpn', 'MacBook2005')

proxy_handler = urllib.request.ProxyHandler({'http': '120.36.131.66:1723'})

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)
opener = urllib.request.build_opener(proxy_handler, handler)

# use the opener to fetch a URL
a_url = "http://admin.huanleguang.com"
x = opener.open(a_url)
print(x.read())

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)

a = urllib.request.urlopen(a_url).read().decode('utf8')
print(a)