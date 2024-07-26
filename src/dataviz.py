import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("Final.csv")
    return df

def main():
    st.title("Impact of Factors on Home Price Index")

    df = load_data()

    # data preview
    st.subheader("Data Preview")
    st.write(df.head())

    # Time Series Plot of Home Price Index
    st.subheader("Time Series Plot of Home Price Index")
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        fig = px.line(df, x='date', y='Home Price Index', title='Home Price Index Over Time')
        st.plotly_chart(fig)

    # Sidebar for feature selection
    st.sidebar.header("Visualizations")
    feature = st.sidebar.selectbox("Select Feature", df.columns.difference(['Home Price Index']))

    # Time Series Plot of Selected Feature
    st.subheader(f"Time Series Plot of {feature}")
    if 'date' in df.columns:
        fig = px.line(df, x='date', y=feature, title=f'{feature} Over Time')
        st.plotly_chart(fig)

    # Scatter Plot of Feature vs Home Price Index
    st.subheader(f"Scatter Plot of {feature} vs Home Price Index")
    fig = px.scatter(df, x=feature, y='Home Price Index', title=f'{feature} vs Home Price Index')
    st.plotly_chart(fig)

    # Correlation Heatmap
    st.subheader("Correlation Heatmap")
    corr_matrix = df.corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

if __name__ == "__main__":
    main()