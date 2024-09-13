import matplotlib.pyplot as plt

infrared = open("PS.txt").readlines()
x = []
y = []
for line in infrared:
    newLine = line.split("	")
    abcisa = newLine[0]
    ordenada = newLine[1]
    x.append(float(abcisa))
    y.append(float(ordenada))
fig = plt.figure(figsize = (12, 7))
plt.plot(x, y, alpha = 0.7, color="black", label="Poliestireno")
plt.xlim((max(x) + 10), (min(x) - 10))
plt.ylim(0, (max(y) + 0.02))
plt.title(f'Espectro Infrarrojo para Poliestireno', fontsize = 24)
plt.ylabel('Intensidad (a. u.)', fontsize = 24)
plt.xlabel(f'λ (cm¯¹)', fontsize = 24)
plt.show()