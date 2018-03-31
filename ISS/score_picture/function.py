from aip import AipOcr, AipNlp
import re
import math
from ISS import settings

APP_ID = '10699257'
API_KEY = 'XHv2xiAOqnOUZmIvjzPhGhfZ'
SECRET_KEY = 'i0loV0FEEGzWS4FvZOGoUywUpFteKMBv'
key = ['123', '321', '231']

client_ocr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

client_nlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)

fname = '%s/pic/%s' % (settings.MEDIA_ROOT, 'key.txt')
def get_key(fname):
    key = []
    with open(fname) as f:
        key = f.read().split('\n')
    return key

def get_file_content(filePath):
    '''
    获取图片
    '''

    with open(filePath, 'rb') as fp:
        return fp.read()

def read_image(image):
    '''
    通过图片读取答案
    '''

    answer = ['', '', '',]
    index = 0
    image = get_file_content(image)
    return_data = client_ocr.basicAccurate(image);
    for line in return_data['words_result']:
        # print(line['words'])
        # print(re.search(r'\d+', line['words'])[0])
        answer[index] = re.search(r'\d+', line['words'])[0]
        index += 1
    return answer

def score(tester_answer, key):
    '''
    评判分数
    '''
    key = get_key(fname)
    score = 0
    for num1, num2 in zip(tester_answer, key):
        if num1 == num2:
            score += 1
        else:
            score -= 0.5
    if score < 0:
        score = 0
    return math.ceil(score)
