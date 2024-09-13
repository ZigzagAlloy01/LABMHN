import matplotlib.pyplot as plt
from math import sqrt

x = [248799.3491,
69833.44367,
37060.0139,
22663.98621,
15603.08712]
y = [-2.993712692,
-2.147928428,
-1.658765423,
-1.50902301,
-1.629626308]
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

def calculusCurve(m, b):
    round = 9000
    while round < (258000):
        yvalue = (m * (round)) + (b)
        equationy.append(yvalue)
        axisX.append(round)
        round = round + 1000
    return equationy

def drawGraph(list, listTwo, m, b, sm, sb):
    calculusCurve(m, b)
    fig = plt.figure(figsize = (12, 7))
    plt.scatter(list, listTwo, alpha = 1, color='black', s=40)
    plt.plot(axisX, equationy, color='black')
    fig.text(0.45, 0.17, f'E = 285.13 (kJ mol⁻¹)',
        fontsize = 24, color ='black',
        ha ='right', va ='bottom',
        alpha = 1)
    fig.text(0.45, 0.13, f'R{chr(0x00B2)} = {coefficientOfDetermination(list, listTwo):.2f}',
        fontsize = 24, color ='black',
        ha ='right', va ='center',
        alpha = 1)
    #plt.grid(alpha =.6, linestyle ='--')
    plt.title(f'Isoterma de Dubinin-Radushkevich: Al₂O₃-CeO₂', fontsize = 20)
    plt.ylabel('ln(q)', fontsize = 24)
    plt.xlabel(f'ε{chr(0x00B2)}', fontsize = 24)
    plt.xlim((0), (max(x) + 15000))
    plt.ylim(-3.5, (max(y) + 0.12))
    print(f'y = ({m} ± {sm})x + ({b:.2f} ± {sb:.2f})')
    plt.show()
main()