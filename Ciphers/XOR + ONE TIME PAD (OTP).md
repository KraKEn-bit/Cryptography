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

The answer is simple. If you go through the [Bitwise Operation](https://github.com/KraKEnbit/Cryptography/blob/main/Ciphers/Bitwise_Operations.md) Article thoroughly and try to find the answer by yourselve you'll understand the concept more crystal clearly.

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


To visualize this more clearly I've made a probability diagram to understand more easily. Here's the image:

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/probabiliy_Diagram_AND_OR_XOR.png?raw=true)


Here’s a visual probability diagram for AND, OR, XOR — each square represents a dice-like random input combination (A, B).

  - Green = output 1

  - Red = output 0

From this, you can clearly see why:

AND gives 1 only when both are 1 (1 case → 25%). OR gives 0 only when both are 0 (1 case → 25%). XOR splits evenly (2 cases each → 50%).

---

Let’s look at a visual example to see the different scrambling effects of AND vs. OR vs. XOR  by encrypting an image. Here is a digital image of Charles Babbage:

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Charles_Babbage_Original.jpg?raw=true)


It contains thousands of tiny colored squares called pixels. Each pixel in this image can be represented as a 24 bit sequence as shown in the previous article. Let's call this our plaintext image (or message).
First let’s see what happens when we AND each bit in the image file with a stream of random bits.


# **AND:**

Notice most of the original message shines through. This happens anytime a random shift of 1 is applied, or when the plaintext is 0:

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/AND_Charles_Babbage.jpg?raw=true)


# **OR:**

Notice most of the original message shines through. This happens anytime a random shift of 0 is applied, or when the plaintext is 1:

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/OR_Charles_Babbage.jpg?raw=true)


# **XOR:**

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/XOR_Charles_Babbage.jpg?raw=true)


Notice that the plaintext only shines through 50% of the time, which results in noise as each pixel is equally likely to be 0 or 1.
This image contains no information about the original image. If we didn’t provide the shift sequence it would be impossible for you to reverse it back to the original image. You could try every possible sequence, but that would result in every possible image! How could you know it was Babbage? It's equally likely to be a picture of you or anything else you can think of.


--- 

**Let's face a question:**

`The end of the article claims "This image contains no information about the original image." But is that right? In the last article, the one time pad was only a few dozen bits. Now this image is thousands of times longer. If the one time pad is short, and the message is long, doesn't information leak? (It seems like probably the encrypted version used a one time pad the same size as the image, but reading this article and the last one, you might not think so.)`

Ans:

 The one time pad must be the same size as the image to prevent information from being leaked. A stream of random bits is used, so we can safely say that the size of the one time pad equals the size of the message (in this case the picture is the message).


 `What do you mean by "This happens anytime a "RANDOM SHIFT" of __ is applied..." ? What does this have to do with anything, or what does this mean?`

 Ans:

 In the AND demonstration, "This happens anytime a random shift of 1 is applied [...]" simply means that the original image data is unchanged when a 1 in the series of random binary digits is used to operate on the image data by means of the AND operation.

Why? Take a look at the possibilities:

Image data in random bit image data out<br>

0 1 0<br>
1 1 1<br>

As you can see the image data out is the exact same as the image data in when the random bit is 1.
