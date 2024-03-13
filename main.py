stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

mantissa = stdform[:stdform.find("x")]
exponent = stdform[stdform.find("^") + 1::]
E_not = mantissa + "E" + exponent

if " " in E_not or stdform.count(".")>1 or stdform.count("x")>1 or stdform.count("^")>1 or not exponent.replace("-","").isdigit() or ((mantissa.replace(".","")).replace("-","")).isdigit()==False:
  print("Error converting to scientific E notation.")

else:
   print(f"This number in E notation is {E_not}.")