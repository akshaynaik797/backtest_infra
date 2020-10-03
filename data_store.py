import sqlite3
from datetime import datetime
import pandas as pd


class SqliteStore:
    """
    class for sqlite connection and other operations
    """

    def __init__(self, dbname):
        """
        :param dbname: name of the db file with extension
        """
        self.dbname = dbname

    def get_data(self, instrument, from_date, to_date):
        """
        :param instrument: Name of the instrument
        :param from_date: starting date
        :param to_date: end date
        :return: pandas dataframe
        """
        pass

    def list_symbols(self):
        """
        :return: list of available symbols in db
        """
        pass

    def get_date_range(self, instrument):
        """
        :param instrument: Name of the instrument
        :return: range of date of stored data for instrument
        """
        pass

    def put_data_from_csv(self, csv_filename):
        """
        pull data from csv and save to db
        :param csv_filename:
        :return:
        """
        csv_file_df = pd.read_csv(csv_filename)
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
        temp_dict = {value: key for key, value in temp_dict.items()}
        result_df.rename(columns=temp_dict, inplace=True)
        with sqlite3.connect(self.dbname) as con:
            for index, row in result_df.iterrows():
                cur = con.cursor()
                row_date = datetime.strptime(row['date'], "%d-%b-%Y")
                b = f"insert into prices values ('{row['instrument']}', '{row_date}', '{row['open']}'," \
                    f" '{row['high']}', '{row['low']}', '{row['close']}', '{row['volume']}')"
                cur.execute(b)
