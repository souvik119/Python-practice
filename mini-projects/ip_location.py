import requests

ip_url = 'https://api.ipify.org'
location_url = 'http://ipinfo.io/json'

def get_ip(ip_url):
    '''
    Returns external IP address of the machine
    '''
    ip = requests.get(ip_url).content.decode('utf-8')
    return ip

def get_location(location_url):
    '''
    Returns city country and region of the computer
    '''
    response = requests.get(location_url)
    data = response.json()
    city = data['city']
    country = data['country']
    region = data['region']
    return city, country, region

def main():
    ip = get_ip(ip_url)
    city, country, region = get_location(location_url)
    print('Machine details : ')
    print(f'IP : {ip}')
    print(f'City : {city}')
    print(f'Country : {country}')
    print(f'Region : {region}')

if __name__ == '__main__':
    main()