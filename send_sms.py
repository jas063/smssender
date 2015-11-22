import pycurl
import cStringIO
import urllib
class send_sms:
	# function to set workingkey sender id and api
  def  setparam(self,api,wk,sd):
   self.setapiurl(api)
   self.setworkingkey(wk)
   self.setsenderid(sd)
   
     # function to set working key
  def setworkingkey(self,wk):
    self.working_key=wk
    
  # function to set sender id
  def setsenderid(self,sd):
    self.sender_id=sd
    
  #function to set api url
  def setapiurl(self,api):
   a=api
   key=a[:7]
   if(key=="http://"):
      self.api_url=a[7:]
      #print self.api_url
      self.start="http://" 
   elif(key=="https:/"):
      self.api_url=a[8:]
      #print self.api_url
      self.start="https://"
   else:
      self.api_url=a
      self.start="http://"

      # function to send sms
  def send_sms(self,to,message,dlr_url,type):  
   message=urllib.quote_plus(message);
   self.url=self.start+self.api_url+"/web2sms.php?workingkey="+self.working_key+"&sender="+self.sender_id+"&to="+to+"&message="+message+"&type=xml"
   buf = cStringIO.StringIO()

   c = pycurl.Curl()
   c.setopt(c.URL, self.url)
   c.setopt(c.WRITEFUNCTION, buf.write)
   c.perform()

   print buf.getvalue()
   output=buf.getvalue()
   return output
   buf.close()
   
  # function to send unicode sms
  def unicode_sms(self,to,message,dlr_url,type,unicode):  
   message=urllib.quote_plus(message);
   self.url=self.start+self.api_url+"/web2sms.php?workingkey="+self.working_key+"&sender="+self.sender_id+"&to="+to+"&message="+message+"&unicode="+unicode+"&type=xml"
   buf = cStringIO.StringIO()

   c = pycurl.Curl()
   c.setopt(c.URL, self.url)
   c.setopt(c.WRITEFUNCTION, buf.write)
   c.perform()

   print buf.getvalue()
   output=buf.getvalue()
   return output
   buf.close()
   
  #function to send schedule sms
  def schedule_sms(self,to,message,dlr_url,type,time):  
   message=urllib.quote_plus(message);
   self.url=self.start+self.api_url+"/web2sms.php?workingkey="+self.working_key+"&sender="+self.sender_id+"&to="+to+"&message="+message+"&time="+time+"&type=xml"
   buf = cStringIO.StringIO()

   c = pycurl.Curl()
   c.setopt(c.URL, self.url)
   c.setopt(c.WRITEFUNCTION, buf.write)
   c.perform()

   print buf.getvalue()
   output=buf.getvalue()
   return output
   buf.close()
  
  #function to check message delivery status
  def  messagedelivery_status(self,mid):  

   self.url=self.start+self.api_url+"/status.php?workingkey="+self.working_key+"&messageid="+mid+"&type=xml"
   buf = cStringIO.StringIO()

   c = pycurl.Curl()
   c.setopt(c.URL, self.url)
   c.setopt(c.WRITEFUNCTION, buf.write)
   c.perform()

   print buf.getvalue()
   output=buf.getvalue()
   return output
   buf.close()
  
  #function to check group delivery status
  def  groupdelivery_status(self,gid):  

   self.url=self.start+self.api_url+"/groupstatus.php?workingkey="+self.working_key+"&messagegid="+gid+"&type=xml"
   buf = cStringIO.StringIO()
  
   #print self.url
   c = pycurl.Curl()
   c.setopt(c.URL, self.url)
   c.setopt(c.WRITEFUNCTION, buf.write)
   c.perform()

   print buf.getvalue()
   output=buf.getvalue()
   return output
   buf.close()
