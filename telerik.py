#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
C0 = "\033[0;36m"
C1 = "\033[1;36m"
G0 = "\033[0;32m"
G1 = "\033[1;32m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"

try:
	import requests, os, sys
	from multiprocessing.pool import ThreadPool
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
except:
	os.system('pip2 install requests')


def check(site):
	try:
		exp1=requests.get(site+'/DesktopModules/Admin/RadEditorProvider/DialogHandler.aspx',verify=False,timeout=10)
		if 'Loading the dialog' in exp1.text:
			print ('%s[%sYES VULN%s]  %s'%(W0,G0,W0,site))
			open('results.txt','a+').write(site+'/DesktopModules/Admin/RadEditorProvider/DialogHandler.aspx\n')
		else:
			exp2=requests.get(site+'/providers/htmleditorproviders/telerik/telerik.web.ui.dialoghandler.aspx',verify=False,timeout=10)
			if 'Loading the dialog' in exp2.text:
				print ('%s[%sYES VULN%s]  %s'%(W0,G0,W0,site))
				open('results.txt','a+').write(site+'/providers/htmleditorproviders/telerik/telerik.web.ui.dialoghandler.aspx\n')
			else:
				exp3=requests.get(site+'/desktopmodules/telerikwebui/radeditorprovider/telerik.web.ui.dialoghandler.aspx',verify=False,timeout=10)
				if 'Loading the dialog' in exp3.text:
					print ('%s[%sYES VULN%s]  %s'%(W0,G0,W0,site))
					open('results.txt','a+').write(site+'/desktopmodules/telerikwebui/radeditorprovider/telerik.web.ui.dialoghandler.aspx\n')
				else:
					exp4=requests.get(site+'/desktopmodules/dnnwerk.radeditorprovider/dialoghandler.aspx',verify=False,timeout=10)
					if 'Loading the dialog' in exp4.text:
						print ('%s[%sYES VULN%s]  %s'%(W0,G0,W0,site))
						open('results.txt','a+').write(site+'/desktopmodules/dnnwerk.radeditorprovider/dialoghandler.aspx\n')
					else:
						print ('%s[%sNOT VULN%s]  %s'%(W0,R0,W0,site))
	except:
		print ('%s[%sUNK EROR%s]  %s'%(W0,R0,W0,site))

try:
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	os.system('clear')
	print '''%s
  ______    __        _ __
 /_  __/__ / /__ ____(_) /__    %sMass Telerik Checker%s
  / / / -_) / -_) __/ /  '_/    %sIG @anonroz_team%s
 /_/  \__/_/\__/_/ /_/_/\_\     %sFB gg.gg/AnonRoz-Team
'''%(C1,W0,C1,W0,C1,W0)
	ThreadPool(30).map(check,open(sys.argv[1]).read().splitlines())
	print ('%s[%sDONE BRO%s]  Saved in results.txt'%(W0,G0,W0))
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] %sCheck internet'%(W1,R1,W1,W0))
except IndexError:
	exit('%s[%s!%s] %sUse : python2 %s target.txt \n%s[%s!%s] %sFill in target.txt with http/https'%(W1,R1,W1,W0,sys.argv[0],W1,R1,W1,W0))
except IOError:
	exit('%s[%s!%s] %sFile does not exist'%(W1,R1,W1,W0))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] %sExit'%(W1,R1,W1,W0))
