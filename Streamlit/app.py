
# importing streamlit
import streamlit as st
  
# this is the main function in which we define our app  
def main():
    # header of the page
    st.markdown("Check your Loan Eligibility") 

    # Loading the data
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.selectbox('Gender',("Male","Female","Other"))
    Married = st.selectbox('Marital Status',("Unmarried","Married","Other")) 
    ApplicantIncome = st.number_input("Monthly Income in Rupees") 
    LoanAmount = st.number_input("Loan Amount in Rupees")
    result =""
      
    # when 'Check' is clicked, make the prediction and store it 
    if st.button("Check"): 
        result = prediction(Gender, Married, ApplicantIncome, LoanAmount) 
        st.success('Your loan is {}'.format(result))

# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married, ApplicantIncome, LoanAmount):

    # Building the model to automate Loan Eligibility
    if (ApplicantIncome < 20000):
        loan_status = 'Rejected'
    elif (LoanAmount > 600000):
        loan_status = 'Rejected'
    else:
        loan_status = 'Approved'
    return loan_status
     
if __name__=='__main__': 
    main()
