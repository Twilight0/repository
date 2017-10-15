# -*- coding: utf-8 -*-

"""
    Toronto-Channels Add-on
    Author: Twilight0

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os, sys, urlparse
import xbmcaddon, xbmcgui, xbmcplugin, xbmc, xbmcvfs

# Addon variables:
join = os.path.join
addon = xbmcaddon.Addon()
language = addon.getLocalizedString
addonname = addon.getAddonInfo("name")
addonid = addon.getAddonInfo("id")
addonpath = addon.getAddonInfo("path")
addonfanart = addon.getAddonInfo("fanart")
addItem = xbmcplugin.addDirectoryItem
endDir = xbmcplugin.endOfDirectory
transpath = xbmc.translatePath
datapath = transpath(addon.getAddonInfo("profile")).decode("utf-8")
dialog = xbmcgui.Dialog()
infoLabel = xbmc.getInfoLabel
fp = infoLabel('Container.FolderPath')
player = xbmc.Player().play

# Misc variables:
addonicon = join(addonpath, 'icon.png')
addonart = join(addonpath, 'resources/media')
NETVToronto_img = join(addonart, 'NETV_Toronto.png')
NETVToronto_2_img = join(addonart, 'NETV_Toronto_2.png')
Cannali_img = join(addonart, 'CANNALI_WEB_MUSIC.png')
Melodia_img = join(addonart, 'RADIO_MELODIA_TORONTO.png')
Life_img = join(addonart, 'LIFEHD.png')
Eugo24_img = join(addonart, 'EUGO24.png')
Settings_img = join(addonart, 'settings.png')
Voice_img = join(addonart, 'mag_oct_thumb.jpg')
Voice_path = join(addonart, 'mag_oct.jpg')

# Links:
if addon.getSetting('hls') == 'false':
    NETVToronto_url = 'rtmp://live.netvtoronto.com/NetvToronto/NetvToronto'
    NETV_Toronto_2_url = 'rtmp://162.219.176.210/live/eugo242017p1a'
    Eugo24_url = 'rtmp://162.219.176.210:18935/live/eugo242017p1a'
    Cannali_url = 'rtmp://live.streams.ovh/cannali/cannali'
    Life_url = 'rtmp://live.streams.ovh:1935/LIFEHD/LIFEHD'
else:
    NETVToronto_url = 'http://live.netvtoronto.com:1935/NetvToronto/NetvToronto/playlist.m3u8'
    NETV_Toronto_2_url = 'http://162.219.176.210/live/eugo242017p1a/playlist.m3u8'
    Eugo24_url = 'http://162.219.176.210:18935/live/eugo242017p1a/playlist.m3u8'
    Cannali_url = 'http://live.streams.ovh:1935/cannali/cannali/playlist.m3u8'
    Life_url = 'http://live.streams.ovh:1935/LIFEHD/LIFEHD/playlist.m3u8'

Melodia_url = 'http://149.202.208.214:9086/live'

# Handlers:
sysaddon = sys.argv[0]
syshandle = int(sys.argv[1])
params = dict(urlparse.parse_qsl(sys.argv[2][1:]))
action = params.get('action', None)
url = params.get('url')


def play_item(path):

    li = xbmcgui.ListItem(path=path)
    xbmcplugin.setResolvedUrl(syshandle, True, listitem=li)

def display(path):

    return xbmc.executebuiltin('ShowPicture({0})'.format(path))


def main_menu():

    xbmcplugin.setContent(int(sys.argv[1]), 'movies')

    # NETV Toronto
    if addon.getSetting('netv') == 'true':
        url1 = '{0}?action=play&url={1}'.format(sysaddon, NETVToronto_url)
        li1 = xbmcgui.ListItem(label='NETV Toronto', iconImage=NETVToronto_img)
        li1.setArt({'poster': NETVToronto_img, 'thumb': NETVToronto_img, 'fanart': addonfanart})
        li1.setInfo('video', {'title': 'NETV Toronto', 'plot': language(30006), 'genre': 'Live'})
        li1.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url1, listitem=li1, isFolder=False)
    elif addon.getSetting('netv') == 'false':
        pass

    # NETV Toronto 2
    if addon.getSetting('netv2') == 'true':
        url2 = '{0}?action=play&url={1}'.format(sysaddon, NETV_Toronto_2_url)
        li2 = xbmcgui.ListItem(label='NETV Toronto 2', iconImage=NETVToronto_2_img)
        li2.setArt({'poster': NETVToronto_2_img, 'thumb': NETVToronto_2_img, 'fanart': addonfanart})
        li2.setInfo('video', {'title': 'NETV Toronto 2', 'plot': language(30019), 'genre': 'Live'})
        li2.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url2, listitem=li2, isFolder=False)
    elif addon.getSetting('netv2') == 'false':
        pass

    # Eugo24
    if addon.getSetting('eugo24') == 'true':
        url3 = '{0}?action=play&url={1}'.format(sysaddon, Eugo24_url)
        li3 = xbmcgui.ListItem(label='Eugo24', iconImage=Eugo24_img)
        li3.setArt({'poster': Eugo24_img, 'thumb': Eugo24_img, 'fanart': addonfanart})
        li3.setInfo('video', {'title': 'Eugo24', 'plot': language(30021), 'genre': 'Live'})
        li3.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url3, listitem=li3, isFolder=False)
    elif addon.getSetting('eugo24') == 'false':
        pass

    # Life HD
    if addon.getSetting('life') == 'true':
        url4 = '{0}?action=play&url={1}'.format(sysaddon, Life_url)
        li4 = xbmcgui.ListItem(label='Life HD', iconImage=Life_img)
        li4.setArt({'poster': Life_img, 'thumb': Life_img, 'fanart': addonfanart})
        li4.setInfo('video', {'title': 'Life HD', 'plot': language(30008), 'genre': 'Live'})
        li4.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url4, listitem=li4, isFolder=False)
    elif addon.getSetting('life') == 'false':
        pass

    # Cannali Music
    if addon.getSetting('cannali') == 'true':
        url5 = '{0}?action=play&url={1}'.format(sysaddon, Cannali_url)
        li5 = xbmcgui.ListItem(label='CANNALI Music', iconImage=Cannali_img)
        li5.setArt({'poster': Cannali_img, 'thumb': Cannali_img, 'fanart': addonfanart})
        li5.setInfo('video', {'title': 'CANNALI Music', 'plot': language(30007), 'genre': 'Live'})
        li5.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url5, listitem=li5, isFolder=False)
    elif addon.getSetting('cannali') == 'false':
        pass

    # Radio Melodia Toronto
    if addon.getSetting('melodia') == 'true':
        url6 = '{0}?action=play&url={1}'.format(sysaddon, Melodia_url)
        li6 = xbmcgui.ListItem(label='Radio Melodia Toronto', iconImage=Melodia_img)
        li6.setArt({'poster': Melodia_img, 'thumb': Melodia_img, 'fanart': addonfanart})
        li6.setInfo('music', {'title': 'Radio Melodia Toronto', 'comment': language(30009), 'genre': 'Live'})
        li6.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url6, listitem=li6, isFolder=False)
    elif addon.getSetting('melodia') == 'false':
        pass

    # Voice Life & Style
    if addon.getSetting('voice') == 'true':
        url7 = '{0}?action=display&url={1}'.format(sysaddon, Voice_path)
        li7 = xbmcgui.ListItem(label='Voice Life & Style', iconImage=Voice_img)
        li7.setArt({'poster': Voice_img, 'thumb': Voice_img, 'fanart': addonfanart})
        li7.setInfo('image', {'title': 'Voice Life & Style', 'picturepath': Voice_path})
        li7.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url7, listitem=li7, isFolder=False)
    elif addon.getSetting('melodia') == 'false':
        pass

    # Settings
    settings_url = '{0}?action=settings'.format(sysaddon)
    settings_li = xbmcgui.ListItem(label=language(30001), iconImage=Settings_img)
    settings_li.setArt({'thumb': Settings_img, 'fanart': addonfanart})
    addItem(handle=syshandle, url=settings_url, listitem=settings_li, isFolder=True)

    endDir(syshandle)


if action is None:

    if 'audio' in fp:
        listitem = xbmcgui.ListItem(thumbnailImage=Melodia_img)
        listitem.setInfo('music', {'title': 'Radio Melodia Toronto', 'genre': 'Greek Music'})
        player(item=Melodia_url, listitem=listitem)
    elif 'image' in fp:
        display(Voice_path)
    else:
        main_menu()

elif action == 'play':

    play_item(url)

elif action == 'display':

    display(url)

elif action == 'settings':

    addon.openSettings()

elif action == 'setup_iptv':

    if not xbmcvfs.exists(datapath):

        xbmcvfs.mkdirs(datapath)

    iptv_folder = transpath('special://profile/addon_data/pvr.iptvsimple')

    def seq():

        xbmcvfs.copy(join(addonpath, 'resources', 'iptv', 'iptv_settings.xml'), join(iptv_folder, 'settings.xml'))
        # xbmcvfs.copy(join(addonpath, 'resources', 'iptv', 'simple-client.m3u'), join(datapath, 'simple-client.m3u'))
        iscon = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
        liveon = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
        xbmc.executeJSONRPC(iscon)
        xbmc.executeJSONRPC(liveon)
        dialog.notification(addonname, language(30015), sound=False)

    if not xbmcvfs.exists(join(iptv_folder, 'settings.xml')):

        xbmcvfs.mkdirs(iptv_folder)

        if dialog.yesno(addonname, language(30013), language(30014)):
            seq()
        else:
            dialog.notification(addonname, language(30016), sound=False)

    elif xbmcvfs.exists(join(iptv_folder, 'settings.xml')):

        if dialog.yesno(addonname, language(30013), language(30017)):
            seq()
        else:
            dialog.notification(addonname, language(30016), sound=False)
