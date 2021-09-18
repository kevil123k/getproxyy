from lxml import html
import requests

page = requests.get("https://free-proxy-list.net/")
tree = html.fromstring(page.content)
a = 1
f=open("proxyler.txt","a")
while a<101:
    ip = tree.xpath('//*[@id="proxylisttable"]/tbody/tr['+str(a)+']/td[1]/text()')
    proxy = tree.xpath('//*[@id="proxylisttable"]/tbody/tr['+str(a)+']/td[2]/text()')
    print(ip[0]+":"+proxy[0])
    f.write(ip[0]+":"+proxy[0]+"\n")
    
    a+=1
f.close()
