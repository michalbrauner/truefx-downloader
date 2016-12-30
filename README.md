
## About

TrueFX downloader is a script written in Python in order to download Forex tick data from [TrueFX](http://www.truefx.com/) service.

## Usage

You can download all tick data for given year. Data are downloaded for each month, extracted and concatenated into one file.
```
python get_data_for_year_in_csv.py
```

There are some configuration variables in this script:

- `truefx_username` - username to login in TrueFX 
- `truefx_username` - password to login in TrueFX
- `destination_folder` - folder where to download data (should contain `symbol` folder)
- `year` - year for which to download data
- `symbol` - symbol for which to download data

