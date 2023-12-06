import streamlit as st
import pandas as pd

data = {
    'Model': ['Redmi Note 6 Pro', 'Redmi 4K Ultra HD Android Smart LED TV X65', 'Redmi 20000Mah Li-Polymer Power Bank', 'Redmi 5A', 'Redmi 12C', 'Redmi Note 4', 'Redmi Note 11S', 'Redmi Watch 2 Lite', 'Redmi 9A Sport', 'Redmi 4K Ultra HD Android Smart LED TV X55', 'Redmi 9I Sport', 'Redmi Note 11', 'Redmi 9 Prime', 'Redmi Note 12 5G', 'Redmi Note 12 Pro 5G', 'Redmi Note 12', 'Redmi Note 12 Pro Plus 5G', 'Redmi 12C', 'Redmi Note 12 4G'],
    'Price': [14799, 59999, 1899, 6999, 9299, 9999, 16499, 1790, 6599, 28124.22, 7990, 11499, 11970, 15499, 19245, 15499, 27345, 6799, 10799],
    'Category': ['Mobile', 'TV', 'Power Bank', 'Mobile', 'Mobile', 'Mobile', 'Mobile', 'Watch', 'Mobile', 'TV', 'Mobile', 'Mobile', 'Mobile', 'Mobile', 'Mobile', 'Mobile', 'Mobile', 'Mobile', 'Mobile'],
    'Storage': ['64GB', 'N/A', '20000mAh', '16GB', '64GB', '64GB', '64GB', 'N/A', '32GB', 'N/A', '32GB', '64GB', '64GB', '64GB', '128GB', '64GB', '128GB', '64GB', '64GB'],  # Add your storage data here
    'Camera': ['20MP', 'N/A', 'N/A', '13MP', '13MP', '13MP', '48MP', 'N/A', '13MP', 'N/A', '13MP', '48MP', '13MP', '48MP', '108MP', '48MP', '108MP', '13MP', '48MP']  # Add your camera data here
}

redmi_data = pd.DataFrame(data)

redmi_data.index = range(1, len(redmi_data) + 1)

def main():
    st.title("MI Redmi Models Explorer")

    st.subheader("MI Redmi Models Data")
    st.write(redmi_data)

    st.sidebar.header("Filter Models")

    # Allow null options for filtering
    price_options = ["Select Price"] + list(redmi_data['Price'].unique())
    selected_price = st.sidebar.selectbox("Select Price", price_options)

    category_options = ["Select Category"] + list(redmi_data['Category'].unique())
    selected_category = st.sidebar.selectbox("Select Category", category_options)

    # Apply filters based on user selection
    if selected_price != "Select Price":
        filtered_data = redmi_data[redmi_data['Price'] == selected_price]
    else:
        filtered_data = redmi_data

    if selected_category != "Select Category":
        filtered_data = filtered_data[filtered_data['Category'] == selected_category]

    filtered_data.index = range(1, len(filtered_data) + 1)

    st.subheader("Filtered Models Data")
    st.write(filtered_data)

    # Plotting the graph
    st.subheader("Price Distribution of Models")
    st.bar_chart(filtered_data.set_index('Model')['Price'])

    # Pie chart for storage
    st.subheader("Storage Distribution of Models")
    storage_counts = filtered_data['Storage'].value_counts()
    st.pie_chart(storage_counts)

    # Pie chart for camera
    st.subheader("Camera Distribution of Models")
    camera_counts = filtered_data['Camera'].value_counts()
    st.pie_chart(camera_counts)

if __name__ == "__main__":
    main()
