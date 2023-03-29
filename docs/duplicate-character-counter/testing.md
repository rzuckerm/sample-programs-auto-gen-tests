Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Duplicate Character Counter.
In order to keep things simple, we split up the testing as follows:

- Duplicate Character Counter Valid
- Duplicate Character Counter Invalid

### Duplicate Character Counter Valid

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input: No Duplicates | "hola" | "No duplicate characters" |
| Sample Input: Routine | "goodbyeblues" | "o: 2"<br>"b: 2"<br>"e: 2" |

### Duplicate Character Counter Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |

All of these tests should output the following:

```
Usage: please provide a string
```
