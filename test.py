#!C:\Users\hp\AppData\Local\Programs\Python\Python312\python.exe
# -*- coding: utf-8 -*-

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
 
form = cgi.FieldStorage()
# 入力チェック（必要な変数が送信されていない場合はエラー。）
#if 'inputData' not in form:
#    print('Content-type: text/html; charset=UTF-8')
#    print('')
#    result="inputdata フィールドが送信されていません。"
#    sys.exit()
 
# your_name の値を取得して変数にセット。
# 値が入力されていない場合は「匿名」を設定。

# 文中に目標単語が含まれているか確認
if check_word_match(form.getfirst('inputData','匿名'),"モデル"):
    #print('Content-type: text/html; charset=UTF-8')
    #print('')
    result="モデル相談会は作ったモデルで疑問に思っているところなどを聞く場所です。"
    #print("モデル相談会は作ったモデルで疑問に思っているところなどを聞く場所です。")
elif check_word_match(form.getfirst('inputData','匿名'), "ロボコン"):
    #print('Content-type: text/html; charset=UTF-8')
    #print('')
    result="ETロボコンとは初心者エンジニアを対象としたロボットコンテストです。"
    #print("ETロボコンとは初心者エンジニアを対象としたロボットコンテストです。")
else:
    #print('Content-type: text/html; charset=UTF-8')
    #print('')
    result="一致しませんでした"
    #print("一致しませんでした")

#結果をHTMLに返す
print('Content-type: text/html; charset=UTF-8')
print('')
print(f"{result}")
