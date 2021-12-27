package main

import (
	"os"
	"strings"
)

type bingoCard struct {
	nums map[int]struct{ x, y int }
	card map[struct{ x, y int }]bool
}

func (b *bingoCard) Mark(number int) {
	if coord, ok := b.nums[number]; ok {
		b.card[coord] = true
	}
}

func (b *bingoCard) Won() bool {
	return b.checkHorizontal() && b.checkVertical()
}

func (b *bingoCard) checkHorizontal() bool {
	won := true
	for x := 0; x < 5; x++ {
		for y := 0; y < 5; y++ {
			won = b.card[struct {
				x int
				y int
			}{x, y}] && won
		}
	}

	return true
}

func buildBingoCard(lines []string) bingoCard {
	card := bingoCard{}
	// for line := range lines {

	// }

	return card
}

func (b *bingoCard) checkVertical() bool {
	return true
}

func main() {
	data, _ := os.ReadFile("input.txt")
	content := string(data)
	lines := strings.Split(content, "\n")

	b := buildBingoCard(lines)
	b.Won()
}
