import json
import config


def main():
    with open(config.JSON_SUB_FILE, 'r', encoding=config.JSON_SUB_FILE_ENCODING) as f:
        data = json.load(f)
        stations_closed = []
        for one in data:
            if one['ObjectStatus'] == 'временно закрыт':
                stations_closed.append(one['NameOfStation'])
        print('Временно закрыты эскалаторы на станциях:')
        for one in set(stations_closed):
            print(one)


if __name__ == "__main__":
    main()
