import requests
from openpyxl import load_workbook

counter = 1
for counter in range (counter,21):
    
    url = 'https://eservicesredp.rega.gov.sa/api/Query/v1/Broker'
    myobj = {"licenseType":"","brokerType":"","licenseNumber":"","brokerName":"","brokerId":"","regionId":"9e7cb8e3-f28d-0fa8-3388-f4273702054b","cityId":"202ea443-2031-9ce7-c413-078e4ad890aa","districtId":"","maxResult":10,"skipCount":counter}

    x = requests.post(url, json=myobj) 

    data = x.json()
    forc = data["result"]["items"]

    # Load the existing workbook
    workbook = load_workbook('brokers.xlsx')

    # Select the active worksheet
    worksheet = workbook.active

    # Write the data to the worksheet
    for item in forc:
        id = item["id"]
        response = requests.get(f"https://eservicesredp.rega.gov.sa/api/Query/v1/BrokerDetails/{id}")
        data = response.json()
        name_ = data["result"]["brokerName"]
        type_ = data["result"]["brokerType"]
        mobile_ = data["result"]["mobileNumber"]
        email_ = data["result"]["emailAddress"]
        cnn_ = data["result"]["crNationalNumber"]
        region_ = data["result"]["location"]["region"]
        city_ = data["result"]["location"]["city"]
        citycode_ = data["result"]["location"]["cityCode"]
        district_ = data["result"]["location"]["district"]
        districtcode_ = data["result"]["location"]["districtCode"]
        street_ = data["result"]["location"]["street"]
        postalCode_ = data["result"]["location"]["postalCode"]
        buildingNumber_ = data["result"]["location"]["buildingNumber"]
        additionalNumber_ = data["result"]["location"]["additionalNumber"]

        # Write a row of data to the worksheet
        worksheet.append([name_, type_, mobile_, email_, cnn_, region_, city_, citycode_, district_, districtcode_,street_,postalCode_, buildingNumber_, additionalNumber_])

    # Save the changes to the workbook
    workbook.save('brokers.xlsx')
    print (f"{counter} is done")
    counter+=1