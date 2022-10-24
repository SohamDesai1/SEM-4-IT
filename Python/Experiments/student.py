while True:
    print("1.Calculate average and total marks")
    print("2.Display students with specific key")
    print("3.Enter admission date")
    print("0.Exit")
    choice = int(input("Enter your choice: "))
    a = (78,45,58,69,90)
    if choice == 1:
      print("Students marks: ", a)
      print("Total marks: ", sum(a))
      print("Average marks: ", sum(a)/len(a))
    elif choice == 2:
        key = int(input("Enter the key: "))
        print("The student at given key is:", a[key])
    elif choice == 3:
        student_date = ((12,2,2022),(11,2,2022),(10,2,2022),(9,2,2022),(8,2,2022))
        studentsID = 100
        toCheck = False
        toGetYear = int(input("Enter year (2020 or 2021) to get student's having addmission in the year : "))
        if 2020 or 2021 in toGetYear:
            for addDate in a:
                if toGetYear in addDate:
                     print(f"Student {studentsID} ", end=" ")
            toCheck = True
            studentsID = studentsID + 1
            if toCheck :
                print("Having Admission In The Year",toGetYear)
        else:
            print("enter valid year!!!!(2020-2021)")
    elif choice == 0:
        exit()            