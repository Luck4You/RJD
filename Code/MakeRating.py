import pandas as pd
import numpy as np

# Загрузите файл с данными
file_path = 'data/data(main).xlsx'

car_df = pd.read_excel(file_path, sheet_name="Справочник")
telematics_df = pd.read_excel(file_path, sheet_name="Телематика")
trip_sheet_df = pd.read_excel(file_path, sheet_name="Путевой лист")

def Make_Car_Ratio(df_with_car, df_with_data_tel, df_with_data_trip):
    new_df_car = pd.DataFrame(columns=['ID транспорта',
                                          'Наименование полигона',
                                          'Полигон',
                                          'Наименование структурного подразделения',
                                          'Тип закрепления',
                                          'Номерной знак ТС',
                                          'Данные телематики, пробег',
                                          'Данные путевых листов, пробег',
                                          'Штрафы',
                                          'Манера вождения',
                                          'Общий рейтинг',])
    
    return df_with_car





# car_df = Make_Car_Ratio(car_df,telematics_df,trip_sheet_df)
pivot_table = car_df.pivot_table(index=['Наименование полигона', 'Наименование структурного подразделения'], values='ID транспорта', aggfunc='sum')
print(pivot_table)
for index, row in pivot_table.itterows():
    print[row['Наименование полигона']]
