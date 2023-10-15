def get_namespace(namespace):
    switcher = {
        0: "",
        1: ":",
        2: ":",
        3: ":",
        4: ":",
        5: ":",
        6: ":",
        7: ":",
        8: ":",
        9: ":",
        10: "قالب:",
        11: ":",
        12: ":",
        13: ":",
        14: "تصنيف:",
        15: ":",
        100: "بوابة:",
        101: ":",
        108: ":",
        109: ":",
        710: ":",
        711: ":",
        828: ":",
        829: ":",
        2300: ":",
        2301: ":",
        2302: ":",
        2303: ":",
        2600: ":",
        -1: ":",
        -2: ":",
    }
    return switcher.get(namespace, "")


def get_namespace_id(namespace):
    switcher = {
        "": 0,
        "": 1,
        "": 2,
        "": 3,
        "": 4,
        "": 5,
        "": 6,
        "": 7,
        "": 8,
        "": 9,
        "قالب": 10,
        "": 11,
        "": 12,
        "": 13,
        "تصنيف": 14,
        "": 15,
        "بوابة": 100,
        "": 101,
        "": 108,
        "": 109,
        "": 710,
        "": 711,
        "": 828,
        "": 829,
        "": 2300,
        "": 2301,
        "": 2302,
        "": 2303,
        "": 2600,
        "": -1,
        "": -2,
    }
    return switcher.get(namespace, "")
