import pandas as pd

csv_file_df = pd.read_csv('/home/akshay/Downloads/USDINR_FUTCUR_01-06-2020_30-06-2020.csv')
csv_df_fields = list(csv_file_df.columns)
fields = {
            "instrument": ['Underlyings'],
            "date": ['Trade Date'],
            "open": ['Open Price'],
            "high": ['High Price'],
            "low": ['Low Price'],
            "close": ['Close Price'],
            "volume": ['No. of Contracts'],
        }
temp_list, temp_dict = list(), dict()
for index, field in enumerate(csv_df_fields):
    for key, value in fields.items():
        if field in value:
            temp_dict[key] = index
            temp_list.append(csv_df_fields[index])
for key, value in temp_dict.items():
    temp_dict[key] = csv_df_fields[value]
result_df = csv_file_df[temp_list]
df_fields = list(result_df.columns)
fields_keys = list(fields.keys())
temp_dict = {value:key for key,value in temp_dict.items()}
result_df.rename(columns=temp_dict, inplace=True)
for index, row in result_df.iterrows():
    print(row['open'], row['close'])
pass