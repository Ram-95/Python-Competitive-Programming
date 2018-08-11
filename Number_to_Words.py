#Number to Words
n_inp = int(input(''))
for item in range(0,n_inp):
    
    num = input()
    num_list = list(num)

    dict_names_ones = {'1':'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0' : 'zero'}
    dict_names_tens = {'1':'ten', '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety', '0': ''}
    dict_ones_in_tens = {'11':'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '10': 'ten'}
    list_len = len(num_list)



#Printing 4 digit Numbers
    if num_list[0] != 0:
        if len(num_list) == 4:
            if (''.join(num_list[1:])) == '000':
                print(dict_names_ones[num_list[0]] + ' thousand')
            elif (''.join(num_list[2:])) == '00':
                print(dict_names_ones[num_list[0]] + ' thousand ' + dict_names_ones[num_list[1]] + 'hundred')
            #elif (''.join(num_list[3:])) == '0':
             #   print(dict_names_ones[num_list[0]] + ' thousand ' + dict_names_ones[num_list[1]] + ' hundred and ' + dict_names_tens[num_list[2]])
            elif (num_list[1] == '0' and num_list[2] != '0'):
                if (num_list[2] != '1' and num_list[3] != '0'):
                    print(dict_names_ones[num_list[0]] + ' thousand and ' + dict_names_tens[num_list[2]] + ' '+ dict_names_ones[num_list[3]])
                elif (num_list[2] == '1'):
                    print(dict_names_ones[num_list[0]] + ' thousand and ' + dict_ones_in_tens[''.join(num_list[-2:])])
                elif (num_list[2] != '1' and num_list[3] == '0'):
                    print(dict_names_ones[num_list[0]] + ' thousand and ' + dict_names_tens[num_list[2]])
            elif (num_list[1] == '0' and num_list[2] == '0'):
                print(dict_names_ones[num_list[0]] + ' thousand and ' + dict_names_ones[num_list[3]])
                
            else:
                if (num_list[-2] == '1'):
                    print(dict_names_ones[num_list[0]] + ' thousand ' + dict_names_ones[num_list[1]]+' hundred and '+ dict_ones_in_tens[''.join(num_list[-2:])])
                if (num_list[-2] != '0' and num_list[-1] != '0'):
                    print(dict_names_ones[num_list[0]] + ' thousand ' + dict_names_ones[num_list[1]]+' hundred and '+ dict_names_tens[num_list[2]] + ' ' + dict_names_ones[num_list[3]])
                if (num_list[2] == '0' and num_list[3] != '0'):
                    print(dict_names_ones[num_list[0]] + ' thousand '+ dict_names_ones[num_list[1]] + ' hundred and ' + dict_names_ones[num_list[3]])
                if (num_list[-2] != '1' and num_list[-1] == '0'):
                    print(dict_names_ones[num_list[0]] + ' thousand ' + dict_names_ones[num_list[1]]+ ' hundred and ' + dict_names_tens[num_list[2]])
                

# Printing 3 digit Numbers
        elif len(num_list) == 3:
            if (''.join(num_list[1:])) == '00':
                print(dict_names_ones[num_list[0]] + ' hundred')
            else:
                if num_list[1] == '1':
                    print(dict_names_ones[num_list[0]]+' hundred and '+ dict_ones_in_tens[''.join(num_list[-2:])])
                if (num_list[2] == '0'):
                    print(dict_names_ones[num_list[0]]+' hundred and '+ dict_names_tens[num_list[1]])
                    #print(dict_names_ones[num_list[0]]+' hundred and '+ dict_names_tens[num_list[1]]+ dict_names_ones[num_list[2]])
                if(num_list[1] != '0' and num_list[2] != '0'):
                    #print(dict_names_ones[num_list[0]]+' hundred and '+ dict_names_tens[num_list[1]])
                    print(dict_names_ones[num_list[0]]+' hundred and '+ dict_names_tens[num_list[1]]+ ' ' + dict_names_ones[num_list[2]])
                if(num_list[1] == '0' and num_list[2] != '0'):
                    print(dict_names_ones[num_list[0]] + ' hundred and ' + dict_names_ones[num_list[2]])


# Priting 2 digit Numbers
        elif len(num_list) == 2:
            if (''.join(num_list[1:])) == '0':
                print(dict_names_tens[num_list[0]])
            else:
                if num_list[-2] == '1':
                    print(dict_ones_in_tens[''.join(num_list[-2:])])
                else:
                    print(dict_names_tens[num_list[0]] + ' ' + dict_names_ones[num_list[1]])
        elif len(num_list) == 1:
            print(dict_names_ones[num_list[0]])
        else:
            print('Please Enter a Number!!')
        
        
    
