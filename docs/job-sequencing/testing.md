Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Job Sequencing.
In order to keep things simple, we split up the testing as follows:

- Sequencing Valid
- Sequencing Invalid

### Sequencing Valid

| Description | Profits | Deadlines | Output |
| ----------- | ------- | --------- | ------ |
| Sample Input One | "25, 15, 10, 5" | "3, 1, 2, 2" | "50" |
| Sample Input Two | "20, 15, 10, 5, 1" | "2, 2, 1, 3, 3" | "40" |

### Sequencing Invalid

| Description | Profits | Deadlines |
| ----------- | ------- | --------- |
| No Input |  |  |
| Empty Input | "" |  |
| Missing Input | "25, 15, 10, 5" |  |
| Lists Different Lengths | "1, 2, 3, 4" | "1, 2, 3, 4, 5" |

All of these tests should output the following:

```
Usage: please provide a list of profits and a list of deadlines
```
