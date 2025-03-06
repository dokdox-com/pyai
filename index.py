import streamlit
from google import genai

a = "소설을 작성해줘.재미있게 길이는 2000문장 정도"

client = genai.Client(api_key="AIzaSyBx7d8QupJbmbvzyfuCc-QvPmq1cBtAVVU")
response = client.models.generate_content(
 model="gemini-2.0-flash", contents=a
)
streamlit.write(response.text)
