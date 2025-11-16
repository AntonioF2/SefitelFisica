import pandas as pd
import matplotlib.pyplot as plt

# Carregar a tabela
df = pd.read_csv("terremotos.csv")

def gerar_grafico(opcao):
    match opcao:
        # -----------------------------------------------------------
        # 1. Relação entre magnitude e profundidade
        # Quanto maior a profundidade, maior a atenuação das ondas
        # -----------------------------------------------------------
        case 1:
            plt.scatter(df["depth_km"], df["magnitude"])
            plt.title("Relação entre Profundidade do Epicentro e Magnitude")
            plt.xlabel("Profundidade (km)")
            plt.ylabel("Magnitude (Escala Richter)")
            plt.grid(True)
            plt.show()

        # -----------------------------------------------------------
        # 2. Histograma da magnitude (intensidade das ondas sísmicas)
        # Relaciona-se com o conteúdo energético das ondas mecânicas
        # -----------------------------------------------------------
        case 2:
            plt.hist(df["magnitude"])
            plt.title("Distribuição das Magnitudes")
            plt.xlabel("Magnitude")
            plt.ylabel("Frequência")
            plt.grid(True)
            plt.show()

        # -----------------------------------------------------------
        # 3. Gráfico de linha mostrando evolução temporal da magnitude
        # Ajuda a visualizar padrões e energia ao longo do tempo
        # -----------------------------------------------------------
        case 3:
            plt.plot(pd.to_datetime(df["date"]), df["magnitude"], marker='o')
            plt.title("Magnitude dos Terremotos ao Longo do Tempo")
            plt.xlabel("Data")
            plt.ylabel("Magnitude")
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.show()

        # -----------------------------------------------------------
        # 4. Comparação entre profundidade e energia estimada
        # Estimativa de energia: E ≈ 10^(1.5*M + 4.8)
        # -----------------------------------------------------------
        case 4:
            df["energia_J"] = 10 ** (1.5 * df["magnitude"] + 4.8)

            plt.scatter(df["depth_km"], df["energia_J"])
            plt.title("Energia Estimada vs Profundidade")
            plt.xlabel("Profundidade (km)")
            plt.ylabel("Energia (J)")
            plt.yscale("log")  # energia cresce muito → escala log
            plt.grid(True)
            plt.show()

        # -----------------------------------------------------------
        # Caso padrão
        # -----------------------------------------------------------
        case _:
            print("Opção inválida. Escolha 1, 2, 3 ou 4.")


# --------------------------
# Exemplo de uso:
# --------------------------

print("""
Escolha um gráfico:

1 - Profundidade vs Magnitude
2 - Histograma de Magnitudes
3 - Magnitude ao longo do tempo
4 - Energia sísmica estimada vs Profundidade
""")

op = int(input("Digite a opção desejada: "))
gerar_grafico(op)