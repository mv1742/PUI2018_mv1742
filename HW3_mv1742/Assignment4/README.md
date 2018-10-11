# Assignment 4: next stop information

Python script that displays information on the next stop location of all busses of a given line. For example, whether the bus is approaching a stop, or is 1 stop
away from it. All the information is already included in the response JSON: your code needs to pull the current JSON file from the MTA API (as before) and parse it to find it. 
Have this script *output the data to a CSV file*. 
For buses that do not have this information,
output is “N/A” in the stop information fields. 

__Single Python file, named get_bus_info_mv1742.py that takes 3 arguments in the following format:__

```
python get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx <BUS_LINE> <BUS_LINE>.csv
```
__and output to a CSV file named \<BUS_LINE>.csv__:

```
Latitude,Longitude,Stop Name,Stop Status
40.755489,-73.987347,7 AV/W 41 ST,at stop
40.775657,-73.982036,BROADWAY/W 69 ST,approaching
40.808332,-73.944979,MALCOLM X BL/W 127 ST,approaching
40.764998,-73.980416,N/A,N/A
40.804702,-73.947620,MALCOLM X BL/W 122 ST,< 1 stop away
40.776950,-73.981983,AMSTERDAM AV/W 72 ST,< 1 stop away
40.737650,-73.996626,AV OF THE AMERICAS/W 18 ST,< 1 stop away
```
