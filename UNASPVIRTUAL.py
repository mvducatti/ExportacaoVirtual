import csv
import re

credentials = {}
fileGroup = []
fileEnroll = []

'''
                        Arquivo de configuração 
    (Antes do : acontece a identificação do curso se é AD = Administração)

'''
with open('UNASPVIRTUAL.txt', 'r') as f: 
    for line in f:
        curso, nameGroup = line.strip().split(':') #nome do grupo é igual ao que se encontra no unasp Virtual
        credentials[curso] = nameGroup #Cria um vetor de importação        

cursoEad = 'CV-MP'

with open('ENROLL.CSV') as csvfile: #Le arquivo .csv 
    readCSV = csv.reader(csvfile, delimiter=',') 
    next(readCSV)   
    for row in readCSV:                                 
        if(row[3] == 'student' and credentials.has_key(row[1])):
            lineArquivoGroup = "{},{},{},{}".format(row[0],cursoEad,row[2],credentials[row[1]])    
            lineArquivoENROLL = "{},{},{},{}".format(row[0],cursoEad,row[2],row[3])

            fileGroup.append(lineArquivoGroup)    
            fileEnroll.append(lineArquivoENROLL)
        

        #seleciona coluna que tem o código da disciplina e verificar de qual curso
        # o Row[1] e a informação do curso em código como  HT_AD_AC_2A
        # importante que a abreviação do curso deve ficar na segunda posição 
    
csvfile = "group_members.csv"

with open(csvfile, "w") as text_file:
    text_file.writelines('action,coursekey,userkey,groupkey\n')
    for f  in fileGroup:
        text_file.writelines(f+'\n')


csvfile = "ENROLL_Python.csv"

with open(csvfile, "w") as text_file:
    text_file.writelines('action,coursekey,userkey,rolekey\n')    
    for f  in fileEnroll:
        text_file.writelines(f+'\n')