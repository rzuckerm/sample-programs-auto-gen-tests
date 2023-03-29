Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Dijkstra.
In order to keep things simple, we split up the testing as follows:

- Dijkstra Valid
- Dijkstra Invalid

### Dijkstra Valid

| Description | Matrix | Source | Destination | Output |
| ----------- | ------ | ------ | ----------- | ------ |
| Sample Input: Routine | "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "0" | "1" | "2" |

### Dijkstra Invalid

| Description | Matrix | Source | Destination |
| ----------- | ------ | ------ | ----------- |
| No Input |  |  |  |
| Empty Input | "" | "" | "" |
| Non-Square Input | "1, 0, 3, 0, 5, 1" | "1" | "2" |
| No Destination | "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "0" | "" |
| No Source Or Destination | "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "" | "" |
| Source Or Destination < 0 | "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "-1" | "2" |
| Weight < 0 | "0, 2, 0, -6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, -6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "1" | "2" |
| Source Or Destination > Number Of Vertices | "0, 2, 0, -6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, -6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "1" | "10" |
| No Way | "0, 0, 0, 0" | "0" | "1" |

All of these tests should output the following:

```
Usage: please provide three inputs: a serialized matrix, a source node and a destination node
```
