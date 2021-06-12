#!/usr/bin/env python
#http://localhost:8080/JSON/spider/view/fullResults/?apikey=m2a58n594fjhsaliofsmjtas77&scanId=0
#http://localhost:8080/JSON/spider/view/scans/?apikey=m2a58n594fjhsaliofsmjtas77
import time
from zapv2 import ZAPv2
import requests

# The URL of the application to be tested
target = 'https://google-gruyere.appspot.com/559857475944133831323694044374422400395/'
# Change to match the API key set in ZAP, or use None if the API key is disabled
apiKey = 'm2a58n594fjhsaliofsmjtas77'

# By default ZAP API client will connect to port 8080
zap = ZAPv2(apikey=apiKey)
# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
# zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

print('Ajax Spider target {}'.format(target))
scanID = zap.ajaxSpider.scan(target)

timeout = time.time() + 60*2   # 2 minutes from now
# Loop until the ajax spider has finished or the timeout has exceeded
while zap.ajaxSpider.status == 'running':
    if time.time() > timeout:
        break
    print('Ajax Spider status' + zap.ajaxSpider.status)
    time.sleep(2)

print('Ajax Spider completed')
ajaxResults = zap.ajaxSpider.results(start=0, count=10)
print(ajaxResults)
# If required perform additional operations with the Ajax Spider results

# TODO: Start scanning the application to find vulnerabilities


headers = {
  'Accept': 'application/json',
  'X-ZAP-API-Key': apiKey
}

r = requests.get('http://zap/JSON/spider/view/results/', params={

}, headers = headers)

print(r.json())


