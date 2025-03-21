



df_category = df.select_dtypes(include='object')
df_numeric = df.select_dtypes(exclude=['int64', 'float64'])