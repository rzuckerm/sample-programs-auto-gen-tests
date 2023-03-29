Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Factorial.
In order to keep things simple, we split up the testing as follows:

- Factorial Valid
- Factorial Invalid

### Factorial Valid

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input: Zero | "0" | "1" |
| Sample Input: One | "1" | "1" |
| Sample Input: Four | "4" | "24" |
| Sample Input: Eight | "8" | "40320" |
| Sample Input: Ten | "10" | "3628800" |

### Factorial Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Invalid Input: Not A Number | "asdf" |
| Invalid Input: Negative | "-1" |

All of these tests should output the following:

```
Usage: please input a non-negative integer
```
