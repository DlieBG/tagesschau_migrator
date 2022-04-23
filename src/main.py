from dotenv import load_dotenv, find_dotenv
from requests import post
from mongo import Mongo
from postgres import Postgres

load_dotenv(find_dotenv())

mongo = Mongo()
postgres = Postgres()

postgres.delete_articles()

for article in mongo.get_articles():
    postgres.insert_article(article)