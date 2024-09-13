import matplotlib.pyplot as plt
from math import sqrt

x = [15,
30,
45,
60,
75,
120,
135,
165]
y = [-8.26554328,
-8.42111652,
-8.298319279,
-8.416997889,
-8.332646966,
-8.586314262,
-8.383868666,
-8.563332584]
xyValues = []
xSquareValues = []
dSquareValues = []
equationy = []
axisX = []

def main():
    n = len(y) 
    MX = sum(x)
    MY  = sum(y)
    MXY  = calculusXY(0)
    MXSquare = calculusXSquare(0)
    determinant = ((n) * (MXSquare)) - ((MX * MX))
    m = ((MXY * n) - (MX * MY)) / determinant
    b = ((MXSquare * MY) - (MXY * MX)) / determinant
    MDSquare = calculusDSquare(0, m, b)
    sY = sqrt(MDSquare/(n-2))
    s2m = ((sY**2) * n) / determinant
    s2b = ((sY**2) * MXSquare) / determinant
    sm = sqrt(s2m)
    sb = sqrt(s2b)
    return drawGraph(x, y, m, b, sm, sb)

def calculusXY(round):
    while round < (len(x)):
        xy = (x[round]) * (y[round])
        xyValues.append(xy)
        round = round + 1
    xySumatory = sum(xyValues)
    return xySumatory

def calculusXSquare(round):
    while round < (len(x)):
        xSquare = (x[round])**2
        xSquareValues.append(xSquare)
        round = round + 1
    xSquareSumatory = sum(xSquareValues)
    return xSquareSumatory

def calculusDSquare(round, m, b):
    while round < (len(x)):
        dValue = (y[round]) - (m * (x[round])) - b
        dSquare = dValue ** 2
        dSquareValues.append(dSquare)
        round = round + 1
    dSquareSumatory = sum(dSquareValues)
    return dSquareSumatory

def coefficientOfDetermination(x, y):
    averagex = (sum(x))/(len(x))
    averagey = (sum(y))/(len(y))
    cycle = 0
    sustractionsx = []
    sustractionsy = []
    while cycle < len(y):
        sustractionx = ((x[cycle]) - (averagex))**2
        sustractiony = ((y[cycle]) - (averagey))**2
        sustractionsx.append(sustractionx)
        sustractionsy.append(sustractiony)
        cycle = cycle + 1
    product = sum((i - averagex) * (j - averagey) for i, j in zip(x, y))
    r = (product)/(((sum(sustractionsx))*(sum(sustractionsy)))**0.5)
    print(product)
    print(sum(sustractionsx))
    print(sum(sustractionsy))
    r2 = r**2
    return r2

def calculusCurve(round, m, b, y):
    round = 10
    while round < (180):
        yvalue = (m * (round)) + (b)
        equationy.append(yvalue)
        axisX.append(round)
        round = round + 10
    return equationy

def drawGraph(list, listTwo, m, b, sm, sb):
    calculusCurve(0.005, m, b, listTwo)
    fig = plt.figure(figsize = (12, 7))
    plt.plot(axisX, equationy, alpha = 1, color='black')
    plt.scatter(list, listTwo, alpha = 1, color='black', s=40)
    #fig.text(0.9, 0.17, f'y = ({m:.6f} ± {sm:.6f})x + ({b:.6f} ± {sb:.6f})', fontsize = 18, color ='black', ha ='right', va ='bottom', alpha = 1)
    fig.text(0.9, 0.24, f'qe = 0.00025 (mg g⁻¹)', fontsize = 24, color ='black', ha ='right', va ='bottom', alpha = 1)
    fig.text(0.9, 0.17, f'K₁ = 0.00157 (min⁻¹)', fontsize = 24, color ='black', ha ='right', va ='bottom', alpha = 1)
    fig.text(0.9, 0.13, f'R{chr(0x00B2)} = {coefficientOfDetermination(list, listTwo):.4f}',
        fontsize = 24, color ='black',
        ha ='right', va ='center',
        alpha = 1)
    #plt.grid(alpha =.6, linestyle ='--')
    plt.title(f'Cinética de Pseudo Primer Orden: Al₂O₃-CeO₂', fontsize = 24)
    plt.ylabel('ln(qe-qt)', fontsize = 24)
    plt.xlabel(f't (min)', fontsize = 24)
    plt.xlim((0), (max(x) + 17))
    plt.ylim(-9, (max(y)) + 0.2)
    print(f'y = ({m:.6f} ± {sm:.6f})x + ({b:.6f} ± {sb:.6f})')
    plt.show()
main()