import socket
import sys

def scan_ports(host, ports):
    print(f"🔍 Escaneando {host}...\n")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Tempo máximo para resposta
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"[+] Porta {port} ➤ ABERTA")
            else:
                print(f"[-] Porta {port} ➤ fechada")
            sock.close()
        except Exception as e:
            print(f"[!] Erro ao escanear porta {port}: {e}")
            continue

def main():
    if len(sys.argv) < 2:
        print("📢 Uso: python port_scanner.py <dominio_ou_ip>")
        print("Exemplo: python port_scanner.py google.com")
        sys.exit(1)

    host = sys.argv[1]

    # Lista de portas comuns para escanear
    common_ports = [
        20,   # FTP Data
        21,   # FTP Control
        22,   # SSH
        23,   # Telnet
        25,   # SMTP
        53,   # DNS
        80,   # HTTP
        110,  # POP3
        143,  # IMAP
        443,  # HTTPS
        3306, # MySQL
        3389, # Remote Desktop
        8080, # Proxy/HTTP Alt
    ]

    scan_ports(host, common_ports)

if __name__ == "__main__":
    main()