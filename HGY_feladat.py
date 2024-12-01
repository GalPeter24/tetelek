date_list = [ '1983-06-15', '1991-12-07', '1987-03-24', '2001-08-19', '2015-04-03', '1980-11-21', '1999-02-28', '2008-09-12', '1995-01-05', '2020-07-09', '1986-10-30', '1993-05-14', '2011-06-26', '1989-12-18', '2005-03-11', '2018-09-01', '1997-07-20', '2012-11-03', '2023-01-22', '1990-04-09' ]
szeptember = []
darab = 0
legutolso = str (1980-11-21)
for date in date_list:
    if date[0] < '2':
       darab = darab + 1
    if date[6:7] == '9' :
        szeptember.append(date)
    if date[:4] > legutolso :
        legutolso = date
        
print( "A szeptember hónapra eső dátumok:", szeptember)
print(darab, ' dátum volt az 2000 előtt')
print( legutolso,'volt a legutolsó év a dátumok között')
