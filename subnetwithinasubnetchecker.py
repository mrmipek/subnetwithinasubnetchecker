import sys
from datetime import datetime
from netaddr import IPNetwork, IPAddress
'''
subnet1.csv and subnet2.csv should be sorted as integer ascending(you can use notepad++) 
this tool takes each subnet in subnet1 and checks if it is in the subnet2 list or subnet2 subnet is within the subnet1 list,
if it is not matching any of this check, it will be written to a file subnetnotmatch.txt 
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
##RESULT subnetnotmatch.txt
2023-03-18 22:34:12.348187
1.12.0.0/23
2023-03-18 22:34:12.427192
'''
print(str(datetime.now()))
data = open('subnet1.csv','r').read().splitlines()
data1 = open('subnet2.csv','r').read().splitlines()
ind=0
with open('subnetnotmatch.txt','w') as datawrite:
        datawrite.writelines(str(datetime.now())+"\n")
        for line in data:
                a=0
                for line1 in data1[ind::]:
                        if IPNetwork(line.split(',')[0]) in IPNetwork(line1.split(',')[0]) or IPNetwork(line1.split(',')[0]) in IPNetwork(line.split(',')[0]):
                                a=1
                                break
                if a==0:
                        datawrite.writelines(line.split(',')[0]+"\n")
                else:
                        if ind!=data1.index(line1):
                                print(ind,data1.index(line1))
                        ind=data1.index(line1)
        datawrite.writelines(str(datetime.now())+"\n")               


