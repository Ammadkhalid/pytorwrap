<<<<<<< HEAD
# Python 3 PytorWrap Module used to apply tor as proxy and renew IP.
## You have install and configure TOR
=======
# Python3 PyTorWrap Module

> You have install and configure TOR on your PC to make this work

Python3 module to wrap the function to handle requests from TOR proxy and renew IP periodically

>>>>>>> e7342079c91c21f3a0aa546b1b60c1b03c486fd8
After Installing TOR then active the tor...
will write soon about this later

```
┌─[ammadkhalid@TheKiller] - [/mnt/D0E0EC3BE0EC2A04/python/me/pytorwrap] - [اتوار مارچ 18, 21:19]
└─[$] <git:(master*)> learc
┌─[ammadkhalid@TheKiller] - [/mnt/D0E0EC3BE0EC2A04/python/me/pytorwrap] - [اتوار مارچ 18, 21:19]
└─[$] <git:(master*)> python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pytorwrap import Tor
>>> Tor.renewConnection(password="Ammad")
>>> from gimmeproxy import GimmeProxy
>>> gp = GimmeProxy()
>>> gp.request(proxy="socks5://localhost:9050")
{'ipPort': '179.210.192.185:23068', 'anonymityLevel': 1, 'supportsHttps': True, 'referer': True, 'speed': 40.34, 'post': True, 'get': True, 'cookies': True, 'type': 'socks5', 'websites': {'yelp': False, 'amazon': False, 'example': True, 'google': False}, 'tsChecked': 1521388805, 'curl': 'socks5://179.210.192.185:23068', 'otherProtocols': {}, 'user-agent': True, 'port': '23068', 'ip': '179.210.192.185', 'country': 'BR', 'protocol': 'socks5'}
>>> gp.request(proxy="socks5://localhost:9050")
{'ipPort': '191.180.232.252:32319', 'anonymityLevel': 1, 'supportsHttps': True, 'referer': True, 'speed': 33.07, 'post': True, 'get': True, 'cookies': True, 'type': 'socks5', 'websites': {'yelp': True, 'amazon': False, 'example': True, 'google': False}, 'tsChecked': 1521390290, 'curl': 'socks5://191.180.232.252:32319', 'otherProtocols': {}, 'user-agent': True, 'port': '32319', 'ip': '191.180.232.252', 'country': 'BR', 'protocol': 'socks5'}
>>> gp.request(proxy="socks5://localhost:9050", country="Us", supportsHttps=True, curl=True)
'socks5://184.158.88.74:42271'
>>> gp.request(proxy="socks5://localhost:9050", country="Us", supportsHttps=True, curl=True)
'socks5://71.213.82.131:20637'
>>> gp.request(proxy="socks5://localhost:9050", country="Us", supportsHttps=True, curl=True)
'socks5://71.213.189.12:48914'
>>> gp.request(proxy="socks5://localhost:9050", country="Us", supportsHttps=True, curl=True)
'socks5://76.2.19.34:16891'
>>> Tor.renewConnection(password='Ammad')
>>> gp.request(proxy="socks5://localhost:9050", country="Us", supportsHttps=True, curl=True)
'socks5://67.197.145.57:64395'
>>> gp.request(proxy="socks5://localhost:9050", country="Us", supportsHttps=True, curl=True)
'socks5://76.3.42.28:19172'
>>> gp.request(proxy="socks5://localhost:9050", country="Us", supportsHttps=True, curl=True)
```
