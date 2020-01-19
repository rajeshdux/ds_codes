import os.path
import pickle



def fwrite(file_name, a_data):

    try:

        fname = file_name
        w_data = a_data

        if os.path.exists('E:/PythonProjects/datafiles/' + fname):
            print("File Found..to append")
        else:
            print("Write: FIle not Found...")

        filename,file_extension = os.path.splitext('E:/PythonProjects/datafiles/' + fname)
        print("fName: ",filename," ","Ext: ",file_extension)

        if file_extension=='.txt' and type(w_data) == list:
            with open("E:/PythonProjects/datafiles/" + fname, 'w') as f:
                f.writelines(["%s " % item for item in w_data])
                # f.write("\n")
                print("Written list in file...")


        elif file_extension == '.pickle' and type(a_data) == dict :
            with open("E:/PythonProjects/datafiles/" + fname, 'wb') as f:
                d={}
                d=w_data
                print('Pickle_dict_a: ',d)
                pickle.dump(d,f,protocol=pickle.HIGHEST_PROTOCOL)
                print("Dumped data into file...written")
        else:
            raise Exception("Problem writing file...")

    except Exception as ex:
        print(ex)

    finally:
        f.close()




def fread(file_name: object) -> object:
    try:

        fname = file_name

        if os.path.exists('E:/PythonProjects/datafiles/' + fname):
            print("File Found to read...")
        else:
            print("Read: FIle Not Found...")

        filename, file_extension = os.path.splitext('E:/PythonProjects/datafiles/' + fname)
        print("fName: ", filename, " ", "Ext: ", file_extension)

        if file_extension == ".txt":
            with open("E:/PythonProjects/datafiles/" + fname, 'r') as f:
                l=[]
                l=f.read().strip().split(' ')
                return l


        elif file_extension == '.pickle':
            with open("E:/PythonProjects/datafiles/" + fname, 'rb') as f:
                d = pickle.load(f)
                print('Pickle_dict_r: ', d)
                return d
        else:
            raise Exception("Problem reading file...")

    except Exception as ex:
        print(ex)

    finally:
        f.close()


def fappend(file_name, a_data):

    try:
        fname = file_name
        a_data = a_data

        if os.path.exists('E:/PythonProjects/datafiles/' + fname):
            print("File Found..to append")
        else:
            print("Append: File Not Found.....")

        filename, file_extension = os.path.splitext('E:/PythonProjects/datafiles/' + fname)
        print("fName: ",filename," ","Ext: ",file_extension)

        if file_extension=='.txt' and type(a_data) == list:
            with open("E:/PythonProjects/datafiles/" + fname, 'a') as f:
                f.writelines(["%s " % item for item in a_data])
                # f.write("\n")
                print("Appended list in file...")


        elif file_extension == '.pickle' and type(a_data) == dict :
            with open("E:/PythonProjects/datafiles/" + fname, 'ab') as f:
                d={}
                d=a_data
                print('Pickle_dict_a: ',d)
                pickle.dump(d,f,protocol=pickle.HIGHEST_PROTOCOL)
                print("Dumped data into file...appended")
        else:
            raise Exception("Problem appending file...")

    except Exception as ex:
        print(ex)

    finally:
        f.close()
