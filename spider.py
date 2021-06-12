#!/usr/bin/env python
import time
from zapv2 import ZAPv2
import requests
import json
# The URL of the application to be tested
target = 'https://public-firing-range.appspot.com'
# Change to match the API key set in ZAP, or use None if the API key is disabled
apiKey = 'm2a58n594fjhsaliofsmjtas77'

# By default ZAP API client will connect to port 8080
zap = ZAPv2(apikey=apiKey)
# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
# zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

print('Spidering target {}'.format(target))
# The scan returns a scan id to support concurrent scanning
scanID = zap.spider.scan(target)

while int(zap.spider.status(scanID)) < 100:
    # Poll the status until it completes
    print('Spider progress %: {}'.format(zap.spider.status(scanID)))
    time.sleep(1)

payload = {'apikey': apiKey, 'scanId': scanID}
req = requests.get('http://localhost:8080/JSON/spider/view/fullResults/', params=payload)
response = json.loads(req.text)
#print('Spider has completed!')
# Prints the URLs the spider has crawled
#print('\n'.join(map(str, zap.spider.results(scanID))))
# If required post process the spider results
#http://localhost:8080/JSON/spider/view/fullResults/
print("Scan Id", scanID)
print("Results", response)

#{
#    "url":"https://public-firing-range.appspot.com"
#}
# TODO: Explore the Application more with Ajax Spider or Start scanning the application for vulnerabilities