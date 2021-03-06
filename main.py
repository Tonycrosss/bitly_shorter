import requests
import os
from dotenv import load_dotenv
import argparse


class WrongLinkException(Exception):
    pass


def make_short_link(token, long_link):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
      "Authorization": f"Bearer {token}"
      }
    payload = {
      "long_url": f"{long_link}"
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.ok:
        short_link = response.json()['id']
    else:
        raise WrongLinkException("Wrong Link was written!")
    return short_link


def bitlink_clicks(token, bitlink):
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    headers = {
      "Authorization": f"Bearer {token}"
      }
    payload = {
      "units": -1,
      "unit": "month"
    }
    response = requests.get(url, headers=headers, json=payload)
    if response.ok:
        total_clicks = response.json()['total_clicks']
    else:
        raise WrongLinkException("Wrong Link was written!")
    return total_clicks


def is_bitlink(token, link):
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{link}"
    headers = {
      "Authorization": f"Bearer {token}"
      }
    response = requests.get(url, headers=headers)
    return response.ok


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--link', '-l', type=str, help='Enter link to make it short',
                        required=True)
    args = parser.parse_args()
    return args


def main():
    load_dotenv()
    args = parse_args()
    token = os.getenv("TOKEN")
    link = args.link
    if is_bitlink(token, link):
        total_clicks = bitlink_clicks(token, link)
    else:
        bitlink = make_short_link(token, link)
        total_clicks = bitlink_clicks(token, bitlink)
        print(bitlink)
    print(f"Количество кликов на битли: {total_clicks}")


if __name__ == '__main__':
    main()
