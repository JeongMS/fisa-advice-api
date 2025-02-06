import requests
import os
from datetime import datetime

URL = f"https://api.adviceslip.com/advice"

# README 파일 경로
README_PATH = "README.md"

def get_advice():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        advice = data["slip"]["advice"]
        return f"{advice}"
    else:
        return "조언을 가져오는데 실패했습니다."

def update_readme():
    """README.md 파일을 업데이트"""
    advice_info = get_advice()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    readme_content = f"""
# 마음에 새깁시다.......

> {advice_info}
"""

    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    update_readme()

