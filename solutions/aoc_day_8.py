from textwrap import wrap
from math import inf
from collections import Counter


def part_two(layers):
    output = [2] * 25 * 6
    idx = 0
    for layer in layers:
        for pixel in layer:
            if pixel != 2 and output[idx] == 2:
                output[idx] = pixel
            idx += 1
        idx = 0
    output = wrap(''.join(str(x) for x in output), 25)
    for line in output:
        print(" ".join(line))
        
    
def part_one(layers):
    minimum = inf
    layer_num = 0
    minimum_layer = inf
    for layer in layers:
        counter = Counter(layer)
        if(counter[0] < minimum):
            minimum = counter[0]
            minimum_layer = layer_num
        layer_num += 1

    counter = Counter(layers[minimum_layer])
    print(counter[1] * counter[2])



def get_layers():
    with open('../input/input_8.txt') as f:
        input = wrap(f.readline(), 25)

    x = 0
    y = 0  

    layers = []
    layer = []
    for line in input:
        for point in range(len(line)):
            pixel = int(line[point])
            layer.append(pixel)
            x += 1
        if y == 5:
            layers.append(layer.copy())
            layer = []
        y = (y + 1) % 6
        x = 0
    return layers

if __name__ == "__main__":
    layers = get_layers()
    part_one(layers)
    part_two(layers)