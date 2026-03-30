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