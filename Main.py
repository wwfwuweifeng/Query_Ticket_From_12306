# coding: utf-8
from query_station import station_name
from query_ticket import get_ticket

if __name__=='__main__':
    start_name=input('请输入出发城市:')
    end_name = input('请输入目标城市:')
    date=input('请输入出发日期(如：2017-01-01)')
    station=station_name()
    print('i am ok')
    tickets=get_ticket(station[start_name],station[end_name],date)
    for line in tickets:
        print(line)
