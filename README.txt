VLCHTTPAPI is a Python module that uses the VLC HTTP API to control VLC.

Usage:
    >>>import VLCHTTPAPI
    >>>vlc = VLCHTTPAPI()
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
    - Looks like the spec on the VLC website lags the spec in README.txt, need to review
    - Implement all of the functions in VLCHTTPAPI() that require additional arguments
    - Parse out returned XML (status/playlist) into something useful
        - Or maybe leave that up to the caller?
        - How about I include some helper classes for parsing the XML?
    - Comments/Examples
    - I need better ideas for how to inform the caller that a connection error
      happened, else the caller has to check the HTTP status and connection status
      every time (unless that's ok?). Maybe instead just check once on init and hope
      nothing bad happens later.
