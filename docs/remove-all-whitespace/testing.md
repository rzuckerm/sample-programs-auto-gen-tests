Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Remove All Whitespace.
In order to keep things simple, we split up the testing as follows:

- Remove All Whitespace Valid
- Remove All Whitespace Invalid

### Remove All Whitespace Valid

| Description | Input |
| ----------- | ----- |
| Sample Input: No Spaces | "RemoveAllWhitespace" |
| Sample Input: Leading Spaces | "    RemoveAllWhitespace" |
| Sample Input: Trailing Spaces | "RemoveAllWhitespace    " |
| Sample Input: Inner Spaces | "Remove All Whitespace" |
| Sample Input: Tabs | "\tRemove\tAll\tWhitespace\t" |
| Sample Input: Newlines | "\nRemove\nAll\nWhitespace\n" |
| Sample Input: Carriage Returns | "\rRemove\rAll\rWhitespace\r" |

All of these tests should output the following:

```
RemoveAllWhitespace
```

### Remove All Whitespace Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |

All of these tests should output the following:

```
Usage: please provide a string
```
