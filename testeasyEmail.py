#encoding: u8
from easyEmail import easyEmail


def sendtextmail(mail_host, mail_user, mail_pass, mailto_list):
    mail_title = "发送纯文件邮件,不支持内置图片"
    mobj = easyEmail(mail_host, mail_user, mail_pass)
    res = mobj.send_email_threds(mailto_list, 
                                 mail_title, 
                                 "text", 
                                 ["hello\nhaha"], #文本
                                 ["d:\\1.txt"] #附件
                                 )

def sendhtmlmail(mail_host, mail_user, mail_pass, mailto_list):
    mail_title = "发送html邮件,支持内置图片"
    mobj = easyEmail(mail_host, mail_user, mail_pass)
    res = mobj.send_email_threds(mailto_list, 
                                 mail_title, 
                                 "html", 
                                 ["<b>详见下图:</b>","d:\\1.jpg", "d:\\2.jpg"], #html+内置图片
                                 ["d:\\1.txt","d:\\2.txt"] #附件
                                 )  

def main():
    mail_host = "smtp.exmail.qq.com"
    mail_user = "xxx@xxx.xxx"
    mail_pass = "xxxxxx"
    mailto_list=["xxx@xxx.xxx"]
    sendtextmail(mail_host, mail_user, mail_pass, mailto_list)
    sendhtmlmail(mail_host, mail_user, mail_pass, mailto_list)



if __name__ == '__main__':
    main()
