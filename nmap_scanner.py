import subprocess
import ipaddress
import xml.etree.ElementTree as ET

# 輸入 IP 位址並驗證格式
while True:
    try:
        ip = input("請輸入目標 IP 位址 : ")
        ipaddress.ip_address(ip)
        break
    except ValueError:
        print("無效的 IP 位址！")

# 呼叫 nmap 執行指令
result = subprocess.run(["nmap", "-sV", "-oX", "-", ip], capture_output = True, text = True)
if result.returncode != 0:
    print(result.stderr)
    exit()

# 解析 XML 結構
root = ET.fromstring(result.stdout)
for port in root.findall(".//port"):
    # 取得 port, protocol
    port_id = port.get("portid")
    protocol = port.get("protocol")
    # 取得 state
    state = port.find("state").get("state")
    # 取得 service, product, version
    service_elem = port.find("service")
    if service_elem is not None:
        service = service_elem.get("name")
        product = service_elem.get("product", "N/A")
        version = service_elem.get("version", "N/A")
    else:
        service = "N/A"
        product = "N/A"
        version = "N/A"
    print(f"Port : {port_id}/{protocol}, State : {state}, Service : {service}, Product : {product}, Version : {version}")