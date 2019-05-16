VLCHTTPAPI is a Python module that uses the VLC HTTP API to control VLC.

Usage:
    >>>from pyvlchttp import VLCHTTPAPI
    >>>vlc = VLCHTTPAPI('127.0.0.1', '8080', 'password')
    >>>vlc.play()
    >>>vlc.last_http_status_code
    200
    >>>vlc.stop()
    etc...

None of the functions check the HTTP status codes for success. This is the responsibility
of the caller.

VLC HTTP spec is documented at https://wiki.videolan.org/VLC_HTTP_requests/, and
is documented in more detail in VideoLAN\VLC\lua\http\requests\README.txt wherever VLC
is installed.

TODO:
    - Implement all of the functions in VLCHTTPAPI() that require additional arguments
    - Comments/Examples
    - Utility functions for converting browse_dir() output to something useful
    - Tests (integration more so than unit)
