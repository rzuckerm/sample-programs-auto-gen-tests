Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Longest Common Subsequence.
In order to keep things simple, we split up the testing as follows:

- Lcs Valid
- Lcs Invalid

### Lcs Valid

| Description | Sequence 1 | Sequence 2 | Output |
| ----------- | ---------- | ---------- | ------ |
| Sample Input Same Length | "1, 4, 5, 3, 15, 6" | "1, 7, 4, 5, 11, 6" | "1, 4, 5, 6" |
| Sample Input Different Length | "1, 4, 8, 6, 9, 3, 15, 11, 6" | "1, 7, 4, 5, 8, 11, 6" | "1, 4, 8, 11, 6" |

### Lcs Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Missing Input | "25 15 10 5" |

All of these tests should output the following:

```
Usage: please provide two lists in the format "1, 2, 3, 4, 5"
```
