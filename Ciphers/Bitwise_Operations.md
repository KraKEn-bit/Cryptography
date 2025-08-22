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

--- 


**Let's Face a Question**
<br>
<br>

`Why for color combination RED,GREEN,BLUE (RGB) is used?`

Ans:


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

<br>

`You may think, how the numbers from 0-255 combines together to form a color?` 

Ans:


No worries, I am covering up for you. 
<br>
The thing is **"It all comes down to binary representation and efficiency."**
Computers store data in bytes (8 bits).<br>
<br>
**8 bits can represent numbers from:
    00000000(binary)=0 to 111111111(binary)=255**
    <br>
That gives 256 possible values (0 to 255 inclusive).

<br>

### **RGB Uses 3 Bytes**

Each pixel color is usually stored as 3 channels:

  - Red = 0–255
  - Green = 0–255
  - Blue = 0–255

Together, that’s 24 bits (3 × 8) per pixel.

Total possible colors:
     256 X 256 X 256 = almost 16 millions Combinations can be Made out of those 3 colors.
<br>

0–1 could be used (and often is, in graphics/math libraries) but 0–255 is chosen in files and hardware because: 1 byte is a natural storage unit. It’s efficient for memory and bandwidth.

 Easy mapping to binary numbers.

---

**Let's see the sample green used in the Leaf in by using an Image editing tool like Photoshop:**

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Color%20Grades.png?raw=true)


Notice it stores it as RED=156, GREEN=181, BLUE=58. If we express these numbers in binary we get:<br>
RED=10011100, GREEN=10110101, BLUE=00111010 <br>
We can squeeze those together as: 100111001011010100111010

<br>

### **Binary representation of the 'Green' Color:**

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Leaf_Binary_Representation.jpg?raw=true)

<br>

## **Applications of Random Shifts**

Now let’s say you generate a shift sequence using Dice Rolls converted into binary as:

Say we roll two 6-sided dice:<br>

  - Dice A = 5 (0101 in binary, 4 bits)

  - Dice B = 3 (0011 in binary, 4 bits)


**Let’s do AND, OR, XOR:**

### **AND:**

0101<br>
0011<br>
----<br>
0001  = 1


### **OR:**

0101<br>
0011<br>
----<br>
0111  = 7


### **XOR:**

0101<br>
0011<br>
----<br>
0110  = 6


**Now TO see the RGB colors:**

Let’s assign each result to a color channel:

  - AND → Red channel (R)

  - OR → Green channel (G)

  - XOR → Blue channel (B)

So we get RGB = (1, 7, 6).

But color channels usually range from 0–255. We can scale dice results by multiplying by ~36 (≈ 255 ÷ 7, since max dice OR is 7).

  - R = 1 × 36 = 36

  - G = 7 × 36 = 252

  - B = 6 × 36 = 216

**Final RGB color = (36, 252, 216) (a bright teal/cyan shade).**


**Here's the Image if you ever wonder how it would look like:**


![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/(36,%20252,%20216)_color.png?raw=true)


---

**Let's Face a question related to this:**

`We can scale dice results by multiplying by ~36 (≈ 255 ÷ 7, since max dice OR is 7). why we used 36 and why does it matter?`

Ans:

Dice rolls (when combined with AND/OR/XOR) only produce results in the range 0 → 7 (since a die max is 6 = 0110, OR two dice can give 7 = 0111). But colors in RGB use 0 → 255 (because each channel is stored in 8 bits).<br>
So, if we want to "stretch" the dice result range [0–7] to fill the RGB range [0-255], we need a **Scaling Factor**.


So, Actually The math behind this is:<br>

  **Scaling Factor=Target Max/Source Max**
                  =255/7 ≈ 36

That’s where the ≈ 36 comes from.<br>
Multiply dice result (0–7) × 36 → new value in 0–252 (close to 255).

Slight rounding, but good enough for visualization.


So,

**Summary:**

We use ~36 because 255 ÷ 7 ≈ 36.4, and that maps dice results (0–7) evenly into the 0–255 RGB scale. It’s basically a linear scaling so our small dice numbers can be visualized as proper colors.

---
