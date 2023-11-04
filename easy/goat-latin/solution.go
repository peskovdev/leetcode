package main

import (
	"fmt"
	"strings"
)

func toGoatLatin(sentence string) string {
	var new_sentence []string
	for i, word := range strings.Fields(sentence) {
		if strings.ContainsAny(strings.ToLower(string(word[0])), "aeiou") {
			word = fmt.Sprintf("%sma", word)
		} else if strings.ContainsAny(strings.ToLower(string(word[0])), "bcdfghjklmnpqrstvwxyz") {
			word = fmt.Sprintf("%s%sma", string(word[1:]), string(word[0]))
		}
		word = fmt.Sprintf("%s%s", word, strings.Repeat("a", i+1))

		new_sentence = append(new_sentence, word)
	}
	return strings.Join(new_sentence, " ")
}
