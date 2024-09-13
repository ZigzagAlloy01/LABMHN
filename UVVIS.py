import matplotlib.pyplot as plt

ultraviolet = open("AgNps.txt").readlines()
x = []
y = []
for line in ultraviolet:
    newLine = line.split("	")
    abcisa = newLine[0]
    ordenada = newLine[1]
    x.append(float(abcisa))
    y.append(float(ordenada))
fig = plt.figure(figsize = (12, 7))
plt.plot(x, y, alpha = 0.7, color="black")
plt.xlim((min(x)),(max(x))+100)
plt.ylim(min(y), (max(y) + 0.1))
plt.title(f'Espectro UV-VIS Ag Nps', fontsize = 24)
plt.ylabel('Absorbancia', fontsize = 24)
plt.xlabel(f'λ (nm)', fontsize = 24)
plt.show()