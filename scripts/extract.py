import pandas as pd

def extract_file(file_path):

    df = pd.read_csv(file_path, sep=None, engine="python")
    return df

if __name__ == "__main__":
    file_path = "../data/marketing_campaing.csv"
    df = extract_file(file_path)
    
    
