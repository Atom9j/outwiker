# -*- coding: UTF-8 -*-

from parser.tokenfonts import FontsFactory, BoldToken, ItalicToken, BoldItalicToken, UnderlineToken
from parser.tokenheading import HeadingFactory
from parser.tokencommand import CommandFactory
from parser.tokenlink import LinkFactory
from parser.tokenurl import UrlFactory
from parser.tokenlinebreak import LineBreakFactory
from parser.tokennoformat import NoFormatFactory
from parser.tokenpreformat import PreFormatFactory
from parser.tokentext import TextFactory


class WikiColorizer (object):
    def __init__ (self, editor):
        self._editor = editor

        self.text = TextFactory.make (None)
        self.bold = FontsFactory.makeBold (None).setParseAction(lambda s, l, t: None)
        self.italic = FontsFactory.makeItalic (None).setParseAction(lambda s, l, t: None)
        self.bold_italic = FontsFactory.makeBoldItalic (None).setParseAction(lambda s, l, t: None)
        self.underline = FontsFactory.makeUnderline (None).setParseAction(lambda s, l, t: None)
        self.heading = HeadingFactory.make (None).setParseAction(lambda s, l, t: None)
        self.command = CommandFactory.make (None).setParseAction(lambda s, l, t: None)
        self.link = LinkFactory.make (None).setParseAction(lambda s, l, t: None)
        self.url = UrlFactory.make (None).setParseAction(lambda s, l, t: None)
        self.linebreak = LineBreakFactory.make (None).setParseAction(lambda s, l, t: None)
        self.noformat = NoFormatFactory.make (None).setParseAction(lambda s, l, t: None)
        self.preformat = PreFormatFactory.make (None).setParseAction(lambda s, l, t: None)

        self.colorParser = (
            self.url |
            self.text |
            self.linebreak |
            self.link |
            self.noformat |
            self.preformat |
            self.command |
            self.bold_italic |
            self.bold |
            self.italic |
            self.underline |
            self.heading)

        self.insideBlockParser = (
            self.url |
            self.text |
            self.linebreak |
            self.link |
            self.noformat |
            self.preformat |
            self.bold_italic |
            self.bold |
            self.italic |
            self.underline)


    def colorize (self, text):
        textlength = self._editor.calcByteLen (text)
        stylelist = [0] * textlength
        self._colorizeText (text, 0, textlength, self.colorParser, stylelist)

        return stylelist


    def _colorizeText (self, text, start, end, parser, stylelist):
        tokens = parser.scanString (text[start: end])

        for token in tokens:
            pos_start = token[1] + start
            pos_end = token[2] + start

            tokenname = token[0].getName()

            if tokenname == "text":
                self._editor.runSpellChecking (stylelist, pos_start, pos_end)
                continue

            if (tokenname == "linebreak" or
                    tokenname == "noformat" or
                    tokenname == "preformat"):
                continue

            # Нас интересует позиция в байтах, а не в символах
            bytepos_start = self._editor.calcBytePos (text, pos_start)
            bytepos_end = self._editor.calcBytePos (text, pos_end)

            # Применим стиль
            if tokenname == "bold":
                self._editor.addStyle (stylelist,
                                       self._editor.STYLE_BOLD_ID,
                                       bytepos_start,
                                       bytepos_end)
                self._colorizeText (text,
                                    pos_start + len (BoldToken.start),
                                    pos_end - len (BoldToken.end),
                                    self.insideBlockParser, stylelist)

            elif tokenname == "italic":
                self._editor.addStyle (stylelist,
                                       self._editor.STYLE_ITALIC_ID,
                                       bytepos_start,
                                       bytepos_end)
                self._colorizeText (text,
                                    pos_start + len (ItalicToken.start),
                                    pos_end - len (ItalicToken.end),
                                    self.insideBlockParser, stylelist)

            elif tokenname == "bold_italic":
                self._editor.addStyle (stylelist,
                                       self._editor.STYLE_BOLD_ITALIC_ID,
                                       bytepos_start,
                                       bytepos_end)
                self._colorizeText (text,
                                    pos_start + len (BoldItalicToken.start),
                                    pos_end - len (BoldItalicToken.end),
                                    self.insideBlockParser, stylelist)

            elif tokenname == "underline":
                self._editor.addStyle (stylelist,
                                       self._editor.STYLE_UNDERLINE_ID,
                                       bytepos_start,
                                       bytepos_end)
                self._colorizeText (text,
                                    pos_start + len (UnderlineToken.start),
                                    pos_end - len (UnderlineToken.end),
                                    self.insideBlockParser,
                                    stylelist)

            elif tokenname == "heading":
                self._editor.setStyle (stylelist,
                                       self._editor.STYLE_HEADING_ID,
                                       bytepos_start,
                                       bytepos_end)
                self._editor.runSpellChecking (stylelist, pos_start, pos_end)

            elif tokenname == "command":
                self._editor.setStyle (stylelist,
                                       self._editor.STYLE_COMMAND_ID,
                                       bytepos_start,
                                       bytepos_end)

            elif tokenname == "link":
                self._editor.addStyle (stylelist,
                                       self._editor.STYLE_LINK_ID,
                                       bytepos_start,
                                       bytepos_end)
                self._editor.runSpellChecking (stylelist, pos_start, pos_end)

            elif tokenname == "url":
                self._editor.addStyle (stylelist,
                                       self._editor.STYLE_LINK_ID,
                                       bytepos_start,
                                       bytepos_end)
