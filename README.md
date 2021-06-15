# CertMan
Post Certificates and send mails using gmail smtp
<dl>
  <dt>Basic syntax</dt>
  <dd>certMan.py $gmail_ID $Pass [options]</dd>
  <dt>Debug syntax</dt>
    <dd>
      $ python3 -m smtpd -c DebuggingServer -n localhost:1025(run in a background terminal for debug smtp server)<br>
      $ certMan.py -d
    </dd>
 </dl>
    Options:
 <dl>
  <dt>-d</dt>
   <dd> debug mode shows verbose output</dd>
   <dt>-c</dt>
   <dd> use custom input</dd>
   <dt>-n</dt>
   <dd> no file upload, only post message</dd>
   
 </dl>
  
