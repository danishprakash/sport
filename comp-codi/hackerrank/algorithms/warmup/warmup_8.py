stamp = input()
flag = stamp[len(stamp)-2:]
stamp = stamp[:-2]
stamp = stamp.split(':')

fif = int(stamp[0])                 #first element or hours

if fif == 12 and flag == 'AM':
    stamp[0] = '00'
elif fif == 12 and flag == 'PM':
    stamp[0] == '24'
elif fif < 12 and flag == 'PM':
    fif += 12
    stamp[0] = str(fif)

print(':'.join(stamp))
