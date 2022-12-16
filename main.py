from selenium import webdriver
from selenium.webdriver.common.by import By
import time, json, discord
from datetime import datetime


date = datetime.now()
current_time = date.strftime("%H:%M:%S")

with open("/ignore/config.json", "r") as config:
  data = json.load(config)

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client) + current_time) 
  url = "https://www.pepal.eu/"
  driver = webdriver.Chrome(executable_path='chromedriver.exe')
  driver.get(url)
  username = driver.find_element(By.ID, 'username')
  password = driver.find_element(By.ID, 'password')
  username.send_keys(data['username'])
  password.send_keys(data['password'])
  driver.find_element(By.ID, "login_btn").click()
  time.sleep(4)
  driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/div/div/div/a[4]").click() 

  presence = False

  while presence == False:
    for i in [1,2]:
      driver.find_element(By.XPATH, f"//*[@id=\"body_presences\"]/tr[{i}]/td[3]/a").click()
      check = driver.find_element(By.ID,"body_presence")
      verify = check.text
      if 'Valider la présence' in verify:
        presence = True
        await client.get_channel(data["channel"]).send(f"L'appel est ouvert : {current_time}")
      driver.back()
    

client.run(data['token'])



