Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Rot13.
In order to keep things simple, we split up the testing as follows:

- Rot13 Valid
- Rot13 Invalid

### Rot13 Valid

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input Lower Case | "the quick brown fox jumped over the lazy dog" | "gur dhvpx oebja sbk whzcrq bire gur ynml qbt" |
| Sample Input Upper Case | "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG" | "GUR DHVPX OEBJA SBK WHZCRQ BIRE GUR YNML QBT" |
| Sample Input Punctuation | "The quick brown fox jumped. Was it over the lazy dog?" | "Gur dhvpx oebja sbk whzcrq. Jnf vg bire gur ynml qbt?" |

### Rot13 Invalid

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |

All of these tests should output the following:

```
Usage: please provide a string to encrypt
```
