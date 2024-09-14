import cloudscraper
import json

# Create a cloudscraper session
scraper = cloudscraper.create_scraper()

# Define the URL
url = "https://api.magickpen.com/ask"

# Define headers
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9,en-IN;q=0.8",
    "content-type": "application/json",
    "dnt": "1",
    "nonce": "0.8469722879062136",
    "origin": "https://magickpen.com",
    "referer": "https://magickpen.com/",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "secret": "IEODE9aBhM",
    "signature": "54cf77e8df46e92b10f25d35e9a617d9",
    "timestamp": "1726208648735",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
    "x-api-secret": "8B6CKEUVDZK7ESN7AM"
}

# Define payload data
payload = {
    "query": "Who is +919412094596?",
    "turnstileResponse": "0.mCW09RXI7Ww4F7pzeXh3rvjLmCMl36nwwmipN2HQp9FvUcZ2CW6ujEPTxvLTBlgBRtj21pIJ2dJGK3kCwU_X8dx5OHqNCY6U-V6lzBy3fMR8BMlgY1EN0V0TNqaFK7K7Tem_4Rm2R7Q9Zlnhww9u5jTdisO8hi70FUH72iCUGbTHLdHEil8oaEkmBzLgXlGElJWZxh-SfQNqnwgNZeiKEezCZuWtz1AtV-Ryips0am8FilKRjLkspl4FV1oiK-ovQ0dFbIf1QxlhTBCMYCPhdrGdVctiNf1JXwBa-4GjSryTW9tcRM-mpy8lumISc6YP0atzTzD-ZWK0nc56ldmVBnMgFor6lIitETm99ysDfhgjZB3BdaOQ0HegZqH5-BxNj-IIPPAg7lKwqE59hY7NnXbuszDDg5BLk0y40V40Ks5D4VatvfBwJU_u8ga54KY2vZ8D0TfqqFp4MwJmfMihcJbOYfO9kBW4yTJKZ10p_J03MRpf-zbfiSB0QRywt4xNeEeI6Mx2_eYGB_HONVJ01KmD6gWnZp9TSBsz0Ex_TU6YcvdhYhrp8mUmw7KAdhp3Ahjp33voWKd3sXiMqViNuMLzw8790dlxs1DLW5EjEoVNnjoESnzct6HRNGtmWQ9djymyStZ6-7JLRR92VcU3LRakTgI4n7arpa56Ybw1ippZ-GRtmKgzuYKD2ObkZlF5Tn-RdTTTtlBurEKvxmtIsWZhirMsr13jAtzQZ2urFZGonGBDc8uDEJNa7dZL_XwG.YzJe99n19PEv1w4aNJigwg.4f10ba3265961caf909165843e0296517f9acdcc22a4c8fd53e69ca3c816b063",
    "action": "verify"
}

# Make the POST request
response = scraper.post(url, headers=headers, json=payload)

print(response.text)
