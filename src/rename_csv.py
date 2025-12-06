import pandas as pd
import os

def rename_csv_headers(input_csv: str, output_csv: str):
    """
    Đổi tên tiêu đề của CSV theo danh sách định sẵn, bỏ các số đánh dấu.
    
    Args:
        input_csv: đường dẫn file CSV đầu vào
        output_csv: đường dẫn file CSV đầu ra
    """
    new_columns = [
        "Flow ID",
        "Src IP",
        "Src Port",
        "Dst IP",
        "Dst Port",
        "Protocol",
        "Timestamp",
        "Flow Duration",
        "Total Fwd Packet",
        "Total Bwd packets",
        "Total Length of Fwd Packet",
        "Total Length of Bwd Packet",
        "Fwd Packet Length Max",
        "Fwd Packet Length Min",
        "Fwd Packet Length Mean",
        "Fwd Packet Length Std",
        "Bwd Packet Length Max",
        "Bwd Packet Length Min",
        "Bwd Packet Length Mean",
        "Bwd Packet Length Std",
        "Flow Bytes/s",
        "Flow Packets/s",
        "Flow IAT Mean",
        "Flow IAT Std",
        "Flow IAT Max",
        "Flow IAT Min",
        "Fwd IAT Total",
        "Fwd IAT Mean",
        "Fwd IAT Std",
        "Fwd IAT Max",
        "Fwd IAT Min",
        "Bwd IAT Total",
        "Bwd IAT Mean",
        "Bwd IAT Std",
        "Bwd IAT Max",
        "Bwd IAT Min",
        "Fwd PSH Flags",
        "Bwd PSH Flags",
        "Fwd URG Flags",
        "Bwd URG Flags",
        "Fwd Header Length",
        "Bwd Header Length",
        "Fwd Packets/s",
        "Bwd Packets/s",
        "Packet Length Min",
        "Packet Length Max",
        "Packet Length Mean",
        "Packet Length Std",
        "Packet Length Variance",
        "FIN Flag Count",
        "SYN Flag Count",
        "RST Flag Count",
        "PSH Flag Count",
        "ACK Flag Count",
        "URG Flag Count",
        "CWR Flag Count",
        "ECE Flag Count",
        "Down/Up Ratio",
        "Average Packet Size",
        "Fwd Segment Size Avg",
        "Bwd Segment Size Avg",
        "Fwd Bytes/Bulk Avg",
        "Fwd Packet/Bulk Avg",
        "Fwd Bulk Rate Avg",
        "Bwd Bytes/Bulk Avg",
        "Bwd Packet/Bulk Avg",
        "Bwd Bulk Rate Avg",
        "Subflow Fwd Packets",
        "Subflow Fwd Bytes",
        "Subflow Bwd Packets",
        "Subflow Bwd Bytes",
        "FWD Init Win Bytes",
        "Bwd Init Win Bytes",
        "Fwd Act Data Pkts",
        "Fwd Seg Size Min",
        "Active Mean",
        "Active Std",
        "Active Max",
        "Active Min",
        "Idle Mean",
        "Idle Std",
        "Idle Max",
        "Idle Min",
        "Stage"
    ]

    # Đọc CSV
    df = pd.read_csv(input_csv)

    if len(df.columns) != len(new_columns):
        raise ValueError(f"Số cột trong CSV ({len(df.columns)}) khác số cột header mới ({len(new_columns)})")

    # Đổi tên header
    df.columns = new_columns

    # Lưu file mới
    df.to_csv(output_csv, index=False)
    print(f"Đã đổi header và lưu file: {output_csv}")


# -----------------------------
# Ví dụ sử dụng
# -----------------------------
if __name__ == "__main__":
    input_csv = "csv/input.pcap_Flow.csv"
    output_csv = "csv/input.csv"
    rename_csv_headers(input_csv, output_csv)
