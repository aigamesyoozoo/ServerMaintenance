'''Description: Download all server logs'''
 
from urllib import request
import datetime

def download_all_server_logs():
    yesterday = datetime.datetime(2019, 5, 11)
    # yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
    current = start_date 
    count = 0

    while current <= yesterday:
        filename = "snmp_" + current.strftime('%y-%m-%d') + ".csv"
        url = site + filename
        request.urlretrieve(url, filename)
        print('Downloaded', filename)
        current += datetime.timedelta(days=1)
        count += 1

    print('Download files: ', count)


site = ""
start_date = datetime.datetime(2019, 5, 10)
download_all_server_logs()