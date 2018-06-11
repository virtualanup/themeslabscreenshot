# Screenshot generator for themeslab.co
import sys
from selenium import webdriver
from PIL import Image

if __name__ == "__main__":
    if(len(sys.argv) <= 2):
        print("Syntax : python3 generate.py <website_url> <filename>")
        exit(1)

    print("Generating screenshot of the URL")
    website_url = sys.argv[1]
    screenshot_file_name = sys.argv[2] + ".png"
    preview_file_name = sys.argv[2] + "_preview.png"

    DRIVER = 'chromedriver'
    driver = webdriver.Chrome(DRIVER)

    dx, dy = driver.execute_script("var w=window; return [w.outerWidth - w.innerWidth, w.outerHeight - w.innerHeight];")
    driver.set_window_size(1920 + dx, 1080 + dy)

    driver.get(website_url)
    screenshot = driver.save_screenshot(screenshot_file_name)
    driver.quit()

    print("Screenshot taken..creating preview image")

    screenshot = Image.open(screenshot_file_name, "r")
    frame = Image.open("frame.jpg")

    w, h = screenshot.size

    frame_screenshot_width = 690
    frame_screenshot_height = 300

    factor = frame_screenshot_width/w

    size = (w*factor, h+factor)
    screenshot.thumbnail(size, Image.ANTIALIAS)

    # Crop the screenshot
    screenshot_crop = screenshot.crop((0, 0, frame_screenshot_width, frame_screenshot_height))

    frame.paste(screenshot_crop, (30, 37))
    frame.save(preview_file_name)
