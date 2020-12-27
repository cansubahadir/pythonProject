studentlist=["Cansu Bahadir","Cemil Bahadir","Kemal Akyasan","Busranur Dogru","Sila Oral"]

i=0
while i<3:
    name = input("Please enter your name and surname:")
    if name in studentlist:
       print("Welcome")
       break

    elif name not in studentlist:
       i+=1

       if i==3:
           print("Please try again later")

CoursesList=["python","java","c++","machine learning","c#"]

Studentcourses=[]
print("Lütfen Listeden en az 3, en fazla 5 ders seçiniz")
print(CoursesList)
#tt
i=0
while i<=5 :
    choosencourses=input("please choose the course")
    if choosencourses in Studentcourses:
        print("bu ders secildi yeni ders seciniz")
        i-=1
    elif len(Studentcourses)>5:
        break

    else:
      Studentcourses.append(choosencourses)
      print(Studentcourses)

