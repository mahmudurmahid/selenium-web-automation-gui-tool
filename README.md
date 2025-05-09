# Selenium Web Automation GUI Tool

A simple and intuitive web automation tool built with Selenium for automating various web tasks via a user-friendly graphical interface.

## 📖 Table of Contents

- [🎓 Selenium Web Automation GUI Tool](#selenium-web-automation-gui-tool)
- [📖 Table of Contents](#table-of-contents)
- [🧑‍💼 User Experience (UX)](#user-experience-ux)
  - [🧾 User Stories](#user-stories)
- [🎨 Design](#design)
  - [🗂 Interface Structure](#interface-structure)
  - [🌈 Color Scheme & Typography](#color-scheme--typography)
- [🚀 Features](#features)
  - [✅ Implemented Features](#implemented-features)
  - [🛠️ Planned Improvements](#planned-improvements)
- [💻 Technologies Used](#technologies-used)
  - [🧑‍💻 Languages Used](#languages-used)
  - [📚 Libraries Used](#libraries-used)
- [📁 Project Files](#project-files)
- [🛠 Installation & Usage](#installation--usage)
  - [⚙️ How to Run](#how-to-run)
  - [🧾 Database Configuration](#database-configuration)
- [✅ Testing](#testing)
- [🙌 Credits](#credits)
  - [👨‍💻 Author](#author)
  - [🧰 Tools & Technologies](#tools--technologies)
  - [📚 Learning Resources & Documentation](#learning-resources--documentation)
  - [💡 Inspiration](#inspiration)
  - [🤝 Contributions](#contributions)

## 🧑‍💼 User Experience (UX)

The tool is designed to be intuitive and user-friendly. Its goal is to enable users to automate tasks such as form filling, scraping data, or web browsing, using a simple graphical interface.

### 🧾 User Stories

- **As a user**, I want to be able to automate repetitive tasks on a webpage using a GUI interface without needing to write code.
- **As a user**, I want to be able to input various parameters such as URLs, form fields, and other automation tasks, so I can customize the automation process.
- **As a user**, I want to receive clear feedback from the application on the status of the automation process (e.g., success or failure messages).

## 🎨 Design

### 🗂 Interface Structure

The interface is divided into key sections for easy navigation:

1. **Main Window**: Displays the tool’s primary functionality for interacting with web pages.
2. **Input Fields**: Allow the user to specify web elements and their actions (e.g., URL, form field identifiers, button clicks).
3. **Action Controls**: Buttons for running automation, stopping tasks, and viewing results.
4. **Logs/Status Area**: Displays logs or statuses of the current automation process.

### 🌈 Color Scheme & Typography

- **Primary Colors**: Light blue and green tones to ensure a modern, clean look.
- **Typography**: The tool uses a combination of **Poppins** for headers and **Lato** for body text to create an approachable and professional user experience.
- **Button Styles**: Softly rounded buttons with hover effects to enhance usability.

## 🚀 Features

### ✅ Implemented Features

1. **URL Input**: Users can input the URL of the web page they wish to automate tasks on.
2. **Automated Form Filling**: Automatically fills form fields based on pre-set input values.
3. **Button Click Automation**: Clicks on buttons or links as specified by the user.
4. **Web Scraping**: Extracts data from specified elements on a web page.
5. **Browser Control**: Provides start, stop, and reset options to control the browser session during automation.

### 🛠️ Planned Improvements

- **Multiple Browser Support**: Enable support for various browsers (e.g., Chrome, Firefox, Edge).
- **Error Handling**: Improve error handling to provide more detailed logs and feedback during task execution.
- **Custom Script Execution**: Allow users to run custom Python scripts alongside the GUI tool for advanced automation.
- **Export Results**: Implement functionality to export automation logs and scraped data to CSV or Excel files.

## 💻 Technologies Used

### 🧑‍💻 Languages Used

- **Python**: The main programming language used for implementing automation logic and the backend.
- **HTML/CSS**: For creating the GUI layout and styling the application.
- **JavaScript**: Used in the GUI for handling dynamic elements and actions.

### 📚 Libraries Used

- **Selenium**: The core library for web automation.
- **Tkinter**: Used for creating the GUI interface.
- **WebDriver**: Helps manage the browser instance for automating tasks.
- **Pillow**: For image handling and GUI element customization.
- **pyautogui**: Allows the automation of mouse and keyboard events for better UI interaction.

## 📁 Project Files

- **/src**: Contains the main codebase for the automation tool.
  - **gui.py**: The main GUI file that defines the interface and handles user interactions.
  - **automation.py**: Contains the logic for automating web tasks using Selenium.
  - **utils.py**: Helper functions for logging, handling inputs, and interacting with the web.
- **/assets**: Contains icons, images, and other assets for the GUI.
- **/docs**: Documentation files, including a user manual and installation guide.

## 🛠 Installation & Usage

### ⚙️ How to Run

1. **Clone the repository**:

   ```bash
   git clone https://github.com/mahmudurmahid/selenium-web-automation-gui-tool.git
   cd selenium-web-automation-gui-tool
   ```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python gui.py
```

### 🧾 Database Configuration

Currently, this tool does not require any database setup. However, for future enhancements (e.g., saving automation logs or task histories), a database connection can be implemented.

## ✅ Testing

Thorough testing is essential to ensure the reliability of any automation tool. This project includes the following types of tests:

### 🧪 Test Structure

- **Unit Tests**:

  - Located in the `tests/` directory.
  - Cover individual functions from `automation.py`, such as element locators, action triggers, and input validation.
  - Examples:
    - Testing form field input accuracy.
    - Verifying proper element selection via XPath or CSS selectors.
    - Ensuring correct logging output.

- **Integration Tests**:

  - Simulate complete automation workflows on mock or real websites.
  - Validate interactions between GUI inputs and Selenium actions.
  - Examples:
    - Full task: open a URL, fill a form, click a button, extract confirmation text.
    - Check if browser instances are managed (opened/closed) correctly.

- **GUI Tests (Manual)**:
  - Due to Tkinter’s limitations for automated GUI testing, manual checks are performed to ensure:
    - Buttons trigger correct events.
    - Inputs are properly collected and passed.
    - Application responds gracefully to user errors (e.g., invalid URL, missing selectors).

### 🚦 Running Tests

To execute tests (unit and integration):

1. Make sure all dependencies are installed:

   ```bash
   pip install -r requirements.txt
   pip install pytest
   ```

2. Run tests using pytest:

```bash
pytest tests/
```

3. (Optional) View test coverage:

```bash
pip install pytest-cov
pytest --cov=src tests/
```

## 🧼 Test Scenarios Checklist

| Feature                 | Test Type     | Status    |
| ----------------------- | ------------- | --------- |
| URL Input Validation    | Unit          | ✅ Passed |
| Form Field Input        | Unit          | ✅ Passed |
| Button Click Automation | Integration   | ✅ Passed |
| Log Output Verification | Unit          | ✅ Passed |
| Browser Control         | Integration   | ✅ Passed |
| GUI Input Flow          | Manual (GUI)  | ✅ Passed |
| Invalid Input Handling  | Unit / Manual | ✅ Passed |

---

## 🙌 Credits

This project is the result of dedicated efforts, learning, and inspiration from the wider Python and automation communities.

### 👨‍💻 Author

**Mahmudur Mahid**

- GitHub: [@mahmudurmahid](https://github.com/mahmudurmahid)

### 🧰 Tools & Technologies

| Tool/Library | Purpose                                    |
| ------------ | ------------------------------------------ |
| Python       | Core programming language                  |
| Selenium     | Web automation and browser control         |
| Tkinter      | GUI development                            |
| pyautogui    | GUI-level automation (optional use)        |
| Pillow       | Image support in GUI                       |
| WebDriver    | Browser instance management for automation |

### 📚 Learning Resources & Documentation

- [Selenium Python Bindings Documentation](https://selenium-python.readthedocs.io/)
- [Tkinter Widget Reference](https://docs.python.org/3/library/tkinter.html)
- [Python Official Documentation](https://docs.python.org/3/)
- YouTube tutorials, Stack Overflow discussions, and blog articles on automation scripting.

### 💡 Inspiration

- Real-world needs for simplifying repetitive web tasks.
- Tools like UiPath and browser automation plugins that inspired a lightweight, Python-based alternative.
- Community-driven GitHub projects showcasing Selenium + GUI implementations.

### 🤝 Contributions

Contributions, bug reports, and feature suggestions are welcome! Here's how to contribute:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/YourFeature
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add YourFeature"
   ```

4. Push to your fork:

   ```bash
   git push origin feature/YourFeature
   ```

5. Open a pull request with a clear title and description.
   🙏 Special thanks to all open-source contributors and educators who provide free learning resources that made this project possible.
