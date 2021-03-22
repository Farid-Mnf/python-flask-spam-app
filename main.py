import pandas as pd

data = pd.read_csv("spam.csv")

import string
import nltk

nltk.download('stopwords')
nltk.download('punkt')

stopwords = nltk.corpus.stopwords.words('english')
punctuation = string.punctuation


def pre_process(sms):
    remove_punct = "".join([word.lower() for word in sms if word not in punctuation])
    tokenize = nltk.tokenize.word_tokenize(remove_punct)
    remove_stopwords = [word for word in tokenize if word not in stopwords]
    return remove_stopwords


# adding a column to our data with our processed messages
data['processed'] = data['EmailText'].apply(lambda x: pre_process(x))


def categorize_words():
    spam_words = []
    ham_words = []
    # handling messages associated with spam
    for EmailText in data['processed'][data['Label'] == 'spam']:
        for word in EmailText:
            spam_words.append(word)
    # handling messages associated with ham
    for EmailText in data['processed'][data['Label'] == 'ham']:
        for word in EmailText:
            ham_words.append(word)
    return spam_words, ham_words


spam_words, ham_words = categorize_words()


def predict(EmailText):
    spam_counter = 0
    ham_counter = 0
    # count the occurances of each word in the sms string
    for word in EmailText:
        spam_counter += spam_words.count(word)
        ham_counter += ham_words.count(word)

    # if the message is ham
    if ham_counter > spam_counter:
        accuracy = round((ham_counter / (ham_counter + spam_counter) * 100))
        print('messege is not spam, with {}% certainty'.format(accuracy))
        return 'not spam'
    # if the message could be equally spam and ham
    elif ham_counter == spam_counter:
        print('message could be spam')
        return 'could be spam'
    # if the message is spam
    else:
        accuracy = round((spam_counter / (ham_counter + spam_counter) * 100))
        print('message is spam, with {}% certainty'.format(accuracy))
        return 'message is spam, with {}% certainty'.format(accuracy)


def spam_service(email_input):
    # pre-processing the input before prediction
    processed_input = pre_process(email_input)
    return predict(processed_input)
