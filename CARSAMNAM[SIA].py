def getCharts(icao):
    import requests
    from bs4 import BeautifulSoup
    url = 'https://www.sia.aviation-civile.gouv.fr/dvd/eAIP_31_DEC_2020/CAR-SAM-NAM/AIRAC-2020-12-03/html/index-fr-FR.html'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    r = requests.get(url,verify=False,headers=headers)
    lst = BeautifulSoup(r.content,'html.parser')
    lnk = lst.find('frame',{'name':'eAISNavigationBase'})['src']
    lnk = 'https://www.sia.aviation-civile.gouv.fr/dvd/eAIP_31_DEC_2020/CAR-SAM-NAM/AIRAC-2020-12-03/html/'+lnk
    r = requests.get(lnk,verify=False,headers=headers)
    lst = BeautifulSoup(r.content,'html.parser')
    lnk = lst.find('frame',{'name':'eAISNavigation'})['src']
    lnk = 'https://www.sia.aviation-civile.gouv.fr/dvd/eAIP_31_DEC_2020/CAR-SAM-NAM/AIRAC-2020-12-03/html/'+lnk
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
            return (('https://www.sia.aviation-civile.gouv.fr/dvd/eAIP_31_DEC_2020/CAR-SAM-NAM/AIRAC-2020-12-03/html/eAIP/' + str(i).split('?')[0].replace('eAIP/../','').replace('../','')))
    return 'Not Found'


print(getCharts('TFFB'))
