Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Fibonacci.
In order to keep things simple, we split up the testing as follows:

- Fibonacci Valid
- Fibonacci Invalid

### Fibonacci Valid

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input 0 | "0" |  |
| Sample Input 1 | "1" | "1: 1" |
| Sample Input 2 | "2" | "1: 1"<br>"2: 1" |
| Sample Input 5 | "5" | "1: 1"<br>"2: 1"<br>"3: 2"<br>"4: 3"<br>"5: 5" |
| Sample Input 10 | "10" | "1: 1"<br>"2: 1"<br>"3: 2"<br>"4: 3"<br>"5: 5"<br>"6: 8"<br>"7: 13"<br>"8: 21"<br>"9: 34"<br>"10: 55" |

### Fibonacci Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Invalid Input: Not A Number | "a" |

All of these tests should output the following:

```
Usage: please input the count of fibonacci numbers to output
```
