import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_cafe_sales.csv', index_col=0)
    return df
df = load_data()
st.title("Cafe Owner Dashboard")
col1,col2,col3 = st.columns(3)

total_revenue = df['Total Spent'].sum()

col1.metric(
    label = ":green[Total Revenue Till date]",
    value = f"{total_revenue:.2f}",
    border=True
) 

total_transactions = df['Transaction ID'].count()

col2.metric(
    label = ":orange[Total Transactions Till Date]",
    value = f"{total_transactions:.2f}",
    border= True
)

total_quantity_sold = df['Quantity'].sum()

col3.metric(
    label = ":blue[Total Quantity Sold]",
    value = f"{total_quantity_sold:.2f}",
    border=True
)

col4,col5,col6 = st.columns(3)
with col4:
    st.markdown("### :violet[TOP 2 Best Selling Items]")
    
    # 1. Get the top 2 data points as a clean DataFrame table
    top_2_df = df.groupby('Item', as_index=False)['Quantity'].sum().nlargest(2, 'Quantity')
    # st.write(top_2_df)
    # 2. Display it cleanly as a mini table inside the column
    st.dataframe(top_2_df, hide_index=True, use_container_width=True)
st.subheader("cleaned data")
st.dataframe(df.head(5))
available_columns = df.columns
selected_filter = st.multiselect("select a filter: ", available_columns)

filtered_df = df[selected_filter]

st.write(f"Showing filtered data for :{selected_filter}")
st.write(filtered_df)