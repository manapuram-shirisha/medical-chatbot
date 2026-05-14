import pandas as pd
import os

def load_data():

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    data_path = os.path.join(BASE_DIR, "data")

    print("Checking path:", data_path)

    files = ["dataset1.csv", "dataset2.csv", "dataset3.csv"]

    dfs = []

    for file in files:
        full_path = os.path.join(data_path, file)

        if not os.path.exists(full_path):
            raise FileNotFoundError(f"{file} NOT FOUND at {full_path}")

        print(f"Loading: {full_path}")
        dfs.append(pd.read_csv(full_path))

    df = pd.concat(dfs)

    df = df.fillna("")
    df = df.astype(str)

    df['symptoms'] = df.iloc[:, :-1].apply(lambda x: ' '.join(x), axis=1)
    df['disease'] = df.iloc[:, -1]

    return df