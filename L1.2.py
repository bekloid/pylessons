min = int(input())
if min // 60 == 0:
  print('00 часов', min, 'минут')
 if min % 60 > 0:
   print(min % 60, "часов", min / 60, "минут")