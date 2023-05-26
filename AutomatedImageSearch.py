from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome(# path of your WebDriver)

def automate_image_search(image_paths):
    driver.get('https://Google.com/')
    driver.maximize_window()

    search_box = driver.find_element(By.CSS_SELECTOR,"svg.Gdd5U").click()
    time.sleep(2)
        
    upload_box = driver.find_element(By.CSS_SELECTOR,"span.DV7the")
    time.sleep(2)
        
    upload_image = driver.find_element(By.NAME,"encoded_image").send_keys(image_path)
    time.sleep(10)

    find_links = driver.find_elements(By.TAG_NAME,"a")
    print(len(find_links))

    result_list = []
    for link in find_links:
        result = link.get_attribute('href')
        result_list.append(result)
        print('Results from Google lens: ',result)
    result_list = result_list[3:]
        
    with open("D:\\result_google_lens.html", "w") as f:
            f.write("<html><head><title>Search Results</title></head><body>")
            for link in result_list:
                f.write('<a href="' + link + '">' + link + '</a><br>')
            f.write("</body></html>")

    Tineye_site = driver.get('https://tineye.com/')
    time.sleep(2)
    
    upload_image = driver.find_element(By.CSS_SELECTOR,"input#upload_box").send_keys(image_path)
    time.sleep(6)
    
    find_links=driver.find_elements(By.CSS_SELECTOR,'div.matches.col-sm-12')
    print(find_links)
    result_list = []
    for find_link in find_links:
        find_tags=find_link.find_elements(By.TAG_NAME,"a")

        
        for link in find_tags:
            result = link.get_attribute('href')
            if result:result_list.append(result)
        print('Results from Tineye: ',result_list)
        
    with open("D:\\result_tineye.html", "w") as f:
            f.write("<html><head><title>Search Results</title></head><body>")
            for link in result_list:
                f.write('<a href="' + str(link) + '">' + str(link) + '</a><br>')
            f.write("</body></html>")

    driver.quit()
    
image_paths = [ # your Image path ]
for image_path in image_paths:
    automate_image_search(image_path)

