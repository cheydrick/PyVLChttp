import requests
import json

def _make_command(url_name, parameters):
    def command_function(self):
        return self._send_command(self.URLs[url_name], parameters)

    return command_function

def _make_simple_command(command):
    return _make_command('status', {'command': command})


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
        self.URLs = {
            'status': self.vlc_url + '/requests/status.json',
            'playlist': self.vlc_url + '/requests/playlist.json',
            'browse': self.vlc_url + '/requests/browse.json',
            }

        # Last HTTP status code storage
        self.last_http_status_code = None
        # Last response storage
        self.last_response = None


    def get_status(self):
        r = self._send_command(self.URLs['status'])
        return json.loads(r.text)
    
    def get_playlist(self):
        #TODO make this return something sensible
        r = self._send_command(self.playlist_url)
        return r

    play = _make_simple_command('pl_play')
    pause = _make_simple_command('pl_pause')
    stop = _make_simple_command('pl_stop')
    play_next = _make_simple_command('pl_next')
    play_previous = _make_simple_command('pl_previous')

    empty_playlist = _make_simple_command('pl_empty')
    toggle_random = _make_simple_command('pl_random')
    toggle_loop = _make_simple_command('pl_loop')
    toggle_repeat = _make_simple_command('pl_repeat')
    toggle_fullscreen = _make_simple_command('fullscreen')
    
    def add_to_playlist(self, mrl):
       _make_command('status', {'command': 'in_enqueue', 'input': mrl})(self)

    def browse_dir(self, dir):
        ''' >>>browse_dir('/Users/Joe/Media/') '''
        # TODO make this return something sensible
        response = _make_command('browse', {'dir': dir})(self)
        return response

    def _send_command(self, command_url, command_params={}):
        self.last_response = requests.get(command_url, params=command_params, auth=('', self.password))
        self.last_http_status_code = self.last_response.status_code
        return self.last_response
