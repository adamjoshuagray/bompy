# bompy
A light python wrapper around the json api provided by the www.bom.gov.au for Australian weather data.
**Note that this is an unofficial api and is in no way supported by or affiliated with the Australian Bureau of Meteorology.**

You can either use `bompy.Client` to make cached calls or simply make direct calls with 
`get_station`, `get_station_dataframe` or `get_station_last_update`. 

For example:

```python
import bompy as bp
# Perth weather station data
station_data = bp.get_station('IDW60901.94608')
data_frame = bp.get_station_dataframe(station_data)
last_data = bp.get_station_last_update(data_frame)
last_air_temp = last_data['air_temp']
```

or

```python
import bompy as bp
client = bp.Client()
# Perth weather station data
last_air_temp = client.get_station_last_update('IDW60901.94608')
```

## Installation
```
    pip install bompy
```