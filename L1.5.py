firm=input ("Здравствуйте, введите название фирмы: ")
print ("программа для расчета  выручки и издержек фирмы: " , firm ,)
money = float( input ("Введите выручку: "))
izd = float( input ("Введите издержки: "))
eql = money - izd
if  eql > 0:
    print ("прибыль: ",  (round(eql, 2)), "поздравляем!")
    if eql < 0:
     print ("убыток: ", (round(eql, 2)), "надо постараться:)")