import snap7
import os

plc_ip = "YOUR_BRIDGE_IP_ADDRESS"  # The IP address of the Ethernet Bridge

# Ensure snap7.dll is in the path
if not os.environ.get('SNAP7_PATH') and 'snap7.dll' not in os.environ['PATH']:
    # Add path to snap7.dll to PATH env variable if not already there
    # ...
    pass

client = snap7.client.Client()

try:
    client.connect(plc_ip, 0, 0)  # Example: rack 0, slot 0
    if client.get_connected():
        print(f"Connected to PLC at {plc_ip}")
        input("Pressione Enter para continuar...")  # Pausa para leitura
        # Perform read/write operations here
        client.disconnect()
        print("Disconnected from PLC.")
        input("Pressione Enter para encerrar...")
    else:
        print("Connection failed.")
        input("Pressione Enter para encerrar...")
except Exception as e:
    print(f"An error occurred: {e}")
    input("Pressione Enter para encerrar...")
