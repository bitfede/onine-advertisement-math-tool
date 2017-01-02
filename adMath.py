##
#	Author: Federico Giorgio De Faveri
##

def calc_CPM(cpc, ctr):
	cpm = cpc * ctr * 10.0
	return cpm

def calc_CPC(cpm, ctr):
	cpc = cpm / (ctr * 10.0)
	return cpc

def calc_CTR_viewsclicks(clicks, views):
	ctr = (100.0 * clicks) / views
	return ctr
def calc_CTR_cpmcpc(cpm, cpc):
	ctr = cpm / (cpc * 10.0)
	return ctr

def main():
	print "Enter the number corresponding to what you want to calculate"
	#choices
	print "[1] CPM - Cost per Mille"
	print "[2] CPC - Cost per Click"
	print "[3] CTR - Clickthrough Rate"

	#get choice from user
	choice = input("Enter your choice: ")

	#running functions based on choice
	if 		choice == 1:
		cpc = input("Plase enter your CPC (example $0.50): $")
		ctr = input("Please enter your CTR in % (example 1): ")
		cpm = calc_CPM(cpc, ctr)
		print "$" + str(cpm)
	elif	choice == 2:
		cpm = input("Please enter your CPM (example $5): $")
		ctr = input("Please enter your CTR in % (example 1): ")
		cpc = calc_CPC(cpm, ctr)
		print "$" + str(cpc)
	elif choice  == 3:
		print "If you have: number of clicks and views enter [1]"
		print "If you have: CPM and CPC enter [2]"
		ctr_choice = input("Your choice: ")
		if ctr_choice == 1:
			clicks = input("Please enter the number of clicks: ")
			views = input("Please enter the number of views: ")
			ctr = calc_CTR_viewsclicks(clicks, views)
			print str(ctr) + "%"
		elif ctr_choice == 2:
			cpm = input("Please enter your CPM (example $5): $")
			cpc = input("Plase enter your CPC (example $0.50): $")
			ctr = calc_CTR_cpmcpc(cpm, cpc)
			print str(ctr) + "%"
		else:
			print "Incorrect Choice."


print "Hello user! This program will help you with ad Math"
main()		