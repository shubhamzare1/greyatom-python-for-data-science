# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





#Code starts here
data = pd.read_csv(path)
#print(data)
loan_status = data['Loan_Status'].value_counts()
print(loan_status)
plt.bar(loan_status.index,20)
plt.show()


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area','Loan_Status'])
print(property_and_loan)
property_and_loan = property_and_loan.size().unstack()
plt.bar(property_and_loan.index,20)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status'])
education_and_loan = education_and_loan.size().unstack()
plt.bar(education_and_loan.index,20)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here
graduate = data[data['Education']== 'Graduate']
not_graduate = data[data['Education']== 'Not Graduate']

graduate['LoanAmount'].plot(kind ='density',label='Graduate')
not_graduate['LoanAmount'].plot(kind ='density',label='not_graduate')

#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows = 3 , ncols = 1)
#res = data.groupby(['ApplicantIncome', 'LoanAmount']).size().unstack()
#res.plot(kind='scatter', stacked=True, ax=ax_1,title='Applicant Income')
data.plot.scatter('ApplicantIncome','LoanAmount', ax=ax_1,title='Applicant Income')
data.plot.scatter('CoapplicantIncome','LoanAmount', ax=ax_2 ,title='Coapplicant Income')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
#print(data)
data.plot.scatter('ApplicantIncome','LoanAmount', ax=ax_3, title='Total Income')


