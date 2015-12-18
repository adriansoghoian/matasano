package main

import (
	"encoding/base64"
	"encoding/hex"
	"fmt"
)

func hexToBase64(s string) string {
	data, err := hex.DecodeString(s)
	if err != nil {
		fmt.Println("error: ", err)
	}
	result := base64.StdEncoding.EncodeToString(data)
	fmt.Println("Problem 1: ", result)
	return result
}

func fixedLengthXOR(firstString string, secondString string) string {
	first, err := hex.DecodeString(firstString)
	if err != nil {
		fmt.Println("error: ", err)
	}
	second, err := hex.DecodeString(secondString)
	if err != nil {
		fmt.Println("error: ", err)
	}
	numBytes := len(first)
	var results []byte
	results = make([]byte, numBytes)

	for i := 0; i < numBytes; i++ {
		results[i] = first[i] ^ second[i]
	}

	encodedResults := hex.EncodeToString(results)
	fmt.Println("Problem 2: ", encodedResults)
	return encodedResults
}

func mostFrequentCharacter(s string) string {
    charCount := make(map[string]int)

    for _, value := range s {
        if val, ok := charCount[string(value)]; ok {
            charCount[string(value)] = val + 1
        } else {
            charCount[string(value)] = 1
        }
    }

    var maxCount = 0
    var maxChar string
    for key, value := range charCount {
        if value > maxCount {
            maxCount = value
            maxChar = key
        }
    }
    return maxChar
}

func singleCharXOR(s string, char string) string {
    singleByte := []byte(char)[0]

    decodedString, err := hex.DecodeString(s)
    if err != nil {
        fmt.Println("error: ", err)
    }
    var xorResult []byte
    xorResult = make([]byte, len(s))

    for i, each := range decodedString {
        xorResult[i] = each ^ singleByte
    }
    var encodedResult = hex.EncodeToString(xorResult)
    fmt.Println("Problem 3: ", encodedResult)
    return encodedResult
}
