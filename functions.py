def match_from_array(data: str, array) -> bool:
    out = False
    for x in array:
        if x == data:
            out = True
        if out:
            return True
        else:
            return False

