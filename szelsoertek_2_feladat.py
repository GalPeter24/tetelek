szavak= []
szo = input('Írj be szavakat! Ha ENTER-t ütsz vége. ')
legrovidebb = szo
leghosszabb = szo

while szo != "" :
    szavak.append(szo)
    if len(szo) < len(legrovidebb) :
        legrovidebb = szo
    elif len(szo) > len(leghosszabb) :
        leghosszabb = szo
    szo = input('Írj be szavakat! Ha ENTER-t ütsz vége.')
print('Beírt szavak: ',szavak)
print('leghoszabb beírt szó: ',leghosszabb)
print('legrövidebb beírt szó: ',legrovidebb)