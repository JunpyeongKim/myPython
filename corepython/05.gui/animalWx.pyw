#!/usr/bin/env python
# encoding=utf-8

# animalWx.pyw

# Core Python Application Programming 3E, Wesley J. Chun
# - 5.4.3 wxWidgets and wxPython
#   - Example 5-9. wxPython GUI Demo
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/animalWx.py
#   - ImportError: No module named wx


import wx


class MyFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, title=''):
        wx.Frame.__init__(self, parent, id, title,
            size=(200,140))
        top = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        font = wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD)
        lb = wx.StaticText(top, -1,
            'Animals (in pairs; min: pair, max: dozen)')
        sizer.Add(lb)

        c1 = wx.StaticText(top, -1, 'Number:')
        c1.SetFont(font)
        ct = wx.SpinCtrl(top, -1, '2', min=2, max=12)
        sizer.Add(c1)
        sizer.Add(ct)

        c2 = wx.StaticText(top, -1, 'Type:')
        c2.SetFont(font)
        cb = wx.ComboBox(top, -1, '',
            choices=('dog', 'cat', 'hamster', 'python'))
        sizer.Add(c2)
        sizer.Add(cb)

        qb = wx.Button(top, -1, "QUIT")
        qb.SetBackgroundColour('red')
        qb.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON,
            lambda e: self.Close(True), qb)
        sizer.Add(qb)

        top.SetSizer(sizer)
        self.Layout()


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(title="wxWidgets")
        frame.Show(True)
        self.SetTopWindow(frame)
        return True


def main():
    app = MyApp()
    app.MainLoop()


if __name__ == '__main__':
    main()
