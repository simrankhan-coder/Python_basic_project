import requests
def convert_currency(from_currency,to_currency,amount):
    url=f"https://api.exchangerate.host/convert"
    params={"from":from_currency,
            "to":to_currency,
            "amount":amount
            }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 
        data = response.json()
        if data.get('success'):
            converted = data['result']
            print(f"{amount:.2f} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
        else:
            # The API call was not successful, so print the reason from the response
            print("Error: The conversion was not successful.")
            error_info = data.get('error', {})
            print(f"Reason: {error_info.get('info', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        print(f"Network or API Error: {e}")
    except KeyError:
        # Fallback for unexpected API response format
        print("Error: Unexpected response format from the API.")

fro = input("Enter the currency you want to convert from (e.g., USD): ")
to = input("Enter the currency you want to convert to (e.g., EUR): ")
try:
    amo = float(input("Enter the amount: "))
    convert_currency(fro, to, amo)
except ValueError:
    print("Invalid amount entered. Please enter a valid number.")

