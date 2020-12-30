def getCharts(icao):
    import requests
    from bs4 import BeautifulSoup
    url = 'https://aim-india.aai.aero/eaip-v2-02-2020/index-en-GB.html'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    r = requests.get(url,verify=False,headers=headers)
    lst = BeautifulSoup(r.content,'html.parser')
    lnk = lst.find('frame',{'name':'eAISNavigationBase'})['src']
    lnk = 'https://aim-india.aai.aero/eaip-v2-02-2020/'+lnk
    r = requests.get(lnk,verify=False,headers=headers)
    lst = BeautifulSoup(r.content,'html.parser')
    lnk = lst.find('frame',{'name':'eAISNavigation'})['src']
    lnk = 'https://aim-india.aai.aero/eaip-v2-02-2020/'+lnk
    r = requests.get(lnk,verify=False,headers=headers)
    lst = BeautifulSoup(r.content,'html.parser')
    ass = lst.find('a',{'title':icao})
    try:
        return (('https://aim-india.aai.aero/eaip-v2-02-2020/eAIP/'+ass['href']).replace(' ','%20'))
    except:
        return 'Not Found'