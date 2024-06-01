import pandas as pd
import numpy as np

# Загрузите файл с данными
file_path = 'data/dataset.xlsx'

car_df = pd.read_excel(file_path, sheet_name="Справочник")
telematics_df = pd.read_excel(file_path, sheet_name="Телематика")
trip_sheet_df = pd.read_excel(file_path, sheet_name="Путевой лист")

def Make_Car_Ratio(df_with_car, df_with_data_tel, df_with_data_trip):
    Df_With_Ratio = pd.DataFrame(columns=['ID транспорта',
                                          'Номерной знак ТС',
                                          'Наименование полигона',
                                          'Полигон',
                                          'Наименование структурного подразделения',
                                          'Тип закрепления',
                                          'Данные телематики, пробег',
                                          'Данные путевых листов, пробег',
                                          'Отклонение пробега',])
    # df_with_car.insert(-1, 'Рейтинг пробега', None)
    df_with_car["Рейтинг пробег"] = np.nan
    df_with_car["Рейтинг рейтинг штрафов"] = np.nan
    df_with_car["Рейтинг манера вождения"] = np.nan

    for index, raw in df_with_car.iterrows():
        Sum_tel_way_dist = 0
        Sum_trip_way_dist = 0
        Sum_tel_penalty = 0
        for indextel, rawtel in df_with_data_tel.iterrows():
            if raw['ID транспорта'] == rawtel['ID транспорта']:
                Sum_tel_way_dist += rawtel['Данные телематики, пробег']
                Sum_tel_penalty += rawtel['Штрафы']
            
        for indextrip, rawtrip in df_with_data_trip.iterrows():
            if raw['ID транспорта'] == rawtrip['ID транспорта']:
                Sum_trip_way_dist += rawtrip['Данные путевых листов, пробег']

        Car_Ratio = 0
        if Sum_tel_way_dist == 0 or Sum_trip_way_dist == 0:
            rate_car = 0,6
        else:
            Car_Ratio = Sum_trip_way_dist / Sum_tel_way_dist
            if Car_Ratio >= 1:
                Car_Ratio = 1 - Car_Ratio
            else:
                Car_Ratio = abs(Car_Ratio - 1)
            if (Car_Ratio < 1.05): rate_car = 1
            elif (Car_Ratio < 1.1): rate_car = 0.8
            elif (Car_Ratio < 1.2): rate_car = 0.7
            else: rate_car = 0.6
        
        raw['Рейтинг пробега'] = rate_car
        
        rate_carefull = 0.6
        Car_Carefull = raw['манера вождения']
        if Car_Carefull > 5.4: rate_carefull = 1
        if Car_Carefull > 5.1: rate_carefull = 0.9
        if Car_Carefull > 4.8: rate_carefull = 0.8
        if Car_Carefull == 0: rate_carefull = 0
        else: rate_carefull = 0.7
        raw['Рейтинг манера вождения'] = rate_carefull

        raw['Рейтинг рейтинг штрафов'] = Sum_tel_penalty
        print (f"Сделано {index} из {df_with_car.shape[0]}")
    return df_with_car





car_df = Make_Car_Ratio(car_df,telematics_df,trip_sheet_df)
pivot_table = car_df.pivot_table(index=['Наименование полигона', 'Наименование структурного подразделения'], values='Рейтинг рейтинг штрафов', aggfunc='mean')
print(pivot_table)

