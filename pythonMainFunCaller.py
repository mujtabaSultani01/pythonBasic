# Here we can access the func but not the output which is calculated over there..
import pythonMainFun
print("I'm caller file!")
area = pythonMainFun.calculate_area(5,6)
print("The area calculated from caller file is: ", area)