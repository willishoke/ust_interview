import subprocess
import re

def run_command(command):
    """Runs a shell command and returns the output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return str(e)

def get_pcie_devices():
    """Gets a list of PCIe devices with details."""
    output = run_command("lspci -vvv")
    return output

def check_pcie_link_status():
    """Checks PCIe link speed and width."""
    output = run_command("lspci -vvv | grep -i 'LnkSta'")
    return output

def check_dmesg_errors():
    """Checks dmesg logs for PCIe-related errors."""
    output = run_command("dmesg | grep -i pci")
    return output

def analyze_output():
    """Analyzes collected data and provides diagnostics."""
    print("\n--- PCIe Device List ---")
    print(get_pcie_devices())
    
    print("\n--- PCIe Link Status ---")
    link_status = check_pcie_link_status()
    print(link_status)
    
    # Check for reduced link width/speed
    if re.search(r'LnkSta:\s+Speed\s+\d+\.\d+GT/s,\s+Width\s+x\d+', link_status):
        print("\n[INFO] PCIe link speed and width appear normal.")
    else:
        print("\n[WARNING] Potential PCIe link speed or width issue detected!")
    
    print("\n--- Checking dmesg for PCIe errors ---")
    dmesg_output = check_dmesg_errors()
    print(dmesg_output if dmesg_output else "No PCIe errors found in dmesg.")


if __name__ == "__main__":
    analyze_output()
