import requests
import sys
import json

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
        self.vlc_url = 'http://' + ip + ':' + port
        self.password = password

        # URLs that return status/playlist
        self.status_url = self.vlc_url + '/requests/status.json'
        self.playlist_url = self.vlc_url + '/requests/playlist.json'
        self.browse_url = self.vlc_url + '/requests/browse.json'
        
        # URLs that send simple commands
        self.play_url = self.status_url + '?command=pl_play'
        self.stop_url = self.status_url + '?command=pl_stop'
        self.play_next_url = self.status_url + '?command=pl_next'
        self.play_previous_url = self.status_url + '?command=pl_previous'
        self.empty_playlist_url = self.status_url + '?command=pl_empty'
        self.random_toggle_url = self.status_url + '?command=pl_random'
        self.loop_toggle_url = self.status_url + '?command=pl_loop'
        self.toggle_repeat_url = self.status_url + '?command=pl_repeat'
        self.toggle_fullscreen_url = self.status_url + '?command=fullscreen'

        # URLs that require additional arguments
        self.play_mrl_url_prefix = self.status_url + '?command=in_play&input='
        self.add_mrl_playlist_url_prefix = self.status_url + '?command=in_enqueue&input='
        self.play_id_url_prefix = self.status_url + '?command=pl_play&id='
        self.browse_dir_url_prefix = self.browse_url + '?dir='

        # Last HTTP status code storage
        self.last_http_status_code = None
        # Last response storage
        self.last_response = None


    def get_status(self):
        r = self._send_command(self.status_url)
        return json.loads(r.text)
    
    def get_playlist(self):
        #TODO make this return something sensible
        r = self._send_command(self.playlist_url)
        return r

    def play(self):
        self._send_command(self.play_url)

    def stop(self):
        self._send_command(self.stop_url)

    def play_next(self):
        self._send_command(self.play_next_url)

    def play_previous(self):
        self._send_command(self.play_previous_url)

    def empty_playlist(self):
        self._send_command(self.empty_playlist_url)

    def toggle_random(self):
        self._send_command(self.random_toggle_url)

    def toggle_loop(self):
        self._send_command(self.loop_toggle_url)
    
    def toggle_repeat(self):
        self._send_command(self.toggle_repeat_url)

    def toggle_fullscreen(self):
        self._send_command(self.toggle_fullscreen_url)
    
    def add_to_playlist(self, mrl):
        self._send_command(self.add_mrl_playlist_url_prefix, mrl)

    def browse_dir(self, dir):
        ''' >>>browse_dir('/Users/Joe/Media/') '''
        # TODO make this return something sensible
        r = self._send_command(self.browse_dir_url_prefix, dir)
        return r

    def _send_command(self, command_url, mrl_or_id = None):
        if mrl_or_id == None:
            tmp_url = command_url
        else:
            tmp_url = command_url + mrl_or_id

        self.last_response = requests.get(tmp_url, auth=('', self.password))
        self.last_http_status_code = self.last_response.status_code
        return self.last_response
