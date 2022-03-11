#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import  translator
class TestenglishToFrench(unittest.TestCase): 
       def test1(self): 
          
           self.assertEqual(translator.english_to_french('Hello'), 'Bonjour' )
           self.assertEqual(translator.english_to_french(""), "Null" )


class Testfrenchtoenglish(unittest.TestCase): 
       def test1(self): 
           
           self.assertEqual(translator.french_to_english('Bonjour'), 'Hello' )   
           self.assertEqual(translator.french_to_english(''), "Null" ) 
unittest.main()