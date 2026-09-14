# Cadastro da Startup
startup = {
    "nome": "CyberPulse Tech",
    "segmento": "Segurança da Informação",
    "ano_adesao": "2026"
}
solucoes_ativas = ["Firewall IA, Scan de Vulnerabilidades"]
print("nome:", startup["nome"])
print("segmento:", startup["segmento"])
print("primeiro produto:", solucoes_ativas[0])

# Bancadas
bancadas = [
    [1,0],
    [0,1]
]
print("bancada n1:", bancadas[0][0])
print("bancada n2:", bancadas[0][1])
print("bancada s1:", bancadas[1][0])
print("bancada s2:", bancadas[1][1])
print("1 = ocupado e 0 = livre")

with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    linha_dados_1 = arquivo.readline()
    linha_dados_2 = arquivo.readline()
    linha_dados_3 = arquivo.readline()
    linha_dados_4 = arquivo.readline()

print(cabecalho)
print(linha_dados_1)
print(linha_dados_2)
print(linha_dados_3)
print(linha_dados_4)

custo_1 = float(linha_dados_1.split(",")[1].strip())
custo_2 = float(linha_dados_2.split(",")[1].strip())
custo_3 = float(linha_dados_3.split(",")[1].strip())
custo_4 = float(linha_dados_4.split(",")[1].strip())
total = custo_1 + custo_2 + custo_3 + custo_4

print("\nPainel final de consolidação")
print("Startup:", startup["nome"])
print("Bancada alocada: Bancada N1")
print(f"Total da infraestrutura Cloud: R$ {total:.2f}")
