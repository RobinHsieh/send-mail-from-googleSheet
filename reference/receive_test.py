import imaplib

mail = imaplib.IMAP4_SSL("imap.example.com")
mail.login("your_email@example.com", "your_password")

# 選擇收件匣
mail.select("inbox")

# 搜尋郵件
result, data = mail.search(None, "ALL")

# 讀取郵件
for num in data[0].split():
    result, data = mail.fetch(num, "(RFC822)")
    print("Message: {}".format(data[0][1]))

# 關閉連接
mail.close()
mail.logout()
