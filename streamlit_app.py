import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import chardet

# Define the path to your data file
data_path = "C:/Users/17742/OneDrive/Desktop/NYU/2023 Fall/study/global_education_data.csv"

# Read data and detect encoding
with open(data_path, 'rb') as f:
    result = chardet.detect(f.read())

file_encoding = result['encoding']
df = pd.read_csv(data_path, encoding=file_encoding)

# Rest of the code remains the same...

# Read data and detect encoding
with open(data_path, 'rb') as f:
    result = chardet.detect(f.read())

file_encoding = result['encoding']
df = pd.read_csv(data_path, encoding=file_encoding)

# Streamlit application
st.title("Global Education Data Analysis")

# Sidebar with analysis options
st.sidebar.title("Research Questions")
selected_analysis = st.sidebar.radio("Select analysis question", [
    "Question 1: Top 10 countries with the highest out-of-school rates",
    "Question 2: Top 10 countries with the highest completion rates",
    "Question 3: Top 10 countries with primary and high school enrollment rates"
])

# Display analysis results
st.subheader("Analysis Results")

if selected_analysis == "Question 1: Top 10 countries with the highest out-of-school rates":
    # Age group selection
    age_group = st.selectbox("Select age group", ["Pre0Primary", "Primary", "Lower_Secondary", "Upper_Secondary"])

    # Filter data
    df_filtered = df[df[f'OOSR_{age_group}_Age_Male'].notna()]

    # Get top 10 countries with the highest dropout rates
    top_countries = df_filtered.nlargest(10, f'OOSR_{age_group}_Age_Male')[['Countries and areas', f'OOSR_{age_group}_Age_Male']]

    # Display table
    st.table(top_countries)

    # Bar chart
    fig, ax = plt.subplots()
    ax.bar(top_countries['Countries and areas'], top_countries[f'OOSR_{age_group}_Age_Male'])
    ax.set_xlabel('Countries and areas')
    ax.set_ylabel(f'OOSR_{age_group}_Age_Male')
    ax.set_title(f'Top 10 Countries with Highest Dropout Rate ({age_group} Age Group - Male)')
    st.pyplot(fig)

elif selected_analysis == "Question 2: Top 10 countries with the highest completion rates":
    # Age group selection
    age_group = st.selectbox("Select age group", ["Primary", "Lower_Secondary", "Upper_Secondary"])

    # Filter data
    df_filtered = df[df[f'Completion_Rate_{age_group}_Male'].notna()]

    # Get top 10 countries with the highest completion rates
    top_countries = df_filtered.nlargest(10, f'Completion_Rate_{age_group}_Male')[['Countries and areas', f'Completion_Rate_{age_group}_Male']]

    # Display table
    st.table(top_countries)

    # Bar chart
    fig, ax = plt.subplots()
    ax.bar(top_countries['Countries and areas'], top_countries[f'Completion_Rate_{age_group}_Male'])
    ax.set_xlabel('Countries and areas')
    ax.set_ylabel(f'Completion_Rate_{age_group}_Male')
    ax.set_title(f'Top 10 Countries with Highest Completion Rate ({age_group} Age Group - Male)')
    st.pyplot(fig)

elif selected_analysis == "Question 3: Top 10 countries with primary and high school enrollment rates":
    # Select top 10 countries
    top_countries = df.nlargest(10, 'Gross_Primary_Education_Enrollment')

    # Display table
    st.table(top_countries[['Countries and areas', 'Gross_Primary_Education_Enrollment', 'Gross_Tertiary_Education_Enrollment']])

    # Line chart
    st.subheader("Line Chart for Top 10 Countries with Highest Enrollment Rates")
    fig, ax = plt.subplots()
    ax.plot(top_countries['Countries and areas'], top_countries['Gross_Primary_Education_Enrollment'], label='Primary Enrollment')
    ax.plot(top_countries['Countries and areas'], top_countries['Gross_Tertiary_Education_Enrollment'], label='Tertiary Enrollment')
    ax.set_xlabel('Countries')
    ax.set_ylabel('Enrollment')
    ax.set_title('Top 10 countries with primary and high school enrollment rates')
    ax.legend()
    st.pyplot(fig)
