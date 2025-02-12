import pandas as pd

    df[['FGM', 'FGA']] = df['FG'].str.split('-', expand=True).astype(int)

    df[['3PM', '3PA']] = df['3PT'].str.split('-', expand=True).astype(int)

    df[['FTM', 'FTA']] = df['FT'].str.split('-', expand=True).astype(int)
    
    df = df.drop(columns=['FG', '3PT', 'FT'])
    
    df['FG'] = df['FGM'].astype(str) + '-' + df['FGA'].astype(str)
    df['3PT'] = df['3PM'].astype(str) + '-' + df['3PA'].astype(str)

    df['FT'] = df['FTM'].astype(str) + '-' + df['FTA'].astype(str)
    
    df.insert(df.columns.get_loc('FTA') + 1, ' ', '')
    
    return df

def main():

    frame = pd.read_csv("cleanbrogdonstats.csv")
    frame = cleanStats(frame)
    
    frame = frame.drop(frame.columns[4:17], axis=1)
    
    print(frame.to_string(index=False))

if __name__ == "__main__":
    main()
