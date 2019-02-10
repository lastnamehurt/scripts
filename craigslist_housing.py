from __future__ import unicode_literals

import os
import sys

import schedule
from craigslist import CraigslistHousing
from slackclient import SlackClient


class CLBot(object):

    def __init__(self):
        self.slack = SlackClient(os.environ.get('SLACK_TOKEN'))
        self.rental_ids = set()

    def post_message(self, channel, text, username='CLBOT'):
        self.slack.api_call("chat.postMessage", channel=channel, text=text, username=username, unfurl_links="true")

    def reminder_find_housing(self, channel=''):
        """
        channel: id or channel name
        reminder for craigslist housing
        :return:
        """
        if not channel:
            raise KeyError("Must include a channel or the notification wont send")
        rentals = self.find_housing()
        for rental in rentals:
            self.post_message(channel, rental)

    def find_housing(self, price='2500', location='', cat='hhh', private=True):
        rentals = CraigslistHousing(site='sfbay', area=location, category=cat,
                                    filters={'max_price': price, 'private_room': private})
        houses = rentals.get_results(sort_by='newest', geotagged=True)
        count = 0
        responses = []
        for house in houses:
            res_map = {
                "name": house['name'] if house['name'] else '',
                "url": house['url'] if house['url'] else '',
                "price": house['price'] if house['price'] else '',
                "location": house['where'] if house['where'] else '',
            }
            rental_id = filter(lambda x: x.isdigit(), res_map['url'])
            if rental_id not in self.rental_ids:
                self.rental_ids.add(int(rental_id))
                bot_response = {
                    "attachments": [
                        {
                            "fallback": "Craigslist SF",
                            "color": "#36a64f",
                            "title": res_map['name'],
                            "title_link": res_map['url'],
                            "text": res_map['price'],
                            "fields": [
                                {
                                    "title": res_map['location']
                                }
                            ],
                            "footer": "Craigslist"}
                    ]
                }
                responses.append(bot_response)
                count += 1
                if count > 25: break
        return responses


if __name__ == '__main__':
    bot = CLBot()
    schedule.every(20).minutes.do(bot.reminder_find_housing, channel='craigslist_slack_channel')
    while True:
        try:
            schedule.run_pending()
        except KeyboardInterrupt:
            sys.exit()
