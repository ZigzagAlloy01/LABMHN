import matplotlib.pyplot as plt
from math import sqrt

x = [0.5565277684,
0.9788038161,
1.413470643,
1.541016767,
1.569955075,
1.787715821,
1.886577837]
y = [0.02011698037,
0.0350692932,
0.05716330704,
0.05528820261,
0.04997023871,
0.07088132997,
0.06346326345]

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
    round = 0.52
    while round < (2):
        yvalue = (m * (round)) + (b)
        equationy.append(yvalue)
        axisX.append(round)
        round = round + 0.05
    return equationy

def drawGraph(list, listTwo, m, b, sm, sb):
    calculusCurve(0.005, m, b, listTwo)
    fig = plt.figure(figsize = (12, 7))
    plt.scatter(list, listTwo, alpha = 1, color='black', s=40)
    plt.plot(axisX, equationy, color='black')
    fig.text(0.9, 0.24, f'b  = 69,790.76 (J mol⁻¹) ', fontsize = 24, color ='black', ha ='right', va ='bottom', alpha = 1)
    fig.text(0.9, 0.17, f'K  = 1.03 (L g⁻¹)',
        fontsize = 24, color ='black',
        ha ='right', va ='bottom',
        alpha = 1)
    fig.text(0.9, 0.13, f'R{chr(0x00B2)} = {coefficientOfDetermination(list, listTwo):.3f}',
        fontsize = 24, color ='black',
        ha ='right', va ='center',
        alpha = 1)
    #plt.grid(alpha =.6, linestyle ='--')
    plt.title(f'Isoterma de Temkin: Al₂O₃-CeO₂', fontsize = 20)
    plt.ylabel('q', fontsize = 24)
    plt.xlabel(f'ln(Ce)', fontsize = 24)
    plt.xlim((0.45), (max(x) + 0.13))
    plt.ylim(0.014, (max(y) + 0.005))
    print(f'y = ({m:.4f} ± {sm:.4f})x + ({b:.4f} ± {sb:.4f})')
    plt.show()
main()