from collections import Counter, defaultdict

ARQUIVO_LOG = "logs/auth.log"
LIMITE_FALHAS = 10  

falhas_por_ip = Counter()          
sucessos_por_ip = Counter()        
periodo_por_ip = defaultdict(lambda: {"primeiro": None, "ultimo": None})
total_ips = 0
total_falhas = 0
total_sucessos = 0

with open(ARQUIVO_LOG, "r") as arquivo:
    for linha in arquivo:
        partes = linha.split()
        if len(partes) < 3:
            continue

        data, horario = partes[0], partes[1]
        ip = partes[2].replace("IP=", "")

        if "status=failed" in linha:
            falhas_por_ip[ip] += 1
            total_falhas += 1
            total_ips += 1

            if periodo_por_ip[ip]["primeiro"] is None:
                periodo_por_ip[ip]["primeiro"] = (data, horario)
            periodo_por_ip[ip]["ultimo"] = (data, horario)

        elif "status=success" in linha:
            sucessos_por_ip[ip] += 1
            total_sucessos += 1
            total_ips += 1


if not falhas_por_ip:
    print("Nenhuma falha de autenticação registrada.")
else:
    ip_suspeito, qtd = falhas_por_ip.most_common(1)[0]
    primeiro = periodo_por_ip[ip_suspeito]["primeiro"]
    ultimo   = periodo_por_ip[ip_suspeito]["ultimo"]

    print(f"IP mais suspeito: {ip_suspeito}")
    print(f"  Falhas:          {qtd}")
    print(f"  Primeira falha:  {primeiro[0]} às {primeiro[1]}")
    print(f"  Última falha:    {ultimo[0]} às {ultimo[1]}")
    print(f"  Sucessos desse IP: {sucessos_por_ip.get(ip_suspeito, 0)}")

print(f"\nTotal de falhas:   {total_falhas}")
print(f"Total de sucessos: {total_sucessos}")
print(f"Total de IPs distintos: {total_ips}")

suspeitos = [(ip, q) for ip, q in falhas_por_ip.items() if q > LIMITE_FALHAS]
if suspeitos:
    print(f"\n⚠  IPs com mais de {LIMITE_FALHAS} falhas:")
    for ip, q in sorted(suspeitos, key=lambda x: -x[1]):
        print(f"  {ip}: {q} falhas | {sucessos_por_ip.get(ip, 0)} sucessos")