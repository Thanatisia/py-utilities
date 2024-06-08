"""
Unit Test for type functins
"""
import os
import sys
from pyutils.libraries.types.dict import key_lookup

def unittest():
    dict_obj = {
        "Hello" : {
            "World" : "Yes"
        },
        "Hello-2" : "String Yes",
        "Hello-3" : {
            "Hello-4" : {
                "Hello-5" : "No"
            }
        }
    }
    print(key_lookup(dict_obj, ["Hello", "World"], "Hello-2", "Hello-3", ["Hello-3", "Hello-4", "Hello-5"]))

if __name__ == "__main__":
    unittest()

