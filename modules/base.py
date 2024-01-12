#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 18:08:21 2024

@author: edombek
"""

cmds['Базовые команды'] = {'desc':'description',
                           'cmds':{}}
cmdspart = cmds['Базовые команды']

@bot.middleware_handler(update_types=['message'])
def new_message(bot, msg):
    if msg.content_type == 'text':
        users_cmd[f'{msg.chat.id}_{msg.chat.username}'] = {'cmd':msg.text, 'env':{}}

cmdspart['cmds']['/help'] = 'Вывод справки бота'
@bot.message_handler(commands=['start', 'help'])
def send_help(msg):
    helpstr = ''
    for partname in cmds:
        helpstr += f'{partname}({cmds[partname]["desc"]}):\n'
        for cmdname in cmds[partname]['cmds']:
            helpstr += f' - {cmdname}: {cmds[partname]["cmds"][cmdname]}'
    bot.reply_to(msg, helpstr)