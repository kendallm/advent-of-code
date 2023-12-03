from utils import Computer
from collections import deque, defaultdict


def main():
    with open("../input/input_11.txt") as f:
        memory = f.readline()
    output = deque()
    computer = Computer(memory, output, 2)

    position = (0, 0)
    headed = "N"
    grid = {}

    computer.add_input("1")
    computer.run()
    painted = 0
    while not computer._halted:
        if computer._paused:
            color = output.popleft()
            direction = output.popleft()
            if position not in grid:
                painted += 1
            grid[position] = color

            # print(f'direction {direction}, headed {headed}')
            if direction == 0:
                # turn left
                if headed == "N":
                    headed = "W"
                elif headed == "W":
                    headed = "S"
                elif headed == "S":
                    headed = "E"
                else:
                    headed = "N"
            else:
                # turn right
                if headed == "N":
                    headed = "E"
                elif headed == "W":
                    headed = "N"
                elif headed == "S":
                    headed = "W"
                else:
                    headed = "S"

            if headed == "N":
                position = (position[0], position[1] + 1)
            elif headed == "W":
                position = (position[0] - 1, position[1])
            elif headed == "S":
                position = (position[0], position[1] - 1)
            else:
                position = (position[0] + 1, position[1])
            # print(f'direction {direction}, headed {headed}')
            if position not in grid:
                computer.add_input("0")
            else:
                computer.add_input(grid[position])
            computer.run()
    print(painted)
    import cv2
    import numpy as np

    img = 255 * np.zeros(shape=[100, 100, 3], dtype=np.uint8)
    for k, v in grid.items():
        color = [0, 0, 0] if v == 0 else [255, 255, 255]
        img[k[1] + 50, k[0] + 50] = color
    scale_percent = 400  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    flipped = cv2.flip(resized, 0)
    cv2.imshow("Decoded Image", flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
