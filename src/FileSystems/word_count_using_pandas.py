import pandas as pd

df = pd.read_csv("./input/google_file_store.txt", sep='|')

#df = df[df["filename"].str.contains("draft", case=False)]

df["contents"] = df["contents"].str.replace('"', '')

df["contents"] = df["contents"].str.replace(',', '')

df["contents"] = df["contents"].str.replace('.', '')

df = df["contents"].str.split(" ")

df = df.explode("contents").reset_index(name="contents")

print(df.to_string(index=False))

grp_df = df.groupby("contents").size().sort_values(ascending=False).reset_index(name='count')

grp_df.to_csv(index=False, path_or_buf='./output/word_count.csv')
