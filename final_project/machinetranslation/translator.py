#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 00:50:06 2022

@author: kaiser
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version= "2018-05-01",
    authenticator=authenticator
)
language_translator.set_service_url(url)
a = ""

def english_to_french(english_text):
    """
    this method take a English  text and translate it to french language 
    """
    if a != english_text:
        translation = language_translator.translate(
        text= english_text,
          model_id='en-fr').get_result()
        french_text = json.loads(json.dumps(translation, indent=2, ensure_ascii=False))
        return (french_text["translations"][0]["translation"])
    return "Null"
    
def french_to_english(french_text):
    """
     this method take a french text and translate it to English language 
    """
    if a != french_text:
        translation = language_translator.translate(
            text= french_text,
            model_id='fr-en').get_result()
        english_text = json.loads(json.dumps(translation, indent=2, ensure_ascii=False))
        return (english_text["translations"][0]["translation"])
    return "Null"
  

