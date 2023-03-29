Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Transpose Matrix.
In order to keep things simple, we split up the testing as follows:

- Transpose Matrix Valid
- Transpose Matrix Invalid

### Transpose Matrix Valid

| Description | Cols | Rows | Matrix | Output |
| ----------- | ---- | ---- | ------ | ------ |
| Sample Input: Routine | "3" | "2" | "1, 2, 3, 4, 5, 6" | "1, 4, 2, 5, 3, 6" |

### Transpose Matrix Invalid

| Description | Cols | Rows | Matrix |
| ----------- | ---- | ---- | ------ |
| No Input |  |  |  |
| Missing Input: No Columns Or Rows | "" | "" | "1, 2, 3, 4, 5, 6" |
| Missing Input: No Matrix | "3" | "3" | "" |

All of these tests should output the following:

```
Usage: please enter the dimension of the matrix and the serialized matrix
```
