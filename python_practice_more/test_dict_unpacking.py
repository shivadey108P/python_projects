import random

# Simulate reading keys from a set (unordered)
keys = {"accountId", "positionKey", "accountMap"}


def build_item():
    d = {}
    for k in keys:  # unordered iteration!
        if k == "accountId":
            d[k] = {"id1": 123}
        elif k == "positionKey":
            d[k] = {"pk1": 456}
        elif k == "accountMap":
            d[k] = {"outerKey": {"innerKey": {"value": "xyz"}}}
    return d


for i in range(100):
    print(list(build_item().keys()))
