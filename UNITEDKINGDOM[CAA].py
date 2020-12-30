def getCharts(icao):
    import requests
    from bs4 import BeautifulSoup
    url = 'https://www.aurora.nats.co.uk/htmlAIP/Publications/2020-12-31-AIRAC/html/index-en-GB.html'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    r = requests.get(url,verify=False,headers=headers)
    lst = BeautifulSoup(r.content,'html.parser')
    lnk = lst.find('frame',{'name':'eAISNavigationBase'})['src']
    lnk = 'https://www.aurora.nats.co.uk/htmlAIP/Publications/2020-12-31-AIRAC/html/'+lnk
    r = requests.get(lnk,verify=False,headers=headers)
    lst = BeautifulSoup(r.content,'html.parser')
    lnk = lst.find('frame',{'name':'eAISNavigation'})['src']
    lnk = 'https://www.aurora.nats.co.uk/htmlAIP/Publications/2020-12-31-AIRAC/html/'+lnk
    r = requests.get(lnk,verify=False,headers=headers)
    lst = BeautifulSoup(r.content,'html.parser')
    ass = lst.findAll('a')
    possibilities = []
    for i in ass:
        try:
            if (icao in i['href']) and (icao in i['id']) and (icao in str(i)):
                possibilities.append(str(i['href']).split('?')[0].replace('eAIP/../','').replace('../',''))                
        except:
            pass
    for i in possibilities:
        if (icao in i) and ('.html' in i):
            return (('https://www.aurora.nats.co.uk/htmlAIP/Publications/2020-12-31-AIRAC/html/' + str(i).split('?')[0].replace('eAIP/../','').replace('../','')))
    return 'Not Found'
print(getCharts('EGLL'))