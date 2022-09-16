import pprint

if __name__ == "__main__":
    #  a ---> c
    #  |      |
    #  v      v
    #  b <--- e
    #  |
    #  v
    #  d <--- f
    
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": [],
        "e": ["b"],
        "f": ["d"]
    }
    print('graphs algorithm implementation')