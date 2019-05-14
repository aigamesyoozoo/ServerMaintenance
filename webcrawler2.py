''' Description: Download the latest server log file over HTTP'''
 
from urllib import request
import datetime

def download_latest_server_log():
    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
    filename = "snmp_" + yesterday.strftime('%y-%m-%d') + ".csv"
    url = site + filename
    request.urlretrieve(url, filename)
    print('Download complete')

site = ""
download_latest_server_log()