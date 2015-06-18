# -*- coding: UTF-8 -*-

import wx

from outwiker.core.application import Application
from outwiker.gui.guiconfig import TagsConfig


class TagsPanel(wx.Panel):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)

        self.ACTIONS_COMBOBOX_WIDTH = 300

        self._actions = [
            (_(u'Search pages with the tag'), TagsConfig.ACTION_SHOW_LIST),
            (_(u'Toggle tag selection'), TagsConfig.ACTION_MARK_TOGGLE),
        ]

        self._config = TagsConfig (Application.config)

        self._createGui()


    def _createGui (self):
        mainSizer = wx.FlexGridSizer (cols=1)
        mainSizer.AddGrowableCol (0)

        self._createColorsGui (mainSizer)
        self._createActionssGui (mainSizer)

        self.SetSizer (mainSizer)


    def _addControlsPairToSizer (self, sizer, label, control):
        sizer.Add(label, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=2)
        sizer.Add(control, 0, wx.ALL | wx.ALIGN_RIGHT, border=2)


    def _createColorsGui (self, mainsizer):
        colorFontNormalLabel = wx.StaticText (self, label = _(u'Tag color'))
        self.colorFontNormalPicker = wx.ColourPickerCtrl(self, style=wx.CLRP_SHOW_LABEL)

        colorFontNormalHoverLabel = wx.StaticText (self, label = _(u'Hover tag color'))
        self.colorFontNormalHoverPicker = wx.ColourPickerCtrl(self, style=wx.CLRP_SHOW_LABEL)

        colorFontSelectedLabel = wx.StaticText (self, label = _(u'Marked tag color'))
        self.colorFontSelectedPicker = wx.ColourPickerCtrl(self, style=wx.CLRP_SHOW_LABEL)

        colorFontSelectedHoverLabel = wx.StaticText (self, label = _(u'Hover marked tag color'))
        self.colorFontSelectedHoverPicker = wx.ColourPickerCtrl(self, style=wx.CLRP_SHOW_LABEL)

        colorBackSelectedLabel = wx.StaticText (self, label = _(u'Marked tag background'))
        self.colorBackSelectedPicker = wx.ColourPickerCtrl(self, style=wx.CLRP_SHOW_LABEL)

        colorsSizer = wx.FlexGridSizer(cols=2)
        colorsSizer.AddGrowableCol(0)
        colorsSizer.AddGrowableCol(1)

        self._addControlsPairToSizer (colorsSizer,
                                      colorFontNormalLabel,
                                      self.colorFontNormalPicker)

        self._addControlsPairToSizer (colorsSizer,
                                      colorFontSelectedLabel,
                                      self.colorFontSelectedPicker)

        self._addControlsPairToSizer (colorsSizer,
                                      colorBackSelectedLabel,
                                      self.colorBackSelectedPicker)

        self._addControlsPairToSizer (colorsSizer,
                                      colorFontNormalHoverLabel,
                                      self.colorFontNormalHoverPicker)

        self._addControlsPairToSizer (colorsSizer,
                                      colorFontSelectedHoverLabel,
                                      self.colorFontSelectedHoverPicker)

        mainsizer.Add (colorsSizer, 0, wx.EXPAND | wx.ALL, border = 2)


    def _createActionssGui (self, mainsizer):
        leftClickActionLabel = wx.StaticText (
            self,
            label = _(u'Left click on the tag')
        )

        self.leftClickActionCombo = wx.ComboBox (
            self,
            -1,
            style=wx.CB_DROPDOWN | wx.CB_READONLY)


        middleClickActionLabel = wx.StaticText (
            self,
            label = _(u'Middle click on the tag')
        )

        self.middleClickActionCombo = wx.ComboBox (
            self,
            -1,
            style=wx.CB_DROPDOWN | wx.CB_READONLY)

        self.leftClickActionCombo.SetMinSize((self.ACTIONS_COMBOBOX_WIDTH, -1))
        self.middleClickActionCombo.SetMinSize((self.ACTIONS_COMBOBOX_WIDTH, -1))

        self._fillActionsCombos()

        actionsSizer = wx.FlexGridSizer(cols=2)
        actionsSizer.AddGrowableCol(0)

        self._addControlsPairToSizer (actionsSizer,
                                      leftClickActionLabel,
                                      self.leftClickActionCombo)

        self._addControlsPairToSizer (actionsSizer,
                                      middleClickActionLabel,
                                      self.middleClickActionCombo)

        mainsizer.Add (actionsSizer, 0, wx.EXPAND | wx.ALL, border = 2)


    def _fillActionsCombos (self):
        for action in self._actions:
            self.leftClickActionCombo.Append (action[0])
            self.middleClickActionCombo.Append (action[0])

        self.leftClickActionCombo.SetSelection (0)
        self.middleClickActionCombo.SetSelection (0)

        for n, action in enumerate (self._actions):
            if action[1] == self._config.leftClickAction.value:
                self.leftClickActionCombo.SetSelection (n)

            if action[1] == self._config.middleClickAction.value:
                self.middleClickActionCombo.SetSelection (n)


    def LoadState(self):
        self.colorFontNormalPicker.SetColour (self._config.colorFontNormal.value)
        self.colorFontNormalHoverPicker.SetColour (self._config.colorFontNormalHover.value)

        self.colorFontSelectedPicker.SetColour (self._config.colorFontSelected.value)
        self.colorFontSelectedHoverPicker.SetColour (self._config.colorFontSelectedHover.value)

        self.colorBackSelectedPicker.SetColour (self._config.colorBackSelected.value)


    def _saveColorsState (self):
        self._config.colorFontNormal.value = self.colorFontNormalPicker.GetColour().GetAsString (wx.C2S_HTML_SYNTAX)
        self._config.colorFontNormalHover.value = self.colorFontNormalHoverPicker.GetColour().GetAsString (wx.C2S_HTML_SYNTAX)

        self._config.colorFontSelected.value = self.colorFontSelectedPicker.GetColour().GetAsString (wx.C2S_HTML_SYNTAX)
        self._config.colorFontSelectedHover.value = self.colorFontSelectedHoverPicker.GetColour().GetAsString (wx.C2S_HTML_SYNTAX)

        self._config.colorBackSelected.value = self.colorBackSelectedPicker.GetColour().GetAsString (wx.C2S_HTML_SYNTAX)


    def _saveActionsState (self):
        leftClickAction = self.leftClickActionCombo.GetSelection()
        middleClickAction = self.middleClickActionCombo.GetSelection()

        assert leftClickAction >= 0 and leftClickAction < len (self._actions)
        assert middleClickAction >= 0 and middleClickAction < len (self._actions)

        self._config.leftClickAction.value = self._actions[leftClickAction][1]
        self._config.middleClickAction.value = self._actions[middleClickAction][1]


    def Save (self):
        self._saveColorsState()
        self._saveActionsState()
