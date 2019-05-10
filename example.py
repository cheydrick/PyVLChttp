from pyvlchttp import VLCHTTPAPI

test_mrl = 'file:///Users/cheydrick/Music/MojoFrankenstein/superstitious final.mp3'

if __name__ == '__main__':
    vlc = VLCHTTPAPI('127.0.0.1', '8080', 'password')
    vlc.add_to_playlist(test_mrl)
    vlc.toggle_repeat()
    vlc.play()
    # TODO