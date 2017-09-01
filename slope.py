#Gary Li
#9/1/17
#slope.py

x1 = float(input('Enter value for x1: '))
x2 = float(input('Enter value for x2: '))
y1 = float(input('Enter value for y1: '))
y2 = float(input('Enter value for y2: '))
slope = float(((y2-y1)/(x2-x1)))
print('The slope of the line is', slope)
yIntercept = float(((slope*(-1)*(x1))+y1))
print('The equation of the line is Y =' , slope, '+', yIntercept)