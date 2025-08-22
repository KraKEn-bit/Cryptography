Let me give some brief Explanations about XOR . I know you already know and learnt about them in [Bitwise Operation](https://github.com/KraKEn-bit/Cryptography/blob/main/Ciphers/Bitwise_Operations.md) . To recall the topic- XOR I'm just writing some points and short notes for it.


XOR (Exclusive OR) is a logical operation often used in cryptography. It outputs 1 if the two inputs are different, otherwise 0. The truth table for XOR can be written like this:

| A | B | A ⊕ B |
| - | - | ----- |
| 0 | 0 | 0     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 0     |


So, from this we can say if the value of A and B are different then 1 else 0. For Encryption the property of XOR we use is:
If C = A ⊕ B, then:

  - A = C ⊕ B

  - B = C ⊕ A
