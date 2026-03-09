# wtrite a program to fill in letter template given below with name and date.
letter='''Dear <|Name| 
          you are selected!
            <|date| >'''

print(letter.replace("<|Name|","Nitish").replace("<|date| >","23 may 2026"))    #chaining of replace