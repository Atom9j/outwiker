#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os.path

from outwiker.gui.baseaction import BaseAction
from outwiker.core.commands import openWiki
from outwiker.core.system import getCurrentDir


class OpenHelpAction (BaseAction):
    """
    Открыть справку
    """
    stringId = u"Help"

    def __init__ (self, application):
        self._application = application


    @property
    def title (self):
        return _(u"Help")


    @property
    def description (self):
        return _(u"Open help")
    

    def run (self, params):
        help_dir = u"help"
        current_help = _("help_en")
        path = os.path.join (getCurrentDir(), 
                help_dir, 
                current_help)
        openWiki (path, readonly=True)