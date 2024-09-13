import matplotlib.pyplot as plt
from math import sqrt

x = [3.872983346,
5.477225575,
6.708203932,
7.745966692,
8.660254038,
9.486832981,
10.24695077,
10.95445115,
12.24744871,
13.41640786,
16.88194302,
18.57417562
]
y = [0.00497834, 0.012714827, 0.018904018, 0.027259426, 0.033758077, 0.036543213, 0.046445919, 0.050468893, 0.060216869, 0.06671552, 0.091317555, 0.098744584]
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
    round = 3.5
    while round < (20):
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
    fig.text(0.9, 0.17, f'Kdiff = 0.0067 (mg g⁻¹ min⁻¹)', fontsize = 24, color ='black', ha ='right', va ='bottom', alpha = 1)
    fig.text(0.9, 0.13, f'R{chr(0x00B2)} = {coefficientOfDetermination(list, listTwo):.3f}',
        fontsize = 24, color ='black',
        ha ='right', va ='center',
        alpha = 1)
    plt.title(f'Cinética de Difusión Intrapartícula: Al₂O₃-CeO₂-Ag', fontsize = 20)
    plt.ylabel('qt', fontsize = 24)
    plt.xlabel(f'√t', fontsize = 24)
    plt.xlim((2.6), (max(x) + 2))
    plt.ylim(-0.001, (max(y)) + 0.011)
    print(f'y = ({m:.8f} ± {sm:.2f})x + ({b:.2f} ± {sb:.2f})')
    plt.show()
main()