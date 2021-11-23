import re 



def atumation_regex(path):
      words = []
      with open(path) as a_file:
        for line in a_file:
          stripped_line=line.strip()
          words += stripped_line.split(' ')
         

    

      emails = ''
      phon_numbers = ''

      for word in words :
         email = re.search(r'([\w\.-]+)@([\w\.-]+)', word)
         if email :
            if email.group() not in emails :
               emails+=email.group()

      
        

      for word in words :
         phon_number = re.search(r'((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}', word)
         if phon_number :
            if phon_number.group() not in phon_numbers :
               phon_numbers += phon_number.group() 
      

      with open('assets/emails.txt','w') as final_file:
        final_file.write(f'{emails}\n')    
      with open('assets/phon_numbers.txt','w') as final_file:
        final_file.write(f'{phon_numbers} \n') 
            

      



atumation_regex("assets/potential-contacts.txt")




""" 
from faker import Faker
fake = Faker()
print(fake.text())


content = '' 
for i in range(10):
     temp = ""
     temp += fake.paragraph()
     temp += fake.phone_number()
     temp += fake.paragraph()
     temp += fake.ascii_email()
     content+=temp
"""




""" with open('text.txt','w+') as f  :
   f.write(content)  """
"""


import shutil
shutil.copy('text.txt','..')
 """

    