import json
import random

def lambda_handler(event, context):
  # randint generates a random integar between the first parameter and the second
  print(random.randint(1, 100))
