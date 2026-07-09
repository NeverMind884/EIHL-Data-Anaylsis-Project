import os
import requests
import pdfplumber
import pandas as pd
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
import json
from firecrawl import Firecrawl

session = requests.Session()

""" 
aiohappyeyeballs       2.6.1
aiohttp                3.13.4
aiosignal              1.4.0
annotated-types        0.7.0
anyio                  4.13.0
attrs                  26.1.0
beautifulsoup4         4.14.3
bs4                    0.0.2
certifi                2026.2.25
cffi                   2.0.0
charset-normalizer     3.4.6
cryptography           46.0.6
firecrawl              4.21.0
firecrawl-py           4.21.0
frozenlist             1.8.0
h11                    0.16.0
httpcore               1.0.9
httpx                  0.28.1
idna                   3.11
lxml                   6.0.2
multidict              6.7.1
mysql                  0.0.3
mysql-connector        2.2.9
mysql-connector-python 9.6.0
mysqlclient            2.2.8
nest-asyncio           1.6.0
numpy                  2.4.3
pandas                 3.0.1
pdfminer.six           20251230
pdfplumber             0.11.9
pillow                 12.1.1
pip                    23.2.1
propcache              0.4.1
pycparser              3.0
pydantic               2.12.5
pydantic_core          2.41.5
pyodbc                 5.3.0
pypdfium2              5.6.0
pypyodbc               1.3.6
PySide6_Addons         6.11.0
PySide6_Essentials     6.11.0
python-dateutil        2.9.0.post0
python-dotenv          1.2.2
requests               2.33.0
setuptools             75.1.0
shiboken6              6.11.0
six                    1.17.0
soupsieve              2.8.3
typing_extensions      4.15.0
typing-inspection      0.4.2
tzdata                 2025.3
urllib3                2.6.3
websockets             16.0
yarl                   1.23.0 
"""