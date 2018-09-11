# http://www.geeksforgeeks.org/find-itinerary-from-a-given-list-of-tickets/

''' Input:
"Chennai" -> "Banglore"
"Bombay" -> "Delhi"
"Goa"    -> "Chennai"
"Delhi"  -> "Goa"

Output: 
Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore, '''

d = dict()
n = int(input())
for i in range(n):
    a, b = input().split()
    d[a] = b
for key in d.keys():
    if key not in d.values():
        source = key
        break
for i in range(len(d)):
    print(source + ' -> ' + d[source] + ', ', end='')
    source = d[source]
