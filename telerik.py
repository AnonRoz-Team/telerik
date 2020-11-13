#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
G = '\033[0;32m'; C = '\033[0;36m'; W = '\033[0;37m'; R = '\033[0;31m'; Y='\033[0;33m'
import requests, os, sys
from multiprocessing.pool import ThreadPool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
def check(site):
	try:
		exp_=requests.get(site+'/DesktopModules/Admin/RadEditorProvider/DialogHandler.aspx',verify=False,timeout=10).text
		if 'Loading the dialog' in exp_:print ('%s[%s✓%s] %s%s'%(W,G,W,G,site));open('vuln.txt','a+').write(site+'/DesktopModules/Admin/RadEditorProvider/DialogHandler.aspx\n')
		else:
			_exp_=requests.get(site+'/providers/htmleditorproviders/telerik/telerik.web.ui.dialoghandler.aspx',verify=False,timeout=10).text
			if 'Loading the dialog' in _exp_:print ('%s[%s✓%s] %s%s'%(W,G,W,G,site));open('vuln.txt','a+').write(site+'/providers/htmleditorproviders/telerik/telerik.web.ui.dialoghandler.aspx\n')
			else:
				_exp__=requests.get(site+'/desktopmodules/telerikwebui/radeditorprovider/telerik.web.ui.dialoghandler.aspx',verify=False,timeout=10).text
				if 'Loading the dialog' in _exp__:print ('%s[%s✓%s] %s%s'%(W,G,W,G,site));open('vuln.txt','a+').write(site+'/desktopmodules/telerikwebui/radeditorprovider/telerik.web.ui.dialoghandler.aspx\n')
				else:
					__exp__=requests.get(site+'/desktopmodules/dnnwerk.radeditorprovider/dialoghandler.aspx',verify=False,timeout=10).text
					if 'Loading the dialog' in __exp__:print ('%s[%s✓%s] %s%s'%(W,G,W,G,site));open('vuln.txt','a+').write(site+'/desktopmodules/dnnwerk.radeditorprovider/dialoghandler.aspx\n')
					else:print ('%s[%sx%s] %s%s'%(W,R,W,R,site))
	except:print ('%s[%sunk error%s] %s%s'%(W,R,W,R,site));pass
try:
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	os.system('clear')
	print '''%s
  ______    __        _ __
 /_  __/__ / /__ ____(_) /__    %sMass Telerik Checker%s
  / / / -_) / -_) __/ /  '_/    %sIG @anonroz_team%s
 /_/  \__/_/\__/_/ /_/_/\_\     %sFB gg.gg/AnonRoz-Team

	'''%(C,W,C,W,C,W)
	ThreadPool(30).map(check,open(sys.argv[1]).read().splitlines())
	print ('%s[%s DONE BROn%s]  Saved in vuln.txt'%(W,G,W))
except IndexError:exit('%s[%s!%s] Use : python2 %s target.txt\n    Example: https://target.com'%(W,R,W,sys.argv[0]))
except IOError:exit('%s[%s!%s] File does not exist'%(W,R,W))
except requests.exceptions.ConnectionError:exit('%s[%s!%s] Check internet'%(W,R,W))
except KeyboardInterrupt:exit('%s[%s!%s] Exit'%(W,R,W))