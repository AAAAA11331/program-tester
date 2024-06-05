
# Grading System


## Introduction

This project is a grading system designed to automate the evaluation of student assignments. It includes a text-based user interface for ease of use, grading logic encapsulated in modular code, and utility functions to support the main functionalities.

## Features

- **Automated Grading**: Automatically evaluates student assignments based on predefined criteria.
- **Text User Interface (TUI)**: Easy-to-use interface for interacting with the grading system.
- **Utility Functions**: Includes various utility functions to support the main grading logic.

## Installation

### Prerequisites

- Python 3.x
- Required Python packages (listed in `requirements.txt`)

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/gradingsystem.git
   ```
2. Change to the project directory:
   ```sh
   cd gradingsystem
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To run the grading system, execute the following command:

```sh
python main.py
```

Follow the on-screen instructions to use the text-based user interface for grading.

## Project Structure

The project is organized as follows:

```
gradingsystem/
│
├── main.py          # Main script to run the project
├── grading.py       # Module for grading logic
├── tui.py           # Text User Interface
├── utils.py         # Utility functions
├── README.md        # Project README
└── requirements.txt # List of dependencies
```

### main.py
The entry point of the project, which initiates the grading process and user interface.

### grading.py
Contains the logic for evaluating and grading student assignments.

### tui.py
Handles the text-based user interface for user interaction with the grading system.

### utils.py
Provides various utility functions used throughout the project.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request
