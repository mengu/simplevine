# -*- coding: utf8 -*-

import requests
import re


def get_vine_id(url):
    results = re.findall('http(?:s?):\/\/(?:www\.)?vine\.co\/v\/([a-zA-Z0-9]{1,13})', url)
    if len(results) == 0:
        return False
    return results[0]


def dump(url):

    vine_id = get_vine_id(url)
    if not vine_id:
        raise ValueError("invalid vine URL")

    response = requests.get(url)

    if not response.status_code == 200:
        raise ValueError("invalid vine URL.")

    data = response.text

    sender = re.search('<meta property="twitter:title" content="(.*?)\'s post on Vine">', data).group(1)
    sender_avatar = re.search('<img src="(.*?)" class="avatar">', data).group(1)

    title = re.search('<meta property="twitter:description" content="(.*?)">', data).group(1)
    thumbnail = re.search('<meta property="og:image" content="(.*?)">', data).group(1)
    mp4_stream = re.search('<meta property="twitter:player:stream" content="(.*?)">', data).group(1)

    tags = []
    if '#' in title:
        tags = re.findall('\#[\w]{1,}', title)

    for index, value in enumerate(tags):
        tags[index] = value.strip()

    return {
        'sender': {
            'name': sender,
            'avatar': sender_avatar,
        },
        'tags': tags,
        'title': title,
        'thumbnail': thumbnail,
        'mp4_stream': mp4_stream,
        'id': vine_id,
    }
