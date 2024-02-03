import subprocess
import xml.etree.ElementTree as ET
from time import sleep

def domainList(list_Domain):
        
        
        # parsing directly.
        tree = ET.parse('./blitz-c4.jmx')
        root = tree.getroot()


        # traversing the tag to find stringProp.
        for domain in list_Domain:
                for elm in root.findall('.//hashTree/HTTPSamplerProxy'):
                        x = (elm.find("stringProp[@name='HTTPSampler.domain']"))
                        name = elm.find('stringProp')
                        name.text = domain
                        print(name.text)
                        tree.write('output.jmx')
                        # writing the changes to the file. 
                        result = subprocess.run(["./c4"], shell=True, capture_output=True, text=True)
                        print(result.stdout)
                        sleep(3)
               
        
#ebs_domain = ['urlshort-env.eba-znv3nv9i.us-east-1.elasticbeanstalk.com', 'ebs-url-shortener-dev.us-east-1.elasticbeanstalk.com', 'urlshortener-env.eba-ejerb5qe.us-east-1.elasticbeanstalk.com', 'url-shortener-2-env-1.eba-myyytpit.us-east-1.elasticbeanstalk.com', 'urlshort-env.eba-h7pf59us.us-east-1.elasticbeanstalk.com', 'urlshortenerblitz-env.eba-byqfwgm4.us-east-1.elasticbeanstalk.com']
ebs_domain = ['urlshortner-env.eba-ig2ke5ke.us-east-1.elasticbeanstalk.com', 'blitz3-env-1.eba-5hmdmdcn.us-east-1.elasticbeanstalk.com', 'url-short-env.eba-j3emz3vx.us-east-1.elasticbeanstalk.com', 'url-short-bllitz-env.eba-iwtx9btv.us-east-1.elasticbeanstalk.com', 'urlshortenerblitz-env.eba-3nx42ut2.us-east-1.elasticbeanstalk.com', 'urlshortyyyapp-env.eba-adqbcnty.us-east-1.elasticbeanstalk.com']

domainList(ebs_domain)