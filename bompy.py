__author__ = 'Adam J. Gray'

__BASE_URL = "http://www.bom.gov.au/fwo"


def get_station(station_code):
    """Get a dict representation of all the data for a station.

    :param station_code: The code of the station that you wish to get data for.

    For example IDW60901.94608 is the code for Perth. The IDW60901 is the product part of the
    code and will typically be the same in each state, while the 94608 part of the code is a
    code which uniquely identifies the station.

    :return: A dict representation of the station and the weather data for that station.
    """
    import urllib2
    import json
    product, station = station_code.split('.')
    url = '%s/%s/%s.json' % (__BASE_URL, product, station_code)
    f = urllib2.urlopen(url)
    station_dict = json.loads(f.read())
    return station_dict


def get_station_dataframe(station):
    """ Get a pandas dataframe of the weather data for a station.
    :param station: The dict representation of the station as returned by get_station.
    :return: A pandas dataframe with the weather data for the station (indexed by datetime).
    """
    import pandas as pd
    from dateutil import parser
    data = station['observations']['data']
    df = pd.DataFrame(data)
    df['local_date_time_full'] = df['local_date_time_full'].apply(parser.parse)
    df.set_index('local_date_time_full', inplace=True)
    return df


def get_station_last_update(station_dataframe):
    """ Get a dict of the last weather conditions for a station.

    :param station_dataframe: The dataframe of the data for a station as returned by get_station_dataframe.
    :return: A dict of the last weather conditions for a station.
    """
    return dict(station_dataframe.ix[0])




