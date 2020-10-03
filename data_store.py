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
        pass
