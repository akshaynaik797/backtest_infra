from data_store import SqliteStore

temp = SqliteStore('data.db')
temp.put_data_from_csv('/home/akshay/Downloads/USDINR_FUTCUR_01-06-2020_30-06-2020.csv')
pass