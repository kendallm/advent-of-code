package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func sum(lines []string) int {
	var suma int
	for _, x := range lines {
		i, _ := strconv.Atoi((x))
		suma += i
	}
	return suma
}

func part1(lines []string) {
	a, _ := strconv.Atoi(lines[0])
	inc := 0
	for _, x := range lines {
		b, _ := strconv.Atoi(x)
		if a < b {
			inc += 1
		}
		a = b
	}
	fmt.Println(inc)
}

func part2(lines []string) {
	inc := 0
	as := lines[0:3]
	suma := sum(as)
	for i := range lines {
		if i > len(lines)-3 {
			break
		}
		bs := lines[i : i+3]
		sumb := sum(bs)

		if suma < sumb {
			inc += 1
		}
		suma = sumb
	}

	fmt.Println(inc)
}

func main() {
	data, _ := os.ReadFile("2021/input/input_1.txt")
	file_content := string(data)
	lines := strings.Split(file_content, "\n")
	part1(lines)
	part2(lines)
}
