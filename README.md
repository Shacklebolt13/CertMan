# CertMan
Post Certificates and send mails using gmail smtp
<dl>
  <dt>Basic syntax</dt>
  <dd>certMan.py $gmail_ID $Pass [options]</dd>
  <dt>Debug syntax</dt>
    <dd>
      $ python3 -m smtpd -c DebuggingServer -n localhost:1025(run in a background terminal)<br>
      $ certMan.py -d
    </dd>
 </dl>
    Options:
 <dl>
  <dt>-d</dt>
   <dd> debug server(needs localhost smtp)</dd>
   <dt>-v</dt>
   <dd>shows verbose output</dd>
   <dt>-c</dt>
   <dd> use custom input</dd>
   <dt>-n</dt>
   <dd> no file upload, only post message</dd>
 </dl>
<h4>usage:</h4>
<ul>  
<li>clone the repo</li>
<li>run locMan.py with your certificate template as template.jpg</li>
<li>confirm location of the drawn text or change the location(x,y)</li>
<li>go to your google account and enable less secure apps(remember to turn off later)</li>
<li>put the name-email list as participants.csv in this folder</li>
<li>customize the fields in the file</li>
<li>run command and send mails!!</li>
