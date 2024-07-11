import pandas as pd

def clean_dataframe(df):

    df = df.dropna()


    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    df[numerical_cols] = (df[numerical_cols] - df[numerical_cols].mean()) / df[numerical_cols].std()

    # Encoding categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    df = pd.get_dummies(df, columns=categorical_cols)

    return df

data = {
    'A': [1, 2, None, 4],
    'B': ['x', 'y', 'x', None],
    'C': [1.0, 2.5, 3.0, 4.5]
}
df = pd.DataFrame(data)
cleaned_df = clean_dataframe(df)
print(cleaned_df)
