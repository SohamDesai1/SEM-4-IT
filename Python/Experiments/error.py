while True:
   print("1.ZeroDivisionError\n 2.NameError\n 3.SyntaxError\n 4.IndexError\n5.KeyError\n6.TypeError\n 7.ImportError\n 0.Exit")
   a = int(input("Enter your choice: "))
   if a == 1:
      try:
       print(1/0)
      except ZeroDivisionError as e:
          print("ZeroDivisionError:", e)
   elif a == 2:
      try:
         print(b.name)
      except NameError as e:
         print("NameError")
   elif a == 3:
      try:
         print(1+"1")
      except SyntaxError as e:
         print("SyntaxError :",e)
   elif a == 4:
      try:
         print(a[10])
      except IndexError as e:
         print("IndexError :",e)
   elif a == 5:
      try:
         print(a["name"])
      except KeyError as e:
         print("KeyError :",e)
   elif a == 6:
      try:
         print(int("a"))
      except TypeError as e:
         print("TypeError :",e)