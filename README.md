# Paytm Mall Pickles Scraper

This Python script scrapes pickle products data from the Paytm Mall website. It retrieves information such as pickle name and price.

## Overview

The script utilizes BeautifulSoup and requests libraries to fetch and parse data from the specified Paytm Mall URL (`https://paytmmall.com/fmcg-sauces-pickles-glpid-101471?page=1&latitude=12.8682381&longitude=77.7129198`). It extracts details of each pickle product listed on the webpage and prints out processed data.

## How It Works

The script performs the following steps:

1. **Fetching Data**: It sends a request to the Paytm Mall webpage containing pickle products.

2. **Parsing HTML**: It uses BeautifulSoup to parse the HTML content of the webpage.

3. **Extracting Pickle Details**: It locates the relevant HTML elements containing pickle names and prices.

4. **Processing Data**: It processes each pickle name to remove unnecessary text and formats the data for display.

5. **Displaying Data**: It prints the processed pickle names.

## Usage

To use this script:

1. Clone the repository or download the `pickledb.py` file.

2. Make sure you have Python installed on your system.

3. Install the required libraries using pip:

4. The script will print the processed pickle names extracted from the Paytm Mall webpage.

## Example Output

Here is an example of the output produced by the script:

```
MTR Mixed Pickle
Maggi Hot & Sweet Tomato Chilli Sauce
Gits Instant Mix Rava Dosa Mix
```


Thank you for using the Paytm Mall Pickles Scraper. Enjoy exploring pickle products on Paytm Mall!


