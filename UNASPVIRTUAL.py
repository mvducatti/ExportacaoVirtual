import csv
import codecs
import io


credentials = {}
fileGroup = []
fileEnroll = []

'''
                        Arquivo de configuração 
    (Antes do : acontece a identificação do curso se é AD = Administração)

'''

with open('UNASPVIRTUAL.txt', 'r') as f: 
    for line in f:
        curso, nameGroup,cursoEad = line.strip().split(':') #nome do grupo é igual ao que se encontra no unasp Virtual
        credentials[curso] = [nameGroup,cursoEad] #Cria um vetor de importação        


with open('ENROLL.CSV') as csvfile: #Le arquivo .csv 
    readCSV = csv.reader(csvfile, delimiter=',') 
    next(readCSV)   
    for row in readCSV:
        if(credentials.has_key(row[1])):#Verifica se ele pertence ao grupo do curso EAD CV-MP
            if(row[3] == 'student'):
                nameOfGroup = credentials[row[1]][0] # Nome do grupo que é extraido do arquivo de configuração
                initialsCourse = credentials[row[1]][1] # sigla do curso a ser importado extraido ... 

                lineArquivoGroup = "{},{},{},{}".format(row[0],initialsCourse,row[2],nameOfGroup)    
                lineArquivoENROLL = "{},{},{},{}".format(row[0],initialsCourse,row[2],row[3])
                
                fileGroup.append(lineArquivoGroup)
        else:
            lineArquivoENROLL = "{},{},{},{}".format(row[0],row[1],row[2],row[3])                                                                     
                
        fileEnroll.append(lineArquivoENROLL)
        

        #seleciona coluna que tem o código da disciplina e verificar de qual curso
        # o Row[1] e a informação do curso em código como  HT_AD_AC_2A
        # importante que a abreviação do curso deve ficar na segunda posição 
    
csvfile = "3_group_members.csv"

with open(csvfile, "w") as text_file:
    text_file.writelines('action,coursekey,userkey,groupkey\n')
    for f  in fileGroup:
        text_file.writelines(f+'\n')


csvfile = "2_ENROLL_Python.csv"

with open(csvfile, "w") as text_file:
    text_file.writelines('action,coursekey,userkey,rolekey\n')    
    for f  in fileEnroll:
        text_file.writelines(f+'\n')

path =  'USERS.CSV'



#read input file
with codecs.open(path, 'r', encoding = 'latin-1') as file:
  lines = file.read()  

#write output file
with codecs.open('1_UserPython.CSV', 'w', encoding = 'utf_8_sig') as file:
  file.write(lines)