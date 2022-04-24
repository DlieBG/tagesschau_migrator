from dotenv import load_dotenv, find_dotenv
from requests import post
from mongo import Mongo
from postgres import Postgres

def print_progress_bar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()


load_dotenv(find_dotenv())

mongo = Mongo()
postgres = Postgres()

print('Altdaten werden gelöscht...', end = '\r')

postgres.delete_articles()

length = mongo.get_count()

for index, article in enumerate(mongo.get_articles()):
    postgres.insert_article(article)
    print_progress_bar(index, length, prefix = 'Fortschritt', suffix = 'migriert')

postgres.commit()
