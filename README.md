# scrapy-nepse
A simple crawler for NEPSE based on scrapy.

You can find the documentation for scrapy here.
https://docs.scrapy.org/en/latest/

#Prerequisites
You need to have Python as well as scrapy installed in your system.

#Usgae
1. Open CMD on that folder and run "scrapy crawl nepse".
2. The json files will be outputed under historical-prices folder.

#If you get error while installing scrapy for twisted package on windows

Go to https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted and download the version for your system. I was using python 3.9 on 64bit windows so I used "Twisted‑20.3.0‑cp39‑cp39‑win_amd64.whl"

After downloading go to the directory and run
pip install Twisted‑20.3.0‑cp39‑cp39‑win_amd64.whl

After that install scrapy
pip install scrapy
