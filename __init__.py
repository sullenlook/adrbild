#!/usr/bin/python
# -*- coding: utf-8 -*-

#author: SullenLook sullenlook@sullenlook.eu
#project: SiriServer plugin
#Testbild plugin


from plugin import *
import urllib
from BeautifulSoup import BeautifulSoup
from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView
from siriObjects.answerObjects import AnswerSnippet, AnswerObject, AnswerObjectLine

class adrbild(Plugin):

        res = {
                'adrbild': {
                        'de-DE': '.*deineadresse.*|.*Deine .*Adresse.*',
                }
        }

        @register("de-DE", res['adrbild']['de-DE'])
        def adrbild(self, speech, language):
                html = urllib.urlopen("http://siri.sullenlook.eu/banner.png/")
                soup = BeautifulSoup(html)
                ImageURL = "http://siri.sullenlook.eu/banner.png/"
                view = AddViews(self.refId, dialogPhase="Completion")
                ImageAnswer = AnswerObject(title=str("Du findest mich hier"),lines=[AnswerObjectLine(image="http://sullenlook.eu/Pix/cydia/info/testbild.png")])
                view1 = AnswerSnippet(answers=[ImageAnswer])
                view.views = [view1]
                self.sendRequestWithoutAnswer(view)
