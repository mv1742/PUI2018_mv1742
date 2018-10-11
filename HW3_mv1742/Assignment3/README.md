# Assignment 3:  tracking each vehicle for a line

Python script to retrieve and report information about active
vehicle for a bus line. 

__Single Python file, named show_bus_locations_mv1742.py that takes exactly 2 arguments in the following format:__
```
python show_bus_locations.py <MTA_KEY> <BUS_LINE>
```

For example \<BUS_LINE> could be B52:

```
python show_bus_locations.py xxxxx-xxxxx-xxxxx-xxxxx-xxxxx B52
```
The above command fetches data from the MTA website through the SIRI API using the
provided key and return information on all available vehicles for the bus line \<BUS_LINE> (e.g. B52). 

__Program outputs the following to the console:__ 
- the bus name, 
- the number of vehicles
- their current position

###SAMPLE OUTPUT:
```
Bus Line : B52
Number of Active Buses : 5
Bus 0 is at latitude 40.687241 and longitude -73.941661
Bus 1 is at latitude 40.690822 and longitude -73.920759
Bus 2 is at latitude 40.688363 and longitude -73.979563
Bus 3 is at latitude 40.688282 and longitude -73.979356
Bus 4 is at latitude 40.686839 and longitude -73.964694
```
