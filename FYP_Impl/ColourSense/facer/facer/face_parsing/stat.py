import pandas as pd
import numpy as np

# Read the TSV file into a DataFrame
df_all = pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/FinalYear/FYP/FYP_Impl/ColourSense/facer/facer/face_parsing/test/eval.lapa_test_0.tsv", delimiter='\t')

# Calculate summary statistics for the 'fg_mean' column
fg_mean_summary_statistics = df_all['fg_mean'].describe()

# Display summary statistics for the 'fg_mean' column
print(fg_mean_summary_statistics)