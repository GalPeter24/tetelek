print('Írj be egy számot [-5;5] intervallumban')
print('ha az intervallumon kívüli számot írsz be, a program véget ér!')
szam = int(input())
szamok = []
osszeg = 0

while szam >= -5 and szam <=5 : 
    osszeg = osszeg + szam
    szamok.append(szam)
    szam = int(input('Írj be egy számot [-5;5] intervallumban '))
print('Ezeket a számokat írtad be: ',szamok)
print('A beírt számok összege: ', osszeg)
