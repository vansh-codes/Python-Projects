# Currency Converter Project

This project includes two versions of a currency converter:

1. **Non-GUI Version**: A command-line script for currency conversion.
2. **GUI Version**: A Tkinter-based graphical user interface for the same functionality with API Integration.

## Project Structure

```bash
currency_converter/
│
├── currency_converter.py
├── gui_currency_converter.py
├── .env
└── README.md
```

## Setup Instructions

### 1. Install Dependencies

For the GUI version, you need to install the `requests` and `python-dotenv` libraries. You can do this using pip:

```bash
pip install requests python-dotenv
```

### 2. Set Up Environment Variables

To use the API key securely, follow these steps:

1. **Create a `.env` File:**

   In the root directory of the project, create a file named `.env` and add your API key in the following format:

   ```
   API_KEY=your_actual_api_key
   ```

2. **Add `.env` to `.gitignore:**

   Ensure the `.env` file is not committed to version control. Add `.env` to your `.gitignore` file:

   ```
   .env
   ```

### 3. Run the Scripts

- **Non-GUI Version:**

  You can run the command-line version directly:

  ```bash
  python currency_converter.py
  ```

- **GUI Version:**

  To run the Tkinter GUI version, use:

  ```bash
  python gui_currency_converter.py
  ```

## Usage

- **Non-GUI Version:**

  Follow the prompts in the terminal to select currencies, enter conversion rates, and specify the amount to be converted.

- **GUI Version:**

  Use the graphical interface to select currencies, enter the amount to be converted, and view the result in the application window.

## Additional Information

- Make sure to replace `"your_actual_api_key"` in the `.env` file with a valid API key from your chosen exchange rate service.
- The API key is required for the GUI version to fetch real-time conversion rates.

For any issues or questions, feel free to open an issue on the GitHub repository or contact the project maintainers.

## 📞Contact

For any questions or feedback, please contact [vansh-codes](https://github.com/vansh-codes).

### - Created by **Vansh Chaurasiya** 
Show some ❤️ by starring this repository !


## 🔗Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vanshchaurasiya24)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://www.twitter.com/vanshchaurasiy4) <p align="right"><a href="#top">BACK TO TOP</a></p>