"""
如果您想要在 Google 文件中新增成員，您可以使用 Google Drive API 的 permissions.create 方法。

以下是一個示例代碼，它會將一個使用者新增到 Google 文件中並授予他們編輯權限：

請注意，這個程式碼只是一個示例，您可能需要根據您的需求進行適當的修改。如果您要新增群組或其他類型的成員，您可以更改 permission 變數。也可以改變權限類型。
"""

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# 使用您的 API 金鑰和認證資訊建立服務物件
creds = Credentials.from_json("path/to/credentials.json")
drive_service = build("drive", "v3", credentials=creds)

# 新增成員並授予編輯權限
permission = {'type': 'user', 'role': 'writer', 'emailAddress': 'user@example.com'}
drive_service.permissions().create(fileId='your_doc_id', body=permission, sendNotificationEmail=True).execute()
