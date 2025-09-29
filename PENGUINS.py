from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Abre o seletor de arquivos
uploaded = files.upload()

# Lê o primeiro arquivo enviado
for file_name in uploaded.keys():
    df = pd.read_csv(file_name)
    print(f'Arquivo "{file_name}" carregado com sucesso!')

# Visualizar as primeiras linhas
df.head()

# Definir estilo dos gráficos
sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.boxplot(
    data=df,
    x='island',              # Local onde vivem
    y='body_mass_g',         # Tamanho (peso corporal)
    palette='Set2'           # Paleta de cores agradável
)

df.columns

plt.title('Distribuição do Peso dos Pinguins por Ilha', fontsize=16)
plt.xlabel('Ilha', fontsize=12)
plt.ylabel('Peso Corporal (g)', fontsize=12)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.tight_layout()
plt.show()

df['island'].unique()

altitude_ilhas = {
    'Torgersen': 10,   # Exemplo
    'Biscoe': 30,      # Exemplo
    'Dream': 50        # Exemplo
}

# Criar nova coluna com a altitude da ilha
df['altitude_m'] = df['island'].map(altitude_ilhas)

plt.figure(figsize=(8, 6))
sns.regplot(
    data=df,
    x='altitude_m',
    y='body_mass_g',
    scatter_kws={'s': 60, 'alpha': 0.6},
    line_kws={'color': 'red'}
)

plt.title('Relação entre Altitude da Ilha e Peso dos Pinguins', fontsize=14)
plt.xlabel('Altitude da Ilha (m)', fontsize=12)
plt.ylabel('Peso Corporal dos Pinguins (g)', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

# Categorizar altitude em faixas
df['faixa_altitude'] = pd.cut(df['altitude_m'], bins=[0, 20, 40, 60], labels=['Baixa', 'Média', 'Alta'])

plt.figure(figsize=(8, 6))
sns.boxplot(
    data=df,
    x='faixa_altitude',
    y='body_mass_g',
    palette='Set3'
)

plt.title('Peso dos Pinguins por Faixa de Altitude das Ilhas', fontsize=14)
plt.xlabel('Faixa de Altitude', fontsize=12)
plt.ylabel('Peso Corporal (g)', fontsize=12)
plt.tight_layout()
plt.show()

# Estatísticas básicas do peso corporal
print("=== Estatísticas Gerais do Peso Corporal dos Pinguins ===")
print(df['body_mass_g'].describe())  # Inclui média, std, min, 25%, 50%, 75%, max

# Medianas
mediana = df['body_mass_g'].median()
print(f"\nMediana do peso corporal: {mediana:.2f} g")

# Estatísticas x ilha
print("\n=== Estatísticas por Ilha ===")
estatisticas_ilha = df.groupby('island')['body_mass_g'].agg(['count', 'mean', 'median', 'std', 'min', 'max'])
print(estatisticas_ilha)

# Estatísticas x altitude
print("\n=== Estatísticas por Faixa de Altitude ===")
estatisticas_altitude = df.groupby('faixa_altitude')['body_mass_g'].agg(['count', 'mean', 'median', 'std', 'min', 'max'])
print(estatisticas_altitude)

# Dados das estatísticas
estatisticas = {
    'Mínimo': df['body_mass_g'].min(),
    '25% (1º Quartil)': df['body_mass_g'].quantile(0.25),
    'Média': df['body_mass_g'].mean(),
    'Mediana (50%)': df['body_mass_g'].median(),
    '75% (3º Quartil)': df['body_mass_g'].quantile(0.75),
    'Máximo': df['body_mass_g'].max()
}

# Ordenar as métricas para melhor visualização
labels = list(estatisticas.keys())
values = list(estatisticas.values())

# Gerar o gráfico
plt.figure(figsize=(10, 6))
plt.barh(labels, values, color='lightblue')

# Adicionar rótulos e título
plt.xlabel('Peso Corporal (g)', fontsize=12)
plt.title('Estatísticas de Peso Corporal dos Pinguins', fontsize=14)
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# Exibir o gráfico
plt.tight_layout()
plt.show()



