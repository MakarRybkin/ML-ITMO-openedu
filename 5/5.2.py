import pandas as pd
import math
info = pd.read_csv("data.csv",sep=";")
print(info)
words = pd.read_csv("words.csv",sep=";")
print(words)
arr_words = "Million Online Access Cash Bill Offer Money".split()
email_row = info.iloc[0]
email_spam = email_row[1] / (email_row[2] + email_row[1])
print(f"Email is spam: {format(email_spam)}")
ln_email_spam = math.log(email_spam)
print("Email is spam ln: {}".format(ln_email_spam))
freq_spam = dict()
for i in arr_words:
    have = False
    for j in range(words.shape[0]):
        if i == words.iloc[j][0]:
            have = True
            freq_spam[words.iloc[j][0]] = words.iloc[j][1] + 1
    if not have:
        freq_spam[i] = 1
print(freq_spam)
total_spam_words = words.shape[0]
for i in range(words.shape[0]):
    total_spam_words += words.iloc[i][1]
print("Total words marked spam: {}".format(total_spam_words))
y_spam = ln_email_spam
for i in arr_words:
    y_spam += math.log(freq_spam[i]/total_spam_words)
print("Y_spam_ln: {}".format(y_spam))
email_row = info.iloc[0]
email_not_spam = email_row[2]/ (email_row[2] + email_row[1])
print("Email is not spam: {}".format(email_not_spam))
ln_email_not_spam = math.log(email_not_spam)
print("Email is ham ln: {}".format(ln_email_not_spam))
freq_not_spam = dict()
for i in arr_words:
    have = False
    for j in range(words.shape[0]):
        if i == words.iloc[j][0]:
            have = True
            freq_not_spam[words.iloc[j][0]] = words.iloc[j][2] + 1
    if not have:
        freq_not_spam[i] = 1
print(freq_not_spam)
total_not_spam_words = words.shape[0]
print(total_not_spam_words)
for i in range(words.shape[0]):
    total_not_spam_words += words.iloc[i][2]
print("Total words marked ham: {}".format(total_not_spam_words))
y_not_spam = ln_email_not_spam
for i in arr_words:
    y_not_spam += math.log(freq_not_spam[i]/total_not_spam_words)
print("Y_not_spam_ln: {}".format(y_not_spam))
p = 1 / (1 + math.exp(y_not_spam - y_spam))
print("Prediction: {}".format(round(p, 3)))
print("Email is spam probability: {}".format(round(email_spam, 3)))
posterior_spam = 0
for amount in freq_spam.values():
    posterior_spam += amount / total_spam_words
print("ln Posterior probability of spam: {}".format(round(posterior_spam, 3)))
posterior_not_spam = 0
for amount in freq_not_spam.values():
    posterior_not_spam += amount / total_not_spam_words
print("ln Posterior probability of not spam: {}".format(round(posterior_not_spam, 3)))