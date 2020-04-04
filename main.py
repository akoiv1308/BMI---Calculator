name = input("What is your name?")
pounds = int(input("What is your weight?"))
height = float(input ("How tall are you(in inches)?"))

BMI = round(pounds * 703/(height * height))

print ("Your BMI is: " + str(BMI))
if BMI < 18:
  print ("You are an underweight person")
if BMI >= 18 and BMI < 25:
  print ("You are a normal weight")
if BMI >= 25 and BMI < 30:
  print ("You are an overweight person")
if BMI > 30:
  print ("You have an obesity")