import streamlit as st
import plotly.express as px
import time

before_str = "<h3><b>Before Balancing</b></h3>"
after_str = "<h3><b>After Balancing</b></h3>"

def show_dataset_preview(df):
    with st.spinner("🔍 Generating dataset preview..."):
        time.sleep(1)
        st.subheader("📋 Dataset Preview:")
        st.dataframe(df.head())

def show_distribution(df, target_column):
        with st.spinner("📊 Generating value counts..."):
            time.sleep(1)
            st.subheader("📈 Target Variable Distribution")
            st.write(df[target_column].value_counts())

def show_pie_chart(df, target_column):
    df_pie = df[target_column].value_counts().reset_index()
    df_pie.columns = [target_column, 'count']
    
    df_pie['percentage'] = (df_pie['count'] / df_pie['count'].sum()) * 100
    df_pie['info'] = df_pie.apply(lambda row: 
                                  f"Target Variable: {row[target_column]} \
                                    <br>Count: {row['count']} \
                                    <br>Percentage: {row['percentage']:.2f}%", 
                                    axis=1)

    fig = px.pie(df_pie, 
                 names=target_column, 
                 values='count', 
                 hover_data={'info': True}, 
                 custom_data=['info'])
    fig.update_traces(hovertemplate='%{customdata[0]}')
    st.plotly_chart(fig)

def show_bar_chart(df, target_column):
    df_bar = df[target_column].value_counts().reset_index()
    df_bar.columns = ['Class', 'Count']
    df_bar['Percentage'] = (df_bar['Count'] / df_bar['Count'].sum()) * 100
    fig = px.bar(df_bar, 
                 x='Class', 
                 y='Count', 
                 text=df_bar['Percentage'].apply(lambda x:f'{x:.2f}%'), 
                 color='Class', 
                 color_discrete_sequence=px.colors.qualitative.Set1)
    fig.update_traces(textposition='outside')
    st.plotly_chart(fig)

def show_charts(df, df_balanced, target_column):
    st.subheader("📊 Class Distribution Before and After Balancing")

    chart_type = st.radio("Select chart type:", ["Pie Chart", "Bar Chart"], horizontal=True)
    сhart_before, chart_after = st.columns(2)

    if chart_type == "Pie Chart":
        with сhart_before:
            st.markdown(before_str, unsafe_allow_html=True)
            show_pie_chart(df, target_column)
        with chart_after:
            st.markdown(after_str, unsafe_allow_html=True)
            show_pie_chart(df_balanced, target_column)
    else:
        with сhart_before:
            st.markdown(before_str, unsafe_allow_html=True)
            show_bar_chart(df, target_column)
        with chart_after:
            st.markdown(after_str, unsafe_allow_html=True)
            show_bar_chart(df_balanced, target_column)

def show_summary(df, df_balanced, target_column):
    st.subheader("📊 Summary Description")
    # Layout with centered columns for data summary
    summary_before, summary_after = st.columns([1, 1])
    with summary_before:
        st.markdown(before_str, unsafe_allow_html=True)
        st.write(df.describe())
    with summary_after:
        st.markdown(after_str, unsafe_allow_html=True)
        st.write(df_balanced.describe())

def show_download_button(df):
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div>", unsafe_allow_html=True)
    st.write("### ⬇ Download Processed Dataset")
    st.markdown(
                '<a href="data:file/csv;base64,' + df.to_csv(index=False) + '" download="balanced_data.csv">'
                '<button>Download Balanced CSV</button>'
                '</a>',
                unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)