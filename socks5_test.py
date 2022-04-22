import requests, socket, socks

# 将127.0.0.1：10800设为全局代理
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 10800)
socket.socket = socks.socksocket

requests.get('https://www.google.com', timeout=5).status_code
