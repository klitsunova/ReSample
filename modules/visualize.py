import streamlit as st
import plotly.express as px

def generate_pie_chart(df, target_column):
    """Создает круговую диаграмму распределения целевой переменной"""
    value_counts = df[target_column].value_counts().reset_index()
    value_counts.columns = [target_column, 'count']
    value_counts['percentage'] = (value_counts['count'] / value_counts['count'].sum()) * 100
    return px.pie(value_counts, names=target_column, values='count', 
                  hover_data={'percentage': ':.2f%'})

def show_charts(df, target_column):
    st.header("📊 Визуализация данных")
    st.subheader("Распределение классов")
    
    fig = generate_pie_chart(df, target_column)
    st.plotly_chart(fig)