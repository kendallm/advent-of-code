package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func part1(lines []string) {
	depth, pos := 0, 0

	for _, line := range lines {
		direction, dist := parseLine(line)

		switch direction {
		case "forward":
			pos += dist
		case "up":
			depth -= dist
		default:
			depth += dist
		}
	}

	fmt.Println(depth * pos)
}

func part2(lines []string) {
	pos, depth, aim := 0, 0, 0
	for _, line := range lines {
		direction, dist := parseLine(line)

		if direction == "forward" {
			pos += dist
			depth += dist * aim
		} else if direction == "up" {
			aim -= dist
		} else {
			aim += dist
		}
	}

	fmt.Println(depth * pos)
}

func parseLine(line string) (string, int) {
	cmd := strings.Split(line, " ")
	direction := cmd[0]
	dist, _ := strconv.Atoi(cmd[1])
	return direction, dist
}

func main() {
	data, _ := os.ReadFile("2021/input/input_2.txt")
	file_content := string(data)
	lines := strings.Split(file_content, "\n")
	lines = lines[:len(lines)-1]

	part1(lines)
	part2(lines)
}
