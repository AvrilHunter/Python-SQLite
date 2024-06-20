def list_to_dict(data, headers):
    new_dict ={}
    for i in range(0,len(headers)):
        new_dict[headers[i]] = data[i]
    return new_dict


def nested_list_to_dict(data, headers):
    response = []
    for treasure in data:
        response.append(list_to_dict(treasure, headers))
    return response
