#Gary Li
#9/8/17
#isItATriangle.py

sideA = float(input('Enter side A: '))
sideB = float(input('Enter side B: '))
sideC = float(input('Enter side C: '))

smallSide = min(sideA, sideB, sideC)
bigSide = max(sideA, sideB, sideC)
middleSide = (sideA+sideB+sideC)-smallSide-bigSide
print(smallSide + middleSide > bigSide)