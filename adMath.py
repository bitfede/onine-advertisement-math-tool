def calc_CPM(cpc, ctr):
	cpm = cpc * ctr * 10
	return cpm


print "Hello user! This program will help you with ad Math"
print "Enter the number corresponding to what you want to calculate"
#choices
print "[1] CPM - Cost per Mille"



#get choice from user
choice = input("Enter your choice: ")

#running functions based on choice
if 		choice == 1:
	cpc = input("Plase input your CPC: ")
	ctr = input("Please input your CTR: ")
	print calc_CPM(cpc, ctr)
elif	choice == 2:
	#do stuff
