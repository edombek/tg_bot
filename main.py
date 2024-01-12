#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 18:14:01 2024

@author: edombek
"""
import json
import telebot
from telebot.handler_backends import BaseMiddleware
import glob
from pathlib import Path

telebot.apihelper.ENABLE_MIDDLEWARE = True
config = json.load(open('config.json'))
bot = telebot.TeleBot(config['token'])

users_cmd = {}
'''
cmds = {
        'part1':{
            'desc':'description',
            'cmds':{'cmd1':'description'}
                }
        }
'''
cmds = {}

for modulefile in glob.glob('modules/*.py'):
    print(f'load: {modulefile}')
    exec(Path(modulefile).read_text())
print('done!')

@bot.message_handler()
def send_reply(msg):
    bot.reply_to(msg, f'Команда "{msg.text}" не найдена')

bot.infinity_polling()