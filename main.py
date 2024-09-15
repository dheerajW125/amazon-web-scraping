import requests
from bs4 import BeautifulSoup
import smtplib
import time
import datetime

#connecting to website

URL = 'https://www.amazon.in/Levis-Mens-Regular-T-Shirt-16960-1205_White/dp/B0CRVKDKXG/ref=nav_signin?dib=eyJ2IjoiMSJ9.aLwv_4Q2tF2wq6WsWqOQZnUpumsvez1oGmURoE5IuMVVpnoDYvzJOPiNzG09NjnSzcWnc9OqJmyzCAZo-plhP2Qa7Xq6B8Feww1BtKh2datz75DqngJG_7mpRAfnR1jRAPYQSof1FUqnhO7vxlgW-jOXR_u1HRJmEEk_rdK6860Enk1mu1zmIc4d4CnVWhPOQnB1EaxnRZuDTGtl0OyBEKHXJv0UBv-UCOvkppdNXhFq1IVna5yZ0Itkn6p0dx9s2HR7bM2B2PtOgtxY11TYfiUuJbqQsvzhCv4KO3t9PQs.2evma9NRleIovwnwge3oCDwmhEu4-ivWnC1wiEu5goI&dib_tag=se&pf_rd_i=1968024031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=47eb2614-e403-4fbc-969d-414042c8d4f7&pf_rd_r=VGWZQNZ8GAFS096X8J46&pf_rd_s=merchandised-search-7&qid=1726424280&refinements=p_n_pct-off-with-tax%3A2665401031%2Cp_85%3A10440599031%2Cp_123%3A1298678%7C156780%7C198664%7C200356%7C232621%7C232755%7C232761%7C232762%7C232763%7C240905%7C256097%7C319726%7C339433%7C373328%7C3878%7C390827%7C398346%7C406102%7C411593%7C435051%7C46245%7C484445%7C573837%7C586466%7C613702%7C709907%2Cp_36%3A60000-&rnid=4595083031&rps=1&s=apparel&sr=1-2&'
headers ={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
response = requests.get(URL, headers=headers)

# Check the status code
if response.status_code == 200:
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title element
    title_element = soup.find('span', id='productTitle')
    
    # Check if title_element is found
    if title_element:
        title = title_element.get_text(strip=True)
        print("Product Title:", title)
    else:
        print("Title element not found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")