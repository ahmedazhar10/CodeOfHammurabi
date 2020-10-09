#----------FORMATTING LAWS.TXT----------#
# insert the string  
# at the beginning of all items in a list 
def prepend(list, str): 
    # Using format() 
    str += '{0}'
    list = [str.format(i) for i in list] 
    return(list) 
#Reading laws.txt
law_file = open("laws.txt", "r")
laws = law_file.readlines()
#Formating laws
format_laws = [law for law in laws if law.strip() != ""]
format_laws = prepend(format_laws, 'Law ')
for i in range(len(format_laws)):
    format_laws[i] = format_laws[i].replace(".", ":", 1)
#Outputting formatted Laws       
format_law_file = open("formatted_laws.txt", "w")
format_law_file.writelines(format_laws)
format_law_file.close()
law_file.close()

#TO-DO
#Incorporate this in main.py
#Define input file path in main.py