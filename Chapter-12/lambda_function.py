import requests
from bs4 import BeautifulSoup
from collections import Counter 
from string import punctuation # already included in lambda modules 

def lambda_handler(event, context):

# get the URL from the event 
  r = requests.get("https://aws.amazon.com/blogs/compute/using-lambda-layers-to-simplify-your-development-process/") #demo 
  #r = requests.get(event['url'])
  bs = BeautifulSoup(r.content, "html.parser")

  # gather all the words within the paragraphs 
  p_txt = (''.join(s.findAll(text=True))for s in bs.findAll('p'))
  count_p = Counter((x.rstrip(punctuation).lower() for y in p_txt for x in y.split()))

  # gather all the text in the divs 
  d_txt = (''.join(s.findAll(text=True))for s in bs.findAll('div'))
  count_div = Counter((x.rstrip(punctuation).lower() for y in d_txt for x in y.split()))

  # create a sum total of the words 
  word_sum = countp + count_div
  # return the number of words 
  return word_sum