#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""Simple Telegram bot that looks for keywords and return media references to a movie, TV show, etc.
Created using python-telegram-bot wrapper <https://github.com/python-telegram-bot>"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import sys
import logging
import importlib

__author__ = "Eliel Parra"
__email__ = "elielparra@gmail.com"
__credits__ = ["Eliel Parra", "python-telegram-bot"]
__licence__ = "MIT"
__maintainer__ = "Eliel Parra"


# Import configuration
config_file = os.getenv('BOT_CONFIG', 'default_config')
config = importlib.import_module(config_file)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a few command handles
def start(bot, update):
	update.message.reply_text(config.start_message)
	

def help(bot, update):
	update.message.reply_text(config.help_response)

def reference(bot, update):
	reference = get_reference(update.message.text)
	if reference:
		update.message.reply_text(format_reference(reference))

def error(bot, update, error):
	logger.warn('Update "%s" caused error: "%s"' % (update, error))

# Data-processing functions
def get_reference(text):
	for reference in config.references:
		if unicode(text.lower()) == reference[0]:
			return reference
	return False

def format_reference(reference):
	return reference[1] + "\n\n" + reference[2]

# Main
def main():
	# Create the EventHandler
	if config.api_key:
		updater = Updater(config.api_key)
	else:
		logger.error('API key not provided, check your configuration file.')
		sys.exit()

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# Answers to commands
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(CommandHandler(('ayuda','help'), help))

	# Answers to non-commands
	dp.add_handler(MessageHandler(Filters.text, reference))

	# Log all errors
	dp.add_error_handler(error)

	# Start the bot
	updater.start_polling()

	# Run the bot until you press Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.
	updater.idle()


if __name__ == '__main__':
	print(config.console_start_message)
	main()