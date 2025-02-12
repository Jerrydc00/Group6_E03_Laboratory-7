import pandas as pd

def cleanStats(df):
    # Split the FG column into FGM and FGA
    df[['FGM', 'FGA']] = df['FG'].str.split('-', expand=True).astype(int)
    # Split the 3PT column into 3PM and 3PA
    df[['3PM', '3PA']] = df['3PT'].str.split('-', expand=True).astype(int)
    # Split the FT column into FTM and FTA
    df[['FTM', 'FTA']] = df['FT'].str.split('-', expand=True).astype(int)
    
    # Drop the original FG, 3PT, and FT columns
    df = df.drop(columns=['FG', '3PT', 'FT'])
    
    # Create new columns with the format <makes-attempts>
    df['FG'] = df['FGM'].astype(str) + '-' + df['FGA'].astype(str)
    df['3PT'] = df['3PM'].astype(str) + '-' + df['3PA'].astype(str)
    df['FT'] = df['FTM'].astype(str) + '-' + df['FTA'].astype(str)
    
    # Insert a blank column between FTA and FG
    df.insert(df.columns.get_loc('FTA') + 1, ' ', '')
    
    return df

def main():
    """Creates the data frame and outputs the cleaned data."""
    frame = pd.read_csv("cleanbrogdonstats.csv")
    frame = cleanStats(frame)
    
    # Remove columns from 5th to 17th
    frame = frame.drop(frame.columns[4:17], axis=1)
    
    # Display the cleaned data in a table format
    print(frame.to_string(index=False))

if __name__ == "__main__":
    main()
