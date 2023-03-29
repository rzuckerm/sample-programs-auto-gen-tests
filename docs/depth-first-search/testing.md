Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Depth First Search.
In order to keep things simple, we split up the testing as follows:

- Depth First Search Valid
- Depth First Search Invalid

### Depth First Search Valid

| Description | Tree Input | Vertex Values | Target Integer Input | Output |
| ----------- | ---------- | ------------- | -------------------- | ------ |
| Sample Input: First True | "0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" | "1, 3, 5, 2, 4" | "1" | "true" |
| Sample Input: Last True | "0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" | "1, 3, 5, 2, 4" | "4" | "true" |
| Sample Input: Middle True | "0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" | "1, 3, 5, 2, 4" | "5" | "true" |
| Sample Input: One True | "0" | "1" | "1" | "true" |
| Sample Input: One False | "0" | "1" | "6" | "false" |
| Sample Input: Many False | "0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" | "1, 3, 5, 2, 4" | "7" | "false" |

### Depth First Search Invalid

| Description | Tree Input | Vertex Values | Target Integer Input |
| ----------- | ---------- | ------------- | -------------------- |
| No Input |  |  |  |
| Missing Input: Tree | "" | "1, 3, 5, 2, 4" | "4" |
| Missing Input: Vertex Values | "0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" | "" | "1" |
| Missing Input: Target | "0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" | "1, 3, 5, 2, 4" | "" |

All of these tests should output the following:

```
Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")
```
