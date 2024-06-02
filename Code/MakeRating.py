import pandas as pd
import numpy as np
import csv

file_path = 'data/dataset(first).xlsx'

car_df = pd.read_excel(file_path)
first_df = pd.read_excel(file_path)

def chettam(path):
    #смена форматирования
    read_file = pd.read_excel(path)

    read_file.to_csv ("dataset.csv",
                    encoding='utf-8', 
                    index = None, 
                    header = True) 

    #открываем csv 
    dataset_file = open("dataset.csv", "r", encoding = "utf-8")
    reader = csv.reader(dataset_file)
    writer_file = open("dataset2.csv", "w", encoding = "utf-8")
    writer = csv.writer(writer_file)

    mileage_travel = open("out/mileage_travel.csv", "w", encoding = "utf-8")
    writer_mileage_travel = csv.writer(mileage_travel)
    mileage_telematics = open("out/mileage_telematics.csv", "w", encoding = "utf-8")
    writer_mileage_telematics = csv.writer(mileage_telematics)
    mileage = open("out/mileage.csv", "w", encoding = "utf-8")
    writer_mileage = csv.writer(mileage)
    base = open("out/base.csv", "w", encoding = "utf-8")
    writer_base = csv.writer(base)
    # polygon = open("out/polygon.csv", "w", encoding = "utf-8")
    # writer_polygon_satistics = csv.writer(polygon)

    full_name_polygon = ""
    name_polygon = ""
    system_name_polygon = ""
    number_car = ""
    name_department = ""
    status_car = ""
    style_driving = 0
    id_car = -1
    costyl = 0
    # list_car = []
    # list_mileage = [[[],[]], [[],[]], [[],[]]]

    for row in reader:
        writer_base_row = []
        writer_mileage_travel_row = []
        writer_mileage_telematics_row = []
        if row[0] == "" or costyl == 1 :
            # if number_car == "Б/Н":
                # if "id" + str(id_car) in list_mileage:
                #     temp1 = list_mileage.index("id" + str(id_car))
                #     if str(row[8]) in list_mileage[temp1]:
                #         temp2 = list_mileage[temp1].index(str(row[8]))
                #         list_mileage[temp1][temp2][0] = str(row[9])
                # else:
                #     list_mileage.append("id" + str(id_car))
                #     temp1 = list_mileage.index("id" + str(id_car))
                #     list_mileage[temp1].append(str(row[8]))
                #     temp2 = list_mileage[temp1].index(str(row[8]))
                #     list_mileage[temp1][temp2].append(str(row[9]), 0)
            
                writer_base_row.append("id" + str(id_car))
                writer_base_row.append(full_name_polygon)
                writer_base_row.append(name_polygon)
                writer_base_row.append(system_name_polygon)
                writer_base_row.append(number_car)
                writer_base_row.append(name_department)
                writer_base_row.append(status_car)
                writer_base_row.append(style_driving)
                # writer_base_row.append(row[8])
                # writer_base_row.append(row[9])
                # writer_base_row.append(row[10])   
                # writer_base_row.append(row[11])
                # writer_base_row.append(row[12])          
                writer_base.writerow(writer_base_row)
                costyl = 0
            # elif number_car not in list_car:
            #     writer_base_row.append("id"+str(id_car))
            #     writer_base_row.append(full_name_polygon)
            #     writer_base_row.append(name_polygon)
            #     writer_base_row.append(system_name_polygon)
            #     writer_base_row.append(number_car)
            #     writer_base_row.append(name_department)
            #     writer_base_row.append(status_car)
            #     # writer_base_row.append(row[8])
            #     # writer_base_row.append(row[9])
            #     # writer_base_row.append(row[10])   
            #     # writer_base_row.append(row[11])
            #     # writer_base_row.append(row[12])          
            #     writer_base.writerow(writer_base_row) 
                writer_mileage_travel_row.append("id"+str(id_car))
                writer_mileage_travel_row.append(number_car)
                if row[8] != "":
                    writer_mileage_travel_row.append(row[8])
                    writer_mileage_travel_row.append(row[9])  
                elif row[10] != "":
                    writer_mileage_travel_row.append(row[10])
                    writer_mileage_travel_row.append(0)  
                writer_mileage_travel.writerow(writer_mileage_travel_row)         

                writer_mileage_telematics_row.append("id"+str(id_car))
                writer_mileage_telematics_row.append(number_car)
                if row[10] != "":
                    writer_mileage_telematics_row.append(row[10])
                    writer_mileage_telematics_row.append(row[11])  
                elif row[8] != "":
                    writer_mileage_telematics_row.append(row[8])
                    writer_mileage_telematics_row.append(0)  
                writer_mileage_telematics_row.append(row[12])
                writer_mileage_telematics.writerow(writer_mileage_telematics_row)             
        else:
            if row[3] != "Номерной знак ТС":
                costyl = 1
            id_car += 1
            full_name_polygon = row[0]
            name_polygon = row[1]
            system_name_polygon = row[2]
            # list_car.append(number_car)
            number_car = row[3]
            if row[4] == "":
                name_department = "Другое"
            else:
                name_department = row[4]
            status_car = row[5]
            style_driving = row[13]
        

    dataset_file.close()    
    writer_file.close()


def Make_Car_Ratio(df_with_car):

    df_with_car["Общий рейтинг"] = np.nan

    for index, row in df_with_car.iterrows():
        ratio_dist = 0
        ratio_carefull = 0
        if row['Данные телематики, пробег'] == 0:
            ratio_dist = 0.6
        elif row['Данные путевого, пробег'] == 0:
            ratio_dist = 0
        else:
            kof_dist = row['Данные путевого, пробег']/row['Данные телематики, пробег']
            if 0.95 < kof_dist < 1.05:
                ratio_dist = 1
            elif 0.9 < kof_dist < 1.1:
                ratio_dist = 0.9
            elif 0.8 < kof_dist < 1.2:
                ratio_dist = 0.8
            else:
                ratio_dist = 0.7
        kof_carefull = row['манера вождения']
        if 6 >= kof_carefull > 5.4:
            ratio_carefull = 1
        elif 5.4 >= kof_carefull > 5.1:
            ratio_carefull = 0.9
        elif 5.1 >= kof_carefull > 4.8:
            ratio_carefull = 0.8
        else:
            ratio_carefull = 0.7
        main_ratio = ratio_dist * 0.6 + ratio_carefull * 0.4
        df_with_car.at[index,"Общий рейтинг"] = main_ratio



    return df_with_car

def Make_pol_ratio (car_table):
    pivot_table1 = car_table.pivot_table(index=['Наименование полигона', 'Наименование структурного подразделения', 'Дата'],
                                    values=['Данные телематики, пробег', 'Данные путевого, пробег'],
                                    aggfunc='sum')
    pivot_table1 = pivot_table1.reset_index()
    pivot_table2 = pivot_table1[['Наименование полигона', 'Наименование структурного подразделения', 'Дата']].copy()
    pivot_table2["Кол-во целевых"] = np.nan
    pivot_table2["Кол-во других"] = np.nan
    for index, row in pivot_table2.iterrows():
        sumcel = 0
        sumdrugoe = 0
        for index1, row1 in car_table.iterrows():
            if row1['Наименование полигона'] == row['Наименование полигона'] and row1['Наименование структурного подразделения'] == row['Наименование структурного подразделения'] and row1['Дата'] == row['Дата']:
                if row1['Тип закрепления'] == 'В целевой структуре парка':
                    sumcel += 1
                else:
                    sumdrugoe += 1
        pivot_table2.at[index, 'Кол-во целевых'] = sumcel
        pivot_table2.at[index, 'Кол-во других'] = sumdrugoe


    pivot_table3 = car_table.pivot_table(index=['Наименование полигона', 'Наименование структурного подразделения', 'Дата'],
                                    values=['манера вождения'],
                                    aggfunc='count')
    pivot_table3 = pivot_table3.reset_index()

    pivot_table3 = pivot_table3.rename(columns = {'манера вождения' : 'Кол-во выездов'})

    pivot_table4 = car_table.pivot_table(index=['Наименование полигона', 'Наименование структурного подразделения', 'Дата'],
                                    values=['Штрафы'],
                                    aggfunc='sum')
    pivot_table4 = pivot_table4.reset_index()
    pivot_table4 = pivot_table4.rename(columns = {'Штрафы' : 'Сумма штрафов'})

    pivot_table5 = car_table.pivot_table(index=['Наименование полигона', 'Наименование структурного подразделения', 'Дата'],
                                    values=['манера вождения'],
                                    aggfunc='count')
    pivot_table5 = pivot_table5.reset_index()
    pivot_table5 = pivot_table5.rename(columns = {'манера вождения' : 'Кол-во манер'})

    pivot_table6 = car_table.pivot_table(index=['Наименование полигона', 'Наименование структурного подразделения', 'Дата'],
                                    values=['манера вождения'],
                                    aggfunc='sum')
    pivot_table6 = pivot_table6.reset_index()
    pivot_table6 = pivot_table6.rename(columns = {'манера вождения' : 'Сумма манер'})

    pivot_table1['Кол-во целевых'] = pivot_table2['Кол-во целевых']
    pivot_table1['Кол-во других'] = pivot_table2['Кол-во других']
    pivot_table1['Кол-во выездов'] = pivot_table3['Кол-во выездов']
    pivot_table1['Сумма штрафов'] = pivot_table4['Сумма штрафов']
    pivot_table1['Кол-во манер'] = pivot_table5['Кол-во манер']
    pivot_table1['Сумма манер'] = pivot_table6['Сумма манер']
    pivot_table1["Общий рейтинг"] = np.nan

    for index, row in pivot_table1.iterrows():
        kof_dist = 0
        kof_cel = 0
        kof_mist = 0
        kof_maner = 0
        ratio_dist = 0
        ratio_cel = 0
        ratio_mist = 0
        ratio_maner = 0
        if row['Данные телематики, пробег'] == 0:
            ratio_dist = 0.6
        elif row['Данные путевого, пробег'] == 0:
            ratio_dist = 0
        else:
            kof_dist = row['Данные путевого, пробег']/row['Данные телематики, пробег']
            if 0.95 < kof_dist < 1.05:
                ratio_dist = 1
            elif 0.9 < kof_dist < 1.1:
                ratio_dist = 0.9
            elif 0.8 < kof_dist < 1.2:
                ratio_dist = 0.8
            else:
                ratio_dist = 0.7
        if row['Кол-во целевых'] == 0:
            ratio_cel = 0.6
        elif row['Кол-во других'] == 0:
            ratio_cel = 0
        else:
            kof_cel = row['Кол-во целевых']/(row['Кол-во других']+row['Кол-во целевых'])
            if 0.95 < kof_cel < 1.05:
                ratio_cel = 1
            elif 0.9 < kof_cel < 1.1:
                ratio_cel = 0.9
            elif 0.8 < kof_cel < 1.2:
                ratio_cel = 0.8
            else:
                ratio_cel = 0.7
        if row['Кол-во выездов'] == 0:
            ratio_mist = 0.6
        elif row['Сумма штрафов'] == 0:
            ratio_mist = 1
        else:
            kof_mist = row['Сумма штрафов']/row['Кол-во выездов']
            if 0 < kof_mist < 0.005:
                ratio_mist = 1
            elif 0.9 < kof_mist < 0.005*1.1:
                ratio_mist = 0.9
            elif 0.8 < kof_mist < 0.005*1.2:
                ratio_mist = 0.8
            else:
                ratio_mist = 0.7
        if row['Кол-во выездов'] == 0:
            ratio_maner = 0.6
        elif row['Сумма штрафов'] == 0:
            ratio_maner = 1
        else:
            kof_maner = 1 - abs(((row['Сумма манер']/row['Кол-во манер'])/6))
            if 0 < kof_maner < 0.005:
                ratio_maner = 1
            elif 0.9 < kof_maner < 0.005*1.1:
                ratio_maner = 0.9
            elif 0.8 < kof_maner < 0.005*1.2:
                ratio_maner = 0.8
            else:
                ratio_maner = 0.7
        
        main_ratio = ratio_dist * 0.4 + ratio_cel * 0.3 + ratio_maner *0.15 + ratio_mist * 0.15
        pivot_table1.at[index,"Общий рейтинг"] = main_ratio
    return car_table

def MakeFirstSort(car_df):
    spavka_df = car_df.dropna(subset=['Наименование полигона'])
    first_catch = False
    car_df["ID"] = np.nan
    temp_car_df = car_df
    Car_index = 0
    for index, row in car_df.iterrows():
        if pd.isna(row['Наименование полигона']):
            car_df.at[index, "ID"] = car_df.at[index - 1, "ID"]
            car_df.at[index, "Тип закрепления"] = car_df.at[index - 1, "Тип закрепления"]
            car_df.at[index,'Наименование полигона'] = car_df.at[index - 1,'Наименование полигона']
            car_df.at[index,'Краткое наименование'] = car_df.at[index - 1,'Краткое наименование']
            car_df.at[index,'Полигон'] = car_df.at[index - 1,'Полигон']
            car_df.at[index,'Номерной знак ТС'] = car_df.at[index - 1,'Номерной знак ТС']
            car_df.at[index,'Наименование структурного подразделения'] = car_df.at[index - 1,'Наименование структурного подразделения']
            car_df.at[index,'манера вождения'] = car_df.at[index - 1,'манера вождения']
            if first_catch: 
                first_catch = not first_catch
                car_df = car_df.drop(index-1)
        else:
            first_catch = True
            car_df.at[index,'ID'] = Car_index + 1
            Car_index += 1
    return car_df

def MakeRdy(car_df):
    car_df['дата путевого листа'] = pd.to_datetime(car_df['дата путевого листа'])
    car_df['Дата сигнала телематики'] = pd.to_datetime(car_df['Дата сигнала телематики'])

    new_df = pd.DataFrame({
        'ID': car_df['ID'],
        'Дата': car_df[['дата путевого листа', 'Дата сигнала телематики']].max(axis=1),
        'Тип закрепления': car_df['Тип закрепления'],
        'Наименование полигона': car_df['Наименование полигона'],
        'Краткое наименование': car_df['Краткое наименование'],
        'Полигон': car_df['Полигон'],
        'Номерной знак ТС': car_df['Номерной знак ТС'],
        'Наименование структурного подразделения': car_df['Наименование структурного подразделения'],
        'Штрафы': car_df['Штрафы'],
        'манера вождения': car_df['манера вождения']
    })

    new_df.drop_duplicates(inplace=True)

    merged_df = new_df.merge(
        car_df[['ID', 'дата путевого листа', 'Данные путевых листов, пробег']],
        left_on=['ID', 'Дата'],
        right_on=['ID', 'дата путевого листа'],
        how='left'
    ).drop(columns=['дата путевого листа'])

    merged_df = merged_df.merge(
        car_df[['ID', 'Дата сигнала телематики', 'Данные телематики, пробег']],
        left_on=['ID', 'Дата'],
        right_on=['ID', 'Дата сигнала телематики'],
        how='left'
    ).drop(columns=['Дата сигнала телематики'])

    merged_df.rename(columns={'Дата': 'Дата', 'Данные путевых листов, пробег': 'Данные путевого, пробег', 'Данные телематики, пробег': 'Данные телематики, пробег'}, inplace=True)
    
    return merged_df


chettam(file_path)

first_df = MakeFirstSort(first_df)
first_df.to_excel("out/normalized.xlsx")
first_df = MakeRdy(first_df)
first_df.to_excel("out/WithAllData.xlsx")
first_df = Make_Car_Ratio(first_df)
first_df.to_excel("out/ForAICar.xlsx")
first_df = Make_pol_ratio(first_df)
first_df.to_excel("out/ForAiPoligons.xlsx")

print(first_df)

first_df.to_excel("test2.xlsx")

