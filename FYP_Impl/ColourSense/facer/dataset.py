from selenium import webdriver
import os
import time
import urllib.request

# Define search terms for each season
search_terms = {
    'spring': 'spring celebrities',
    'summer': 'summer celebrities',
    'autumn': 'autumn celebrities',
    'winter': 'winter celebrities'
}

# Define directories for storing images
# Define the base directory where all class directories will be created
base_dir = 'celebrity_dataset'

# Define the class names
classes = ['spring', 'summer', 'autumn', 'winter']

# Create directories for each class
for class_name in classes:
    class_dir = os.path.join(base_dir, class_name)
    os.makedirs(class_dir, exist_ok=True)
    print(f"Directory created for class '{class_name}': {class_dir}")

# Initialize Selenium webdriver for Microsoft Edge
driver = webdriver.Edge(executable_path='C:\\Windows\\edgedriver_win64\\msedgedriver.exe')  # Update with the path to your EdgeDriver executable

# Function to collect images for a given season
def collect_images(season, search_term, num_images=1000):
    season_dir = os.path.join(base_dir, season)
    os.makedirs(season_dir, exist_ok=True)
    
    # Open Google Images and search for the given term
    driver.get("https://www.google.com/imghp?hl=en")
    search_box = driver.find_element_by_xpath("//input[@title='Search']")
    search_box.send_keys(search_term)
    search_box.submit()
    
    # Scroll down to load more images
    last_height = driver.execute_script("return document.body.scrollHeight")
    while len(driver.find_elements_by_tag_name('img')) < num_images:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    # Download images
    images = driver.find_elements_by_tag_name('img')
    for i, img in enumerate(images[:num_images]):
        src = img.get_attribute('src')
        if src:
            try:
                img_name = f'{season}_{i}.jpg'
                img_path = os.path.join(season_dir, img_name)
                urllib.request.urlretrieve(src, img_path)
                print(f'Downloaded image {i+1}/{num_images} for {season}')
            except Exception as e:
                print(f'Error downloading image {i+1} for {season}: {e}')

# Collect images for each season
for season, search_term in search_terms.items():
    collect_images(season, search_term, num_images=1000)

# Close the webdriver
driver.quit()