Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Palindromic Number.
In order to keep things simple, we split up the testing as follows:

- Palindromic Number Valid
- Palindromic Number Invalid

### Palindromic Number Valid

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input: One Digit | "7" | "true" |
| Sample Input: Even Digits | "2442" | "true" |
| Sample Input: Odd Digits | "232" | "true" |
| Sample Input: Even Digits Not Palindrome | "5215" | "false" |
| Sample Input: Odd Digits Not Palindrome | "521" | "false" |

### Palindromic Number Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Invalid Input: Not A Number | "a" |
| Invalid Input: Negative Integer | "-7" |
| Invalid Input: Float | "5.41" |

All of these tests should output the following:

```
Usage: please input a non-negative integer
```
