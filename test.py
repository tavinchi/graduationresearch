#!/usr/bin/python3
# -*- coding: utf-8 -*-
#print("content-Type: text/plain\n")

import cgi
import sys
import io
import MeCab

def mecab_tokenize(text):
    mecab = MeCab.Tagger("-Owakati")
    result = mecab.parse(text)
    return result.split()

def check_word_match(text, target_word):
    words = mecab_tokenize(text)
    if target_word in words:
        return True
    else:
        return False

# 日本語を受信時にエラーにならないようにする為に必要。
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

storage = cgi.FieldStorage()

# 文中に目標単語が含まれているか確認
if check_word_match(storage.getfirst('data','匿名'),"モデル"):
    result="モデル相談会は作ったモデルで疑問に思っているところなどを聞く場所です。"
elif check_word_match(storage.getfirst('data','匿名'), "ロボ"):
    result="ETロボコンとは初心者エンジニアを対象としたロボットコンテストです。"
elif check_word_match(storage.getfirst('data','匿名'), "コミュニケーション"):
    result="コミュニケーションをとることはむずかしいことです。あきらめましょう。"
elif check_word_match(storage.getfirst('data','匿名'), "腹"):
    result="私も腹が減りました。"
elif check_word_match(storage.getfirst('data','匿名'), "勉強"):
    result="paizaなどでプログラミングの勉強をしましょう。"
else:
    result="一致しませんでした"

#結果をhtmlに返す
print('Content-type: text/html; charset=UTF-8')
print('')
print(f"{result}")
