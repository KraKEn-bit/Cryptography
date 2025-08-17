# **What is Cryptography?**

Let's Explain this with a Simple Example of Data Transmission between Alice and Bob where a person named Eve will try to intercept the informations bewtween them:

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Alics_Bob_Eve_Transmission.png?raw=true)

Alice Shares a code with Bob that only Bob will have access to the datas. This is called **ENCRYPTION** . Bob will then use the code to access the data. This is called **DECRYPTION** . 

The codes will be created in such a way that even if a 3rd person named Eve tries to intercept the messages that is being transfarred between Bob and Alice, he will fail as those messages will seem meaningless to him. Example: **Caeser Cipher** .

But then a major breakthrough was made after 800 years by the acquiring of the method called **FREQUENCY ANALYSIS** . 



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



# **POLYALPHABETIC CIPHER:**

A **Polyalphabetic Cipher** is a type of substitution cipher in which **more than one alphabet is used** to encrypt the message. This makes it **much harder to break** using frequency analysis compared to monoalphabetic ciphers like Caesar Cipher.

### **How it Works**

- Each letter of the plaintext is shifted according to a **repeating keyword** or **master word**.  
- Example: Keyword = `KEY`

For example:
Encrypting the message **"LOVE"** using the key or master keyword **"SLIP"**.

---
Let's assume (A=1,B=2,...Z=26)


| Step | Plaintext | Equivalent Numbers | Key / Master Word | Key Numbers | Sum (mod 26) | Ciphertext |
|------|-----------|------------------|-----------------|------------|---------------|------------|
| 1    | L         | 11               | S               | 18         | 29 → 3        | D          |
| 2    | O         | 14               | L               | 11         | 25            | Z          |
| 3    | V         | 21               | I               | 8          | 29 → 3        | D          |
| 4    | E         | 4                | P               | 15         | 19            | T          |

---

So, placed the message "LOVE" over the master word "SLIP" . This method is known as **SHIFTING** . 

## **Frequency Fingerprint**

**Frequency Fingerprinting** is a method used to **identify the language or probable plaintext** by analyzing the **frequency patterns of letters or symbols** in a ciphertext.

---

### How it Works

1. Each language has a **distinct frequency distribution** of letters.  
   - For example, in English: E > T > A > O > I > N > …  
2. Count the occurrences of each letter in the ciphertext.  
3. Compare the distribution with known **language frequency patterns**.  
4. The **closest match** helps identify the language or plaintext characteristics.  

---

Here's a simple program to demonstrate the Frequency Fingerprints:

[Frequency Fingerprint](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/pi/frequency-fingerprint-exploration)


**Let's Face a Question**

`Any Time there's a Differential in Letter frequencies; a leak of information occurs. These are caused by repeatation of the encrypted message. What does it mean?`

Ans: With each code there is almost always some form of patters no matter how minor it is. Each pattern/unique difference is something that may stand out which will draw the attention to the intercepter's mind that could be dangerous for its privacy. 

For example: Frequency of words in a sentence. 

**The best code will have a lessened "Fingerprint" or more minuscle and therefore harder to intercept.** 

`How can Someone design a cypher that hides her fingerprint?`

Ans: By Randomness/Random Shifting method. As a result Frequency distribution will be uniform. It is known as **ONE TIME PAD**


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

### **Encryption Process:**

Each plaintext letter is combined with a truly random key letter (mod 26).
Example: Plaintext H + Random key X → Ciphertext letter.

### **Effect on Ciphertext:**

Because the key is completely random, every possible ciphertext letter is equally likely, regardless of the plaintext.
This means the letter frequency in the ciphertext is uniform.

### **Implications:**

Frequency analysis is useless against OTP.
The ciphertext contains no patterns, so an attacker cannot deduce anything about the plaintext from the ciphertext alone.

This is why OTP is called “perfectly secure”.

Here's a simple image to understand the frequency distributions of the letters:

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Uniform%20Distribution%20of%20letters.png?raw=true)
