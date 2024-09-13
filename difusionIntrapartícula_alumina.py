import matplotlib.pyplot as plt
from math import sqrt

x = [
4.472135955,
6.32455532,
7.745966692,
8.94427191,
10.95445115,
11.83215957,
12.64911064,
13.41640786,
14.14213562,
14.83239697,
15.49193338
]
y = [
0.007451470844,
0.007451470844,
0.009330934258,
0.01046359102,
0.01044699531,
0.01194060862,
0.01120209982,
0.01381177419,
0.01381177419,
0.01271230883,
0.01380347634
]
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
    round = 4
    while round < (17):
        yvalue = (m * (round)) + (b)
        equationy.append(yvalue)
        axisX.append(round)
        round = round + 0.5
    return equationy

def drawGraph(list, listTwo, m, b, sm, sb):
    calculusCurve(0.005, m, b, listTwo)
    fig = plt.figure(figsize = (12, 7))
    plt.scatter(list, listTwo, alpha = 1, color='black', s=40)
    plt.plot(axisX, equationy, color='black')
    fig.text(0.9, 0.17, f'Kdiff = 0.000617 (mg g⁻¹ min⁻¹)', fontsize = 24, color ='black', ha ='right', va ='bottom', alpha = 1)
    fig.text(0.9, 0.13, f'R{chr(0x00B2)} = {coefficientOfDetermination(list, listTwo):.4f}',
        fontsize = 24, color ='black',
        ha ='right', va ='center',
        alpha = 1)
    #plt.grid(alpha =.6, linestyle ='--')
    plt.title(f'Cinética de Difusión Intrapartícula: Al₂O₃', fontsize = 20)
    plt.ylabel('qt', fontsize = 24)
    plt.xlabel(f'√t', fontsize = 24)
    plt.xlim((3.2), (max(x) + 1.8))
    plt.ylim(0.005, (max(y)) + 0.002)
    print(f'y = ({m:.9f} ± {sm:.9f})x + ({b:.9f} ± {sb:.9f})')
    plt.show()
main()