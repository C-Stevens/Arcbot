![Logo](https://user-images.githubusercontent.com/5940454/29853902-3b4a47dc-8d08-11e7-9158-31874826084c.png)

# About Arcbot
[![Python](https://img.shields.io/badge/Python-3.6-7289da.svg?style=flat-square)](https://www.python.org/downloads/release/python-360/)
[![License](https://img.shields.io/badge/License-GPL-7289da.svg?style=flat-square)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![Build Status](https://img.shields.io/travis/ns-phennessy/Arcbot.svg?style=flat-square)](https://travis-ci.org/ns-phennessy/Arcbot)

Arcbot is an extensible chatbot written entirely in Python, inspired by
[Errbot](https://github.com/errbotio/errbot) and [Hubot](https://hubot.github.com/) projects.
The goal of this project is to provide a simple to extend bot framework for [Discord](https://discordapp.com).

Batteries included:
* Simple command creation
* Hook any event from Discord
* Receive data ingress with webhooks
* Run code on a set interval
* Schedule code to be run after a time period
* Simple database interaction with MongoDB
* Intuitive Discord object mapping

Arcbot originally started out as a simple Trivia Bot that used long polling and webhooks to read and
write to chat channels. I became obsessed with making this bot more robust and at that time, no bots
existed for Discord, so this bot evolved into a fully vetted framework that I could use to build
functionality off of. This project is a place I can experiment with design ideas and evolve a sense
of personal code standards. I treat it more as an academic project to learn about new libraries and
tools available to me as Python continues to grow.
