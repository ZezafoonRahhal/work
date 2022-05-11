list=['zeina','ali','reem','samar','dalal']
stdname=input('enter student name')
for i in range(len(list)):
    if stdname in list:
        print(stdname ,'well done student graduated')
        break
    else:
        print(stdname,'unfortunately the student did not graduate')
        break
