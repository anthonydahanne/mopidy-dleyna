from __future__ import absolute_import, unicode_literals

import os

from mopidy import backend

import pykka

from . import Extension
from .dleyna import dLeynaClient
from .library import dLeynaLibraryProvider
from .playback import dLeynaPlaybackProvider


class dLeynaBackend(pykka.ThreadingActor, backend.Backend):

    uri_schemes = [Extension.ext_name]

    def __init__(self, config, audio):
        super(dLeynaBackend, self).__init__()
        # FIXME: how to use session bus?
        self.dleyna = dLeynaClient(os.environ['DBUS_SESSION_BUS_ADDRESS'])
        self.library = dLeynaLibraryProvider(self)
        self.playback = dLeynaPlaybackProvider(audio, self)
