import requests

def get_ip_details(ip_address):
    url = f"http://ip-api.com/json/{ip_address}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"

    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] == "fail":
            print(f"Failed to get details. Reason: {data['message']}")
        else:
            print("IP Details:")
            for key, value in data.items():
                print(f"{key}: {value}")

    except requests.exceptions.RequestException as e:
        print(f"Error during the request: {e}")

# Example usage
ip_address =  input("enter ip address: ")
get_ip_details(ip_address)
