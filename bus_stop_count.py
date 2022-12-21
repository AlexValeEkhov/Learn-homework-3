import csv
from collections import Counter
import config


def main():
    with open(config.CSV_BUS_FILE, 'r', encoding=config.CSV_BUS_FILE_ENCODING) as f:
        fields = ['ID', 'Name', 'Longitude_WGS84', 'Latitude_WGS84',
                  'AdmArea', 'District', 'RouteNumbers', 'StationName',
                  'Direction', 'Pavilion', 'OperatingOrgName', 'EntryState',
                  'global_id', 'PlaceDescription', 'Works',
                  'geodata_center', 'geoarea']
        bus_stops = csv.DictReader(f, fields, delimiter=";")
        streets_list = []
        for row in bus_stops:
            street = row['PlaceDescription'].split(',')
            if not street[0]:
                continue
            streets_list.append(street[0])
        print('Больше всего остановок на улицах:')
        print(*Counter(streets_list).most_common(config.STREETS_NUM))


if __name__ == "__main__":
    main()
