import requests
url = 'https://eservicesredp.rega.gov.sa/api/Query/v1/Broker'
myobj = {"licenseType":"","brokerType":"","licenseNumber":"","brokerName":"","brokerId":"","regionId":"9e7cb8e3-f28d-0fa8-3388-f4273702054b","cityId":"202ea443-2031-9ce7-c413-078e4ad890aa","districtId":"","maxResult":10,"skipCount":1}
x = requests.post(url, json=myobj) 
data = x.json()
print (data)