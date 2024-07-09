"""
Shadarien Williams
Contact: shadarien@shadwilliams.dev

"""
import pandas as pd
import csv
from datetime import datetime


v2_filename = '/home/shadarien/freelancing/Data_export_software_upwork/Sample Data v3/Inventory_v2.csv' 
lotV4_filename = '/home/shadarien/freelancing/Data_export_software_upwork/Sample Data v3/InventoryLot_v4.csv' 



data = []

v2_content = pd.DataFrame(pd.read_csv(v2_filename))
lotv4_content = pd.DataFrame(pd.read_csv(lotV4_filename))
print(lotv4_content)

joined_data = pd.merge(v2_content,lotv4_content, how='right', on=['product.partNumber','location.locationIdentifier','inventoryType','inventoryParentType','segment'])

joined_data.to_excel('export.xlsx')

