
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def main():
    # 设置 WebDriver
    cService = webdriver.ChromeService(executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome(service = cService)


    try:
        # 打开百度网站
        driver.get("https://www.baidu.com")

        # 测试搜索功能
        search_box = driver.find_element(By.NAME, "wd")
        search_box.send_keys("中南大学强基计划")
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(2)  # 等待页面加载

        # 检查搜索结果
        results = driver.find_elements(By.CSS_SELECTOR, "div.result")
        assert len(results) > 0, "没有找到搜索结果"

        print("🎉 功能测试成功！搜索结果已显示。")

    except Exception as e:
        print(f"❌ 功能测试失败：{str(e)}")

    finally:
        # 关闭浏览器
        time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    main()
