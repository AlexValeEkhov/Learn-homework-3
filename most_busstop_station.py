import json
import config


def busstop_check(coord_x, coord_y):  # Функция вычисляет входит ли точка с координатами остановки в радиус 500 м вокруг станции метро
    halfrad_x = 0.002250   # примерно 250 метров по широте
    halfrad_y = 0.004000   # примерно 250 метров по долготе
    check = coord_x**2/halfrad_x**2 + coord_y**2/halfrad_y**2
    if check <= 1:
        return True
    else:
        return False


def main():
    with open(config.JSON_BUS_FILE, 'r', encoding=config.JSON_BUS_FILE_ENCODING) as f:  # Открываем файл данных по остановкам
        bus_stops = json.load(f)

    with open(config.JSON_SUB_FILE, 'r', encoding=config.JSON_SUB_FILE_ENCODING) as f:  # Открываем файл данных по метро
        subwaydata = json.load(f)

    stop_per_station = {}
    for one_station in subwaydata:  # Для каждой станции метро
        stops_count = 0
        for row in bus_stops:      # берем каждую остановку
            coord_x = float(one_station['Longitude_WGS84']) - float(row['Longitude_WGS84'])  # вычислеяем координаты
            coord_y = float(one_station['Latitude_WGS84']) - float(row['Latitude_WGS84'])  # относительно станции
            check = busstop_check(coord_x, coord_y)  # передаем их в функцию
            if check:
                stops_count += 1  # считаем кол-во остановок вблизи станций
        stop_per_station[one_station['NameOfStation']] = stops_count  # записываем в словарь {станция : количество остановок}
    print("Станция с наибольшим количеством остановок в радиусе 500 м:")  # выводим станцию с максимальным кол-вом остановок
    print(f'{max(stop_per_station, key=stop_per_station.get)} - {stop_per_station[max(stop_per_station, key=stop_per_station.get)]}')


if __name__ == "__main__":  # Работает довольно долго!
    main()
