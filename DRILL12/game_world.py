#game world

objects = [[],[]]

def add_object(o,depth):
    objects[depth].append(o)

def remove_object(o,depth):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            del o

def all_objects():
    for layer in objects:
        for o in layer:
            yield o