Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Binary Search.
In order to keep things simple, we split up the testing as follows:

- Binary Search Valid
- Binary Search Invalid

### Binary Search Valid

| Description | List Input | Target Integer Input | Output |
| ----------- | ---------- | -------------------- | ------ |
| Sample Input: First True | "1, 3, 5, 7" | "1" | "true" |
| Sample Input: Last True | "1, 3, 5, 7" | "7" | "true" |
| Sample Input: Middle True | "1, 3, 5, 7" | "5" | "true" |
| Sample Input: One True | "5" | "5" | "true" |
| Sample Input: One False | "5" | "7" | "false" |
| Sample Input: Many False | "1, 3, 5, 6" | "7" | "false" |
| Sample Input: Middle True | "1, 2, 3, 4, 5, 6, 7" | "3" | "true" |

### Binary Search Invalid

| Description | List Input | Target Integer Input |
| ----------- | ---------- | -------------------- |
| No Input |  |  |
| Missing Input: Target | "1, 2, 3, 4" |  |
| Missing Input: List | "" | "5" |
| Out Of Order Input | "3, 5, 1, 2" | "3" |

All of these tests should output the following:

```
Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")
```
