falhas_por_ip = {}
total_falhas = 0
with open("logs/auth.log", "r") as arquivo:

    for linha in arquivo:
        if "status=failed" in linha:
            partes = linha.split()
            ip = partes[0].replace("IP=", "")

            falhas_por_ip[ip] = falhas_por_ip.get(ip, 0) + 1
            total_falhas += 1
ip_suspeitos = max(falhas_por_ip, key=falhas_por_ip.get)

print(f"IP mais suspeito: {ip_suspeitos} com {falhas_por_ip[ip_suspeitos]} falhas")
print(f"Total de falhas de autenticação: {total_falhas}")