import requests
from requests.structures import CaseInsensitiveDict

url = "https://es.privalia.com/api/authentication/front/v1/login"

headers = CaseInsensitiveDict()
headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0"
headers["Accept"] = "*/*"
headers["Accept-Language"] = "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3"
headers["Accept-Encoding"] = "gzip, deflate, br"
headers["Referer"] = "https://es.privalia.com/gr/portal"
headers["Content-Type"] = "application/json"
headers["User-Agent-Custom"] = "vp-groot-mobile"
headers["mpDistinctId"] = "1812a72405cd5-08b3112aedd2ed8-97f2736-1fa400-1812a72405dd3"
headers["formName"] = "portal"
headers["Origin"] = "https://es.privalia.com"
headers["DNT"] = "1"
headers["Connection"] = "keep-alive"
headers["Cookie"] = "context=v1Qjw3n3ulZI7AqymWiKQyEsgasusmL/wSOYpo8aAv8=XrBxbQMAPWeaB5boIvumDA==&nhl7USxL3Xy3+2WD7Fbc1Cdl2w4Gn8GLgOXNCUmE8iQ=XrBxbQMAPWeaB5boIvumDA==; datadome=.-ELpThq6.7mvxBbKXOpS8-w1uHmmWS6Dsxko-8M7FmaXfIHPDeOzw8ttoMwbpYCf8.Gtq~4Yy7R1nn0q5t1N1FR9WImVIsEBB8KuDY1USPMwOLrClg_.vlZn82RnRfS; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jun+03+2022+18%3A42%3A21+GMT%2B0200+(hora+de+verano+de+Europa+central)&version=6.16.0&isIABGlobal=false&hosts=&consentId=ffbb3e44-f6a3-4305-89e2-5ef11f0d47a7&interactionCount=0&landingPath=https%3A%2F%2Fes.privalia.com%2Fgr%2Fportal&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A0%2CC0007%3A1%2CC0008%3A0"
headers["Sec-Fetch-Dest"] = "empty"
headers["Sec-Fetch-Mode"] = "cors"
headers["Sec-Fetch-Site"] = "same-origin"
headers["TE"] = "trailers"

data = '{"email":"******************","password":"*********","rememberMe":true,"returnUrl":null,"siteId":66}'

resp = requests.post(url, headers=headers, data=data)

cookies = resp.cookies
