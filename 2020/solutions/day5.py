seats = []
seat_vals = []
with open('day5.txt') as f:
    rows = list(range(128))
    cols = list(range(8))
    for line in f.readlines():
        front = 1
        back = len(rows)
        pointer_r = 0

        frontc = 1
        backc = len(cols)
        pointer_c = 0
    
        for c in line:
            if c == 'F':
                back = front + (back - front) // 2
                pointer_r = front
            if c == 'B':
                front = back - (back - front) // 2
                pointer_r = back
            if c == 'L':
                backc = frontc + (backc - frontc) // 2
                pointer_c = frontc
            if c == 'R':
                frontc = backc - (backc - frontc) // 2
                pointer_c = backc
        # mid -= 1
        # midc -= 1
        # seat_vals.append((mid, midc))
        seats.append((pointer_r - 1) * 8 + (pointer_c - 1))

print(max(seats))

list.sort(seats)
prev = seats[0]
for seat in seats:
    if seat - prev > 1:
        print(seat - 1)
    prev = seat

# for seat in seat_vals:
    # print(seat)