Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Capitalize.
In order to keep things simple, we split up the testing as follows:

- Capitalize Valid
- Capitalize Invalid

### Capitalize Valid

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input: Lowercase String | "hello" | "Hello" |
| Sample Input: Uppercase String | "Hello" | "Hello" |
| Sample Input: Long String | "hello world" | "Hello world" |
| Sample Input: Mixed Casing | "heLLo World" | "HeLLo World" |
| Sample Input: Symbols | "12345" | "12345" |

### Capitalize Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input |  |

All of these tests should output the following:

```
Usage: please provide a string
```
