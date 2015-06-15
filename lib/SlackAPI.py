from urllib import urlencode 
from urllib2 import urlopen
 
class SlackAPI():
    def __init__(self):
        self.rtm = rtm()
        
class API():
    def __init__(self):
        pass
        
    def request(self, token, request="?", postData={}, domain="slack.com"):
        postData["token"] = token
        postData = urlencode(postData)

        url = 'https://{}/api/{}'.format(domain, request)

        return urlopen(url, postData.encode('utf-8')) 

class rtm(API):
    def __init__(self):
        pass

    def start(self, token):
        return self.request(token, "rtm.start")
