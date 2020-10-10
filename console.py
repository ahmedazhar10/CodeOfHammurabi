# TO-DO
# Build console for laws
# Turn laws into list - DONE
# Categories law in Dict 
# Dict {category:[list_of_laws]}
# Choose category -> Print laws
# Ask which law best suits your situation
# Option to go back to category page or continue with Qs
# Have yes or no for each if
# if yes -> move on to next if in that law
# if no -> move on to next law in the category
# if no to all laws in that category
#       prompt: Guess you're in the wrong category. Redo program

#List of laws
law_file = open("formatted_laws.txt", "r")
law_list = law_file.readlines()
#Remove new-line character from laws
law_list = [law.strip('\n') for law in law_list]
#Declaring dict for laws
law_dict = dict()
law_dict = {
            'People':[law_list[0], law_list[1], law_list[2], law_list[3], law_list[4]]
            }
#Console
while(True):
    print("What is the crime about?")
    print("Category: 1) People")
    prompt_category = int(input("Enter number associated with category: \n"))
    if prompt_category != 1:
        print("Invalid Category")
        continue
    if prompt_category == 1:
        print("1) Is it about a scandal?")  
        print("2) Is it about an accusation?")
        print("3) Is it about satisfying the elders to impose a fine?")
        print("4) Is it about an error in judgement?")
        #    -> Yes -> Penalty -> Redo Program

        prompt_case = int(input("Enter number associated with the question: "))
        if prompt_case != 1 and prompt_case != 2 and prompt_case != 3 and prompt_case != 4:
            print("Invalid response!")
            continue
        if prompt_case == 1:
            print("Is there valid proof for that scandal?")
            prompt_char = input("Enter character: Yes[y] or No[n]")
            #Response Check
            if prompt_char != "y" and prompt_char != "Y" and prompt_char != "N" and prompt_char != "n":
                print("Error: Invalid Response") 
                continue
            if prompt_char == 'y' or prompt_char == 'Y':
                print("Judgment shan't be passed")
                print("Court adjourned!")
                continue
            if prompt_char == 'n' or prompt_char == 'N':
                print("Judgment has passed")
                print("Put the Accuser to DEATH!")
                print(law_dict['People'][0]) #Law citation
        if prompt_case == 2:
            print("Is it a False accusation")
            prompt_char = input("Enter character: Yes[y] or No[n]")
            #Response Check
            if prompt_char != "y" and prompt_char != "Y" and prompt_char != "N" and prompt_char != "n":
                print("Error: Invalid Response") 
                continue
            if prompt_char == 'y' or prompt_char == 'Y':
                print("Judgment has passed")
                print("Put the Accuser to DEATH!")
                print(law_dict['People'][2]) #Law citation
            if prompt_char == 'n' or prompt_char == 'N':
                print("Did the accused leap in a river and survive?")
                prompt_char = input("Enter character: Yes[y] or No[n]")
                #Response Check
                if prompt_char != "y" and prompt_char != "Y" and prompt_char != "N" and prompt_char != "n":
                    print("Error: Invalid Response") 
                    continue
                if prompt_char == "y" or prompt_char == "Y":
                    print("Judgment has passed")
                    print("Accuser be put to Death and \nThe accused shall take the accucer's house in their possession")
                    print(law_dict['People'][1])    
                if prompt_char == "n" or prompt_char == "N":
                    print("Judgment has passed")
                    print("Accuser shall take possession of the house of the accused")
                    print(law_dict['People'][1])
        if prompt_case == 3:
            print("Did they satisfy the elders to impose a fine?")
            prompt_char = input("Enter character: Yes[y] or No[n]")
            #Response Check
            if prompt_char != "y" and prompt_char != "Y" and prompt_char != "N" and prompt_char != "n":
                print("Error: Invalid Response") 
                continue
            if prompt_char == 'y' or prompt_char == 'Y':
                print("Judgment has passed")
                print("Guilty shall receive a fine")
                print(law_dict['People'][3]) #Law citation
            if prompt_char == "n" or prompt_char == "N":
                print("Judgment shan't be passed")
                print("Court adjourned!")
                continue
        if prompt_case == 4:
            print("Did the judge err in their decision?")
            prompt_char = input("Enter character: Yes[y] or No[n]")
            #Response Check
            if prompt_char != "y" and prompt_char != "Y" and prompt_char != "N" and prompt_char != "n":
                print("Error: Invalid Response") 
                continue
            if prompt_char == "n" or prompt_char == "N":
                print("Judgment shan't be passed")
                print("Court adjourned!")
                continue
            if prompt_char == 'y' or prompt_char == 'Y':
                print("Judgment has passed")
                print("Judge shall pay 12 times the fine set by them \n Judge shall be removed from the judge's bench permanently")
                print(law_dict['People'][4]) #Law citation


      