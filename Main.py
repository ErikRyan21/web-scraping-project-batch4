import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from datetime import datetime as dt

website_url = "https://eshop.winmobileworld.com/"

def create_page_urls(main_url):
    """
    Scrapes the main page to find the maximum page number 
    and generates a list of pagination URLs.
    """
    web_data = requests.get(main_url).text
    bsObj = BeautifulSoup(web_data, "html.parser")
    page_url_list = []
    
    last_page = bsObj.find_all("a", "page-link")[-1].text
    last_page_obj = bsObj.find_all("a", "page-link")[-1]
    
    # If the last button is "Last »", extract the total page number from its link
    if last_page  == "Last »" :
        url_path = last_page_obj.get("href")
        url_path = url_path.split("page=")
        max_page_num = int(url_path[-1])
    for i in range(1, max_page_num + 1):
        page_url = main_url + "?page=" + str(i)
        page_url_list.append(page_url)
    return page_url_list


def extract_p_info_tags(url):
    """
    Extracts all product infos.
    """
    web_data = requests.get(url).text
    bsObj = BeautifulSoup(web_data, "html.parser")
    product_info_list = bsObj.find_all("div", "card product-card")
    return product_info_list
    
def extract_p_name(product_info_list):
    """
    Extract the names of products.
    """
    name_list = []         
    for product_info_tag in product_info_list:
    ## Extract product name tag
        product_name_tag = product_info_tag.find("h3","product-title fs-sm").find("a") # tag, class name
        product_name = product_name_tag.text
        #print(product_name)
        name_list.append(product_name)
    return name_list
            
def extract_p_price(product_info_list):
    """
    Extracts product prices, handling variations between
    original prices and promotional discount prices.
    """
    price_list  = []
    for product_info_tag in product_info_list:
        product_price_list = product_info_tag.find_all("span","text-accent")
                
        for product_price_tag in product_price_list:
            # Check if a special promotion price exists inside it
            if product_price_tag :
                promo_price = product_price_tag.find("span", "promotion-price")
                
                if promo_price:
                    product_price = promo_price.text.strip()
                else:
                    product_price = product_price_tag.text.strip()
        # Data Cleaning            
        product_price = product_price.replace(",", "")
        product_price = product_price.replace("MMK", "")
        price_list.append(product_price)
    return price_list

def extract_p_status(product_info_list):
    """
    Checking the products are out of stock or not.
    """
    status_list = []
    for product_info_tag in product_info_list:
        try:
            #Extract the product_status_tag
            product_status_tag = product_info_tag.find("span","badge bg-danger badge-shadow")
            product_status = product_status_tag.text
            status_list.append(product_status)
        except AttributeError:
            # If the tag doesn't exist, product_status will be "Instock"
            product_status = "Instock"
            status_list.append(product_status)
    return status_list

def get_current_date():
    # Get Current Date Time
    current_dt = dt.now()
    # change date to string
    current_dt = str(current_dt)
    # replace : with -
    current_dt = current_dt.replace(":", "-")
    # remove milliseconds
    current_dt = current_dt.split(".")[0]
    return current_dt

def create_output_file(name_list,price_list,status_list,url_count,current_dt):
    """
    Create the excel data files of each page  
    """
    page_df = pd.DataFrame({"Product Name":name_list,
                            "Product Price":price_list,
                            "Status":status_list})
    # Save the individual page file to disk
    page_df.to_excel(f"Data_{url_count}_{current_dt}.xlsx",index=False)
       
    return page_df
    

def main() :
    web_url_list = create_page_urls(website_url)
    current_dt = get_current_date()
    url_count = 1
    final_df = pd.DataFrame()

    for url in tqdm(web_url_list) :
    
        product_info_list = extract_p_info_tags(url)
    
        # Process attributes from the product_info_list
        name_list = extract_p_name(product_info_list)
        price_list = extract_p_price(product_info_list)
        status_list = extract_p_status(product_info_list)
    
        # Create each data files
        page_df = create_output_file(name_list,price_list,status_list,url_count,current_dt)
        url_count += 1
    
        final_df = pd.concat([final_df, page_df])
    final_df.to_excel(f"Final_Data_{current_dt}.xlsx", index=False)
    print("Project is completed successfully!")
    
if __name__ == "__main__":
        main()



