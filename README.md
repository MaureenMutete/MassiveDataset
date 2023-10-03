# MassiveDataset

This project is a python based project working with the massive dataset from amazon.

## What to expect in the project

#### Pandas

- Utilizing Pandas to convert a large dataset of jsonl files into dataframes and storing all the dataframes in a list.
- Using these dataframes, merging them, and filtering out data that is not needed.
- Storing the filtered data into excel files.


## How the project works

The project works by first converting the dataset of jsonl files into dataframes, storing these in a list, and filtering out unnecessary data from these files. Once that is done,
 the data is stored into excel files. The filtered out data is then split using the "partition" column where data is seperated into 3 categories train, test and dev. These categories
 are stored in different jsonl files. Using the train category we translate english to the other languages, then store the result in a json file. Then we pretty print the json file structure.

## Prerequisites for a fully running project.
In order for one to have a fully running project one needs to have the following:

**Python installed in PC**

One can download and install it from the link: [Python](https://www.python.org/downloads/)

**Libraries**
- *Pandas*

   To install this library, type the following command
  
   `pip install pandas`
  
- *OS*

  In python by default
- *Json*

  In python by default
  

## Setting Up the Environment
  
After installing python, create an environment. The steps are as follows:

1. **Environment Setup:**

      Set up a Python3 development environment. Ensure that Python3 is installed on your system.

2. **Dependency Installation:**

      Install all relevant dependencies required for the project. These dependencies will vary depending on your specific use case, so make sure to install the necessary packages for your environment.

5. **Project Structure:**

      Create a Python3 project with the structure typical for projects in PyCharm or your preferred IDE.

   ## Relevant Sources
   In order for the project to be complete, extensive research was done from articles of related works and youtube tutorials.









