# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from Sem_7 import main1
from Sem_7 import write_names_to_file,generate_name
from Sem_7 import func
from Home_work_7.task_1 import generate_name, renaming


main1('task_1_file.txt', 8)
write_names_to_file('task_2_file.txt',10) 
func()

new_name= generate_name()
renaming(new_name,5,'.txt','.txt', [1,3]) #,'.dat','.txt',