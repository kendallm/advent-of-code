from textwrap import wrap
from math import inf
from collections import Counter
import cv2
import numpy as np


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
    print('=== Part 1 ===')
    print(counter[1] * counter[2])
    print()

def part_two(layers):
    print('=== Part 2 ===')

    output = [2] * 25 * 6
    idx = 0
    for layer in layers:
        for pixel in layer:
            if pixel != 2 and output[idx] == 2:
                output[idx] = pixel
            idx += 1
        idx = 0
    image =  255 * np.ones(shape=[6, 25, 3], dtype=np.uint8)
    output = wrap(''.join(str(x) for x in output), 25)
    black = [0, 0, 0]
    
    y = 0
    x = 0
    for line in output:
        for x in range(len(line)):
            if line[x] == '1':
                image[y, x] = black
        y += 1
    for line in output:
        print(' '.join(line))
    cv2.imshow('Decoded Image', image)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()


if __name__ == '__main__':
    layers = get_layers()
    part_one(layers)
    part_two(layers)