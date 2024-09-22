<h1 align="center">
  <br>
  <a href="https://imgbb.com/"><img src="https://i.ibb.co/Stcxy90/Cortex-Link.png" width="250px" alt="Nuclei"></a>
</h1>
<h4 align="center">CortexLink** is a powerful command-line search tool built using Python, designed to search Google for specific topics, including CVE links, exploits, Proof of Concept (PoC) links, and educational materials. It supports language, region, and proxy configurations for customized and localized search results.</h4>

![CleanShot 2024-09-22 at 12 37 13@2x](https://github.com/user-attachments/assets/f29baaee-c1c6-4d63-aee0-6f79d8451f62)
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Basic Search](#basic-search)
  - [Available Search Options](#available-search-options)
  - [Language and Region Options](#language-and-region-options)
  - [Proxy and SSL Options](#proxy-and-ssl-options)
  - [Examples](#examples)
- [Features](#features)
- [License](#license)

## Installation
### Requirements
CortexLink requires Python 3 and the following Python libraries:

- `googlesearch-python`
- `colorama`
- `tabulate`

### Installation Steps
1. Clone the CortexLink repository from GitHub
```bash
git clone https://github.com/symbolexe/CortexLink.git
```

2. Navigate to the cloned directory
```bash
cd CortexLink
```
3. Install the required dependencies
```bash
pip install googlesearch-python colorama tabulate
```
## Usage
CortexLink can be used to perform different types of Google searches with options to filter by language, region, and more. Below is the general usage and the available search options.
### Basic Search
To run a basic search with CortexLink, you need to specify a query and a search type (e.g., CVE, exploit, PoC, or learning materials).
#### General Command
```bash
python CortexLink.py -<search-type> -query "<search-query>" [options]
```
#### Example
```bash
python CortexLink.py -cve -query "splunk" -region "us" -n 10
```
## Available Search Options
You must specify one of the following mutually exclusive options to define the search type,
- -cve: Search for CVE links.
- -exploit: Search for exploit-related links.
- -poc: Search for Proof of Concept (PoC) download links.
- -learn: Search for learning and educational resources.

## Language and Region Options
- [x] -lang: Specify the language for the search results. Default is en (English).
- Example: -lang fr for French results.

- [x] -region: Specify the region for the search results (e.g., us for the United States, fr for France).
- Example: -region uk for United Kingdom results.

## Proxy and SSL Options
- [x] --proxy: Use a proxy server for your searches (format: http://user:pass@host:port).
- [x] --ssl_verify: Disable SSL verification for proxies that require this.

## Other Options
- [x] -n or --num_results: The number of search results to return (default is 10).
- [x] --output: Specify the output file for the search results (default is Cortex-Link-Result.txt).
- [x] --table: Display results in a table format.
- [x] --no-color: Disable colored output in the terminal.
- [x] --sleep_interval: Time (in seconds) to wait between multiple requests to avoid rate-limiting (default is 0).

## Examples
### Search for CVE Links (10 results, US region)
```bash
python CortexLink.py -cve -query "splunk" -region "us" -n 10
```
### Search for Python Learning Materials in French
```bash
python CortexLink.py -learn -query "cours python" -lang "fr" -region "fr" -n 5
```
### Search for Exploits with Proxy and Table Output
```bash
python CortexLink.py -exploit -query "apache" --proxy "http://127.0.0.1:8080" --table -n 5
```
### Search for PoC Links with SSL Verification Disabled and Delay
```bash
python CortexLink.py -poc -query "splunk exploit" --ssl_verify --sleep_interval 5
```

## Features
- Search Types: Supports searching for CVEs, exploits, PoC, and educational materials.
- Localization: Allows filtering results by language (-lang) and region (-region).
- Proxy Support: Search using proxies with optional SSL verification disabling.
- Result Customization: Customize the number of results and display them in a table format.
- Rate Limiting: Avoid getting blocked by specifying a delay between requests using --sleep_interval.

## License
CortexLink is an open-source project released under the MIT License.
