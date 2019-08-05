from pyvlchttp import VLCHTTPAPI

vlc = VLCHTTPAPI('127.0.0.1', '8080', 'password')
r = vlc.get_status()
print(r.text)
