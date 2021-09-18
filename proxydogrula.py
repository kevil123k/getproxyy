import urllib.request
import socket
import urllib.error


f = open("proxyler.txt", "r")
def is_bad_proxy(pip):    
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('http://www.google.com')  # change the URL to test here
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        print("ERROR:", detail)
        return True
    return False

def main():
    def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
    satir = file_lengthy("proxyler.txt")
    a = 1
    while a<=299:
        proxyler = f.readlines(a)
        socket.setdefaulttimeout(60)
        
        # two sample proxy IPs
        proxyList = proxyler

        for currentProxy in proxyList:
            if is_bad_proxy(currentProxy):
                print("Bad Proxy %s" % (currentProxy))
            else:
                print("%s Working" % (currentProxy))
        a+=1
if __name__ == '__main__':
    main() 
