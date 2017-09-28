# Media References Bot for Telegram

Simple bot that uses predefined keywords and links media related to those keywords in Telegram. Particularly, I use it to share Simpsons references with my friends. For example: Someone in the group says something about communism, I'd reply: "homer communist", the bot would search for this reference and return the full quote: "My homer is not a communist..." and the media reference, in this case [this YouTube video](https://www.youtube.com/watch?v=HDss0Up7Fko)

You can configure this bot to use any reference you want. All you have to do is.

## Pre-requisites

Install **Python**

```bash
$ apt-get install python
```

Install **pip**. Recommended tool to install Python packages.

```bash
$ apt-get install python-pip
```

Install **Virtualenv**. An easy way to run Python applications on independent environments.
```bash
$ pip install virtualenv
```

Create bot directory and go there
```bash
$ mkdir references_bot
$ cd references_bot
```

Setup **virtualenv**
```bash
$ virtualenv venv
$ . venv/bin/activate
```

## Bot Setup

#### Step 1

Clone the repo.

```bash
$ git@github.com:Elielmau/references_bot.git
```

#### Step 2

Duplicate the config file.

```bash
$ cp default_config.py my_config.py
```

*You may just use default_config.py and change its content.*

#### Step 3

* Open **my_config.py** and add your Telegram API key to ```api_key```.
* Change the standard messages if you's like to.
* Change ```references``` to your references, make sure you follow the format. You can use [this doc](https://docs.google.com/spreadsheets/d/1325sJKAzhlmJD9wmoRH-qyZoE2xWaodVz1kVzir9jh8/edit?usp=sharing) to help you format the references.

#### Step 4

Change the config environment variable to point to your config file.

```bash
$ export BOT_CONFIG=my_config
```

#### Step 5

Run the bot.

```bash
$ python references_bot.py
```

#### Step 6

Start talking with the bot and enjoying the references.

## Authors

* Eliel Parra - <elielparra@gmail.com>

## Acknowledgments

This bot was built using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot). Thank you, guys!

## License

This project is licensed under MIT License.