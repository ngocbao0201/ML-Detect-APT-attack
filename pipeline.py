from pcap_to_csv import pcap_to_csv
from rename_csv import rename_csv_headers

pcap_to_csv("input.pcap")
input_csv = "csv/input.pcap_Flow.csv"
output_csv = "csv/input.csv"
rename_csv_headers(input_csv, output_csv)