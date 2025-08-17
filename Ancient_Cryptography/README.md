## **What is Cryptography?**

Let's Explain this with a Simple Example of Data Transmission between Alice and Bob where a person named Eve will try to intercept the informations bewtween them:

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Alics_Bob_Eve_Transmission.png?raw=true)

Alice Shares a code with Bob that only Bob will have access to the datas. This is called **ENCRYPTION** . Bob will then use the code to access the data. This is called **DECRYPTION** . 

The codes will be created in such a way that even if a 3rd person named Eve tries to intercept the messages that is being transfarred between Bob and Alice, he will fail as those messages will seem meaningless to him. Example: **Caeser Cipher** .

But then a major breakthrough was made after 800 years by the acquiring the method called **FREQUENCY ANALYSIS** . 


## **What is 'Frequency Analysis' ?**

![image alt](https://github.com/KraKEn-bit/Cryptography/blob/main/Images/Frequency_of_Letters.png?raw=true)

See how the graphical presentations of each english letter is acting. Every English letters have their own Frequency. It means how many time a letter has been used in a sentence or context.

For example:  In English:
- `E` is the most common letter
  - `T`, `A`, `O`, `I`, `N` follow
- By comparing the frequency of letters in the ciphertext to expected frequencies in the language, an attacker can **guess the substitutions**.

So,
**Frequency Analysis** is a technique used in cryptography to **break classical ciphers** by studying the frequency of letters or groups of letters in a ciphertext.
