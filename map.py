from decouple import config
from utils import *
import requests
import json
import time
import random
import os

auth_key = config('AUTH_KEY')
base_url = config('BASE_URL')
my_name = config('NAME')