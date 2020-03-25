# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/GREGUpdater/plugin.py
from Screens.Screen import Screen
from Screens.Console import Console
from Screens.ChoiceBox import ChoiceBox
from Screens.MessageBox import MessageBox
from Components.ActionMap import ActionMap, NumberActionMap
from Components.MenuList import MenuList
from Components.Sources.List import List
from Plugins.Plugin import PluginDescriptor
from Components.Button import Button
from Components.Label import Label
from Components.ScrollLabel import ScrollLabel
from enigma import eConsoleAppContainer
import Components.PluginComponent
from Tools.Directories import pathExists, fileExists
import glob
import os
path = '/usr/lib/enigma2/python/Plugins/Extensions/GREGUpdater/scripts/'

class GREGUpdater(Screen):
    skin = '\n\t<screen name="GREGUpdater" position="center,center" size="560,400" title="">\n\t\t<ePixmap pixmap="skin_default/buttons/red.png" position="0,0" size="140,40" alphatest="on"/>\n\t\t<ePixmap pixmap="skin_default/buttons/green.png" position="140,0" size="140,40" alphatest="on"/>\n\t\t<widget name="key_red" position="0,0" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1"/>\n\t\t<widget name="key_green" position="140,0" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#1f771f" transparent="1"/>\n\t\t<widget name="lab1" position="0,50" size="560,50" font="Regular; 20" zPosition="2" transparent="0" halign="center"/>\n\t\t<widget name="list" position="10,105" size="540,300" scrollbarMode="showOnDemand"/>\n\t\t<applet type="onLayoutFinish">\n\t\t\tself["list"].instance.setItemHeight(25)\n\t\t</applet>\n\t</screen>'

    def __init__(self, session, args = 0):
        self.session = session
        Screen.__init__(self, session)
        self.skinName = ['GREGUpdater', 'ScriptRunner', 'VIXTAR.GZInstaller']
        self['actions'] = ActionMap(['OkCancelActions', 'ColorActions'], {'red': self.close,
         'green': self.action,
         'ok': self.action,
         'cancel': self.close}, -2)
        self['key_red'] = Button(_('Close'))
        self['key_green'] = Button(_('Run'))
        self['list'] = MenuList([])
        self['info'] = Label()
        self.slist = []
        title = 'GREG Updater'
        self.setTitle(title)
        for root, dirs, files in os.walk(path):
            for name in files:
                self.slist.append(name[:-3])

        self['list'].setList(self.slist)
        for f in glob.glob(path + '*.sh*'):
            os.system('chmod 755 ' + f)

    def action(self):
        sel = self['list'].getSelectionIndex()
        if sel is not None:
            self.shname = self.slist[sel] + '.sh'
            self.cmd = path + self.shname
            message = _('Are you ready to run the script ?')
            ybox = self.session.openWithCallback(self.Run, MessageBox, message, MessageBox.TYPE_YESNO)
            ybox.setTitle(_('Run Confirmation'))
        else:
            self.session.open(MessageBox, _('You have no script to run.'), MessageBox.TYPE_INFO, timeout=10)
        return

    def Run(self, answer):
        if answer is True:
            title = _(self.shname[:-3])
            self.session.open(Console, _(title), [self.cmd])


def main(session, **kwargs):
    session.open(GREGUpdater)


def Plugins(**kwargs):
    return [PluginDescriptor(name='GREG Skins UPDATER', description='Install GREG latest Skins ', where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main, icon='custom-logo.png')]