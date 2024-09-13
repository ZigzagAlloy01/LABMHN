import matplotlib.pyplot as plt

infrared = open("Al2O3.txt").readlines()
x = []
y = []
w = []
z = []
for line in infrared:
    newLine = line.split(",")
    abcisa = newLine[0]
    ordenada = newLine[1]
    x.append(float(abcisa))
    y.append(float(ordenada)*0.64)
infrared = open("Al2O3CeO2.txt").readlines()
for line in infrared:
    newLine = line.split(",")
    abcisa = newLine[0]
    ordenada = newLine[1]
    w.append(float(abcisa))
    z.append(float(ordenada))
fig = plt.figure(figsize = (12, 7))
plt.plot(x, y, alpha = 0.7, color="black", label="Al₂O₃")
plt.plot(w, z, alpha = 0.7, color="red", label="Al₂O₃-CeO₂")
plt.xlim((1800), (min(x)-100))
plt.ylim(min(y), (max(y) + 0.1))
plt.title(f'Espectro FTIR para Al₂O₃ y Al₂O₃-CeO₂', fontsize = 24)
plt.ylabel('Intensidad (a.u.)', fontsize = 24)
plt.xlabel(f'λ (cm¯¹)', fontsize = 24)
plt.show()