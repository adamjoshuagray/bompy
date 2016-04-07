import bompy as bp
import datetime.datetime

__author__ = 'Adam J. Gray'


class Client:
    """ A simple python client for www.bom.gov.au weather data.
    This client essentially just caches queries
    """

    def __init__(self, cache_age_seconds=600):
        """ Create a bompy client which (optionally) caches queries.

        :param cache_age_seconds: Number of seconds to keep items in the cache before forcing reloads.

        :return:
        """
        self.__cache = {}
        self.__cache_age = cache_age_seconds

    def get_station(self, station_code, clear_cache=False):
        """ Get a dict representation of all the data for a station.

        :param station_code: The code of the station that you wish to get data for.

        For example IDW60901.94608 is the code for Perth. The IDW60901 is the product part of the
        code and will typically be the same in each state, while the 94608 part of the code is a
        code which uniquely identifies the station.

        :param clear_cache: Whether to force a reload of the cache when querying.

        :return: A dict representation of the station and the weather data for that station.
        """
        if station_code not in self.__cache or clear_cache:
            station = bp.get_station(station_code)
            self.__cache[station_code] = (datetime.datetime.utcnow(), station)
        elif (datetime.datetime.utcnow() - self.__cache[station_code][0]).total_seconds() > self.__cache_age:
            station = bp.get_station(station_code)
            self.__cache[station_code] = (datetime.datetime.utcnow(), station)

        return self.__cache[station_code][1]

    def get_station_dataframe(self, station_code, clear_cache=False):
        """ Get a pandas dataframe of the weather data for a station.

        :param station_code: The code of the station that you wish to get data for.

        For example IDW60901.94608 is the code for Perth. The IDW60901 is the product part of the
        code and will typically be the same in each state, while the 94608 part of the code is a
        code which uniquely identifies the station.

        :param clear_cache: Whether to force a reload of the cache when querying.

        :return: A pandas dataframe with the weather data for the station (indexed by datetime).
        """
        station = self.get_station(station_code, clear_cache=clear_cache)
        return bp.get_station_dataframe(station)

    def get_last_update(self, station_code, clear_cache=False):
        """ Get a dict of the last weather conditions for a station.

        :param station_code: The code of the station that you wish to get data for.

        For example IDW60901.94608 is the code for Perth. The IDW60901 is the product part of the
        code and will typically be the same in each state, while the 94608 part of the code is a
        code which uniquely identifies the station.

        :param clear_cache: Whether to force a reload of the cache when querying.

        :return: A dict of the last weather conditions for a station.
        """
        df = self.get_station_dataframe(station_code, clear_cache=clear_cache)
        return bp.get_station_last_update(df)


