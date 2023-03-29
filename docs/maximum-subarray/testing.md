Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Maximum Subarray.
In order to keep things simple, we split up the testing as follows:

- Maximum Subarray Valid
- Maximum Subarray Invalid

### Maximum Subarray Valid

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input: One Element | "1" | "1" |
| Sample Input: Many Positive Values | "1, 2, 3" | "6" |
| Sample Input: Many Negative Values | "-1, -2, -3" | "-1" |
| Sample Input: Many Negative Followed By Positive Values | "-2, -1, 3, 4, 5" | "12" |
| Sample Input: Many Alternating Positive And Negative Values | "-1, -4, 2, 3, -3, -4, 9" | "9" |

### Maximum Subarray Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |

All of these tests should output the following:

```
Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"
```
