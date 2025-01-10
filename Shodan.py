import shodan
import requests  # Corrected the import (was `request`, should be `requests`)

# Shodan API Key
SHODAN_API_KEY = "{SHODAN API KEY}"
api = shodan.Shodan(SHODAN_API_KEY)

# Target domain
target = 'target domain'

# Resolve the domain to an IP
dnsresolve = f'https://api.shodan.io/dns/resolve?hostnames={target}&key={SHODAN_API_KEY}'

try:
    # Resolve target's domain to an IP
    resolved = requests.get(dnsresolve)
    resolved.raise_for_status()  # Raise exception if request fails
    hostIP = resolved.json()[target]

    # Perform a Shodan search on the resolved IP
    host = api.host(hostIP)
    print(f"IP: {host['ip_str']}")
    print(f"Organization: {host.get('org', 'n/a')}")
    print(f"Operating System: {host.get('os', 'n/a')}")

    # Print all banners
    for item in host['data']:
        print(f"Port: {item['port']}")
        print(f"Banner: {item['data']}")

    # Print vulnerability information
    if 'vulns' in host:
        for item in host['vulns']:
            CVE = item.replace('!', '')
            print(f"Vulnerability: {CVE}\n")
            exploits = api.exploits.search(CVE)
            for exploit in exploits['matches']:
                if exploit.get('cve') and CVE in exploit.get('cve'):
                    print(f"Description: {exploit.get('description')}")

except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")
except shodan.APIError as e:
    print(f"Shodan API Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
