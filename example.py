from pyvlchttp import VLCHTTPAPI

if __name__ == '__main__':
    vlc = VLCHTTPAPI('127.0.0.1', '8080', 'password')
    vlc.play()
    # TODO