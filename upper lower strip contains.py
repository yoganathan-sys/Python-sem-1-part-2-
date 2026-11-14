import pandas as pd
d={'Name':['john Doe','alice Smith','BOB jones','charlie Brown']}
df=pd.DataFrame(d)
df['LowerCase']=df['Name'].str.lower()
df['UpperCase']=df['Name'].str.upper()
df['TitleCase']=df['Name'].str.title()
df['StripCase']=df['Name'].str.strip()
df['ReplacedCase']=df['Name'].str.replace('john','jonathan',case=False)
df['Contains Doe']=df['Name'].str.contains('Doe',case=False)
print(df)
