
def getRequiredData(keys, data):
    result = {}
    for item in data.items():
      if item[0] in keys:
        result[item[0]] = str(item[1])
    return result
