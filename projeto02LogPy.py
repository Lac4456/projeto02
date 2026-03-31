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

    if r == 1:
        return "/index"
    elif r == 2:
        return "/home"
    elif r == 3:
        return "/about"
    elif r == 4:
        return "/contact"
    elif r == 5:
        return "/products"
    else:
        return "/services"
    
def gerarMetodo(i):
    r = random.randint(1, 2)

    if r == 1:
        return "GET"
    else:
        return "POST"
    
def gerarStatus(i):
    r =  random.randint(1, 3)

    if r == 1:
        return "200"
    elif r == 2:
        return "403"
    else:
        return "404"
    
def gerarTempo(i):
    tempo = random.uniform(10, 500)

    return tempo

def gerarAgente(i):
    r = random.randint(1, 6)

    if r == 1:
        return "Chrome"
    elif r == 2:
        return "Edge"
    elif r == 3:
        return "Firefox"
    elif r == 4:
        return "Opera"
    elif r == 5:
        return "Brave"
    else:
        return "DuckDuckGo"
    
