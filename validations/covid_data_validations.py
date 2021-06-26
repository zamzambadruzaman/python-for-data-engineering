import os
import great_expectations as ge

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
covid_df = ge.read_csv(os.path.join(project_dir, "data/Indonesia_coronavirus_daily_data.csv"))

check_null = covid_df.expect_column_values_to_not_be_null(column='Province')
assert check_null['success'] == True, "Kolom Province tidak boleh NULL"

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

check_province_list = covid_df.expect_column_values_to_be_in_set(column='Province', value_set=list_province)
assert check_province_list['success'] == True, \
    f'Terdapat province yang tak dikenal, test result : {check_province_list}'


covid_df['Total_Cumulative'] = covid_df['Cumulative_Death'] + covid_df['Cumulative_Recovered'] \
                               + covid_df['Cumulative_Active_Case']

check_cumulative_case = covid_df.expect_column_pair_values_to_be_equal(column_A='Total_Cumulative',
                                                                       column_B='Cumulative_Case')
assert check_cumulative_case['success'] == True, f'Data Kumulatif Invalid, test result : {check_cumulative_case}'