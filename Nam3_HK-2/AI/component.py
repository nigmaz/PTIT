import sys
import json
import requests
from flask import Flask, request
import config
PAT = config.PAGE_ACCESS_TOKEN


def send_message(sender_id, message_text):
    r = requests.post("https://graph.facebook.com/v3.3/me/messages",

                      params={"access_token": PAT},

                      headers={"Content-Type": "application/json"},

                      data=json.dumps({
                          "recipient": {"id": sender_id},
                          "message": {"text": message_text}
                      }))


def send_img(sender_id, url):
    r = requests.post("https://graph.facebook.com/v3.3/me/messages",

                      params={"access_token": PAT},

                      headers={"Content-Type": "application/json"},

                      data=json.dumps({
                          "recipient": {
                              "id": sender_id
                          },
                          "message": {
                              "attachment": {
                                  "type": "image",
                                  "payload": {
                                      "url": url
                                  }
                              }
                          }
                      }))
