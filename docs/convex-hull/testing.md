Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Convex Hull.
In order to keep things simple, we split up the testing as follows:

- Convex Hull Valid
- Convex Hull Invalid

### Convex Hull Valid

| Description | Input X | Input Y | Output |
| ----------- | ------- | ------- | ------ |
| Sample Input: Triangle | "100, 180, 240" | "220, 120, 20" | "(100, 220)"<br>"(240, 20)"<br>"(180, 120)" |
| Sample Input: Pentagon | "100, 140, 320, 480, 280" | "240, 60, 40, 200, 300" | "(100, 240)"<br>"(140, 60)"<br>"(320, 40)"<br>"(480, 200)"<br>"(280, 300)" |
| Sample Input: Cluster | "260, 280, 300, 320, 600, 360, 20, 240" | "160, 100, 180, 140, 160, 320, 200, 0" | "(20, 200)"<br>"(240, 0)"<br>"(600, 160)"<br>"(360, 320)" |

### Convex Hull Invalid

| Description | Input X | Input Y |
| ----------- | ------- | ------- |
| No Input |  |  |
| Missing Y | "100, 180, 240" |  |
| Invalid Shape | "100, 180" | "240, 300" |
| Different Cardinality | "100, 180, 240" | "240, 60, 40, 200, 300" |
| Invalid Integers | "100, 1A0, 240" | "220, 120, 20" |

All of these tests should output the following:

```
Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")
```
