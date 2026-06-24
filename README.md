# Privournal

Privoural (Private + Journal, Hehe) is a cool command-line journal encryptor! 

Write your journal anywhere like Notes, Notion, whatever - and then paste it into Privournal, and get back text that's unreadable to anyone. You can then paste that text back into your journaling app, only now even if anyone opens that app, the encrypted journals are unreadable :)

<img width="1280" height="725" alt="ezgif com-video-to-gif-converter (3)" src="https://github.com/user-attachments/assets/7c38b515-9e84-4cf0-af91-ec136bca4c99" />

(This GIF displays the first fully functional version of Privournal 😇)

---

And if you wanna read it? No problem! Open terminal (No internet required) and decrypt the whole thing in under a minute using Privournal. 

It's as easy as that, plus you can make an account on Privournal so that your encryption details can be stored on the database that is private to you, making the process of decryption much smoother!

And if you want to continue without an account - You absolutely can! 

---

> **NOTE:**  PRIVOURNAL RUNS COMPLETELY LOCALLY AS OF NOW, IT NO DATA EXCEPT ACCOUNT DETAILS AND ENCRYPTION KEYS (That too on your own sql lite local database), ECRYPTIONS AND DECRYPTIONS ARE PURELY DONE BY LOGIC AND ENCRYPTION KEY IN USER'S ACCOUNT.

---

> **NOTE:**  Each letter's mapping is reffered to as a cover. For example, if A maps to 27 - then A's cover be 27. An Encryption Key is a dictionary containing the letters and thier covers. 

---

## Demo + Try it yourself!

I will also be uploading a commercial style demo video too, Hehe, it might help you see how the flow looks like in action.
(It will be uploaded on Privournal's Youtube chaneel and don't worry i'll add the link here too!

For now,

See the demo video - **[Watch the demo](https://asciinema.org/a/SRpkqli7cZZXNHVp)**

Even better would be that you try it yourself! I'd really love that :) 
(Look at the PyPI section below!) 


## Install via PyPI

Want to try Privournal yourself? 

> **NOTE:** Make sure your device has python version >= 3.9.0, if not then download it, barely takes a minute! :)

Just open the terminal and run these commands :)

```bash
pip install privournal
```

Then launch it using:

```bash
privournal
```

No need to clone the repository manually this way!

If you have already installed it and want to update it to the newest version, type this into terminal :

```bash
pip install --upgrade privournal
```
Thank you!

## How did the idea stumble upon me?

For me, someone reading my journal is a legit nightmare. I journal on notes sometimes, and it's not just journals, sometimes it's random texts or even chats. So it's happened to me a lot that people open my notes app and start reading 😭

You might say - Manonit why don't you just lock the notes? Well atleast on apple devices, anyone can open the locked notes if they have their fingerprint on the device or the laptop password. (And obviously your laptop password isn't that secret 🥲)

This is where Privournal comes in - It instead converts your entry into ciphertext using a substitution scheme that you can control, so even if the encrypted text leaks, it's just numbers and symbols without the key (Which only you have). 


## Simplified Process at Glance :)

1. Write your journal entry in any app you like.
2. Paste the full text into Privournal.
3. Choose an encryption mode (see below).
4. Privournal returns the encrypted version - paste that back into your journal app instead of the plaintext.
5. To read it later, run Privournal's decrypt flow with the same Key/Account.

No journal content is ever stored. If you make an account, only your encryption *key* (the cover mapping) is saved to the database — never the journal text itself. Without an account, you have to copy-paste the encrypted text and the encryptiong key somewhere.


## Encryption Modes

| Mode | How it works |
|------|--------------|
| **Mark 1** | Each letter maps to a number, A–Z as 1 to 26, a–z as 27 to 52 |
| **ASCII** | Each letter maps to its raw ASCII code |
| **Mark 2** | Reverse-order numbering (A=26, Z=1, From 26 to 1 and 52 to 27 |
| **Mark 3** | Even/odd split — capitals get even numbers, lowercase get odd (From 1 to 52) |
| **Mark 4** | Mirror-alphabet substitution (A=Z, B=Y, ...) |
| **Custom Advanced Encryption** | You manually assign every letter's cover - a number, symbol, another letter, or any combination |
| **Randomised Advanced Encryption** | Our code generates random covers (Like A = x08a792) that are assigned as every letter's cover |


### The Swiption Feature!

The strongest and the most original encryption idea I had! Swiption - (Switch + Encryption, 🙃)

Instead of one fixed cover for each letter, Swiption lets a single letter rotate between multiple covers based on occurrence count. And Swiption by default only runs on Randomised Mode. 

You control exactly when the rotation happens by choosing a "life" value! (Life is the number of occurances after which the cover will be switched to something else) 

For example, "A" initially points to a207n4 and the life has been set to 4 by the user - Now this means that at every 4th occurance of "A" in your journal, the cover will be replaced!

Initially "A" could point to a207n4 and towards the end it could point to something entirely different! A dynamic Encryption :) 


## Accounts

Every time you encrypt, you will be given an Encryption Key that you need to copy and paste somewhere handy. However for users with an account - the Encryption Key is automatically upoloaded to the database and there's no need to store it seperately :) 

While decrypting, if you don't have an account - you must paste the Encryption Key that was provided to you. For users with an account, the Encryption Key will be automatically fetched from the database once you choose which jounal you need to decrypt.


## Technology behind it!

To be honest, I only know Python, that too intermediate level i'd say 😅 

So I coded the whole thing in Python and connected it to a local SQLite database for account storage.

One thing I'm proud of is that there is no database setup required anymore. Privournal automatically creates its own local database on first launch, so it can run locally on any device after installation. 

My highschool CS classes came in real handy Hehe!

Pure terminal app - no GUI yet :)

> **NOTE:** Earlier, Privournal used a MySQL backend for account storage. While it worked on my device, it required users to set up and configure a database before running the program, which wasn't ideal for a tool meant to be easy to install (Obvi lol). So I later moved the project to SQLite, allowing Privournal to create and manage its own local database automatically with zero setup. (Tho a unified MySQL backend still remains my future goal 🙃)

## Small Caveats!
- The Decryption glitches if there are numbers or special symbols in the journal without any gap - Not huge glitches, just a few letters left encrypted. (Will be fixed in V2)
- Encrypted text must be copied whole, even the last trailing space and it should be inputted in a single line - just paste it whole is what I mean to say :)
- The banner and Guide function was made by GPT, I tried making the banner myself but mine looked skinny and I was running low on time, so i got both made by GPT 😭

## What's next!

- Make Privournal's local SQLite database optionally sync with a secure cloud backend (Like a unified db thing)
- Introduce Swiption among Basic Encryption
- Password protection on Encryption Keys
- Eventually a real GUI, possibly a website, so Privournal doesn't live only in the terminal :) 
- Privournal Extension that encrypts chat messages in real time and decrypts them when you tap on messages. (Biggest upgrade!)

## Acknowledgements

- Built as part of [Stardance](https://stardance.hackclub.com), summer 2026.
- Uses sql lite - python connection.
- Thanks to the Python and MySQL documentation.
- GPT for error finding when i failed to see what's wrong with da code 🥲
- Thanks to my brother too, he pointed out 2 major flaws that sneaked past my eyes.  
- Lastly thanks to me 🙄 (For fixing the errors for hours and writing a 1400+ liner code Hehe)

---

*Thank you so much for reading this far — I really really genuinely appreciate it A LOT.*
*Have a nice day!*
