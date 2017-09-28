# Media References Bot for Telegram

Simple bot that uses predefined keywords and links media related to those keywords in Telegram. Particularly, I use it to share Simpsons references with my friends. For example: Someone in the group says something about communism, I'd reply: "homer communist", the bot would search for this reference and return the full quote: "My homer is not a communist..." and the media reference, in this case [this YouTube video](https://www.youtube.com/watch?v=HDss0Up7Fko)

You can configure this bot to use any reference you want. All you have to do is.

## Pre-requisites

Install **Python**

```
$ apt-get install python
```

Install **pip**. Recommended tool to install Python packages.

```
$ apt-get install python-pip
```

Install **Virtualenv**. An easy way to run Python applications on independent environments.
```
$ pip install virtualenv
```

Create bot directory and go there
```
$ mkdir references_bot
$ cd references_bot
```

Setup **virtualenv**
```
$ virtualenv venv
$ . venv/bin/activate
```

## Bot Setup

#### Step 1: Clone the repo

```
$ git@github.com:Elielmau/references_bot.git
```

#### Step 2: Setup the config file

* Duplicate the config file.

```
$ cp default_config.py my_config.py
```

*You may just use default_config.py and change its content.*

* Iside **my_config.py**.
  * Add your Telegram API key to ```api_key```.
  * Change the standard messages ```console_start_message```, ```start_message```, ```help_response```, if you'd like to.
  * Change ```references``` to your references, make sure you follow the format. You can use [this doc](https://docs.google.com/spreadsheets/d/1325sJKAzhlmJD9wmoRH-qyZoE2xWaodVz1kVzir9jh8/edit?usp=sharing) to help you format the references.

* Change the config environment variable to point to your config file.

```
$ export BOT_CONFIG=my_config
```

#### Step 3: Run the bot.

```
$ python references_bot.py
```

#### Step 4: Start talking with the bot

And enjoying the references.

## Authors

* Eliel Parra - <elielparra@gmail.com>

## Acknowledgments

This bot was built using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot). Thank you, guys!

## License

This project is licensed under MIT License.