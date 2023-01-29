import smtplib

sender_email = "your_email@example.com"
receiver_email = "receiver_email@example.com"
password = "your_password"
message = """\
Subject: Test Email

This is a test email sent using Python smtplib library."""

server = smtplib.SMTP("smtp.example.com", 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
print("Email sent!")
server.quit()
這是使用 imaplib 模組收取郵件的示例代碼:

python
Copy code
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