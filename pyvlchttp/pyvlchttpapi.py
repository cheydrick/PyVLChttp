import requests
import sys

class VLCHTTPAPI():
    """
    VLCHTTPAPI is a class that uses the VLC HTTP API to control VLC.

    Usage:
        >>>import VLCHTTPAPI
        >>>vlc = VLCHTTPAPI()
        >>>vlc.play()
        >>>vlc.last_http_status_code
        200
        >>>vlc.stop()
        etc...
    """
    def __init__(self, ip = '127.0.0.1', port = '8080', password = 'password'):
        if 'requests' not in sys.modules:
            try:
                import requests
            except ImportError:
                print("Couldn't import requests module!")

        self.vlc_url = 'http://' + ip + ':' + port
        self.password = password

        # URLs that return status/playlist
        self.status_url = self.vlc_url + '/requests/status.xml'
        self.playlist_url = self.vlc_url + '/requests/playlist.xml'

        # Command url prefix
        self.command_prefix = self.status_url + '?command='
        
        # URLs that send simple commands
        self.play_url = self.command_prefix + 'pl_play'
        self.stop_url = self.command_prefix + 'pl_stop'
        self.play_next_url = self.command_prefix + 'pl_next'
        self.play_previous_url = self.command_prefix + 'pl_previous'
        self.empty_playlist_url = self.command_prefix + 'pl_empty'
        self.random_toggle_url = self.command_prefix + 'pl_random'
        self.loop_toggle_url = self.command_prefix + 'pl_loop'
        self.repeat_toggle_url = self.command_prefix + 'pl_toggle'
        self.fullscreen_toggle_url = self.command_prefix + 'fullscreen'

        # URLs that require additional arguments
        self.play_mrl_url_prefix = self.command_prefix + 'in_play&input='
        self.add_mrl_playlist_prefix = self.command_prefix + 'in_enqueue&input='
        self.play_id_url_prefix = self.command_prefix + 'pl_play&id='

        # Last HTTP status code storage
        self.last_http_status_code = 0
        self.connection_error = False

    def get_status(self):
        r = self._send_command(self.status_url)
        return r
    
    def get_playlist(self):
        r = self._send_command(self.playlist_url)
        return r

    def play(self):
        r = self._send_command(self.play_url)

    def stop(self):
        r = self._send_command(self.stop_url)

    def play_next(self):
        r = self._send_command(self.play_next_url)

    def play_previous(self):
        r = self._send_command(self.play_previous_url)

    def empty_playlist(self):
        r = self._send_command(self.empty_playlist_url)

    def toggle_random(self):
        r = self._send_command(self.random_toggle_url)

    def toggle_loop(self):
        r = self._send_command(self.loop_toggle_url)
    
    def toggle_repeat(self):
        r = self._send_command(self.repeat_toggle_url)

    def toggle_fullscreen(self):
        r = self._send_command(self.fullscreen_toggle_url)

    def _send_command(self, command_url, mrl_or_id = None):
        if mrl_or_id == None:
            tmp_url = command_url
        else:
            tmp_url = command_url + mrl_or_id
        
        try:
            r = requests.get(tmp_url, auth=('', self.password))
        except ConnectionError:
            self.connection_error = True
            # What should I return on failure?
            return 0
        else:
            self.connection_error = False
            self.last_http_status_code = r.status_code
            return r       
