import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('data/concated_amazon_mod.csv')

data = load_data()

# Sidebar
st.sidebar.title("Visualization Options")
visualization = st.sidebar.selectbox("Choose a Visualization", ["Monthly Sales", "Product Sales", "Sales Distribution", 
                                                               "Top Selling Products", "Time of Day Analysis", 
                                                               "Products Frequently Bought Together"])

# Display based on sidebar choice
if visualization == "Monthly Sales":
    st.title("Monthly Sales")
    monthly_sales = data.groupby('Month')['Sales'].sum()
    st.line_chart(monthly_sales)

elif visualization == "Product Sales":
    st.title("Product Sales")
    product_sales = data.groupby('Product')['Sales'].sum().sort_values(ascending=False)
    st.bar_chart(product_sales)

elif visualization == "Sales Distribution":
    st.title("Distribution of Sales Values")
    bin_count = st.slider("Select number of bins", 3, 10, 3)
    hist_data = pd.cut(data['Sales'], bins=bin_count).value_counts().sort_index()
    hist_data.index = hist_data.index.astype(str)
    st.bar_chart(hist_data)


elif visualization == "Top Selling Products":
    st.title("Top Selling Products")
    top_products = data.groupby('Product')['Quantity Ordered'].sum().sort_values(ascending=False)
    st.bar_chart(top_products)

elif visualization == "Time of Day Analysis":
    st.title("Time of Day Analysis")
    hourly_sales = data.groupby('Hour')['Sales'].sum()
    st.bar_chart(hourly_sales)

elif visualization == "Products Frequently Bought Together":
    st.title("Products Frequently Bought Together")
    product_pairs = data.groupby('Product_Pair').size().reset_index(name='Count').sort_values(by='Count', ascending=False)
    st.write(product_pairs.head(10))
