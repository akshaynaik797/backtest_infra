from data_store import SqliteStore

temp = SqliteStore('data.db')
a = temp.get_data("USDINR 280920", "2020-09-01 00:00:00", "2020-09-10 00:00:00")
pass