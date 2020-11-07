
import os
import pprint

def check_nested_folder(file_path, fileOpen, no, totalFile, totalFolder):
    l1 = os.listdir(file_path)

    for i in l1:

        if '.'not in i:
            print('\t \t' + str(no) + i + '\t (Folder)')
            fileOpen.write('\t \t' + str(no)+ ' - ' + i + '\t (Folder) \n')
            no += 1
            totalFolder += 1
            
            no, totalFile, totalFolder = check_nested_folder(file_path + '\\' + i, fileOpen, no, totalFile, totalFolder)

        else:
            print('\t\t'+ str(no) + i + '\t (File)')
            fileOpen.write('\t \t'+ str(no) + ' - ' + i + '\t (File) \n')
            no += 1
            totalFile += 1

    return no, totalFile, totalFolder

if __name__ == '__main__':
    filePath = input('Enter Folder Path to Convert it\'s File Names to store in Text File :')

    # filePath = 'C:\\Users\\{your_username}\\Desktop\\7th Sem'
    # filePath - Path of folder from which files names are to be extracted and stored
    #            in TXT file.
    # txtFile = 'C:\\Users\\{username}\\Desktop\\Programming\\python_output\\file_names.txt'
    # txtFile - Path of TXT file in which you want names.

    txtFile = input('Enter location of TXT file in which You want to store names of files :')
    fileOpen = open(txtFile, 'w')

    no = 1
    totalFile = 0
    totalFolder = 0
    no, totalFile, totalFolder = check_nested_folder(filePath, fileOpen, no, totalFile, totalFolder)

    print(totalFile, totalFolder)

    # pprint.pprint(list1)   # For Printing in Pretty Way.

    fileOpen.write('\n \n')
    fileOpen.write('\t\t' + 'Total Folder : ' + str(totalFolder) + '\n')
    fileOpen.write('\t\t' + 'Total File :   ' + str(totalFile) + '\n')

    # Writing to the TXT File in C:\Users\{username}\Desktop\Programming\python_output

    fileOpen.close()