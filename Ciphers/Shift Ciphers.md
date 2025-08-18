The Caesar Cipher is a type of shift cipher. Shift Ciphers work by using the modulo operator to encrypt and decrypt messages. The Shift Cipher has a key K, which is an integer from 0 to 25. We will only share this key with people that we want to see our message.


<br>

# **How to Encrypt:**

For every letter in the message M :
    - 1. Convert the letter into the number that matches its order in the alphabet starting from 0, and call this number X.
      ( A=0, B=1, C=2, ...,Y=24, Z=25)
    - 2. Calculate: Y = (X + K) mod 26
    - 3. Convert the number Y into a letter that matches its order in the alphabet starting from 0.
      (A=0, B=1, C=2, ...,Y=24, Z=25)

For Example: We agree with our friend to use the Shift Cipher with key K=19 for our message. 
We encrypt the message "KHAN", as follows:​
