import json
import itertools

py_dict = json.loads(input())

def transfer_finder(dict):
    stop_list = {}
    xfer_stops = set()
    for n in dict:
        try:
            stop_list[n['stop_name']] = stop_list[n['stop_name']] + 1
        except KeyError:
            stop_list[n['stop_name']] = 1

    for i in stop_list:
        if stop_list[i] > 1:
            xfer_stops.add(i)
    return xfer_stops


def stopcheck(dct):
    print("On demand stops test:")
    s_stops = set()
    o_stops = set()
    f_stops = set()
    t_stops = transfer_finder(dct)
    error_stops = set()

    for n in itertools.chain(dct):
        if n['stop_type'] == "S":
            s_stops.add(n['stop_name'])
        elif n['stop_type'] == "F":
            f_stops.add(n['stop_name'])
        elif n['stop_type'] == "O":
            o_stops.add(n['stop_name'])

    check_stops = s_stops | f_stops | t_stops

    for n in itertools.chain(dct):
        if (n['stop_name'] in check_stops) and n['stop_name'] in o_stops:
            error_stops.add(n['stop_name'])

    print(f"Wrong stop type: {sorted(error_stops)}")
    if len(error_stops) == 0:
        return "OK"
    else:
        return ""


print(stopcheck(py_dict))
