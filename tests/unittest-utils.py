"""
Unit Test - utils
"""
from pyutils.libraries.utils import progressbar

def unittest():
    tasks:list = [
        {
            "function" : os.getenv,
            "arguments" : ["HOME"]
        },
        {
            "function" : print,
            "arguments" : ["Hello World"]
        },
        {
            "function" : print,
            "arguments" : ["Hello World"]
        },
    ]
    res = progressbar_decorator(tasks)
    print("Results: {}".format(res))

if __name__ == "__main__":
    unittest()
