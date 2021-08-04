import threading
import StellarPlayer
import os
import shutil
import traceback
import sys 
import importlib
import json

from . import douyu
#from . import iqiyi
#from . import sports_iqiyi
#from . import fengbolive
#from . import look
#from . import ppsport
#from . import yangshipin
from . import zhibotv
from . import acfun
from . import bilibili
from . import cc
from . import changyou
from . import douyin
from . import egame
from . import hongle
from . import huajiao
from . import huomao
from . import huya
from . import imifun
from . import immomo
from . import inke
from . import ixigua
from . import jd
from . import kbs
from . import kk
from . import kuaishou
from . import kugou
from . import kuwo
from . import laifeng
from . import lehai
from . import longzhu
from . import maoer
from . import now
from . import pps
from . import qf
from . import qie
from . import renren
from . import showself
from . import tiktok
from . import tuho
from . import twitch
from . import v6cn
from . import wali
from . import woxiu
from . import xunlei
from . import yizhibo
from . import youku
from . import yuanbobo
from . import yy
from . import zhanqi

m2cq = importlib.import_module('zhibo.2cq')
m9xiu = importlib.import_module('zhibo.9xiu')
m17live = importlib.import_module('zhibo.17live')
m51lm = importlib.import_module('zhibo.51lm')
m95xiu = importlib.import_module('zhibo.95xiu')
m173 = importlib.import_module('zhibo.173')

class uiplugin(StellarPlayer.IStellarPlayerPlugin):
    def __init__(self,player:StellarPlayer.IStellarPlayer):
        super().__init__(player)
        print("init zhibo plugin")
        self.grid_val = []
        self.net = ''

    def show(self):
        print('ui start')
        self.grid_val = [
        {'直播网站':'斗鱼','网址':'www.douyu.com'},
#        {'直播网站':'爱奇艺'},
#        {'直播网站':'爱奇艺体育'},
#        {'直播网站':'新浪疯播'},
#        {'直播网站':'网易LOOK'},
#        {'直播网站':'PPTV体育'},
#        {'直播网站':'央视频'},
        {'直播网站':'虎牙','网址':'www.huya.com/l'},
        {'直播网站':'抖音','网址':'www.douyin.com/live','房间号':'分享链接'},
        {'直播网站':'花椒','网址':'huajiao.com'},
        {'直播网站':'龙珠','网址':'longzhu.com'},
        {'直播网站':'中国体育','网址':'website.zhibo.tv/live'},
        {'直播网站':'西瓜','网址':'live.ixigua.com'},
        {'直播网站':'企鹅电竞','网址':'egame.qq.com/livelist'},
        {'直播网站':'战旗','网址':'zhanqi.tv/lives'},
        {'直播网站':'棉花糖','网址':'www.2cq.com'},
        {'直播网站':'九秀','网址':'www.9xiu.com'},
        {'直播网站':'17直播','网址':'17.live/live'},
        {'直播网站':'羚萌','网址':'live.51lm.tv'},
        {'直播网站':'95秀','网址':'www.95.cn'},
        {'直播网站':'艺气山','网址':'www.173.com'},
        {'直播网站':'acfun','网址':'live.acfun.cn'},
        {'直播网站':'bilibili'},
        {'直播网站':'网易cc','网址':'cc.163.com'},
        {'直播网站':'畅秀阁','网址':'cxg.changyou.com'},
        {'直播网站':'红人','网址':'www.hongle.tv'},
        #{'直播网站':'火猫'},
        {'直播网站':'艾米','网址':'www.imifun.com'},
        #{'直播网站':'陌陌'},
        {'直播网站':'映客','网址':'www.inke.cn'},
        #{'直播网站':'京东'},
        #{'直播网站':'腾讯体育'},
        {'直播网站':'KK','网址':'www.kktv5.com'},
        #{'直播网站':'快手'},
        {'直播网站':'酷狗繁星','网址':'fanxing.kugou.com'},
        {'直播网站':'酷我聚星','网址':'jx.kuwo.cn'},
        {'直播网站':'来疯','网址':'v.laifeng.com'},
        #{'直播网站':'乐嗨'},
        {'直播网站':'猫耳','网址':'fm.missevan.com'},
        {'直播网站':'NOW','网址':'now.qq.com'},
        {'直播网站':'PPS奇秀','网址':'x.pps.tv'},
        {'直播网站':'56千帆','网址':'qf.56.com'},
        {'直播网站':'企鹅体育','网址':'live.qq.com/directory/all'},
        #{'直播网站':'人人'},
        {'直播网站':'秀色','网址':'www.showself.com'},
        #{'直播网站':'TikTok'},
        {'直播网站':'星光','网址':'www.tuho.tv'},
        #{'直播网站':'twitch'},
        #{'直播网站':'六间房'},
        {'直播网站':'小米','网址':'live.wali.com/fe'},
        {'直播网站':'我秀','网址':'woxiu.com'},
        {'直播网站':'迅雷','网址':'live.xunlei.com'},
        {'直播网站':'优酷轮播','网址':'live.youku.com'},
        #{'直播网站':'热猫'},
        {'直播网站':'YY','网址':'yy.com'},
        ]
        grid_item_layout = [[{'type':'label','name':'直播网站','width':0.15},{'type':'link','name':'网址','width':0.3,'clickable':True},{'type':'label','name':'房间号','width':60},{'type':'edit','name':'roomid','width':0.35},{'type':'space'},{'type':'button','name':'播放','width':60}]]
        controls = [{'type':'space','height':5},
        [{'type':'list','name':'list1','itemheight':0.9,'itemwidth':300, 'itemlayout':grid_item_layout,'value':self.grid_val,'marginSize':5}],
        {'type':'space','height':5},
        #{'group':[{'type':'edit','name':'房间号','width':0.9,'height':30}],'height':40},
        ]
        
        result, controls = self.player.doModal('main', 800, 600, '看各种直播门户', controls)
        print(f'{result=},{controls=}')


    def onClick(self,page,control):
        print('onClick,{control=}')
            

    def onListItemClick(self, page, control, item):
        print(f'onListItemClick')


    def onListItemControlClick(self, page, listControl, item, itemControl):
        self.net = self.grid_val[item]['直播网站']
        if itemControl == '播放':
            room = self.player.getListItemControlValue('main','list1',item,'roomid')
            print(f'{room=}')
            self.getLiveUrl(self.net,room)
         
    def stop(self):
        super().stop()
        print("pugin stop")
        
    def getLiveUrl(self,web,room):
        if  web == '斗鱼' :
            url = douyu.get_real_url(room)
#        elif  web == '新浪疯播' :
#            url = fengbolive.get_real_url(room)
#        elif  web == '爱奇艺' :
#            url = iqiyi.get_real_url(room)
#        elif  web == '网易LOOK' :
#            url = look.get_real_url(room)
#        elif  web == 'PPTV体育' :
#            url = ppsport.get_real_url(room)
#        elif  web == '爱奇艺体育' :
#            url = sports_iqiyi.get_real_url(room)
#        elif  web == '央视频' :
#            url = yangshipin.get_real_url(room)
        elif web == '中国体育' :
            url = zhibotv.get_real_url(room)
        elif  web == '棉花糖' :
            url = m2cq.get_real_url(room)
        elif  web == '九秀' :
            url = m9xiu.get_real_url(room)
        elif  web == '17直播' :
            url = m17live.get_real_url(room)
        elif  web == '羚萌' :
            url = m51lm.get_real_url(room)
        elif  web == '95秀' :
            url = m95xiu.get_real_url(room)
        elif  web == '艺气山' :
            url = m173.get_real_url(room)
        elif  web == 'acfun' :
            url = acfun.get_real_url(room) 
        elif  web == '网易cc' :
            url = cc.get_real_url(room) 
        elif  web == '畅秀阁' :
            url = changyou.get_real_url(room) 
        elif  web == '抖音' :
            url = douyin.get_real_url(room) 
        elif  web == '企鹅电竞' :
            url = egame.get_real_url(room)
        elif  web == '红人' :
            url = hongle.get_real_url(room)
        elif  web == '花椒' :
            url = huajiao.get_real_url(room)
        #elif  web == '火猫' :
        #    url = huomao.get_real_url(room)
        elif  web == '虎牙' :
            hyjson = huya.get_real_url(room)
            url = hyjson['al_flv']
        elif  web == '艾米' :
            url = imifun.get_real_url(room)
        #elif  web == '陌陌' :
        #    url = immomo.get_real_url(room)
        elif  web == '映客' :
            ykjson = inke.get_real_url(room)
            url = ykjson['record_url']        
        elif  web == '西瓜' :
            xgjson = ixigua.get_real_url(room)
            xgdata = json.loads(xgjson)
            print(xgdata[0])
            url = xgdata[0]['FlvUrl']
        #elif  web == '京东' :
        #    url = jd.get_real_url(room)
        elif  web == '腾讯体育' :
            url = kbs.get_real_url(room)
        elif  web == 'KK' :
            url = kk.get_real_url(room)
        #elif  web == '快手' :
        #    url = kuaishou.get_real_url(room)
        elif  web == '酷狗繁星' :
            url = kugou.get_real_url(room)
        elif  web == '酷我聚星' :
            url = kuwo.get_real_url(room)
        elif  web == '来疯' :
            lfjson = laifeng.get_real_url(room)
            url = lfjson['HttpFlv']
        #elif  web == '乐嗨' :
        #    url = lehai.get_real_url(room)
        elif  web == '龙珠' :
            url = longzhu.get_real_url(room)
        elif  web == '猫耳' :
            mejson = maoer.get_real_url(room)
            url = mejson['flv_pull_url']
        elif  web == 'NOW' :
            url = now.get_real_url(room)
        elif  web == 'PPS奇秀' :
            url = pps.get_real_url(room)
        elif  web == '56千帆' :
            url = qf.get_real_url(room)
        elif  web == '企鹅体育' :
            url = qie.get_real_url(room)
        #elif  web == '人人' :
        #    url = renren.get_real_url(room)
        elif  web == '秀色' :
            url = showself.get_real_url(room)
        #elif  web == 'TikTok' :
        #    url = tiktok.get_real_url(room)
        elif  web == '星光' :
            url = tuho.get_real_url(room)
        #elif  web == 'twitch' :
        #    url = twitch.get_real_url(room)
        #elif  web == '六间房' :
        #    url = v6cn.get_real_url(room)
        elif  web == '小米' :
            url = wali.get_real_url(room)
        elif  web == '我秀' :
            url = woxiu.get_real_url(room)
        elif  web == '迅雷' :
            url = xunlei.get_real_url(room)
        elif  web == '优酷轮播' :
            url = youku.get_real_url(room)
        #elif  web == '热猫' :
        #    url = yuanbobo.get_real_url(room)
        elif  web == 'YY' :
            url = yy.get_real_url(room)
        elif  web == '战旗' :
            url = zhanqi.get_real_url(room)
        elif  web == 'bilibili' :
            url = bilibili.get_real_url(room)
        if url != False and url != '':
            self.player.play(url)
           

def newPlugin(player:StellarPlayer.IStellarPlayer,*arg):
    plugin = uiplugin(player)
    return plugin

def destroyPlugin(plugin:StellarPlayer.IStellarPlayerPlugin):
    plugin.stop()

