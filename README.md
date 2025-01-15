# Shodan Domain Information and Vulnerability Lookup

This project is a Python script that utilizes the [Shodan API](https://www.shodan.io/) to gather information about a target domain. It resolves the domain to its corresponding IP address, retrieves detailed information about the IP, and checks for known vulnerabilities.

## Features

- Resolves a domain to its IP address using Shodan's DNS Resolve API.
- Fetches information about the target IP, such as:
  - Organization
  - Operating System
  - Open Ports
  - Service Banners
- Lists known vulnerabilities (CVEs) associated with the target IP and fetches exploit details (if available).

## Prerequisites

- Python 3.x
  -Ensure you have Python installed.
    -To check if Python is installed on your system, run: 'python --version'
    -To install python3 use 'apt install python3'
  
- Shodan account and API key
  -Create a Shodan account at [Shodan](https://www.shodan.io/)
  -After logging in, navigate to the API Keys section in your dashboard to copy your API key.
  -Install shodan in your linux system using 'pip3 install shodan'
  
- Installed dependencies (`shodan` and `requests` Python modules)

