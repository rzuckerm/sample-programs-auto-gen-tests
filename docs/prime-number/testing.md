Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Prime Number.
In order to keep things simple, we split up the testing as follows:

- Prime Valid
- Prime Invalid

### Prime Valid

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input 0 | "0" | "composite" |
| Sample Input 1 | "1" | "composite" |
| Sample Input 2 | "2" | "prime" |
| Sample Input Small Composite | "4" | "composite" |
| Sample Input Small Prime | "7" | "prime" |
| Sample Input Large Composite | "4011" | "composite" |
| Sample Input Large Prime | "3727" | "prime" |

### Prime Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Invalid Input: Not A Number | "a" |
| Invalid Input: Not An Integer | "6.7" |
| Invalid Input: Negative | "-7" |

All of these tests should output the following:

```
Usage: please input a non-negative integer
```
