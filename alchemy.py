import pandas as pd
import streamlit as st

st.title('Alchemy')
st.markdown("### Welcome to the Alchemy App")
st.markdown("<p style='font-size:20px;'>This app will streamline your alchemy skill building process in Skyrim</p>", unsafe_allow_html=True)
st.markdown("<blockquote style='font-size:18px;'>by <a href=''>Jonathan Ferrari</a></blockquote>", unsafe_allow_html=True)


@st.cache_data
def read_ingredients():
    return pd.read_csv('ingredient_guide.csv')
    
@st.cache_data
def read_effect():
    return pd.read_csv('effect_guide.csv')

effect_guide, ingredient_guide = read_effect(), read_ingredients()
ingredients = ingredient_guide['ingredient'].values


ingredient = st.selectbox('Select an ingredient', ingredients)
effects = ingredient_guide[ingredient_guide['ingredient'] == ingredient].iloc[:, 1:].values[0].tolist()

st.write(f'## Which effects of {ingredient} have you already uncovered?')

ef1_col, ef2_col, ef3_col, ef4_col = st.columns(4)
with ef1_col:
    ef1 = st.checkbox(effects[0])
with ef2_col:
    ef2 = st.checkbox(effects[1])
with ef3_col:
    ef3 = st.checkbox(effects[2])
with ef4_col:
    ef4 = st.checkbox(effects[3])
    
effect_boxes = [ef1, ef2, ef3, ef4]
if all(effect_boxes):
    print('## You have already uncovered all the effects of this ingredient!')
else:
    find = st.button('Find Ingredients')
    if find:
        for effect, name in zip(effect_boxes, effects):
            if not effect:
                st.write(f'## Here are the ingredients you can use to uncover the {name} effect of {ingredient}:')
                filtered = effect_guide[effect_guide["name"] == name]
                other_ingredients = filtered.drop(columns="name").iloc[:, :].dropna(axis=1).values[0].tolist()
                other_ingredients.remove(ingredient)
                for other in other_ingredients:
                    st.write(f"- {other}")
                