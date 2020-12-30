def getCharts(icao):
    import requests
    from bs4 import BeautifulSoup
    url = 'https://aip.caam.gov.my/aip/eAIP/history-en-MS.html'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    r = requests.get(url,verify=False,headers=headers)
    lst = BeautifulSoup(r.content,'html.parser')
    tables = lst.findAll('table',{'class':'transparent'})
    found = 0
    for i in tables:
    	if found==0:
	    	for x in i.findAll('h2'):
	    		if found==0:
		    		if 'Currently Effective' in str(x):
		    			finalurl = i.find('a')['href']
		    			found = 1

    themainurl = 'https://aip.caam.gov.my/aip/eAIP/' + finalurl
    url = themainurl
    themainurl = themainurl.replace('/index-en-MS.html','').replace(finalurl,'')
    
    r = requests.get(url,verify=False,headers=headers)
    lst = BeautifulSoup(r.content,'html.parser')
    lnk = lst.find('frame',{'name':'eAISNavigationBase'})['src']
    lnk = themainurl + '/'+lnk
    r = requests.get(lnk,verify=False,headers=headers)
    lst = BeautifulSoup(r.content,'html.parser')
    lnk = lst.find('frame',{'name':'eAISNavigation'})['src']
    lnk = themainurl + '/'+lnk
    r = requests.get(lnk,verify=False,headers=headers)
    lst = BeautifulSoup(r.content,'html.parser')
    ass = lst.findAll('a')
    for i in ass:
    	try:
    		if icao in i['href']:
    			return ((themainurl+'/eAIP/'+i['href'].replace('../eAIP/','')).replace(' ','%20'))
    	except:
    		pass
    return 'Not Found'

print(getCharts('WMKK'))