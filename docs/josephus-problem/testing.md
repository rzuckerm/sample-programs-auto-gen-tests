Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Josephus Problem.
In order to keep things simple, we split up the testing as follows:

- Josephus Problem Valid
- Josephus Problem Invalid

### Josephus Problem Valid

| Description | Input (n) | Input (k) | Output |
| ----------- | --------- | --------- | ------ |
| Sample Input 5, 2 | "5" | "2" | "3" |
| Sample Input 7 3 | "7" | "3" | "4" |
| Sample Input 41 4 | "41" | "4" | "11" |

### Josephus Problem Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Invalid Input: Not A Number | "a" |
| Invalid Input: No K | "1" |

All of these tests should output the following:

```
Usage: please input the total number of people and number of people to skip.
```
