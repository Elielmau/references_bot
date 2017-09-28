#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Telegram bot token. This bot won't work until you provide a valid API key
api_key = ''

# Bot general messages
console_start_message = "Bot running, talk to it at Telegram"
start_message = "Hello! I'm here to help you displaying the references to your favorites movies, shows, etc."
help_response = "To change the configuration, create a new configuration file and load it using 'BOT_CONFIG' env var"

# Example references eferences
references = (
	(u"be back","I'll be back",'https://www.youtube.com/watch?v=SZdVWKM1ILs'),
	(u"can't refuse","I'm gonna make him an offer he can't refuse",'https://www.youtube.com/watch?v=SeldwfOwuL8'),
	(u"your father","No, I am your father",'https://www.youtube.com/watch?v=_lOT2p_FCvA&t=64'),
	)