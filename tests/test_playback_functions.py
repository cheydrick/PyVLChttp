import unittest
import time
from pyvlchttp import VLCHTTPAPI


class TestPlaybackControls(unittest.TestCase):
    def setUp(self):
        self.vlc = VLCHTTPAPI()

    def test_play(self):
        self.vlc.play()
        time.sleep(1)
        status = self.vlc.get_status()
        self.assertEqual(status['state'], 'playing')

    def test_stop(self):
        self.vlc.stop()
        time.sleep(1)
        status = self.vlc.get_status()
        self.assertEqual(status['state'], 'stopped')


if __name__ == '__main__':
    unittest.main()
