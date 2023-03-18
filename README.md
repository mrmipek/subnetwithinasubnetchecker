# subnetwithinasubnetchecker
this tool takes each subnet in subnet1 and checks if it is in the subnet2 list or subnet2 subnet is within the subnet1 list, if it is not matching any of this check, it will be written to a file 
subnet1.csv and subnet2.csv should be sorted as integer ascending(you can use notepad++) 
subnet1.csv 
1.2.0.0/24,1234,12
1.12.0.0/23,3456,34
1.34.44.0/24,566,45
2.12.45.0/25,345,8
subnet2.csv
1.1.0.0/23,8769,1
1.2.0.0/25,555,54
1.34.44.0/23,234,52
2.12.45.0/25,490,27
as seen below within the start and end date 1.12.0.0/23 is not within any subnet and no subnet on subnet2.csv is within 1.12.0.0/23.
1.2.0.0/24<-1.2.0.0/25   
1.34.44.0/24->1.34.44.0/23
2.12.45.0/25->2.12.45.0/25
##RESULT 
subnetnotmatch.txt
2023-03-18 22:34:12.348187
1.12.0.0/23
2023-03-18 22:34:12.427192
