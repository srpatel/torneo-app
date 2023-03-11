import uuid


# TODO: chose a generator, ensure code is unique
def code_generator():
    return uuid.uuid4().hex
