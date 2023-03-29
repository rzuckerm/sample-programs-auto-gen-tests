Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Longest Palindromic Substring.
In order to keep things simple, we split up the testing as follows:

- Lps Valid
- Lps Invalid

### Lps Valid

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input: One Palindrome | "racecar" | "racecar" |
| Sample Input: Two Palindrome | "kayak mom" | "kayak" |
| Sample Input: Complex Palindrome | "step on no pets" | "step on no pets" |

### Lps Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Invalid Input: No Palindromes | "polip" |

All of these tests should output the following:

```
Usage: please provide a string that contains at least one palindrome
```
