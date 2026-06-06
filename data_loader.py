# data_loader.py

import pandas as pd
import numpy as np

import os
import tkinter as tk
from tkinter import filedialog

class DataLoader:
    def __init__(self):
            pass

    def load_data(self, data_file=None):
        try:
            if data_file is None:
                data_file = self.open_explorer()

            if not data_file:
                print("[INFO] No file selected")
                return None

            ext = os.path.splitext(data_file)[1].lower()

            if ext == '.csv':
                data = pd.read_csv(data_file).values

            elif ext == '.json':
                data = pd.read_json(data_file).values

            elif ext in ['.xls', '.xlsx']:
                data = pd.read_excel(data_file).values

            else:
                raise ValueError(f"[ERROR] Unsupported format: {ext}")

            return np.array(data)

        except Exception as e:
            print(f"[ERROR] {e}")
            return None

    def open_explorer(self):
        """Opens file explorer and returns selected file path"""
        file_path = filedialog.askopenfilename(
            title="Select dataset file",
            filetypes=[
                ("CSV Files", "*.csv"),
                ("Excel Files", "*.xlsx *.xls"),
                ("JSON Files", "*.json"),
                ("All Files", "*.*")
            ]
        )

        return file_path if file_path else None
