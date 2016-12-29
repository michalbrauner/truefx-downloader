import errno
from truefx import manager

truefx_username = 'xxx'
truefx_password = 'xxx'

destination_folder = 'c:\\data\\'

year = 2016
symbol = 'eurusd'

truefxManager = manager.Manager()

if truefxManager.login_to_true_fx(truefx_username, truefx_password):
    print("Successfully logged to TrueFx")

    try:
        truefxManager.download_and_merge_to_one_file(year, symbol, destination_folder + symbol + '\\')

    except OSError as e:
        if e.errno == errno.EEXIST:
            print(e.strerror)
        else:
            raise e
else:
    print("Can't login to TrueFx")
