Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Minimum Spanning Tree.
In order to keep things simple, we split up the testing as follows:

- Minimum Spanning Tree Valid
- Minimum Spanning Tree Invalid

### Minimum Spanning Tree Valid

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input: Routine | "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "16" |

### Minimum Spanning Tree Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Non-Square Input | "1, 0, 3, 0, 5, 1" |

All of these tests should output the following:

```
Usage: please provide a comma-separated list of integers
```
