#!/usr/bin/python

from sys import stdin
from dateutil.parser import parse
from datetime import timedelta

start_date = parse("2014-11-15 00:00:00")
end_date = parse("2014-11-22 00:00:00")
cur_date = start_date
file_date = parse("2014-11-14 23:59:59")
interval = 6

print stdin.readline().strip("\r\n") #header

while cur_date <= end_date:

  while file_date < cur_date:
    line = stdin.readline()
    if line == None or line.strip("\r\n") == "":
      file_date = end_date
    else:
      line_list = line.split(',')
      file_date = parse(line_list[0])
      file_count = line_list[1]

  cur_date = cur_date + timedelta(hours=interval)

  print str(cur_date) + "," + file_count.strip("\r\n")
