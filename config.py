import os
import subprocess
import dracula.draw
from qutebrowser.api import interceptor

config.load_autoconfig(False)

config.unbind('u'),
config.unbind('q'),

dracula.draw.blood(c, {
    'spacing': {
        'vertical': 6,
        'horizontal': 8
    }
})

def filter_yt(info: interceptor.Request):
    """Block the given request if necessary."""
    url = info.request_url
    if (
        url.host() == "www.youtube.com"
        and url.path() == "/get_video_info"
        and "&adformat=" in url.query()
    ):
        info.block()

interceptor.register(filter_yt)

config.set('content.autoplay', False, '*://*/*'),
config.set('content.notifications', False, '*://*/*')
