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

So, the message is perfectly stored. So we can say: OTP uses XOR with a random key. If done properly, OTP is an unbreakable Encryption method.

---

**Let's ask ourselves:**

`Why must we use XOR?`

Ans:

Does it really matter if we used AND, OR or XOR with the one-time pad? The answer is **YES**, and it’s extremely important to understand why. Recall from the [Bitwise Operation](https://github.com/KraKEn-bit/Cryptography/blob/main/Ciphers/Bitwise_Operations.md) Article that AND has a 75% chance of outputting 0 and a 25% chance of outputting a 1. While OR has a 25% chance of outputting 0 and 75% chance of outputting 1. While the XOR operation has a 50% chance of outputting 0 or 1.


Now you may ask:

`AND has a 75% chance of outputting 0 and a 25% chance of outputting a 1. While OR has a 25% chance of outputting 0 and 75% chance of outputting 1. How is this predicted?`

Ans:

The answer is simple. If we go through the [Bitwise Operation](https://github.com/KraKEnbit/Cryptography/blob/main/Ciphers/Bitwise_Operations.md) Article thoroughly and try to find the answer by yourselve you'll understand the concept more crystal clearly.

But Tension not. I am here to remove your hesitance and problems. :
This is actually all about probability in truth tables when inputs are random. Let’s break it down clearly:

- **Step 1: Assume Random Inputs**

  We take two binary inputs A and B.
  Each is random 0 or 1 with equal probability (50%).

<br>

So there are 4 equally likely combinations:

  | A | B | Probability |
  | - | - | ----------- |
  | 0 | 0 | 25%         |
  | 0 | 1 | 25%         |
  | 1 | 0 | 25%         |
  | 1 | 1 | 25%         |

<br>

- **Step 2: Truth Table for AND:**
  
  | A | B | A AND B |
  | - | - | ------- |
  | 0 | 0 | 0       |
  | 0 | 1 | 0       |
  | 1 | 0 | 0       |
  | 1 | 1 | 1       |


3 out of 4 cases give 0 → Probability = 75%

1 out of 4 cases gives 1 → Probability = 25%

That’s why AND outputs 0 with 75% chance, 1 with 25% chance.

<br>

- **Step 3: Truth Table for OR**
  
  | A | B | A OR B |
  | - | - | ------ |
  | 0 | 0 | 0      |
  | 0 | 1 | 1      |
  | 1 | 0 | 1      |
  | 1 | 1 | 1      |


1 out of 4 cases gives 0 → Probability = 25%

3 out of 4 cases give 1 → Probability = 75%

That’s why OR outputs 1 with 75% chance, 0 with 25% chance.

<br>

- **Step 4: XOR (for comparison):**

  | A | B | A XOR B |
  | - | - | ------- |
  | 0 | 0 | 0       |
  | 0 | 1 | 1       |
  | 1 | 0 | 1       |
  | 1 | 1 | 0       |


2 out of 4 cases give 0 → Probability = 50%

2 out of 4 cases give 1 → Probability = 50%
