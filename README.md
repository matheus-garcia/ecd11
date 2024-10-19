# ecd11
ECD11 - Final Project

# Simple Data Pipeline with Linear Regression

This project is a simple data pipeline that reads a CSV file, preprocesses the data, and trains a linear regression model to make predictions. It showcases basic data handling, normalization, and machine learning concepts.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started, clone the repository and install the necessary dependencies.

```bash
git clone <repository_url>
cd <repository_name>
pip install -r requirements.txt
```

Make sure you have Python 3.10 or higher installed.

## Usage

To run the pipeline, provide the path to a CSV file with at least two columns: `value` and `target`.

### Example CSV Format

```csv
id,value,target
1,10,20
2,20,40
3,30,60
4,40,80
5,50,100
```

### Running the Script

You can run the script by executing:

```bash
python main.py <path_to_your_csv_file>
```

### Example Command

```bash
python main.py data/sample_data.csv
```

## Features

- Load data from a CSV file.
- Fill missing values in the `value` column with the mean.
- Normalize the `value` column to a range of [0, 1].
- Train a linear regression model on the processed data.
- Make predictions based on the trained model.

## Testing

This project includes unit tests to ensure the correctness of the data processing and model training functions.

To run the tests, simply execute:

```bash
pytest
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to add new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
