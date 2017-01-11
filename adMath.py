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

def calc_CVR(conversions, visitors):
	cvr = (conversions/ float(visitors)) * 100.0
	return cvr

def calc_EPC(payout, cvr):
	epc = (payout * cvr) / 100.0
	return epc

def calc_CPA(cpc, cvr):
	cpa = (cpc * 100.0) / cvr
	return cpa

def calc_eCPM(ctr, cvr, payout):
	ecpm = (ctr * cvr * payout) / 10.0
	return ecpm

def calc_profit_cpcepc(epc, cpc, ad_spend):
	profit = ( (epc - cpc) * ad_spend) / (cpc + 0.00)
	return profit
def calc_profit_ecpmcpm(ecpm, cpm, ad_spend):
	profit = ( (ecpm - cpm) * ad_spend) / (cpm + 0.00)
	return profit
def calc_profit_payoutcpa(payout, cpa, ad_spend):
	profit = ( (payout - cpa) * ad_spend) / (cpa + 0.00)
	return profit
def calc_profit_roispend(roi, spend):
	profit = (roi * spend) / 100.0
	return profit

def main():
	print "Enter the number corresponding to what you want to calculate"
	#choices
	print "------- Ad Math --------"
	print "[1] CPM  - Cost per Mille"
	print "[2] CPC  - Cost per Click"
	print "[3] CTR  - Clickthrough Rate"
	print "------ Offer Math ------"
	print "[4] CVR  - Conversion Rate"
	print "[5] EPC  - Earning per Click"
	print "[6] CPA  - Cost per Acion"
	print "[7] eCPM - Effective Cost per Mille"
	print "-- Profitability Math --"
	print "[8] P/L  - Profit / Loss"
	print ""
	#get choice from user
	choice = input("Enter your choice: ")

	#running functions based on choice
	
	if choice == 1:
		cpc = input("Plase enter your CPC (example $0.50): $")
		ctr = input("Please enter your CTR as a % (example 1): ")
		cpm = calc_CPM(cpc, ctr)
		print "$" + str(cpm)
	elif choice == 2:
		cpm = input("Please enter your CPM (example $5): $")
		ctr = input("Please enter your CTR as a % (example 1): ")
		cpc = calc_CPC(cpm, ctr)
		print "$" + str(cpc)
	elif choice  == 3:
		print "If you have: number of clicks and views, enter [1]"
		print "If you have: CPM and CPC, enter [2]"
		ctr_choice = input("Enter your choice: ")
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
	elif choice == 4:
		conversions = input("Please enter the number of conversions: ")
		visitors = input("Please enter the number of visitors: ")
		cvr = calc_CVR(conversions, visitors)
		print str(cvr) + "%"
	elif choice == 5:
		payout = input("Please enter your payout: $")
		cvr = input("Please enter your CVR as a % (example 5): ")
		epc = calc_EPC(payout, cvr)
		print "$" + str(epc) 
	elif choice == 6:
		cpc = input("Please enter your CPC (example $0.20): $")
		cvr = input("Please enter your CVR in % (example 5): ")
		cpa = calc_CPA(cpc, cvr)
		print "$" + str(cpa)
	elif choice == 7:
		ctr = input("Please enter your CTR as a % (example 1): ")
		cvr = input("Please enter your CVR as a % (example 5): ")
		payout = input("Please enter your payout: $")
		ecpm = calc_eCPM(ctr, cvr, payout)
		print "$" + str(ecpm)
	elif choice == 8:
		print "If you have: EPC, CPC, total spend on ads, enter [1]"
		print "If you have: eCPM, CPM, total spend on ads, enter [2]"
		print "If you have: payout, CPA, total spend on ads, enter [3]"
		print "If you have: ROI, spend, enter [4]"
		profit_choice = input("Enter your choice: ")
		if profit_choice == 1:
			epc = input("Please enter your EPC (example $0.10): $")
			cpc = input("Please enter your CPC (example $0.20): $")
			ad_spend = input("Please enter your total spend on ads: $")
			profit = calc_profit_cpcepc(epc, cpc, ad_spend)
			print "$" + str(profit)
		elif profit_choice == 2:
			ecpm = input("Please enter your eCPM (example $10): $")
			cpm = input("Please enter your CPM (example $5): $")
			ad_spend = input("Please enter your total spend on ads: $")
			profit = calc_profit_ecpmcpm(ecpm, cpm, ad_spend)
			print "$" + str(profit)
		elif profit_choice == 3:
			payout = input("Please enter your payout (example $2): $")
			cpa = input("Please enter your CPA (example $1): $")
			ad_spend = input("Please enter your total spend on ads: $")
			profit = calc_profit_payoutcpa(payout, cpa, ad_spend)
			print "$" + str(profit)
		elif profit_choice == 4:
			roi = input("Please enter your ROI as a % (example 300): ")
			spend = input("Please enter your maximum spend a day (example $5): $")
			profit = calc_profit_roispend(roi, spend)
			print "$" + str(profit)
		else:
			print "Incorrect Choice."
	else:
		print "fu"


print "Hello user! This program will help you with ad Math"
main()		