Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Even Odd.
In order to keep things simple, we split up the testing as follows:

- Even Odd Valid
- Even Odd Invalid

### Even Odd Valid

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input: Even | "2" | "Even" |
| Sample Input: Odd | "5" | "Odd" |
| Sample Input: Negative Even | "-14" | "Even" |
| Sample Input: Negative Odd | "-27" | "Odd" |

### Even Odd Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Invalid Input: Not A Number | "a" |

All of these tests should output the following:

```
Usage: please input a number
```
