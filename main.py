from exel import writer
from functions import stroygid, profcom
import pandas as pd


writer(profcom)
excel_data_df = pd.read_excel('build.xlsx', sheet_name='products', header=None)
excel_data_df = excel_data_df.drop_duplicates(keep = "last")
excel_data_df.to_excel('Profcom_competitor.xlsx', sheet_name='Прайс', header=['Наименование', 'Цена'], index=False)

writer(stroygid)
excel_data_df = pd.read_excel('build.xlsx', sheet_name='products', header=None)
excel_data_df = excel_data_df.drop_duplicates(keep = "last")
excel_data_df.to_excel('Stroygid_competitor.xlsx', sheet_name='Прайс', header=['Наименование', 'Цена'], index=False)


