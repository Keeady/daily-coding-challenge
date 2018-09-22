1) You are given a huge log file which holds the entry and exit time of each person 
entering and exiting the office on a given day 

format of file: 
entry time exit time 
09:12:23 11:14:35 
10:34:01 13:23:40 
10:34:31 11:20:10 
...
upto N entries for a given day 
Design a function which returns the total number of persons in the office at any given time. e.g input to function is 11:05:20. 

Assuming day starts at 0 and an interval of 1 second is what interests us. Construct an array of 86400 entries
in which each cell contains the number of people currently in the building for that second. 

Parsing the log file, each new entry time increment an entry in the array and each exit decrement.

 Given a specific time, to find the number of people in the building, calculate the number of seconds
 between 0 and the given time and used that as the index
 
 00:30 :1:30
 1800: 1
 5400: 0
 
2) Re-order log entries using natural order by re-arranging the log keys
log format: [key] [log text]
all logs having numbers in key should appear first

z2 ksdnslkdfs slkfmsdfmsl
z11 dsklfnsdlfsflsmfsfms;flms


3) You have a log file. Find the k most frequent entries in  the log file.
