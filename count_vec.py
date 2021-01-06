import re

'''
テキストデータを扱いやすくするための前処理
・文字を小文字に統一
・カンマ、ピリオド、ダッシュ等の記号を分割
'''
def preprocess(text):
    #テキストを全て小文字に統一する
    text = text.lower()
    #文末のピリオド、セミコロンを削除
    text = re.sub('[.;]', '', text)
    #単語ごとに分割してリストに格納
    words = text.split(' ')

    return words 

'''
重複なしの単語リストを作成
'''
def mktuple(texts):
    #重複なしタプルを作成する
    words_tp = tuple(set(texts))
    
    return words_tp

def txt2num(text, word_list):
    #テキストに含まれる単語数の要素を持つリストを作成
    num_text = [0] * len(text)
    
    #各テキスト中にある単語が含まれる位置を返す
    for i in range(len(word_list)):
        num = [j for j, x in enumerate(text) if x == word_list[i]]
        for n in num:
            num_text[n] = i
        
    return num_text

'''
単語出現頻度カウントによるベクトルの作成
'''
def count(all_words_num, id_text):
    #記録用のテーブルを作成
    table = [[0] * all_words_num for i in range(all_words_num)]
    for k in id_text:
        num_k = len(k)
        for l in range(num_k):
            element = table[k[l]]
            if l == 0:#文章の開始単語の場合、右側単語のみを調べる
                right = k[l+1]
                element[right] += 1

            elif l == num_k-1:#文章の終了単語の場合、左側単語のみを調べる
                left = k[l-1]
                element[left] += 1
                
            else:#文章の途中の単語の場合、両側を調べる
                left = k[l-1]
                right = k[l+1]
                element[left] += 1
                element[right] += 1

    return table

def main():
    text1 = 'You can’t connect the dots looking forward;'
    text2 = 'you can only connect them looking backwards.'
    text3 = 'So you have to trust that the dots will somehow connect in your future.'
    texts = []
    id_text = []
    text_list = [preprocess(text1), preprocess(text2), preprocess(text3)]
    #入力テキストをご順を保持して表示
    print('---入力テキスト---')
    for t in text_list:
        print(t)
    #全テキストを連結したテキストを作成
    for text in text_list:
        texts += text
    #重複なしの単語のタプルを作成
    word_list = mktuple(texts)
    all_words_num = len(word_list)#重複なし全単語数

    #重複なしリストを表示
    print('---単語一覧---')
    print(word_list)
    
    #単語をIDにに変換
    for text in text_list:
        id_text.append(txt2num(text, word_list))

    #注目単語周りの単語の出現回数をカウント（ベクトル作成）
    table = count(all_words_num, id_text)

    #ベクトルの表示
    print('---分散表現---')
    for tbl in range(len(table)):
        print(word_list[tbl] + ' : ', table[tbl])

if __name__ == '__main__':
    main()
