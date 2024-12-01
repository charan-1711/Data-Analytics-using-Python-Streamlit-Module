#Importing modules and packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Data Analysis Using Python")

#Uploading csv file
uploaded_file = st.file_uploader("Upload your csv file", type= "csv")

if uploaded_file is not None: #If the file is not empty
    #reading csv file
    df = pd.read_csv(uploaded_file)
    st.write("Overview of Data", df.head()) #Viewing first 5 instances 

    st.divider() #Simple line to seperate contents

    st.header("Data Summary")
    st.write(df.describe()) #Summary statsistics of uploaded dataset
    st.write("Columns:", df.columns)

    st.divider()
    #Data visualization
    st.header("Data Visualization")
    
    #Choose column to plot
    column1 = st.selectbox("Select X-axis", df.columns)
    column2 = st.selectbox("Select Y-axis", df.columns)

    #Choose Type of chart
    chart_type = st.selectbox("Which type of chart you want to visualize", ["Histogram", "Scatter Plot", "Box Plot"])

    if chart_type == "Histogram":
        plt.figure(figsize=(5,5))
        sns.histplot(column1, kde=True)
        st.pyplot(plt)

    elif chart_type == "Scatter Plot":
        plt.figure(figsize=(5,5))
        sns.scatterplot(data=df, x = column1, y = column2)
        st.pyplot(plt)

    elif chart_type == "Box Plot":
        plt.figure(figsize=(5,5))
        sns.boxplot(data = df, x=column1, y=column2)
        st.pyplot(plt)

    st.divider()
    st.header("Data Filtering")
    filtered_column = st.selectbox("Filter by column",df.columns)
    filter_value = st.text_input(f"Show rows where {filtered_column} contains")
    filter_value = filter_value.capitalize()

    if filter_value:
        filtered_data = df[df[filtered_column].astype(str).str.contains(filter_value)]
        st.write(filtered_data)

    st.divider()    

    #Data Transformation
    if st.checkbox("Drop Missing Values"):
        df.dropna()
    elif st.checkbox("Fill Missing Values"):
        fill_values = st.number_input("Value to fill missing data", value = 0)   
        df.fillna(fill_values)

    st.write("Transformed data", df.head())    

    st.divider()
    #Correlation Analysis
    st.header("Correlation Anaalysis")
    corr_matrix = df.corr() 

    sns.heatmap(corr_matrix, cmp="coolwarm", annot=True, fmt=".2f")
    st.pyplot(plt)


