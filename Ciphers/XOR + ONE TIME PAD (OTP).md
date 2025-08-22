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

Because applying XOR twice with the same key restores the original.

# **OTP and XOR:**

The One-Time Pad is a theoretically unbreakable encryption system. To recall how OTP works and how it looked like and how it contributed to Cryptography you can again look into the [Ancient Cryptography Doc where all of them are cleared for your sake](https://github.com/KraKEn-bit/Cryptography/blob/main/Ancient_Cryptography/README.md) . So Buckle up and enjoy Treasure Hunting. <br>

So Back to the point: 

OTP works by XOR-ing the plaintext with a random key of the same length.<br>
The way to do that is: <br>

  1) Convert the message into binary.

  2) Generate a truly random key (same length as message).

  3) Encrypt using: Ciphertext = Plaintext ⊕ Key

  4) Decrypt using: Plaintext = Ciphertext ⊕ Key

For example:

A plaintext: 101101 and key: 110010

- By **Encryption** we get by XOR-ing:

  101101<br>
  110010<br>
  ------<br>
  011111   (Ciphertext)

<br>

- By **Decription** we get by XOR-ing:

  011111 (Ciphertext)<br>
  110010 (Key)<br>
  ------<br>
  101101 (Original Message)

So, the message is perfectly stored. So we can say: OTP uses XOS with a random key.

