from data_store import SqliteStore

temp = SqliteStore('data.db')
a = temp.list_symbols()
pass