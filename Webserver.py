#!/usr/bin/env python3

"""
JSON format expected:
    {
        'command': 'stop'|'up'|'down'|'left'|'right','raw',
        'duration': time_in_seconds,
        'data': raw_int_command
    }
"""

from threading import Thread, Event
from time import sleep
import http.server
import socketserver

import websocket

stop = Event()

def run():
    WS_PORT = 9876
    HTTP_PORT = 8000
        
    ws = websocket.Websocket(WS_PORT)
    Thread(target=ws.serve_forever, args=(stop,)).start()
    
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", HTTP_PORT), handler)
    Thread(target=httpd.serve_forever).start()

    try:
        while True:
            ws.transmit("Hey There!")
            data = websocket.receive(ws.s)
            print(data)
            if len(data) > 0:
                print("received [%s]" % (data))
            else:
                continue
            sleep(1)
    except KeyboardInterrupt:
        print('stopping')
        stop.set()
        httpd.shutdown()
    
if __name__ == "__main__":
    run()