If you’ve seen the lesson on the one-time pad, you know that it is the ultimate shift cipher. It involves the application of a random list of shifts equal to the length of the message. 
It’s important to understand exactly how and why the one-time pad is unbreakable.

<br>

You can go and check out: <br>

[ONE TIME PAD/OTP](https://github.com/KraKEn-bit/Cryptography/blob/main/Ancient_Cryptography/README.md)<br>

for a Quick Review.


**Bitwise simply means that we are dealing with individual bits, or binary numbers.** 
In any modern/computerized encryption scheme we represent our symbols using binary digits. And here in Cryptography Binary Operations can play a Major role. Specifically we must know why **XOR** must be used when performing the **OTP** on computers.  Bitwise Operations are AND,OR,XOR.

---

If you ever want to know why binary digits are used for computerization. Let me give you a brief Description on this:
<br>
<br>

`Why Binary Digits are used in Computers?`<br>
Ans:<br>
So, basically all electronics are naturally binary. A computer’s hardware is built from transistors (tiny electronic switches). Each transistor can only be in two stable states:<br>

  ON → electricity flows (represented as 1)<br>
  OFF → no electricity (represented as 0)

This matches perfectly with binary digits (bits).


### **Simplicity and Reliability:**

Using just two states makes circuits simpler, faster, and less error-prone.If we tried to use 10 different voltage levels (like decimal), tiny errors/noise would cause misreading. With just two states, signals are easier to detect reliably.

### **Mathematical Foundations:**

Boolean algebra (logic with AND, OR, NOT) maps perfectly to binary.Complex operations (addition, storage, comparisons) can be built using combinations of binary logic gates.

<br>
<br>

`How Computer Memory works with Binary?`<br>
Ans:<br>
 - **Bit & Byte:**
 
The smallest unit is a bit (binary digit → 0 or 1). Where: **8 bits = 1 byte, enough to store a letter (like A = 01000001 in ASCII).**

 - **RAM (Main Memory):**

RAM is made of memory cells (tiny flip-flops or capacitors + transistors). Each cell stores a single 0 or 1.The cells are arranged in a grid (rows & columns), and each has a unique address.

 -> The CPU uses the address to read/write values:<br>
      Write: set voltage high (1) or low (0).<br>
      Read: check if the stored voltage is high or low.

 - **Hard Drives / SSDs:**

Hard drives: use magnetic orientation (north/south → 0 or 1). SSDs: use trapped electrons in floating-gate transistors to store charge (charged = 1, uncharged = 0).

 - **Representation of Data:**

  ->Numbers: binary representation (e.g., 13 = 1101).

  ->Text: stored via encoding (ASCII, Unicode).
  
  ->Images: pixels stored as numbers (color values in binary).

Everything—videos, music, programs—is ultimately just patterns of 0s and 1s in memory.

----

<br>
<br>

# **Encrypting Colors:**

Let's start with a Leaf as our base image which is ought to be converted.

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Leaf.jpeg?raw=true)


<br>

`How do we convert a Color?`<br>
<br>
Ans:<br>
Well, right now you are looking at HTML colors which are defined using the RGB color model. This is an additive model based on mixing some amount of red, green and blue light.

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Color.jpg?raw=true)

<br>
Here:<br>
We can define exactly how much RED, GREEN and BLUE using a number from 0-255. Black is all off (0,0,0) while white is all on (255,255,255). In between there are 16 million possible colors (256 * 256 * 256).

<br>
<br>

**Let's Face a Question**

<br>
<br>

`Why for color combination RED,GREEN,BLUE (RGB) is used?`<br>
Ans:<br>
Inside our eyes we have cone cells that detect color. There are 3 types of cones:

  - S-cones → sensitive to blue light<br>
  - M-cones → sensitive to green light<br>
  - L-cones → sensitive to red light<br>
<br>
Every color we see is our brain mixing signals from these three cones. That’s why computers, TVs, and phones use RGB — they just mimic how our eyes naturally process color.
<br>
Let's see how light colors combine by addition:
  1) Red + Green = Yellow
  2) Red + Blue = Magenta
  3) Green + Blue = Cyan
  4)Red + Green + Blue = White light

This is called the Additive Color Model, and it works for anything that emits light (monitors, projectors, LEDs).
