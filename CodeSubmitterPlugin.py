import urllib2
import urllib
import json
import sys
import cookielib

"""Convert json string to a python object.

  Args:
    json_str: string, json response.
  Returns:
    dictionary of deserialized json string.
"""
def GetCookie(cookie_key, cookie_string):

    #logger.debug('Getting cookie from %s', cookie_string)
    id_string = cookie_key + '='
    cookie_crumbs = cookie_string.split(';')
    for c in cookie_crumbs:
      if id_string in c:
        cookie = c.split(id_string)
        return cookie[1]
    return None


#command line arguments to read problem name and file name
#args = str(sys.argv)
with open(sys.argv[2], 'r') as content_file:
    code = content_file.read()

#login
url = 'https://www.hackerrank.com/login'
payload = { 'login': 'username', 'password':'password', 'remember_me' : 'false' }

data = urllib.urlencode(payload)
# This urlencodes your data (that's why we need to import urllib at the top)

cookies = cookielib.LWPCookieJar()
handlers = [
    urllib2.HTTPHandler(),
    urllib2.HTTPSHandler(),
    urllib2.HTTPCookieProcessor(cookies)
    ]
opener = urllib2.build_opener(*handlers)
#opener = urllib2.build_opener()
response = opener.open(url, data)
headers = response.info()

'''print headers['Set-Cookie']
for cookie in cookies:
	print cookie'''

url = 'https://www.hackerrank.com/rest/contests/master/challenges/'+sys.argv[1]+'/compile_tests/'
payload = { 'code': code, 'language':'c', 'customtestcase' : 'false' }

data = urllib.urlencode(payload)
# This urlencodes your data (that's why we need to import urllib at the top)

opener = urllib2.build_opener()

#Add Headers
cookies = "hackerrank_mixpanel_token=eafd4d8d-3325-4b39-bf49-10ace362a5c6; fileDownload=true; hackerrankx_mixpanel_token=85336d93-8ed6-4402-bba5-c578ba73daa9; _hackerrank_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFRkkiJTcyMmMzYzBhYWM2MDIwMTFjMzI3ZDExNzMyYzExODhjBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVN3R2ROVHdtTVkyN0hVTGhQRCszV0paQmZVOTM5N3ZHb3JYK2FaYjhSbGc9BjsARg%3D%3D--ca04397079b869c26f2ad2f7941a5a88e0c4cc57; _cb_ls=1; _chartbeat2=Dj72p7C7gwm6COXKBx.1401276303648.1401276303648.1; _chartbeat_uuniq=3; mp_bcb75af88bccc92724ac5fd79271e1ff_mixpanel=%7B%22distinct_id%22%3A%20%22eafd4d8d-3325-4b39-bf49-10ace362a5c6%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; __utma=74197771.659865560.1401276300.1401276300.1401276300.1; __utmb=74197771.3.9.1401276327783; __utmc=74197771; __utmz=74197771.1401276300.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"
#cookies = "fileDownload=true; hackerrankx_mixpanel_token="+GetCookie("hackerrankx_mixpanel_token", headers['Set-Cookie'])+"; _cb_ls=1; mp_dcd74fdb7c65d92ce5d036daddac0a25_mixpanel=%7B%22distinct_id%22%3A%20%22572bf960-28f1-4a0f-aae2-62cd1cf261ed%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.co.in%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.co.in%22%7D; __hstc=186008246.849aff80f07129c169c81ccfbea10678.1400159989208.1400159989208.1400159989208.1; __hssrc=1; hsfirstvisit=https%3A%2F%2Fwww.hackerrank.com%2Fx%2Fcodepair|https%3A%2F%2Fwww.google.co.in%2F|1400159989202; hubspotutk=849aff80f07129c169c81ccfbea10678; olfsk=olfsk38728408236056566; _ok=3878-630-10-2684; wcsid=3VurXh4hXR8YxpY04621101pDJ0DDPa2; hblid=6n9rexu2szdCSt634621101pDJD0orOD; _okbk=cd5%3Davailable%2Ccd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1400159991438%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _oklv=1400160107376%2C3VurXh4hXR8YxpY04621101pDJ0DDPa2; hackerrank_mixpanel_token="+GetCookie("hackerrank_mixpanel_token", headers['Set-Cookie'])+"; mp_36cfc98842f47eba17d79df294c189f0_mixpanel=%7B%22distinct_id%22%3A%20%22146000be02e0-087f1cc-30710558-100200-146000be02f584%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; hz_amChecked=1; is_returning=1; _hackerrank_session="+GetCookie("_hackerrank_session", headers['Set-Cookie'])+"; hr_categories-master=algorithms%2Cwarmup; mp_bcb75af88bccc92724ac5fd79271e1ff_mixpanel=%7B%22distinct_id%22%3A%20%228704d070-735c-0130-7f6e-12313b0729f4%22%2C%22%24initial_referrer%22%3A%20%22http%3A%2F%2Fstackoverflow.com%2Fquestions%2F19236051%2Fpoints-in-a-plane-from-hackerrank%22%2C%22%24initial_referring_domain%22%3A%20%22stackoverflow.com%22%2C%22%24search_engine%22%3A%20%22google%22%7D; __utma=74197771.1088138763.1399386285.1401341324.1401348154.23; __utmb=74197771.6.10.1401348154; __utmc=74197771; __utmz=74197771.1400225171.5.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _chartbeat2=hVROWC2/DClBI64RZ.1399552299582.1401348157150.0010100000000111; _chartbeat_uuniq=3"
#print cookies
opener.addheaders.append(('Cookie', cookies))
#opener.addheaders.append(('Cookie', headers['Set-Cookie']))
opener.addheaders.append(('X-CSRF-Token', "SwGdNTwmMY27HULhPD+3WJZBfU9397vGorX+aZb8Rlg="))
response = opener.open(url, data)

#print response.read()
data = json.loads(response.read())
submission_id = data['model']['id']
#print data

url += str(submission_id)

#add headers
opener = urllib2.build_opener()
opener.addheaders.append(('Connection', "keep-alive"))
opener.addheaders.append(('Content-Type', "application/json"))
opener.addheaders.append(('Cookie', cookies))
opener.addheaders.append(('X-CSRF-Token', "SwGdNTwmMY27HULhPD+3WJZBfU9397vGorX+aZb8Rlg="))

#continous polling to the server until the code gets successfully executed
while True:
	response = opener.open(url)
	html = response.read()
	#print html
	data = json.loads(html)
	#print data['model']['status_string']
	#print data
	if data['model']['status'] == 1:
		break

#print the result
print data['model']['compilemessage']
if data['model']['stdout'] is not None:
    print "STDOUT :"
    for output in data['model']['stdout']:
	    print output
