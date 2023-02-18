import datetime
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import sys
import io
sys.stdout = io.StringIO()

url = 'https://jkjc.xust.edu.cn/healthCheck/weChatLogin?uid=填写你自己的UID'  
response1 = requests.get(url)
url2 = 'https://jkjc.xust.edu.cn/healthCheck/UserHealthCheck/update'

# 获取当前日期，并加上一天
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

# 将日期转换为指定格式的字符串
date_str = tomorrow.strftime("%Y-%m-%d")

# 构造JSON字符串
json_data = '{ 填写你自己想要的JSON内容clockDate不需要填,"clockDate":"' + date_str + '" }'

try:
    data = json.loads(json_data)
    # print(data)
except json.JSONDecodeError as e:
    print("JSON 解析错误:", e.msg)
    print("错误位置:", e.pos)

headers={"Authorization": "填写你自己的token"}
response =requests.post(url2,data=json_data,headers=headers)

print(response1.text)
print(response.status_code)
print(response.text)


# =====================可一次为多人打卡，有几人就粘贴几份============================
# url = 'https://jkjc.xust.edu.cn/healthCheck/weChatLogin?uid=填写你自己的UID'  
# response1 = requests.get(url)
# url2 = 'https://jkjc.xust.edu.cn/healthCheck/UserHealthCheck/update'

# # 获取当前日期，并加上一天
# today = datetime.date.today()
# tomorrow = today + datetime.timedelta(days=1)

# # 将日期转换为指定格式的字符串
# date_str = tomorrow.strftime("%Y-%m-%d")

# # 构造JSON字符串
# json_data = '{ "填写你自己想要的JSON内容clockDate不需要填,"clockDate":"' + date_str + '" }'

# try:
#     data = json.loads(json_data)
#     # print(data)
# except json.JSONDecodeError as e:
#     print("JSON 解析错误:", e.msg)
#     print("错误位置:", e.pos)

# headers={"Authorization": "填写你自己的token"}
# response =requests.post(url2,data=json_data,headers=headers)

# print(response1.text)
# print(response.status_code)
# print(response.text)
# =====================可一次为多人打卡，有几人就粘贴几份============================




# 获取控制台输出内容
output = sys.stdout.getvalue()

# 邮箱参数
sender_email = '发件人邮箱'  # 发件人邮箱
sender_password = '发件人邮箱密码'  # 发件人邮箱密码
receiver_email = '收件人邮箱'  # 收件人邮箱

# 邮件内容

message = MIMEMultipart('related')
message['Subject'] = '西安科技大学健康监测打卡BY ihjycc'  #邮件主题
message['From'] = sender_email  # 添加发件人
text = MIMEText(output)
message.attach(text)



# message = MIMEMultipart()
# text = MIMEText(output)
# message.attach(text)

# 发送邮件
smtp = smtplib.SMTP('smtp.qq.com', 25)
smtp.ehlo('example.com')
smtp.starttls()
smtp.login(sender_email, sender_password)
smtp.sendmail(sender_email, receiver_email, message.as_string())
smtp.quit()