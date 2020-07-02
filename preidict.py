# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:28:41 2020

@author: cm
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from sentiment_analysis_dict.networks import SentimentAnalysis



sa = SentimentAnalysis()
def predict(sent):
    score1,score0 = sa.norm_score(sent)
    if score1 == score0:
        result = 0
    elif score1 > score0:
        result = 1
    elif score1 < score0:
        result = -1
    return result
        

if __name__ =='__main__':
    sa = SentimentAnalysis()
    text = '对你不满意'
    text = '大美女'
    text = '帅哥'
    text = '我妈说明儿不让出去玩'
    print(predict(text))



