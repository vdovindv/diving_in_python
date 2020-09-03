import os
import argparse
import tempfile
import json


def get_values(i_key, storage):
    key_list = []
    value_list = []
    for record in storage:
        for key, value in record.items():
            if key == i_key:
                value_list.append(value)
            key_list.append(key)

    unique_keys = set(key_list)
    #print("Keys:", unique_keys)
    #print("Values:", value_list)

    key_found = False
    if i_key in unique_keys:
        key_found = True

    return key_found, value_list



def storage(key, value=None):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    try:
        with open(storage_path, 'r') as f:
            #File exists
            data = json.load(f)
    except FileNotFoundError:
        #Storage file is not created yet
        f = open(storage_path, 'w+')
        f.close()
        data = None


    if value is None:
        if data is None:
            return None
        else:
            key_found, value_list = get_values(key, data)
            if key_found:
                return value_list
                #print(", ".join(value_list))
            else:
                return None
    else:
        if data is None:
            data = [{key:value}]
        else:
            data.append({key:value})
        with open(storage_path, 'w+') as f:
            #print(data)
            json.dump(data, f)


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Data storage')
    parser.add_argument(
        '--key',

        default=None,
        help='provide an integer (default: None)'
    )
    parser.add_argument(
        '--value',

        default=None,
        help='provide an integer (default: None)'
    )
    args = parser.parse_args()
    if args.value is None:
        value_list = storage(args.key)
        if value_list is not None:
            print(', '.join(str(i) for i in value_list if i is not None))
        else:
            print(None)
    else:
        storage(args.key, args.value)
    #print(my_namespace.key, my_namespace.value)