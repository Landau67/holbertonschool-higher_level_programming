#!/usr/bin/python3

import pickle


def serialize_and_save_to_file(filename, data):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
    except (TypeError, pickle.PickleError, AttributeError):
        raise TypeError("Object is not serializable")


def load_and_deserialize(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
