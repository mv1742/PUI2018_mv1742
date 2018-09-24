from __future__ import print_function
import pylab as pl
import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

pl.rc('font', size=15)

#MTA_KEY = "d3ccd72f-edb3-433f-8935-1ec3de863290"

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='\
+sys.argv[1]+'&VehicleMonitoringDetailLevel=calls&LineRef='+sys.argv[2]

#url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTAAPIKEY + \
#"VehicleMonitoringDetailLevel=calls&LineRef=B52"
#print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

busx =data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
s="Latitude,Longitude,Stop Name,Stop Status\n"
for i in busx:    
    #print(type(i)) 
    i =i['MonitoredVehicleJourney']
    #print('Onward Calls', len(i['OnwardCalls']))
    printout = str(i['VehicleLocation']['Latitude'])+','+\
    str(i['VehicleLocation']['Longitude'])+','
    if len(i['OnwardCalls']) < 1:
        s = s +str(printout)
        s =s +'N/A \n'
        continue
    printout = printout +str(i['OnwardCalls']['OnwardCall'][0]['StopPointName'])+','\
    +str(i['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
    
    s = s +str(printout) +'\n'
print(s)
f = open(sys.argv[3],'w')
f.write(s) #Give your csv text here.
## Python will convert \n to os.linesep
f.close()