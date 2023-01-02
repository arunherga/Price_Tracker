from bs4 import BeautifulSoup
import requests

def flipkart(url):
    web_text = requests.get(url).text
    soup = BeautifulSoup(web_text,'lxml')
    price = soup.find('div',class_='_30jeq3 _16Jk6d').text.replace(',','').replace('₹','')
    print(price)

flipkart('https://www.flipkart.com/hp-deskjet-2331-multi-function-color-printer/p/itm5708dbe303a73?pid=PRNFTXAWZ9DZ2KHR&lid=LSTPRNFTXAWZ9DZ2KHRNUI3EX&marketplace=FLIPKART&store=6bo%2Ftia%2Fffn%2Ft64&srno=b_1_1&otracker=hp_omu_Best%2Bof%2BElectronics_2_3.dealCard.OMU_D54DFY00C5JD_3&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all%2Chp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_2_NA_view-all_3&fm=neo%2Fmerchandising&iid=ef94fe61-693f-4496-baad-b8f4499b98d5.PRNFTXAWZ9DZ2KHR.SEARCH&ppt=browse&ppn=browse&ssid=w484f4qks00000001670581219912')

def amazon(url):
    for i in range(100):
        web_amazon = requests.get(url).text
        soup1 = BeautifulSoup(web_amazon,'lxml')
        price1 = soup1.find('span',class_='a-price-whole')
        if price1:
            price1 = price1.text.replace(',','').replace('.','')
            print(price1)
            break 

amazon('https://www.amazon.in/Sony-ZV-E10L-Interchangeable-Lens-Mirrorless-Autofocus/dp/B09F9Q7287/ref=sr_1_1_sspa?keywords=camera+dslr&qid=1670596127&sprefix=camera+ds%2Caps%2C249&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1')
