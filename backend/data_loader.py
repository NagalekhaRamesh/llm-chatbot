import pandas as pd
import os

def load_csvs(csv_folder_path="csvs"):
    dataframes = {}
    if not os.path.exists(csv_folder_path):
        print(f"[WARNING] CSV folder '{csv_folder_path}' does not exist.")
        return dataframes

    for filename in os.listdir(csv_folder_path):
        if filename.endswith(".csv"):
            filepath = os.path.join(csv_folder_path, filename)
            df_name = filename.replace(".csv", "")
            try:
                df = pd.read_csv(filepath)
                dataframes[df_name] = df
                print(f"[INFO] Loaded CSV: {df_name} with {len(df)} rows.")
            except Exception as e:
                print(f"[ERROR] Failed to load {filename}: {e}")

    return dataframes
