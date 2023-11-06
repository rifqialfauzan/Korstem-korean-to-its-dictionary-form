from flask import Flask, render_template, request, redirect
from konlpy.tag import Okt,Kkma
from konlpy.utils import pprint
from string import punctuation


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    korstem = None
    if request.method == 'POST':
        korstem = tokenize(request.form.get("textInp"))
        # print(korstem)
        return render_template('index.html', korstem = korstem)
    else:
        # print(korstem)
        return render_template('index.html', korstem = korstem)
    # return tokenize("샘플 코드에서 YOUR_CLIENT_ID또는 YOUR-CLIENT-ID에는 애플리케이션을 등록하고 발급받은 클라이언트 아이디 값을 입력합니다")
    


def tokenize(text):
    kkma = Kkma()
    okt = Okt()

    data = []

    #Make translator, wtf is translator?
    translator = str.maketrans("", "", punctuation)
    #create new string with no punctuation
    clear = text.translate(translator)
    
    #To get original word from input user (Stem = False)
    textInput = okt.pos(clear, norm=True)
    #To get dict form of the word (stem = True)
    dictForm = okt.pos(clear, norm=True, stem=True)

    # Iterate over dictForm
    for i in range(len(dictForm)):
        # print(f"{textInput[i][0]} -> {dictForm[i][0]}")
        wordType = dictForm[i][1] # get the 'type' of the word (noun,verb or etc)
        if ( wordType == 'Verb' or wordType == 'Noun' or wordType == 'Adjective'):
            # Insert into data
            data.append({
                'text': str(textInput[i][0]),
                'dictionaryForm': str(dictForm[i][0]),
                'type': dictForm[i][1],
                'translation': ""
            })
    
    return data
        

    


# tokenize('네, 안녕하세요. 반갑습니다.')








if __name__ == "__main__":
    app.run(debug=True)