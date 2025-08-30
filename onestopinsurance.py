# Description: A program to enter and calculate new insurance policy 
#              information for the One Stop Insurance Company.
# Author: Laura Wiseman 
# Date(s): July 17, 2024 - July 24, 2024


# Define required libraries.
import datetime 
import time
import sys
# import FormatValues as FV


# Define program constants.
f = open('const.dat', 'r')
POLICY_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
DISC_ADDITIONAL = float(f.readline())
LIABILITY_EXTRA = float(f.readline())
GLASS_COVERAGE = float(f.readline())
LOANER_COVERAGE = float(f.readline())
HST_RATE = float(f.readline())
PROCESS_FEE = float(f.readline())
f.close()

CUR_DATE = datetime.datetime.now()
CurDate = CUR_DATE.strftime("%B %d, %Y")


 
# Define program functions.
def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    # Generate and display a progress bar with % complete at the end.
 
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()


def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr

def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%B-%d-%Y")

    return DateValueStr

def get_first_of_next_month(date):
    # Function will get the first day of the next month, for the first payment date.
    next_month = date.month % 12 + 1
    next_year = date.year + (date.month // 12)
    first_of_next_month = datetime.date(next_year, next_month, 1)
    return first_of_next_month





# Main program starts here.
while True: 
    # Gather user inputs
   
    CustFirstName = input('Please enter the customers first name: ').title()
    CustLastName = input('Please enter the customers last name: ').title()
    StAdd = input('Please enter the street address: ').title()
    City = input('Please enter the city: ').title()
    PostalCode = input('Please enter the postal code (XXX XXX): ').upper()

    
        
   
    while True: #format
        PhoneNum = input('Please enter the phone number (9999999999): ')
        if PhoneNum == '':
            print('Data Entry Error - Phone number cannot be blank - Please reenter.')
        elif PhoneNum.isdigit == False:
         print('Data Entry Error - Phone number must be 10 digits - please reenter.')
        else: 
            break
        
    
    ProvLst = ['NL', 'NS', 'PE', 'NB', 'QC', 'ON', 'AB', 'BC', 'PEI', 'MB', 'SK', 'NT', 'NU', 'YT']
    while True:
        Prov = input('Please enter the province (XX): ').upper()
        if Prov == '':
            print('Data Entry Error - Province cannot be blank - Please reenter.')
        elif len(Prov) != 2:
            print('Data Entry Error - Province is a 2 digit code - please reenter.')
        elif Prov not in ProvLst:
            print('Date Entry Error - Not a valid province - please reenter.')
        else:
            break
        
    NumCars = int(input('Enter the number of cars to be insured: '))    
    ExtraLiab = input('Would you like extra liability up to 1,000,000? (Y / N): ').upper()

    GlassCover = input('Would you like glass coverage? (Y / N): ').upper()
    CarLoan = input('Would you like a loaner car? (Y / N ): ').upper()

    PayOptionLst = ['Full', 'Monthly', 'Down Pay']
    while True: 
        PayOption = input('Payment method (Full, Monthly or Down Pay): ').title()
        if PayOption == ('Down Pay'):
            DownPay = float(input('Enter the down payment amount: '))
            break
        elif PayOption == (''):
            print('Data Entry Error - Payment method cannot be blank.')
        elif PayOption not in PayOptionLst:
            print('Data Entry Error - Invalid Payment method. Please reenter.')
        else:
            DownPay = 0
            break


    print()
    print('Payment Option has been successfully entered!')
    print()

    Lst1 = []
    Lst2 = []
    Lst3 = []

    while True:
        ClaimNum = input('Enter the previous customer claim number (XXXXX): ')
        ClaimDate = input('Enter the previous claim date (YYYY-MM-DD): ')
        ClaimAmt = input('Enter the previous claim amount: ')
        Lst1.append(ClaimNum)
        Lst2.append(ClaimDate)
        Lst3.append(ClaimAmt)

        Continue = input('Would you like to add another claim? (Y / N): ').upper()
        if Continue == 'N':
            break
        

 # Perform calculations
    
    BasicRateCar = 869.00

    DiscAdditional = BasicRateCar * DISC_ADDITIONAL

    AddCar = (NumCars - 1) * (BasicRateCar - DiscAdditional)

    InsurancePrem = BasicRateCar + AddCar


    if ExtraLiab == 'Y':
        ExtraLiab = 'Yes'
        LiabCover = LIABILITY_EXTRA
    else:
        ExtraLiab = 'No'
        LiabCover = 0

    if GlassCover == 'Y':
        GlassCover = 'Yes'
        GlassFee = GLASS_COVERAGE
    else:
        GlassCover = 'No'
        GlassFee = 0

    if CarLoan == 'Y':
        CarLoan = 'Yes'
        LoanCharge = LOANER_COVERAGE
    else:
        CarLoan = 'No'
        LoanCharge = 0
    
    TotExtCharge = LiabCover + GlassFee + LoanCharge
    TotInsurPrem = InsurancePrem + TotExtCharge
    HST = TotInsurPrem * HST_RATE
    TotCost = TotInsurPrem + HST

    if PayOption == 'Down Pay':
        MonPay = (TotCost - DownPay + PROCESS_FEE) / 8
    else:
        MonPay = (TotCost + PROCESS_FEE) / 8


    CurrDate = get_first_of_next_month(CUR_DATE)
# Conversions

    PhoneNum = '(' + PhoneNum[0:3] + ')' + '-' + PhoneNum[3:6] + "-" + PhoneNum[6:]


# Display results

    print('==================================================')
    print()
    print('  One Stop Insurance Company')
    print()
    print('  123 Duckworth St')
    print('  709-555-1234')
    print()
    print(f'                       Invoice Date: {FDateS(CUR_DATE)}')
    print('==================================================')
    print()
    print(f' Customer Name: {CustFirstName} {CustLastName}')
    print()
    print(f' Address:  {StAdd}')
    print(f'           {City}, {Prov} {PostalCode}')
    print()
    print(f' Phone:    {PhoneNum} (C)') 
    print()
    print(f' Policy #: {POLICY_NUM}')
    print()
    print('==================================================') 
    print(f' Number of Cars Insured:                       {NumCars:>2d} ')
    print()
    print(f' Extra Liabilitity Coverage:                  {ExtraLiab:>3s}')
    print(f' Glass Coverage:                              {GlassCover:>3s}')
    print(f' Loaner Car:                                  {CarLoan:>3s}')
    print ('--------------------------------------------------')
    print(f' Payment Method:                         {PayOption:>8s}')
    print()
    print(f' Down Payment Amount:                   {FDollar2(DownPay):>9s}')
    print(f' Monthly Payment:                       {FDollar2(MonPay):>9s}')
    print()
    print(f' Insurance Premiums:                    {FDollar2(InsurancePrem):>9s}')
    print(f' Total Insurance Premiums:              {FDollar2(TotInsurPrem):>9s}')
    print ('--------------------------------------------------')
    print(f' Total Extra Charges:                   {FDollar2(TotExtCharge):>9s}')
    print(f' HST:                                   {FDollar2(HST):>9s}')
    print(f' Total Cost:                            {FDollar2(TotCost):>9s}')
    print ('--------------------------------------------------')
    print(f' First Payment Date:               {FDateS(CurrDate)}')

    print('==================================================')
    print(f'               Previous Claims')
    print('==================================================')
    print(f'     Claim #      Claim Date        Amount')
    print('--------------------------------------------------')

    for ClaimNum, ClaimDate, ClaimAmt in zip(Lst1, Lst2, Lst3):
        ClaimAmtFormatted = f'${float(ClaimAmt):,.2f}'
        
        
        print(f'      {ClaimNum}       {ClaimDate}        {ClaimAmtFormatted}')
    print(f'                                   ')

    
    f = open('InsurancePolicy.dat', 'a')
    
    f.write(f'{str(POLICY_NUM)}, ')
    f.write(f'{CustFirstName} {CustLastName}, ')
    f.write(f'{StAdd}, ')
    f.write(f'{City}, ')
    f.write(f'{Prov}, ')
    f.write(f'{PostalCode}, ')
    f.write(f'{PhoneNum}, ')
    f.write(f'{str(NumCars)}, ')
    f.write(f'{ExtraLiab}, ')
    f.write(f'{GlassCover}, ')
    f.write(f'{CarLoan}, ') 
    f.write(f'{PayOption}, ')
    f.write(f'{str(DownPay)}, ')
    f.write(f'{str(TotInsurPrem)}\n')
    
    
    f.close()
   
    print()

    Message = "Saving Insurance Data ..."
    for _ in range(5):  # Change to control no. of 'blinks'
        print(Message, end='\r')
        time.sleep(.3)  # To create the blinking effect
        sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
        time.sleep(.3)
 
    print()

    print()
    print("Insurance information has been successfully saved to InsurancePolicy.dat ...")
    print()

    POLICY_NUM += 1

    f = open ('const.dat', 'w')

    f.write(f'{str(POLICY_NUM)}\n')
    f.write(f'{str(BASIC_PREM)}\n')
    f.write(f'{str(DISC_ADDITIONAL)}\n')
    f.write(f'{str(LIABILITY_EXTRA)}\n')
    f.write(f'{str(GLASS_COVERAGE)}\n')
    f.write(f'{str(LOANER_COVERAGE)}\n')
    f.write(f'{str(HST_RATE)}\n')
    f.write(f'{str(PROCESS_FEE)}\n')

    f.close()



    print()
    Continue = input('Would you like to add another insurance claim? (Y / N): ').upper()
    if Continue == 'N':
        break
 
   
   
   
   
   
  


   

    

