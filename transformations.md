# Drop cols
df_combined.drop(columns=['_id','lease_commence_date','street_name','block', 'flat_model'], inplace=True)

# Conversions

df_combined['remaining_lease'] = df_combined['remaining_lease'].astype(str).str[:2].astype(int)
df_combined['floor_area_sqm'] = df_combined['floor_area_sqm'].astype(float)
df_combined['resale_price'] = df_combined['resale_price'].astype(float)
df_combined['month'] = pd.to_datetime(df_combined['month']).dt.year

# preprocess
df_combined['flat_type'] = df_combined['flat_type'].str.replace('MULTI-GENERATION','MULTI GENERATION')

