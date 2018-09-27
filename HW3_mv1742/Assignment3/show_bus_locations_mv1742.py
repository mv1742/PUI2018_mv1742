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
busx=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
busx

#import pprint //##see structure of the tuple
print("Bus Line : "+sys.argv[2])
buscounter = 0 
for j in busx:
    buscounter+=1
print("Number of Active Buses : "+str(buscounter))

counter = 0 
for i in busx:
    print('Bus', str(counter), 'is at latitude:',i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],\
          'Longitude',i['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    counter+=1