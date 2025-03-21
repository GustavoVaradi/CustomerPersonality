"""
remove 'Z_CostContact', 'Z_Revenue'
"""


def clean_data(df):
    df = df.drop(columns=['Z_CostContact', 'Z_Revenue']) # Same values for all rows