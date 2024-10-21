import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos arquivos CSV
capacitor_data = pd.read_csv('data/capacitor_voltage.csv')
resistor_data = pd.read_csv('data/resistor_voltage.csv')

# Extraindo os dados
tempo_capacitor = capacitor_data['TEMPO (ms)']
vc = capacitor_data['VC (Tensão no Capacitor)']

tempo_resistor = resistor_data['TEMPO (ms)']
vr = resistor_data['VR (Tensão no Resistor)']

# Gráfico da tensão no capacitor
plt.figure(figsize=(10, 6))
plt.plot(tempo_capacitor, vc, label='VC (Tensão no Capacitor)', color='b')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.title('Tensão no Capacitor ao Longo do Tempo')
plt.grid(True)
plt.legend()
plt.show()

# Gráfico da tensão no resistor
plt.figure(figsize=(10, 6))
plt.plot(tempo_resistor, vr, label='VR (Tensão no Resistor)', color='r')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.title('Tensão no Resistor ao Longo do Tempo')
plt.grid(True)
plt.legend()
plt.show()

# Gráfico comparativo das tensões no capacitor e no resistor
plt.figure(figsize=(10, 6))
plt.plot(tempo_capacitor, vc, label='VC (Tensão no Capacitor)', color='b')
plt.plot(tempo_resistor, vr, label='VR (Tensão no Resistor)', color='r')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.title('Comparação das Tensões no Capacitor e Resistor')
plt.grid(True)
plt.legend()
plt.show()
