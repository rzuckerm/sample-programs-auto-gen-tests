Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Longest Word.
In order to keep things simple, we split up the testing as follows:

- Longest Word Valid
- Longest Word Invalid

### Longest Word Valid

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input: Many Words | "May the force be with you" | "5" |
| Sample Input: Single Word | "Floccinaucinihilipilification" | "29" |
| Sample Input: Multiline | "Hi,\nMy name is Paul!" | "5" |

### Longest Word Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |

All of these tests should output the following:

```
Usage: please provide a string
```
