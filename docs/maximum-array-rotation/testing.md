Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Maximum Array Rotation.
In order to keep things simple, we split up the testing as follows:

- Maximimum Array Rotation Valid
- Maximimum Array Rotation Invalid

### Maximimum Array Rotation Valid

| Description | Input |
| ----------- | ----- |
| Sample Input No Rotation | "3, 1, 2, 8" |
| Sample Input One Rotation | "1, 2, 8, 3" |
| Sample Input Many Rotations | "8, 3, 1, 2" |

All of these tests should output the following:

```
29
```

### Maximimum Array Rotation Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |

All of these tests should output the following:

```
Usage: please provide a list of integers (e.g. "8, 3, 1, 2")
```
