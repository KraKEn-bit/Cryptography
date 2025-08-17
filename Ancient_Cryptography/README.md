# **What is Cryptography?**

Let's Explain this with a Simple Example of Data Transmission between Alice and Bob where a person named Eve will try to intercept the informations between them:

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Alics_Bob_Eve_Transmission.png?raw=true)

Alice Shares a code with Bob that only Bob will have access to the datas. This is called **ENCRYPTION** . Bob will then use the code to access the data. This is called **DECRYPTION** . 

The codes will be created in such a way that even if a 3rd person named Eve tries to intercept the messages that is being transferred between Bob and Alice, he will fail as those messages will seem meaningless to him. Example: **Caeser Cipher** .

But then a major breakthrough was made after 800 years by the acquiring of the method called **FREQUENCY ANALYSIS** . 


---
## **What is 'Frequency Analysis' ?**

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Frequency_of_Letters.png?raw=true)

See how the graphical presentations of each english letter is acting. Every English letters have their own Frequency. It means how many time a letter has been used in a sentence or context.

For example:  In English:
- `E` is the most common letter
  - `T`, `A`, `O`, `I`, `N` follow
- By comparing the frequency of letters in the ciphertext to expected frequencies in the language, an attacker can **guess the substitutions**.

For example:
Let's assume a word : 'WKKJ'

Here,

-frequency of W is 1.

-frequency of K is 2.

-frequency of J is 1.

So,
**Frequency Analysis** is a technique used in cryptography to **break classical ciphers** by studying the frequency of letters or groups of letters in a ciphertext.

**Here's a small yet clear Explanations of the above contexts :** 

[Watch this video on Caeser Cipher and Frequency Analysis](https://youtu.be/sMOZf4GN3oc?si=gl5V0I-1-EtaizGY)


Let's dive into **Polyalphabetic Cipher** !

---
# **POLYALPHABETIC CIPHER:**

A **Polyalphabetic Cipher** is a type of substitution cipher in which **more than one alphabet is used** to encrypt the message. This makes it **much harder to break** using frequency analysis compared to monoalphabetic ciphers like Caesar Cipher.

### **How it Works**

- Each letter of the plaintext is shifted according to a **repeating keyword** or **master word**.  
- Example: Keyword = `KEY`

For example:
Encrypting the message **"LOVE"** using the key or master keyword **"SLIP"**.

Let's assume (A=1,B=2,...Z=26)


| Step | Plaintext | Equivalent Numbers | Key / Master Word | Key Numbers | Sum (mod 26) | Ciphertext |
|------|-----------|------------------|-----------------|------------|---------------|------------|
| 1    | L         | 11               | S               | 18         | 29 → 3        | D          |
| 2    | O         | 14               | L               | 11         | 25            | Z          |
| 3    | V         | 21               | I               | 8          | 29 → 3        | D          |
| 4    | E         | 4                | P               | 15         | 19            | T          |


So, placed the message "LOVE" over the master word "SLIP" . This method is known as **SHIFTING** . 

---
## **Frequency Fingerprint**

**Frequency Fingerprinting** is a method used to **identify the language or probable plaintext** by analyzing the **frequency patterns of letters or symbols** in a ciphertext.

### How it Works

1. Each language has a **distinct frequency distribution** of letters.  
   - For example, in English: E > T > A > O > I > N > …  
2. Count the occurrences of each letter in the ciphertext.  
3. Compare the distribution with known **language frequency patterns**.  
4. The **closest match** helps identify the language or plaintext characteristics.  

---

Here's a simple program to demonstrate the Frequency Fingerprints:

[Frequency Fingerprint](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/pi/frequency-fingerprint-exploration)

---
**Let's Face a Question**

`Any Time there's a Differential in Letter frequencies; a leak of information occurs. These are caused by repetition of the encrypted message. What does it mean?`

Ans: With each code there is almost always some form of patters no matter how minor it is. Each pattern/unique difference is something that may stand out which will draw the attention to the intercepter's mind that could be dangerous for its privacy. 

For example: Frequency of words in a sentence. 

- **The best code will have a lessened "Fingerprint" or more minuscle and therefore harder to intercept.** 

`How can Someone design a cypher that hides her fingerprint?`

Ans: By Randomness/Random Shifting method. As a result Frequency distribution will be uniform. It is known as **ONE TIME PAD**

---
# **ONE TIME PAD**

The **One-Time Pad** is a type of **perfectly secure encryption** method.  It uses a **random key** that is as long as the message and is used **only once**.

The **One-Time Pad (OTP)** was famously used during the **Cold War** for secure communication between spies and intelligence agencies.

`Why OTP Was Perfect for Cold War?`

- **Perfect secrecy:** Impossible to crack if the key is random, secret, and used only once.  
- **No pattern to exploit:** Unlike classical ciphers, OTP produces **ciphertext with completely random distribution**.  
- **Portable:** Agents could carry small sheets of key sequences.  

---

**Historical Note**

- OTP machines and key sheets were used by agencies like the **Soviet KGB** and **CIA**.  
- A famous case: The **Venona project** tried to decrypt Soviet communications, but OTP messages that were properly used remained **unbreakable**.  
- Any **reuse of keys** could compromise secrecy, which happened occasionally and allowed some messages to be cracked.
---

### How it Works

1. Generate a **random key** equal in length to the plaintext.  
2. Convert both **plaintext** and **key** letters to numbers (A=0, B=1, … Z=25).  
3. Add corresponding numbers **mod 26**.  
4. Convert the result back to letters to get the **ciphertext**.  

**Important:** The key must be completely random, kept secret, and **never reused**. If reused, the encryption is no longer secure.

`Why One time Pad (OTP) was perfectly secure?`

Ans: It's because of the Uniform Distributions in OTP.

- ### **Encryption Process:**

Each plaintext letter is combined with a truly random key letter (mod 26).
Example: Plaintext H + Random key X → Ciphertext letter.

- ### **Effect on Ciphertext:**

Because the key is completely random, every possible ciphertext letter is equally likely, regardless of the plaintext.
This means the letter frequency in the ciphertext is uniform.

- ### **Implications:**

Frequency analysis is useless against OTP.
The ciphertext contains no patterns, so an attacker cannot deduce anything about the plaintext from the ciphertext alone.

This is why OTP is called “perfectly secure”.

Here's a simple image to understand the frequency distributions of the letters in **One time Pad(OTP)**:

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Uniform%20Distribution%20of%20letters.png?raw=true)


- ### **Disadvantages of OTP**
  
  1) It can only be use if you can meet the other person and translate the pad to them secretly.
  2) It is actually difficult to generate large quantities of truly random Numbers.
  3) You can only use the OTP key only **ONCE**


Here's a simple yet influential Explanation on OTP:

[Watch how OTP works](https://youtu.be/FlIG3TvQCBQ?si=9PaGgqOk5TxxHN-_)

---

**Let's Face a Question**

`Does truly Random numbers exist?`

Ans: It's impossible but we can get closer to it in reality. We derive "random" numbers through algorithms. In order to make it more random, we pick a seed for the Algorithm such as **Stock Price** at a given time on a given day in the future so that programmers don't know what it is and then the algorithm acts on that seed and creates random numbers. That's the most random we can get.


`Note to be Noted:`

True Randomness requires that each flip be independent of any previous flips of a coin. A computer can be programmed to diregard any information on its previous 'Flip' Choices for the next 'Flip' whereas a Human can't help but allow the memory of the previous Flips to influence the next coice. A human will feel that any repition of a certain result (Ex: 4 heads in a row) seems non-random and will modifyy their next choice accordingly.

---

During the World War 2 Encryption-Decryption was the key factor for anticipating the Nazi's moves. And hence, A machine called - **ENIGMA** was invented. 

# **ENIGMA MACHINE**

An elctro mechanical rotor Cipher machine used mainly by the German Military to encrypt and decrypt secret messages. It looked like a typewriter inside a wooden box, but instead of printing letters, it lit them up on a lampboard.

### **How it worked:**

- #### **Keyboard input:**

  1) You press a letter (say A) on the keyboard.
  2) Electricity flows into the wiring system.

- #### **Rotors (the brain of Enigma):**

  1) Enigma had 3–5 rotors, each containing a scrambled alphabet wired internally.
  2) Each rotor maps one letter to another, like a substitution cipher.
  3) Every time you press a key, the rightmost rotor rotates by 1 step (like an odometer), changing the mapping for the next letter.
  4) This creates a polyalphabetic substitution cipher (different encryption for the same letter each time).

- #### **Reflector:**

  1) After passing through all rotors, the current hits a reflector.
  2) The reflector sends the signal back through the rotors in reverse but along a different path.
  3) This ensures encryption is symmetrical: the same settings encrypt and decrypt.

- #### **Lampboard output:**

Finally, a lamp lights up showing the encrypted letter (e.g., pressing A might give G).

- **Plugboard (Steckerbrett):**
  
Before and after the rotors, letters could be swapped via plugboard cables.

This added an extra layer of complexity.

This was the Enigma Machine used by the Nazis at World War-2:

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Enigma%20Mchine.jpeg?raw=true)


- #### **Security strength**
  
With 3 rotors (chosen from 5), 26 positions per rotor, and 10 plugboard pairs → the number of possible initial settings was about 10²³.This made brute-forcing practically impossible at the time.

---

**Let's face an important question**

`What does it mean by "With 3 rotors (chosen from 5), 26 positions per rotor, and 10 plugboard pairs → the number of possible initial settings was about 10²³"?`

Ans:
**The Enigma Machine could be set up in so many ways before starting to encrypt. Each possible setup = 1 key.**

Let's explain this with its properties:

- #### **Rotor Choice:**
  
  Out of 5 rotors (as there are 5 rotors in built) you must choose 3 and decide their orders. So that's Permutation:
    (3 5​)×3!=60 choices

- #### **Rotor Starting Position:**

  Each Rotor can be rotated to 26 positions (A to Z). For 3 rotors = 26^3 choices which is the list of shifts.

   example:
  
  |↑|↑|↑|
  
  |8|2|5|
  
  |↓|↓|↓|

  What it's happening is that Let's assume for 5. So you go up and down like the **Odometer** . Then After completing its sequence you go to the column of 2 and then together with previous one you go up and down. And we will get 26 combinations for each column. That's why it's 26^3 choices.

  Here's an image of an ODOMETER to understand the sequence :
  
  ![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Odometer.png?raw=true)

  To understand how it relates to the Enigma Machine for Encryption, here's another image to understand the inside properties:

  ![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Traversing.png?raw=true)

- #### **Ring Setting:**

  Each Rotor has an internal Ring Offset. So another 26^3 possibilities.

- #### **Plug Board:**

  10 pairs of Letters are swapped out of 26 letters. So Number of ways will be:
  
   26! / ((26 - 20)! * 10! * 2^10) ≈ 1.50541 × 10^14

- #### **Total KEY SPACES:**

  60 * 26^3 * 26^3 * 1.50541 × 10^14 = 1.6 X 10^23

  Different possible Keys.

  **That’s what “about 10²³” means → there are 100,000,000,000,000,000,000,000 possible ways to set up the machine!**

  This was considered “unbreakable” in the 1940s without shortcuts, but Allied cryptanalysts found weaknesses in operator habits and design flaws.

  Here's a well Documented Explanation of Enigma Machine:

  [How Enigma Machine worked and how it was so influencial](https://youtu.be/-1ZFVwMXSXY?si=IR1wRV5XG3ggNwBe)




`What was meant by 'KEY' for Enigma Machine?`

Ans:

- **For the Enigma machine:**

A key meant the machine’s setup for that day →
  - which rotors were chosen and in what order
  - what the starting letters of each rotor were
  - the ring settings inside each rotor
  - the plugboard connections

That whole setup = the key.

If you and I both had Enigma machines:

If I set my machine to today’s key and type a message, it comes out scrambled.

If you set your machine to the same key, and type the scrambled message, you get the original back.

-> So in Enigma’s context, “keys” = the secret daily machine settings.

---

## **CRACKING ENIGMA:**

The Allies (notably Alan Turing at Bletchley Park) developed mathematical shortcuts and electromechanical "Bombes" to test rotor settings quickly.Exploiting operator mistakes (like repeated message keys) and captured Enigma machines also helped.

Breaking Enigma was a turning point in WWII, shortening the war by ~2 years.

`What were 'BOMBES' ?`

Ans:

The Bombe was an electromechanical machine designed by Alan Turing, Gordon Welchman, and their team at Bletchley Park (UK). Its purpose was to find the daily Enigma key settings (rotors, positions, plugboard) by testing thousands of possibilities very quickly.

### **How did they work?**

Ans:

By using the known plaintext (cribs). Allies often guessed parts of German messages (like “WETTER” = "weather" or “HEILHITLER”).These guesses (cribs) gave a starting point.

- #### **Logical deductions:**

  The Bombe wired together multiple Enigma machines inside, simulating how they scrambled letters.It used the guessed plaintext and ciphertext to rule out impossible rotor settings.

- #### **Process:**

  The Bombe didn’t directly decrypt messages.Instead, it rapidly eliminated wrong keys, narrowing millions of possibilities down to a handful.
  
  It iterates through each combinations finding the leading key and elimating the column reducing posibilities down.

  Here's an image to understand how it worked:

  ![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/How%20The%20Bombes%20Iterates%20through%20each%20combinations%20of%20the%20Enigma.png?raw=true)

  
  Human cryptanalysts then tested the remaining candidates on real Enigma machines.

- #### **Speed advantage:**

  A manual check could take weeks/months.A Bombe could cut it down to hours.

  By 1944, Bletchley Park had over 200 Bombes running nonstop.

Bombes allowed the Allies to read German military communications in near real-time.

This intelligence, called Ultra, helped in:

  1) routing convoys safely across the Atlantic,
  2) anticipating attacks,
  3)and even planning D-Day.

Historians believe breaking Enigma shortened WWII by ~2 years.

**The BOMBES didn’t “break” Enigma directly; it was a shortcut machine that searched through the astronomical key space (≈10²³) using logic and known patterns.**

Here's an image of the BOMBE that was used to Decrypt the message transfarred through ENIGMA:


![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/BOMBES.png?raw=true)

---


**Let's get back to the part where Randomness was needed for Encryption**

We can generate truly Random Functions by measuring the Fluctuations which is known as **NOISE** . By sampling the we can predict the randomness. 

`How can we generate through NOISE?`

- #### 1. **Source of True Randomness:**

  True randomness is often derived from physical processes that are inherently unpredictable. Some common sources:

    **Electronic noise:** Thermal noise in resistors or shot noise in semiconductors.

    **Radioactive decay:** Random emission of particles.

    **Photon arrival times:** Quantum fluctuations in light detection.

    **Brownian motion:**  Random movement of microscopic particles in fluid.

These are unpredictable even if you know all initial conditions.

- #### **2. Measuring Fluctuations:**

  You need a device to measure the fluctuating signal from your source. Examples:
  Voltage across a resistor: Thermal noise produces tiny voltage variations.

  **Photon detector:**
        Records times photons hit a sensor.

The signal is analog, continuous, and noisy.

- #### **3. Sampling and Digitizing:**

    Convert the analog fluctuations to digital values:
      1)Use an ADC (Analog-to-Digital Converter) to sample the signal at discrete time intervals.
      2)The ADC output gives a series of numbers corresponding to the measured fluctuations.

Each measurement is slightly different due to the inherent randomness of the source.


- #### **4. Generating Random Numbers or Functions:**

    From these digital samples, you can construct:
    Random numbers (raw or post-processed to remove bias).

**Random functions:**
    Treat the sequence of measurements as a function over time or space.

  Example:

  f(ti)=xi​

  where xi is the digitized measurement at time ti. 

Smoothing '/' interpolation can turn discrete samples into a continuous random function if needed.

---


# **PSEUDO RANDOM NUMBER GENERATOR**

We can generate Truly Random functions by generating and analysing random Fluctuations known as **NOISE** . By measuring this **NOISE** known as sampling. 

**We can Obtain Numbers from this NOISE**

Here's an image of **NOISE** :

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Noise.png?raw=true)


For example if we analyse the electric current of TV static overtime we'll generate a truly sequence of random numbers. We can visualize these random sequences by drawing a path according to each numbers. This called **"Random Walk"** . At each point of the sequence the next move is always unpredictable. 

Random processes are said to be non-deterministic since they are tough to determine in advance. Machines, on the other hand, are deterministic. They are operatable, predictable and controlable . 

So **ENIAC** had a very limited internal memory for storing long sequences of random numbers. So, Neuman developed an Algorithm for storing those sequences of random numbers. Pseudo-random numbers (PRNs) are numbers generated by an algorithm that appear random but are actually deterministic (produced by a formula) . 

**They are called “pseudo or random” because if you know the algorithm and the starting value (called the seed), you can reproduce the same sequence exactly.**

### **How Does a Pseudo-Random Number Algorithm Work?**

Most pseudo-random number generators (PRNGs) work by starting with a seed and repeatedly applying a mathematical function to generate new numbers.

- #### **Middle-Square Method (von Neumann, 1946):**
  
This was one of the earliest PRNGs.
  1) Choose a starting seed (say 1234).
  2) Square it → 1234² = 1522756.
  3) Take the middle digits (e.g., 2275).
  4) That becomes the next random number.
  5) Repeat.


- #### **Linear Congruential Generator (LCG) (later improvement):**

Formula: Xn+1 = (a*Xn + C) mod m
 
 where X0 = Seed 

 a,c,m are carefully chosen Constants. 

 This formula Produces long sequences that look random .


**Let's dive into the history for Pseudo Number genrator. Why it was made in the first place?**

Von Neumann created pseudo-random numbers in the 1940s, during the early days of computers, mainly for Monte Carlo simulations (used in physics, nuclear research, and wartime projects like the Manhattan Project). Computers were deterministic, so they couldn’t generate true randomness.
He devised the middle-square method to give computers a way to produce “random-looking” numbers for simulations.

Von Neumann famously said:
“Anyone who considers arithmetical methods of producing random digits is, of course, in a state of sin.”
He knew they weren’t truly random, but they were good enough for practical use at the time.

---

**Let's Face a question**

`What's the difference between Randomly Generated and Pseudo Randomly Generated Numbers?`


| Feature            | Random Numbers (True Random)            | Pseudo-Random Numbers (PRNG)               |
|--------------------|------------------------------------------|---------------------------------------------|
| **Source**         | Natural/physical phenomena (e.g., radioactive decay, atmospheric noise) | Mathematical algorithms (e.g., Linear Congruential Generator) |
| **Reproducibility**| Cannot be repeated                      | Repeatable if the seed is known             |
| **Predictability** | Completely unpredictable                | Predictable if algorithm + seed are known   |
| **Speed**          | Slower (requires hardware)              | Very fast (software-based)                  |
| **Quality**        | Truly random                            | Only *appears* random (deterministic)       |
| **Use Cases**      | Cryptography, lotteries, gambling       | Games, simulations, testing, ML, graphics   |
