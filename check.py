#!/bin/python3

import requests
import telebot

bot = telebot.TeleBot('7186590499:AAEGtZ_WQCsBKjtFgNJ3pGoVSssh9nzjY_M')

def check_ban(url):
    r = requests.get(url,
                     headers={
                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                         'Accept-Language': 'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
                         'Accept-Encoding': 'gzip, deflate',
                         'Connection': 'keep-alive',
                         'DNT': '1'
                     })

    if '"groups_blocked_text"' in r.text:
        print('Ban')
        bot.send_message(-4200609461, 'banned: ' + url)
    else:
        print('Ok')


with open('groups.txt', 'r', encoding='utf-8') as groups_file:
    for group in groups_file.read().split('\n'):
        check_ban(group)
