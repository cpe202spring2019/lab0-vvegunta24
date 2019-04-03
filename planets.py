def weight_on_planets():
   # write your code here
   weight = float(input("What do you weigh on earth? "))
   mars = 0.38*weight
   jupiter = 2.34*weight
   print("\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(mars,jupiter))
   
   
   
if __name__ == '__main__':
   weight_on_planets()