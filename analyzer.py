import pandas as pd

def analyze_logs(df: pd.DataFrame) -> pd.Series:
    """
    Returns a Series of feature usage counts.
    """
    if 'feature' not in df.columns:
        raise ValueError("Missing 'feature' column in data.")

    feature_counts = df['feature'].value_counts()
    return feature_counts