# BanglapediaCrawler
Scraping Banglapedia Data

In this repository I have built a crawler for extracting all the data from [Banglapedia](https://bn.banglapedia.org) website.

I have extracted the following details:
1. Title of the article.
2. Main text body
3. Image URLs if there is any.
4. Source URL.
5. Published date of the article.
Also, I have set an ID number which is just for numbering my accessed data.

After extracting the informations I saved it into a csv file, you can also save it in a json file.
For saving a file you can write the command on your terminal:

scrapy crawl bangla -o bangladata.csv (for saving as a csv file) or scrapy crawl bangla -o bangladata.json (for saving as a json file)

Requirements:
1. [Pycharm](https://www.jetbrains.com/pycharm/) IDE to run the script
2. [Python](https://www.python.org) version 3.10
3. [scrapy](https://scrapy.org/) version 2.4.1 
