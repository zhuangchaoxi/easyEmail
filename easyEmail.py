#encoding: u8


import sys
reload(sys)
sys.setdefaultencoding('u8')
from threading import Thread
import smtplib
import mimetypes 
import email.MIMEText
import email.MIMEMultipart
from email.MIMEImage import MIMEImage
import email.MIMEBase
import os.path
from email.utils import formataddr


class SpcEmail(object):

    def __init__(self, mail_host, mail_user, mail_pass):
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass


    def send_mails(self, to_list, mail_title, contentIcon, contents, filenames=None):
        '''
        发送邮件
        '''
        main_msg = email.MIMEMultipart.MIMEMultipart()
        if contentIcon == "text":
            text_msg = email.MIMEText.MIMEText(contents[0], 'plain', "utf-8")  #纯文本,不支持内置图片
            main_msg.attach(text_msg)
        elif contentIcon == "html":
            text_msg = email.MIMEText.MIMEText(contents[0], 'html', "utf-8")  #html
            main_msg.attach(text_msg)
            if len(contents) > 1:  #是否内置图片
                images = contents[1:]
                for index,img in enumerate(images):
                    cot = '''</br><img style src="cid:image{index}" alt="digglife\"><br/>\
                                 <div style="margin:0 auto;text-align:center">\
                                   图{imgx}\
                                 </div><br/>'''.format(index=index,imgx=index+1)
                    text_msg = email.MIMEText.MIMEText(cot, 'html', "utf-8")
                    main_msg.attach(text_msg)
                    fp = open(img, 'rb')
                    msgImage = MIMEImage(fp.read())
                    fp.close()
                    msgImage.add_header('Content-ID', 'image{index}'.format(index=index))
                    main_msg.attach(msgImage)
        else:
            print "contentIcon is not supported!"
            return

        if filenames: #附件
            for fn in filenames:
                ctype,encoding = mimetypes.guess_type(fn)
                if ctype is None or encoding is not None:
                    ctype='application/octet-stream'
                maintype,subtype = ctype.split('/',1)
                file_msg=email.MIMEImage.MIMEImage(open(fn,'rb').read(),subtype)
                basename = os.path.basename(fn)
                file_msg.add_header('Content-Disposition','attachment', filename = basename)
                main_msg.attach(file_msg)

        try:  
            main_msg['Subject'] = mail_title
            main_msg['From'] = formataddr(["OPS平台", self.mail_user])
            main_msg['To'] = ";".join(to_list)
            main_msg['Date'] = email.Utils.formatdate()
            server = smtplib.SMTP()
            server.connect(self.mail_host)
            server.login(self.mail_user, self.mail_pass)
            server.sendmail(self.mail_user, to_list, main_msg.as_string())
            server.close()
            return True
        except Exception, e:
            print str(e)
            return False


    def send_email_threds(self, to_list, mail_title, contentIcon, contents, filenames=None):
        thr = Thread(target=self.send_mails, 
                     args=[to_list,
                           mail_title,
                           contentIcon,
                           contents,
                           filenames])
        thr.start()
        return thr
