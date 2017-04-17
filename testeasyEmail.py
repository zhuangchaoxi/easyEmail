#encoding: u8
from easyEamil import easyEamil


def sendtextmail(mail_host, mail_user, mail_pass, mailto_list):
    mail_title = "这是一个测试邮件"
    mobj = easyEamil(mail_host, mail_user, mail_pass)
    res = mobj.send_email_threds(mailto_list, 
                                 mail_title, 
                                 "text", 
                                 ["hello\nhaha"],
                                 ["d:\\1.txt"])

def sendhtmlmail(mail_host, mail_user, mail_pass, mailto_list):
    mail_title = "这是一个测试邮件"
    mobj = easyEamil(mail_host, mail_user, mail_pass)
    res = mobj.send_email_threds(mailto_list, 
                                 mail_title, 
                                 "html", 
                                 ["<b>详见下图:</b>","d:\\1.jpg", "d:\\2.jpg"], 
                                 ["d:\\1.txt","d:\\2.txt"])

def main():
    mail_host = "smtp.exmail.qq.com"
    mail_user = "xxx@xxx.xxx"
    mail_pass = "xxxxxx"
    mailto_list=["xxx@xxx.xxx"]
    sendtextmail(mail_host, mail_user, mail_pass, mailto_list)
    sendhtmlmail(mail_host, mail_user, mail_pass, mailto_list)



if __name__ == '__main__':
    main()
