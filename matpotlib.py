import matplotlib.pyplot as plt

# 1
semanas = [1, 2, 3, 4, 5]
alturas = [3, 6, 9, 12, 15]
plt.plot(semanas, alturas)
plt.title("Crescimento da Planta")
plt.xlabel("Semanas")
plt.ylabel("Altura cm")
plt.grid(True)
plt.show()

# 2
materias = []
notas = []
for i in range(3):
    materia = input(f"Digite a {i + 1}a materia: ")
    materias.append(materia)
for i in range(3):
    nota = float(input(f"Digite sua nota em {materias[i]}: "))
    notas.append(nota)
plt.bar(materias, notas)
plt.title("Notas por Materia")
plt.ylabel("Nota")
plt.show()

# 3
trans = ['Onibus', 'Carro', 'Bicicleta', 'A pe']
perc = [40, 30, 20, 10]
plt.pie(perc, labels=trans, autopct='%1.1f%%')
plt.title("Transportes")
plt.axis('equal')
plt.show()

# 4
horarios = ['Ao acordar', 'Apos exercicio', 'Apos descanso']
bpms = []
for h in horarios:
    bpm = int(input(f"Digite os batimentos cardiacos {h}: "))
    bpms.append(bpm)
plt.plot(horarios, bpms)
plt.title("Batimentos Cardiacos")
plt.ylabel("BPM")
plt.grid(True)
plt.show()

# 5
sabores = ['Chocolate', 'Morango', 'Baunilha']
vendas = [150, 100, 130]
plt.bar(sabores, vendas)
plt.title("Vendas de Sorvete")
plt.ylabel("Unidades Vendidas")
plt.show()

# 6
sono = float(input("Digite horas dormindo: "))
estudo = float(input("Digite koras estudando: "))
lazer = float(input("Digite horas em lazer: "))
atividades = ['Sono', 'Estudo', 'Lazer']
horas = [sono, estudo, lazer]
plt.pie(horas, labels=atividades, autopct='%1.1f%%')
plt.title("Distribuicao do Tempo no Dia")
plt.show()

# 7
t = [0, 5, 10, 15, 20]
vel = [0, 20, 40, 35, 50]
plt.plot(t, vel)
plt.title("Variacao de Velocidade do Carro")
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (km/h)")
plt.grid(True)
plt.show()

# 8
banana = int(input("Quantas bananas você comeu na semana? "))
maca = int(input("Quantas maçãs você comeu na semana? "))
laranja = int(input("Quantas laranjas você comeu na semana? "))
frutas = ['Bananas', 'Maçãs', 'Laranjas']
quant = [banana, maca, laranja]
plt.bar(frutas, quant)
plt.title("Frutas na Semana")
plt.ylabel("Quantidade")
plt.show()

# 9
redes = ['Instagram', 'YouTube', 'TikTok', 'WhatsApp', 'Outros']
horas = []
for rede in redes:
    hora = float(input(f"Digite quantas horas você usa de {rede}? "))
    horas.append(hora)
plt.pie(horas, labels=redes, autopct='%1.1f%%')
plt.title("Uso de Redes Sociais em 1 Dia")
plt.show()

# 10
periodos = ['Manha', 'Tarde', 'Noite']
energia = []
for periodo in periodos:
    nivel = int(input(f"Digite seu nivel de energia de {periodo} (0 a 10): "))
    energia.append(nivel)
plt.plot(periodos, energia)
plt.title("Nivel de Energia ao Longo do Dia")
plt.ylabel("Nivel de Energia")
plt.grid(True)
plt.show()