import csv
from collections import Counter


def main():
    with open('bus_stops.csv', 'r', encoding = 'windows-1251') as f:
        fields = ['ID', 'Name', 'Longitude_WGS84', 'Latitude_WGS84', 'AdmArea', 'District', 'RouteNumbers',
        'StationName', 'Direction', 'Pavilion', 'OperatingOrgName', 'EntryState', 'global_id', 'PlaceDescription',
        'Works', 'geodata_center', 'geoarea']
        bus_stops = csv.DictReader(f, fields, delimiter =";")
        streets_list =[]
        for row in bus_stops:
            street = row['PlaceDescription'].split(',')
            if not street[0]:
                continue
            streets_list.append(street[0])
                   
        print(Counter(streets_list).most_common(5))

if __name__ == "__main__":
    main()
    