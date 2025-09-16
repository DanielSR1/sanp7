import snap7
from snap7.util import get_int
import os

# Configuração do PLC
plc_ip = "YOUR_BRIDGE_IP_ADDRESS"  # Substitua pelo IP do seu PLC
rack = 0
slot = 0

if not os.environ.get('SNAP7_PATH') and 'snap7.dll' not in os.environ['PATH']:
    # Add path to snap7.dll to PATH env variable if not already there
    # ...
    pass

# Inicializa o cliente
client = snap7.client.Client()

try:
    # Tenta conectar ao PLC
    client.connect(plc_ip, rack, slot)
    if client.get_connected():
        print(f"Conectado ao PLC em {plc_ip}")
        input("Pressione Enter para continuar...")

        # ---------- LEITURA DE INT ----------
        db_number = 1   # DB1
        start = 0       # byte inicial
        size = 2        # INT = 2 bytes
        data_int = client.db_read(db_number, start, size)
        value_int = get_int(data_int, 0)
        print(f"Valor do INT em DB{db_number}, byte {start}: {value_int}")
        input("Pressione Enter para continuar...")
        
        # Desconectar
        client.disconnect()
        print("Desconectado do PLC.")
        input("Pressione Enter para encerrar...")

    else:
        print("Falha na conexão com o PLC.")
        input("Pressione Enter para encerrar...")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    input("Pressione Enter para encerrar...")
