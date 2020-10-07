from data_store import SqliteStore

temp = SqliteStore('data.db')
a = temp.get_date_range("USDINR 260620")
pass