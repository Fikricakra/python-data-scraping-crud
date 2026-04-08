# web_scraper.py
import requests
import json
import csv
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    countries = soup.find_all("div", class_="col-md-4 country")

    data = []

    for country in countries:
        nama = country.find("h3", class_="country-name").text.strip()
        Capital = country.find("span", class_="country-capital").text.strip()
        Population = country.find("span", class_="country-population").text.strip()
        Area = country.find("span", class_="country-area").text.strip()
        data.append({
            "negara": nama,
            "ibu_kota": Capital,
            "populasi": Population,
            "luas": Area,
        })

    print(data)

    with open("countries.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Data berhasil disimpan ke countries.json")

    with open("countries.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["negara", "ibu_kota", "populasi", "luas"])
        writer.writeheader()
        writer.writerows(data)

    print("Data berhasil disimpan ke countries.csv")

else:
    print("Gagal mengakses halaman.")
