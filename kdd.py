import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compara os elementos (que agora são tuplas: (item, contagem))
            if lista[j][0] > lista[j+1][0]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# --- PROCESSAMENTO ---
contagem = {}

try:
    # 1. LER, LIMPAR E CONTAR
    with open("texto para ordenar.txt", "r", encoding="utf-8") as f:
        conteudo = f.read().split()
        for item in conteudo:
            limpo = item.strip(",.;:()[]{}")
            if limpo:
                # Tenta converter para número para a contagem ser precisa
                try:
                    chave = int(limpo)
                except ValueError:
                    chave = limpo.lower()
                
                # Alimenta o dicionário de contagem
                if chave in contagem:
                    contagem[chave] += 1
                else:
                    contagem[chave] = 1

    # 2. SEPARAR NÚMEROS E TEXTOS PARA ORDENAR SEM ERRO
    # Criamos listas de tuplas: (valor, quantidade)
    lista_numeros = [(k, v) for k, v in contagem.items() if isinstance(k, int)]
    lista_textos = [(k, v) for k, v in contagem.items() if isinstance(k, str)]
    
    # Ordenação Matemática para números e Alfabética para textos
    lista_numeros.sort() 
    lista_textos.sort()
    
    resultado_final = lista_numeros + lista_textos

    print(f"Itens lidos com sucesso!")
    print(f"Total de itens únicos encontrados: {len(resultado_final)}\n")

    # 3. EXIBIR REPETIÇÕES NO TERMINAL (Opcional para conferência)
    print("--- RESUMO DE REPETIÇÕES ---")
    for item, qtd in resultado_final:
        if qtd > 1:
            print(f"• {item}: repetido {qtd} vezes")

    # 4. SALVAR NO ARQUIVO COM A CONTAGEM
    with open("palavras_ordenadas.txt", "w", encoding="utf-8") as f_out:
        f_out.write("ITEM | REPETIÇÕES\n")
        f_out.write("-" * 20 + "\n")
        for item, qtd in resultado_final:
            f_out.write(f"{item} | {qtd}\n")

    print(f"\n✅ Glossário gerado em 'palavras_ordenadas.txt' com as contagens!")

except FileNotFoundError:
    print("Erro: O arquivo 'texto para ordenar.txt' não foi encontrado.")