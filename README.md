
# Vaultify - A Password Management Application
Vaultify is a simple and secure password management application built using Python and Tkinter. It allows users to securely store and manage their passwords locally, offering features such as password generation, fuzzy search, clipboard integration, and keyboard shortcuts for clearing fields. This tool is designed for users who want a local and self-contained password manager without the need for external databases or cloud services.




## Features

- Local Storage: Stores passwords securely using Python's pickle module for local storage, ensuring your data remains private and protected on your machine.
- Password Generation: Allows users to generate strong, random passwords for their accounts.
- Fuzzy Search: Uses the fuzzywuzzy library to enable users to quickly find stored passwords, even with partial or misspelled searches.
- Clipboard Integration: Allows users to copy passwords to the clipboard for easy pasting into login forms, using the pyperclip library.
- Keyboard Shortcuts: Includes useful keyboard shortcuts like clearing input fields for a more efficient user experience.


## Requirements
To run this project, you need the following Python libraries installed:

- Tkinter - For creating the graphical user interface (GUI).
- pickle - For local data storage (standard Python library).
- fuzzywuzzy - For fuzzy string matching to search stored passwords.
- pyperclip - For clipboard operations, allowing easy copy-paste functionality.

```
pip install fuzzywuzzy pyperclip

```


## Run Locally

Clone the project

```bash
  git clone git@github.com:vijayramanujam/vaultify.git
```

Go to the project directory

```bash
  cd vaultify
```

Install dependencies

```bash
  pip install fuzzywuzzy pyperclip

```

Start the server

```bash
  python vaultify.py

```


## License

This project is open-source and available under the [MIT](https://choosealicense.com/licenses/mit/)

