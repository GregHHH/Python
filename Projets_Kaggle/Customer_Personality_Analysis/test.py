import pandas as pd

# using pandas, read the csv file called "marketing_campaign.csv"
# and store it in a variable called "df_guillaume"
df_guillaume = pd.read_csv("marketing_campaign.csv")

#remove outliers from the collumn called "Birth_Year"
# and store it in a variable called "df_guillaume_no_outliers"
df_guillaume_no_outliers = df_guillaume[df_guillaume["Birth_Year"] < 2000]

#transform values from 