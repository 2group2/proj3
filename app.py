# library imports
from pip._vendor import requests
from urllib.request import urlretrieve
import os

# variable initialization
URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
log_file = 'http_access_log.txt'

# TODO: retrieve log file and save to machine
# (Two People)

if os.path.exists(log_file):
  retrievefile = open(log_file, "r")
else:
  print("Loading Log File...")
  log_file, headers = urlretrieve(URL_PATH, log_file, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)


# TODO: calculating requests from last SIX months
# (Two People)
# 
# should be the 326725'th log line 
# remote - - [11/Apr/1995:00:00:16 -0600] "GET 6721.gif HTTP/1.0" 200 1277
# (last line) local - - [11/Oct/1995:14:14:17 -0600] "GET index.html HTTP/1.0" 304 0
# 
# command (format "dd/mmm/yyyy") > 10/Apr/1995

last_six_month_request_counter = 0
end_date = "09/Apr/1995"

with open(log_file, 'r') as file:
  Content = file.read()
  lines = Content.split("\n")
  
  lines.reverse()
  
  for line in lines:
    if end_date in line:
      break
    else:
      last_six_month_request_counter += 1

print("Total requests from last six months", last_six_month_request_counter)
# def count_ip(ip_list):
#     return collections.Counter(ip_list)

# def read_file(counter):
#     with open('output.csv', 'r') as csvfile:
#         writer = csv.writer(csvfile)
#         header = ['IP', 'Count']
#         writer.writerow(header)
#         for item in counter:
#             writer.writerow((item, counter[item]))



# TODO: calculating TOTAL amount of requests made

# def count_ip(ip_list):
#     return collections.Counter(ip_list)

# def read_file(counter):
#     with open('output.csv', 'r') as csvfile:
#         writer = csv.writer(csvfile)
#         header = ['IP', 'Count']
#         writer.writerow(header)
#         for item in counter:
#             writer.writerow((item, counter[item]))

with open(log_file, "r") as file:
  request_total = len(file.readlines())

print("Total requests:", request_total)
print("Est. from end date to end of April 10 line", request_total-323330)
# TODO: output for marketing

# yessir