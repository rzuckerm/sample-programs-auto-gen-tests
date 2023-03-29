Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Roman Numeral.
In order to keep things simple, we split up the testing as follows:

- Roman Numeral Valid
- Roman Numeral Invalid

### Roman Numeral Valid

| Description | Input | Output |
| ----------- | ----- | ------ |
| Empty Input | "" | "0" |
| Single I | "I" | "1" |
| Single V | "V" | "5" |
| Single X | "X" | "10" |
| Single L | "L" | "50" |
| Single C | "C" | "100" |
| Single D | "D" | "500" |
| Single M | "M" | "1000" |
| Addition | "XXV" | "25" |
| Subtraction | "XIV" | "14" |

### Roman Numeral Invalid

| Description | Input | Output |
| ----------- | ----- | ------ |
| No Input |  | "Usage: please provide a string of roman numerals" |
| Invalid Input | "XT" | "Error: invalid string of roman numerals" |
