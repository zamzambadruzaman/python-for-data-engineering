import os
from datetime import datetime
import glob
import great_expectations as ge
import pandas as pd

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
partition_date = datetime.today().strftime("%Y%m%d")

files = glob.glob(os.path.join(project_dir, f"output/summary_by_province_{partition_date}") + "/*.csv")
list_csv = []
for filename in files:
    df = pd.read_csv(filename)
    list_csv.append(df)
data_frame = pd.concat(list_csv)

summary_df = ge.from_pandas(data_frame)
check_unique_province = summary_df.expect_column_values_to_be_unique(column='Province')
assert  check_unique_province['success']==True, 'Kolom province tidak boleh ada duplikat!'


list_province = [
    'DKI JAKARTA'
    , 'JAWA BARAT'
    , 'JAWA TIMUR'
    , 'JAWA TENGAH'
    , 'SULAWESI SELATAN'
    , 'BANTEN'
    , 'NUSA TENGGARA BARAT'
    , 'BALI'
    , 'PAPUA'
    , 'KALIMANTAN SELATAN'
    , 'SUMATERA BARAT'
    , 'SUMATERA SELATAN'
    , 'KALIMANTAN TENGAH'
    , 'KALIMANTAN TIMUR'
    , 'SUMATERA UTARA'
    , 'DAERAH ISTIMEWA YOGYAKARTA'
    , 'KALIMANTAN UTARA'
    , 'KEPULAUAN RIAU'
    , 'KALIMANTAN BARAT'
    , 'SULAWESI TENGGARA'
    , 'LAMPUNG'
    , 'SULAWESI UTARA'
    , 'SULAWESI TENGAH'
    , 'RIAU'
    , 'PAPUA BARAT'
    , 'SULAWESI BARAT'
    , 'JAMBI'
    , 'MALUKU UTARA'
    , 'MALUKU'
    , 'GORONTALO'
    , 'KEPULAUAN BANGKA BELITUNG'
    , 'ACEH'
    , 'BENGKULU'
    , 'NUSA TENGGARA TIMUR'
]
check_province_list = summary_df.expect_column_values_to_be_in_set(column='Province', value_set=list_province)
assert check_province_list['success'] == True, \
    f'Terdapat province yang tak dikenal, test result : {check_province_list}'

zone = ['Green', 'Yellow', 'Orange', 'Red']
check_zone = summary_df.expect_column_values_to_be_in_set(column='Zone', value_set=zone)
assert check_zone['success'] == True, \
    f'Terdapat Zone yang tak dikenal, test result : {check_zone}'
