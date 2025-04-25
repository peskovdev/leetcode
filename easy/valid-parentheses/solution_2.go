package main

func isValid(s string) bool {
    mapping := map[rune]rune{
        '(': ')',
        '[': ']',
        '{' :'}',
    }

    stack := []rune{}

    for _, char := range s {
        if _, isOpen := mapping[char]; isOpen {
            stack = append(stack, char)
            continue
        }

        if len(stack) == 0 || mapping[stack[len(stack) - 1]] != char {
            return false
        }

        // delete closed parenthese
        stack = stack[0: len(stack) - 1]
    }

    return len(stack) == 0
}
