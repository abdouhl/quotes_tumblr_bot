import json
import os
import random
import pytumblr
from os import listdir, remove
import urllib.request
from supabase import create_client, Client
import sys
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '.env'))
# Authenticate via OAuth 
client = pytumblr.TumblrRestClient(os.environ.get("QUOTES_TUMBLR_BOT_CONSUMER_KEY"),os.environ.get("QUOTES_TUMBLR_BOT_CONSUMER_SECRET"),os.environ.get("QUOTES_TUMBLR_BOT_OAUTH_TOKEN"),os.environ.get("QUOTES_TUMBLR_BOT_OAUTH_SECRET")) 


def create_image_link():
	supabase: Client = create_client(os.environ.get("SUPABASE_URL"),os.environ.get("SUPABASE_KEY"))
	quote_kkey = random.choice(range(0,200000))
	data =supabase.table("quotes").select('*').eq('lang','en').range(quote_kkey,quote_kkey+1).execute().data
	title = data[0]['text']
	author_name = data[0]['username']
	quote_key = data[0]['key']
	auth = author_name.lower()
	quote_image_link = os.environ.get("URLL")+str(quote_key)
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    filename = join(dirname(__file__), 'img.png')
    product_img_url = quote_image_link
    urllib.request.urlretrieve(product_img_url, filename)
    image = join(dirname(__file__), 'img.png')
    tags=[f"{auth}","quotes", "sayings","relatable quotes","relationship", "love quotes","love","quotes", "relationship quotes","life quotes","feelings", "quote","emotions"]
    site_url = "https://www.quotesandsayings.net/quotes/"+author_name
    client.create_photo('quotesandsayings-net', state="published", tags=tags,
                    tweet=title,
                    caption=f""f'<a href="{site_url}">{author_name.title()} quote:{title}</a>',
                    data=image)
      






create_image_link()


