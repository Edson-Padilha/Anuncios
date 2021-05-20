# Edson Marciano Rodrigues Padilha

# Funcao imprimi linhas para separacao de campos na saida de impressao
def linha():
    print("\033[34m_ \033[m" * 20)    
    

# Titulo do sistema
linha() # Chama funcao
print("\033[4;30;46m      CALCULADORA DE ANUNCIOS           \033[m")
linha()

# Entrada de valor para projecao da campanha
vlr = float(input("Digite o valor a ser investido R$ "))

# Variaveis e processamento dos dados

visualizacoes = vlr / 0.0333333333333333             # 0.0333333333333333 = R$ 1 / 30 visualizacoes , para saber o custo de cada visualizacao
comp_origem = vlr / 0.25                             # 0.25 = R$ 1 / 4 compartlhamentos, para saber o custo de cada compartilhamento
click_origem = visualizacoes * 0.12                  # 0.12 = 12 cliques / 100 visualizacoes
comp_redes_sociais = click_origem / 6.666666666666667# 6.666666666666667 = 20 cliques / 3 compartilhamentos
acres_views = comp_redes_sociais * 40                # 40 = Cada compartilhamento equivale a 40 novas visualizacoes
views_totais = visualizacoes + acres_views           # Uniao das duas visualizacoes, original + visualizacoes das redes sociais
click_total = 8.333333333333333                      # 8.333333333333333 = 100 visualizacoes / 12 cliques
comp_total = comp_origem + comp_redes_sociais        # Uniao dos compartilhamentos de origem e redes sociais

# Saida das informacoes
linha ()
print(f"Valor investido: R$ {vlr:.2f}")                          
linha()
print(f"Visualizações originais: {visualizacoes:.0f}")           
linha()
print(f"Compartilhamentos originais: {comp_origem:.0f}")
linha()
print(f"Cliques originais: {click_origem:.0f}" )
linha()
print(f"Compartilhamentos redes sociais: {comp_redes_sociais:.2f}")
linha()
print(f"Acrécimo de visualizações: {acres_views:.0f}")
linha()
print(f"Visualizações totais: {views_totais:.0f}")
linha()
print(f"Compartilhamentos totais: {comp_total:.2f}")
linha()
print("\033[1;31m         -- Fim do Programa -- \033[m")
linha()
# Fim da execucao.