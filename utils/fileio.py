"""This is a function to write a CSV file from Python data"""

import csv
from pathlib import Path
from Module_1_Challenge import inexpensive_loans

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

output_path = Path("inexpensive_loans.csv")

def write_csv():
    with open(output_path, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())