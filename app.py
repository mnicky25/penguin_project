from vetiver import VetiverModel, VetiverAPI
from dotenv import load_dotenv, find_dotenv
import vetiver
import pins
import logging

logging.basicConfig(
  format='%(asctime)s - %(message)s',
  level=logging.INFO
)
logging.info("App Started")

load_dotenv(find_dotenv())

logging.info("Request Made")
r = requests.post(api_url, json = [vals()])
logging.info("Request Returned")

if r.status_code != 200:
  logging.error("HTTP error returned")
  
return r.json().get('predict')[0]

b = pins.board_folder('board', allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'penguin_model', version = '20240417T163307Z-a6f9b')

app = VetiverAPI(v, check_prototype=True)
app.run(port = 8080)
