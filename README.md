**Instagram Brute Force**

This project is a Python script that attempts to brute force an Instagram account password using a provided dictionary of passwords. It demonstrates how to use the `selenium` library to interact with the Instagram login page and how to generate potential passwords using itertools.

**Requirements**

- Python 3.x
- `selenium` library (`pip install selenium`)

**How to Use**

1. Clone the repository to your local machine:

```
git clone https://github.com/Shyam095/Instagram_bruteforce.git
cd instagram-brute-force
```

2. Install the required libraries:

```
pip install selenium
```

3. Generate a dictionary file containing possible passwords. You can use the provided `dictionary.txt` as an example or generate your own using the `dictionary_generator.py` script. To generate a dictionary file, run the following command:

```
python dictionary_generator.py
```

4. Edit the `instagram_brute_force.py` script to specify the `username` variable with the target Instagram account username and `dictionary` with the name of the dictionary file.

5. Run the `instagram_brute_force.py` script:

```
python instagram_brute_force.py
```

The script will attempt to log in to the target Instagram account using the passwords from the provided dictionary. If it successfully logs in, it will print the successful password. The script will stop after a successful login or after trying all the passwords in the dictionary.

**Disclaimer**

This project is for educational purposes only. Attempting to brute force an account without the account owner's permission is illegal and unethical. Please use this script responsibly and only on accounts you own or have explicit permission to test.

**Note**

- The script uses the `selenium` library to interact with the Instagram login page. Make sure you have the Chrome WebDriver installed and the appropriate version compatible with your Chrome browser. You can download the Chrome WebDriver from https://sites.google.com/a/chromium.org/chromedriver/downloads.

- The generated passwords in the dictionary can grow exponentially, leading to large output files. Please use this script responsibly and consider the storage and processing implications.

**Contributing**

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

**License**

[MIT License](LICENSE)

---

Remember that ethical considerations and responsible usage of this type of script are essential. Brute-forcing an account without permission is illegal and unethical. Please use this project responsibly and only for educational purposes or on accounts you own or have explicit permission to test.

If you have any questions or need further assistance, please don't hesitate to ask!
