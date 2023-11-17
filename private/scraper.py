import httpx
from selectolax.parser import HTMLParser

url = "https://duunitori.fi/tyopaikat?alue=Uusimaa&haku=software%3Bjunior"
headers = {"Use-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

response = httpx.get(url, headers=headers)
if response.status_code == 200:
    html = HTMLParser(response.text)
    print(html.css_first("title").text())
    jobs = html.css(".job-box__content")
    for job in jobs:
        jobs = {
            "Job": job.css_first("h3").text(),
            "Location": job.css_first(".job-box__job-location").text(),
            "Listed": job.css_first(".job-box__job-posted").text(),

        }
        print(jobs["Job"], jobs["Location"], jobs["Listed"])
        print("")

else:
    print("Faulty status code")
