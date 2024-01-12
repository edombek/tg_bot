#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 18:17:43 2024

@author: edombek
"""

import json

df = {}
df['token'] = [input('tg bot token:')]
df['admin_id'] = input('admin tg id:')
json.dump(df, open('config.json', 'w'))
