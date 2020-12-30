def getCharts(icao):
    import requests
    from bs4 import BeautifulSoup
    url = 'https://www.airservicesaustralia.com/aip/current/dap/AeroProcChartsTOC.htm'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    r = requests.get(url,verify=False,headers=headers)
    lst = BeautifulSoup(r.content,'html.parser')
    hgs = lst.findAll('h3',{'style':'text-align:left'})
    for i in hgs:
        try:
            if icao in str(i):
                xx = str(i)
                break               
        except:
            pass
    j = ''
    c=0
    for i in str(lst).split('\n'):
        if xx in i:
            j=str(str(lst).split('\n')[c-1:])
        c+=1
    lst = BeautifulSoup(j,'html.parser')
    table = lst.findAll('table')[0]
    lst = BeautifulSoup(str(table),'html.parser')
    links = []
    for i in lst.findAll('a'):
        links.append('https://www.airservicesaustralia.com/aip/current/dap/'+i['href'])
    return {'links':links}

# NOTE : WHILE SCRIPTS USUALLY RETURN ONE LINK, THIS RETURNS A JSON WITH AN ARRAY OF LINKS
print(getCharts('YSSY'))