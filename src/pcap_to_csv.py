import subprocess
import os

def pcap_to_csv(filename: str):
    """
    Chuyển file PCAP sang CSV bằng CICFlowMeter, sử dụng các đường dẫn mặc định.
    
    Args:
        filename: tên file PCAP trong folder 'uploads'
    """
    ROOT_DIR = r"D:\Workspace\AI\VBFinal"
    PCAP_FILE = os.path.join(ROOT_DIR, "uploads", filename)
    OUTPUT_DIR = os.path.join(ROOT_DIR, "csv")
    CFM_PATH = os.path.join(ROOT_DIR, "CICFlowMeter-4.0", "bin", "cfm.bat")
    CWD = os.path.join(ROOT_DIR, "CICFlowMeter-4.0", "bin")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    env = os.environ.copy()
    env["PATH"] = os.path.join(ROOT_DIR, "CICFlowMeter-4.0", "lib") + ";" + env["PATH"]
    
    try:
        cmd = [CFM_PATH, PCAP_FILE, OUTPUT_DIR]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, env=env, cwd=CWD)
        
        print(f"PCAP file: {filename}")
        print("Output from CICFlowMeter:")
        print(result.stdout)
        print("Errors (if any):")
        print(result.stderr)
        
    except subprocess.CalledProcessError as e:
        print(f"CICFlowMeter chạy lỗi với file {filename}!")
        print("Return code:", e.returncode)
        print("Output:", e.output)
        print("Error:", e.stderr)


# ---------------------------
# Ví dụ sử dụng
# ---------------------------
if __name__ == "__main__":
    pcap_to_csv("input.pcap")
