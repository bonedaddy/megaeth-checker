import requests
import time

def check_whitelist(address_file_path):
    # Read addresses from file
    with open(address_file_path, 'r') as file:
        addresses = [line.strip() for line in file if line.strip()]
    
    whitelisted = []
    base_url = "https://nft.megaeth.com/api/whitelist?address="
    
    print(f"Checking {len(addresses)} addresses...")
    
    for address in addresses:
        try:
            # Make API request
            response = requests.get(base_url + address)
            data = response.json()
            
            # Check if address is whitelisted
            if data.get('isWhitelisted'):
                whitelisted.append({
                    'address': address,
                    'persona': data.get('persona'),
                    'position': data.get('whitelistPosition'),
                    'mintType': data.get('mintType')
                })
            
            # Add a small delay to avoid overwhelming the API
            time.sleep(0.1)
            
        except Exception as e:
            print(f"Error checking address {address}: {str(e)}")
    
    return whitelisted

def main():
    # Replace with your file path
    file_path = 'addresses.txt'
    
    try:
        results = check_whitelist(file_path)
        
        print("\nWhitelisted Addresses:")
        print("=====================")
        
        for item in results:
            print(f"\nAddress: {item['address']}")
            print(f"Persona: {item['persona']}")
            print(f"Position: {item['position']}")
            print(f"Mint Type: {item['mintType']}")
        
        print(f"\nTotal whitelisted addresses found: {len(results)}")
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
