
import numpy as np
import requests
import matplotlib.pyplot as plt
from faodata import faodownload

# Download data:
year = 2021
database_id = 'faostat'
datasets = faodownload.get_datasets(database_id)

print(datasets)
