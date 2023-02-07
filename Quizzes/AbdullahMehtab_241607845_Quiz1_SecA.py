##Quiz One
print()
print("Quiz One")
print()
#Working
my_list = [8,6,7,5,4,3,2,1,4,2,6,5,7] 
def my_max(m_list): 
	max = m_list[0] 
	for i in m_list: 
		if m_list[i] > max: 
			max =m_list[i] 
	return max 
print()
#Printing
print('Maximum of all the numbers is ' + str(my_max(my_list))) 
input('Press any Key to END.')