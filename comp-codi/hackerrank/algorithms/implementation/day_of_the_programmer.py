year = int(input())
f8 = 0

if year < 1918:
    if year%4 == 0:
        f8 = 244
    else:
        f8 = 243
elif year > 1918:
    if year%400 == 0 or (year%4 == 0 and year%100 != 0):
        f8 = 244
    else:
        f8 = 243
elif year == 1918:
    f8 = 230
print('{:02d}.{:02d}.{:04d}'.format((256-f8),8,(year)))
