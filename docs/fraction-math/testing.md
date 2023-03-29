Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Fraction Math.
In order to keep things simple, we split up the testing as follows:

- Fractions Valid
- Fractions Invalid

### Fractions Valid

| Description | Fraction 1 | Operation | Fraction 2 | Output |
| ----------- | ---------- | --------- | ---------- | ------ |
| Sample Input: Addition | "2/3" | "+" | "4/5" | "22/15" |
| Sample Input: Multiplication | "2/3" | "*" | "4/5" | "8/15" |
| Sample Input: Subtraction | "2/3" | "-" | "4/5" | "-2/15" |
| Sample Input: Division | "2/3" | "/" | "4/5" | "5/6" |
| Sample Input: Equals | "2/3" | "==" | "4/5" | "0" |
| Sample Input: Greater Than | "2/3" | ">" | "4/5" | "0" |
| Sample Input: Less Than | "2/3" | "<" | "4/5" | "1" |
| Sample Input: Greater Than Equals | "2/3" | ">=" | "4/5" | "0" |
| Sample Input: Less Than Equals | "2/3" | "<=" | "4/5" | "1" |
| Sample Input: Not Equals | "2/3" | "!=" | "4/5" | "1" |

### Fractions Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |

All of these tests should output the following:

```
Usage: ./fraction-math operand1 operator operand2
```
