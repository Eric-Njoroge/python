name  = input ("Please enter your name: ") 
print("Hello ",name,", welcome to your personal unit converter" ) 


print ("Please choose which conversion you would like to perform:")

#2print ("1 - convert cm to inches \n 2 - convert percent to letter grade \n 3- convert cups to ml \n 4- convert grams to ounces \n5- convert fahrenheit to celsius")
choice  = input("1- convert cm to inches \n2- convert percent to letter grade \n3- convert cups to ml \n4- convert grams to ounces \n5- convert fahrenheit to celsius \nChoice: ")

def SwitchExample():
    #choice = {
       # 1: {
 if (choice == "1") :
  value = float(input ("Value in cm to convert: "))
  inches = value / 2.54
  print (value, " cm = " ,inches, "inches")
  print("Goodbye", name) 

 elif choice == "2" :
  value = float(input ("Value in cup to convert: "))
  ml = value*237
  print (value, " cups = " ,ml, "ml")
  print("Goodbye", name) 

 elif choice == "3" :
  value = float(input ("Value in grams to convert: "))
  ounces = value / 28.35
  print (value, " grams = " ,ounces, "ounces")
  print("Goodbye", name) 

 elif choice == "4" :
  value = float(input ("Value in fahrenheit to convert: "))
  celsius = (value - 32) * 5/9
  print (value, " fahrenheit = " ,celsius, "celsius")
  print("Goodbye", name) 

 elif choice == "5" :
 
  value = float(input ("Value in percent to convert: "))
  if value>=80 and value <=100 :
      Grade = "A"
      print (value,"% = ",Grade)

  elif value >=70 and value <80 :
     Grade = "B"
     print (value,"% = ",Grade)

  elif value >= 60 and value <70:
    Grade = "C"
    print (value,"% = ",Grade)

  elif value >= 50 and value <60:
    Grade = "D"
    print (value,"% = ",Grade)

  elif value >= 20 and value <40:
     Grade = "E"
     print (value,"% = ",Grade)

  elif value >= 0 and value <20:
    Grade = "F"
    print (value,"% = ",Grade)

 print("Goodbye", name) 



if __name__ == "__main__":

    SwitchExample()



