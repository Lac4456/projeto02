import random
import datetime

def menu():
    nome_arq = "log.txt"
    while True:
        print("Monitor LogPy")
        print("1|Gerar Log \n2|Analisar Logs \n3|Gerar e Analisar Logs \n4|Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            try:
                qtd = int(input("Quantidade de Logs: "))
                gerarArquivo(nome_arq, qtd)
            except:
                print("Quantidade Incorreta")
        elif opcao == "2":
            analisarArquivo(nome_arq)
        elif opcao == "3":
            try:
                qtd = int(input("Quantidade de Logs: "))
                gerarArquivo(nome_arq, qtd)
                analisarArquivo(nome_arq)
            except:
                print("Quantidade Incorreta")
        elif opcao == "4":
            print("Até mais")
            break
        else:
            print("Opção Errada")
            
def gerarArquivo(nome_arq, qtd):
    with open(nome_arq, "w", encoding="UTF-8") as arq:
        for i in range(qtd):
            arq.write(montarLog(i) + "\n")
        print("Logs gerados")
        
def montarLog(i):
    data = gerarDataHora(i)
    ip = gerarIp(i)
    recurso = gerarRecurso(i)
    metodo = gerarMetodo(i)
    status = gerarStatus(i)
    tempo = gerarTempo(i)
    agente = gerarAgente(i)
    return f"[{data}] {ip} - {metodo} - {status} - {recurso} - {tempo:.0f}ms - 500mb - HTTP/1.1 - {agente} - /home"

def gerarDataHora(i):
    base = datetime.datetime(2026, 3, 30, 22,8,0)
    data = datetime.timedelta(seconds=i * random.randint(5, 20))
    return (base + data).strftime("%d/%m/%Y %H:%M:%S")

def gerarIp(i):
    r = random.randint(1, 6)
#Gerar o IP aleatorio    
    if i >= 20 and i <= 30:
        return "200.0.111.345"
    
    if r == 1:
        return "192.168.5.6"
    elif r ==2:
        return "192.168.5.7"
    elif r ==3:
        return "192.168.32.6"
    elif r ==4:
        return "192.168.12.9"
    elif r ==5:
        return "192.168.52.1"
    else:
        return "192.168.13.2"
    
def gerarRecurso(i):
    r = random.randint(1, 6)
#Gerar o recurso de acesso
    if r == 1:
        return "/index"
    elif r == 2:
        return "/home"
    elif r == 3:
        return "/admin"
    
def gerarMetodo(i):
    r = random.randint(1, 2)
#Gerar se o metodo foi get ou post
    if r == 1:
        return "GET"
    else:
        return "POST"
    
def gerarStatus(i):
    r =  random.randint(1, 4)
#Gerar o código de status
    if r == 1:
        return "200"
    elif r == 2:
        return "403"
    elif r == 3:
        return "404"
    else:
        return "500"
    
def gerarTempo(i):
    tempo = random.uniform(10, 500)

    return tempo

def gerarAgente(i):
    r = random.randint(1, 3)
#Gerar os agentes nos logs (browsers)
    if r == 1:
        return "Chrome"
    elif r == 2:
        return "Edge"
    else:
        return "Firefox"
    
def analisarArquivo(nome_arq):
    #Variáveis de Contagem Geral
    total_acessos = 0
    qtd_200 = 0; qtd_403 = 0; qtd_404 = 0; qtd_500 = 0
    soma_tempos = 0
    maior_tempo = 0
    menor_tempo = 99999
    
    #Categorias de Desempenho
    acessos_rapidos = 0   # < 200ms
    acessos_normais = 0   # 200ms a 799ms
    acessos_lentos = 0    # >= 800ms
    
    #Contadores de Recursos
    c_index = 0; c_home = 0; c_about = 0; c_admin = 0
    
    
    #Contadores de IPs
    ip1_count = 0; ip2_count = 0; ip3_count = 0; ip4_count = 0
    ip5_count = 0; ip6_count = 0; ip_especial_count = 0
    
    #Variáveis de Segurança e Sequências
    ip_anterior = ""
    recurso_anterior = ""
    status_anterior = ""
    tempo_anterior = -1
    
    total_forca_bruta = 0
    seq_forca_bruta = 0
    ultimo_ip_forca = "Nenhum"
    
    total_degradacao = 0
    seq_degradacao = 0
    
    total_falha_critica = 0
    seq_500 = 0
    
    total_bots = 0
    seq_bot = 0
    ultimo_ip_bot = "Nenhum"
    
    acessos_admin_indevidos = 0
    acessos_rotas_sensiveis = 0
    falhas_rotas_sensiveis = 0

    try:
        with open(nome_arq, "r", encoding="UTF-8") as arq:
            for linha in arq:
                linha = linha.strip()
                if linha == "": continue
                
                total_acessos += 1
                
                #EXTRAÇÃO MANUAL
                #Data e Hora
                p1 = linha.find("] ")
                data_hora = linha[1:p1]
                resto = linha[p1+2:]
                
                #IP
                p2 = resto.find(" - ")
                ip = resto[:p2]
                resto = resto[p2+3:]
                
                #Método
                p3 = resto.find(" - ")
                metodo = resto[:p3]
                resto = resto[p3+3:]
                
                #Status
                p4 = resto.find(" - ")
                status = resto[:p4]
                resto = resto[p4+3:]
                
                #Recurso
                p5 = resto.find(" - ")
                recurso = resto[:p5]
                resto = resto[p5+3:]
                
                #Tempo
                p6 = resto.find("ms")
                tempo = float(resto[:p6])
                resto = resto[p6+5:]
                
                #Tamanho
                p7 = resto.find(" - ")
                tamanho = resto[:p7]
                resto = resto[p7+3:]

                #Protocolo
                p8 = resto.find(" - ")
                protocolo = resto[:p8]
                resto = resto[p8+3:]

                #Agente
                p9 = resto.find(" - ")
                agente = resto[:p9]
                
                #Referer
                referer = resto[p9+3:]

                #PROCESSAMENTO DE DADOS
                soma_tempos += tempo
                if tempo > maior_tempo: maior_tempo = tempo
                if tempo < menor_tempo: menor_tempo = tempo
                
                if tempo < 200: acessos_rapidos += 1
                elif tempo < 800: acessos_normais += 1
                else: acessos_lentos += 1

                if status == "200": qtd_200 += 1
                elif status == "403": qtd_403 += 1
                elif status == "404": qtd_404 += 1
                elif status == "500": qtd_500 += 1

                # Contagem manual de Recursos
                if recurso == "/index": c_index += 1
                elif recurso == "/home": c_home += 1
                elif recurso == "/admin": c_admin += 1

                # Contagem manual de IPs
                if ip == "192.168.5.6": ip1_count += 1
                elif ip == "192.168.5.7": ip2_count += 1
                elif ip == "192.168.32.6": ip3_count += 1
                elif ip == "192.168.12.9": ip4_count += 1
                elif ip == "192.168.52.1": ip5_count += 1
                elif ip == "192.168.13.2": ip6_count += 1
                elif ip == "200.0.111.345": ip_especial_count += 1

                #LÓGICAS DE SEGURANÇA
                
                #Força Bruta
                if ip == ip_anterior and recurso == "/login" and status == "403":
                    seq_forca_bruta += 1
                    if seq_forca_bruta == 3:
                        total_forca_bruta += 1
                        ultimo_ip_forca = ip
                else:
                    seq_forca_bruta = 1 if (recurso == "/login" and status == "403") else 0

                #Degradação
                if tempo > tempo_anterior and tempo_anterior != -1:
                    seq_degradacao += 1
                    if seq_degradacao == 3:
                        total_degradacao += 1
                else:
                    seq_degradacao = 0

                #Falha Crítica
                if status == "500":
                    seq_500 += 1
                    if seq_500 == 3:
                        total_falha_critica += 1
                else:
                    seq_500 = 0

                #Suspeita de Bot
                if "Bot" in agente or "Crawler" in agente:
                    total_bots += 1
                    ultimo_ip_bot = ip
                elif ip == ip_anterior:
                    seq_bot += 1
                    if seq_bot == 5:
                        total_bots += 1
                        ultimo_ip_bot = ip
                else:
                    seq_bot = 1

                #Rotas Sensíveis
                if recurso == "/admin" or recurso == "/backup" or recurso == "/config" or recurso == "/private":
                    acessos_rotas_sensiveis += 1
                    if status != "200":
                        falhas_rotas_sensiveis += 1
                    if recurso == "/admin" and status != "200":
                        acessos_admin_indevidos += 1

                ip_anterior = ip
                tempo_anterior = tempo

        #CÁLCULOS FINAIS
        if total_acessos > 0:
            disponibilidade = (qtd_200 / total_acessos) * 100
            taxa_erro = ((total_acessos - qtd_200) / total_acessos) * 100
            media_tempo = soma_tempos / total_acessos
        else:
            print("Arquivo vazio.")
            return

        #Descobrir Recurso mais acessado
        mais_acessado_nome = "/index"; mais_acessado_val = c_index
        if c_home > mais_acessado_val: mais_acessado_nome = "/home"; mais_acessado_val = c_home
        if c_about > mais_acessado_val: mais_acessado_nome = "/about"; mais_acessado_val = c_about
        if c_admin > mais_acessado_val: mais_acessado_nome = "/admin"; mais_acessado_val = c_admin
        

        #Estado do Sistema
        estado = "SAUDÁVEL"
        if total_falha_critica > 0 or disponibilidade < 80: estado = "CRÍTICO"
        elif total_forca_bruta > 0 or acessos_lentos > (total_acessos * 0.2): estado = "ALERTA"

        #IMPRESSÃO DO RELATÓRIO
        print("\n" + "="*40)
        print("      RELATÓRIO MONITOR LOGPY")
        print("="*40)
        print(f"ESTADO DO SISTEMA: {estado}")
        print("-" * 40)
        print(f"Total de Acessos: {total_acessos}")
        print(f"Sucessos (200): {qtd_200} | Erros: {total_acessos - qtd_200}")
        print(f"Disponibilidade: {disponibilidade:.2f}%")
        print(f"Taxa de Erros: {taxa_erro:.2f}%")
        print("-" * 40)
        print(f"Tempo Médio: {media_tempo:.2f}ms")
        print(f"Maior Tempo: {maior_tempo:.2f}ms | Menor: {menor_tempo:.2f}ms")
        print(f"Rápidos: {acessos_rapidos} | Normais: {acessos_normais} | Lentos: {acessos_lentos}")
        print("-" * 40)
        print(f"Recurso mais acessado: {mais_acessado_nome} ({mais_acessado_val} vezes)")
        print("-" * 40)
        print("ALERTAS DE SEGURANÇA:")
        print(f"Força Bruta: {total_forca_bruta} (Último IP: {ultimo_ip_forca})")
        print(f"Suspeitas de Bot: {total_bots} (Último IP: {ultimo_ip_bot})")
        print(f"Falhas Críticas (3x 500): {total_falha_critica}")
        print(f"Degradações de Desempenho: {total_degradacao}")
        print(f"Acessos Indevidos /admin: {acessos_admin_indevidos}")
        print(f"Rotas Sensíveis: {acessos_rotas_sensiveis} (Falhas: {falhas_rotas_sensiveis})")
        print("="*40 + "\n")

    except FileNotFoundError:
        print("Arquivo de log não encontrado!")

menu()