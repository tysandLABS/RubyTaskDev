import subprocess
import xml.etree.ElementTree as ET
from time import sleep

def domainList(list_Domain):
        
        
        # parsing directly.
        tree = ET.parse('test.xml')
        root = tree.getroot()
        num = len(list_Domain)


        # traversing the tag to find stringProp.
        for domain in list_Domain:
                num = len(domain)
                for elm in root.findall('.//hashTree/HTTPSamplerProxy'):
                        x = (elm.find("stringProp[@name='HTTPSampler.domain']"))
                        name = elm.find('stringProp')
                        name.text = domain
                        print(name.text)
                        tree.write(f'output.xml.{domain}')
                        # writing the changes to the file. 
                        command = "Get-ChildItem -Force"
                        result = subprocess.run([command], shell=True, capture_output=True, text=True)
                        print(result.stdout)
                        sleep(2)
               
        
ebs_domain = ['www.google.com', 'www.facebook.com', 'www.youtube.com']

domainList(ebs_domain)