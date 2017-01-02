def calc_CPM(cpc, ctr):
	cpm = cpc * ctr * 10.0
	return cpm

def calc_CPC(cpm, ctr):
	cpc = cpm / (ctr * 10.0)
	return cpc


def main():
	print "Enter the number corresponding to what you want to calculate"
	#choices
	print "[1] CPM - Cost per Mille"
	print "[2] CPC - Cost per Click"


	#get choice from user
	choice = input("Enter your choice: ")

	#running functions based on choice
	if 		choice == 1:
		cpc = input("Plase input your CPC (example $0.50): $")
		ctr = input("Please input your CTR in % (example 1): ")
		cpm = calc_CPM(cpc, ctr)
		print "$" + str(cpm)
	elif	choice == 2:
		cpm = input("Please input your CPM (example $5): $")
		ctr = input("Please input your CTR in % (example 1): ")
		cpc = calc_CPC(cpm, ctr)
		print "$" + str(cpc)



print "Hello user! This program will help you with ad Math"
main()		