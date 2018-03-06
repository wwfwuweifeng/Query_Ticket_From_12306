#-*- coding: utf-8 -*-
import requests
import re


def get_ticket(start,end,date):

    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        date, start, end
    )
    text= requests.get(url, verify=False)  # 最基本的GET请求
    print(text.text)
    result= text.json()["data"]["result"]
    res = re.compile('(\|(.)+)')
    tickets=[]
    for i in range(len(result)):
        p = res.search(result[i])
        train = p.group().split('|')
        train = ['无' if x =='' else x for x in train]       #
        ticket={'train_code':train[3],'from_station':train[6],'to_station':train[7],'start_time':train[8],
                'end_time':train[9],'total_time':train[10],'business_seat':train[32],'first_seat':train[31],
                'second_seat':train[30],'hard_seat':train[29],'hard_bed':train[28],'no_seat':train[26],'soft_bed':train[23]}
        tickets.append(ticket)

    return tickets

