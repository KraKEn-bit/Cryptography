The Caesar Cipher is a type of shift cipher. Shift Ciphers work by using the modulo operator to encrypt and decrypt messages. The Shift Cipher has a key K, which is an integer from 0 to 25. We will only share this key with people that we want to see our message.


<br>

# **How to Encrypt:**

For every letter in the message M :

   -  Convert the letter into the number that matches its order in the alphabet starting from 0, and call this number X.
      ( A=0, B=1, C=2, ...,Y=24, Z=25)
   -  Calculate: Y = (X + K) mod 26
   -  Convert the number Y into a letter that matches its order in the alphabet starting from 0.
      (A=0, B=1, C=2, ...,Y=24, Z=25)

For Example: We agree with our friend to use the Shift Cipher with key K=23 for our message. 
We encrypt the message "RAFSAN", as follows:​


**Plaintext:** `RAFSAN`  
**Key (k):** 23  

### Step 1: Convert letters to numbers (A=0, B=1, ..., Z=25)

| Letter | R | A | F | S | A | N |
|--------|---|---|---|---|---|---|
| Value  | 17| 0 | 5 | 18| 0 | 13|

### Step 2: Apply Caesar cipher formula

\[
C = (P + k) \mod 26
\]

| P  | 17 | 0  | 5  | 18 | 0  | 13 |
|----|----|----|----|----|----|----|
| C = (P+23) mod26 | 14 | 23 | 2  | 15 | 23 | 10 |

### Step 3: Convert numbers back to letters

| C  | 14 | 23 | 2  | 15 | 23 | 10 |
|----|----|----|----|----|----|----|
| Letter | O  | X  | C  | P  | X  | K  |

###  Encrypted Text: OXCPXK

<br>
<br>

---

# **How TO Decrypt:**

For every letter in the cipher text C :<br>
   - Convert the letter into the number that matches its order in the alphabet starting from 0, and call this number Y.
      (A=0, B=1, C=2, ..., Y=24, Z=25)
   - Calculate: X= (Y - K) mod 26
   - Convert the number X into a letter that matches its order in the alphabet starting from 0.
      (A=0, B=1, C=2, ..., Y=24, Z=25)
     
Our friend now decodes the message using our agreed upon key K=23. As follows:

**Ciphertext:** `O X C P X K`  
**Key (k):** 23  

### Step 1: Convert letters to numbers (A=0, B=1, ..., Z=25)

| Letter | O | X | C | P | X | K |
|--------|---|---|---|---|---|---|
| Value  | 14| 23| 2 | 15| 23| 10 |

### Step 2: Apply Caesar cipher decryption formula

\[
P = (C - k) \mod 26
\]

| C  | 14 | 23 | 2  | 15 | 23 | 10 |
|----|----|----|----|----|----|----|
| P = (C - 23) mod26 | 17 | 0  | 5  | 18 | 0  | 13 |

### Step 3: Convert numbers back to letters

| P  | 17 | 0  | 5  | 18 | 0  | 13 |
|----|----|----|----|----|----|----|
| Letter | R  | A  | F  | S  | A  | N  |

###  Decrypted Text: RAFSAN
