import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load your dataset
@st.cache_data
def load_data():
    # Load data from final.csv
    df = pd.read_csv("final.csv")
    return df

# Streamlit app
def main():
    st.title("Feature Visualizations")

    # Load dataset
    df = load_data()

    # Show data preview
    st.subheader("Data Preview")
    st.write(df.head())

    # Display data types
    st.subheader("Data Types")
    st.write(df.dtypes)

    # Filter out non-numeric columns for correlation heatmap
    numeric_df = df.select_dtypes(include=['number'])
    
    st.sidebar.header("Visualizations")

    # Choose feature to visualize
    feature = st.sidebar.selectbox("Select Feature", df.columns)

    # Display selected feature's histogram
    st.subheader(f"Histogram of {feature}")
    fig, ax = plt.subplots()
    sns.histplot(df[feature], kde=True, ax=ax)
    st.pyplot(fig)

    # Display selected feature's box plot
    st.subheader(f"Box Plot of {feature}")
    fig, ax = plt.subplots()
    sns.boxplot(x=df[feature], ax=ax)
    st.pyplot(fig)

    # Display selected feature's scatter plot against Home Price Index
    st.subheader(f"Scatter Plot of {feature} vs Home Price Index")
    if 'Home Price Index' in df.columns:
        fig = px.scatter(df, x=feature, y='Home Price Index', title=f'{feature} vs Home Price Index')
        st.plotly_chart(fig)
    else:
        st.write("Home Price Index column not found in the dataset.")

    # Display correlation heatmap if numeric columns are present
    if not numeric_df.empty:
        st.subheader("Correlation Heatmap")
        fig, ax = plt.subplots()
        corr_matrix = numeric_df.corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
    else:
        st.write("No numeric columns available for correlation analysis.")

if __name__ == "__main__":
    main()
