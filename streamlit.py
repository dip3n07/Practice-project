import streamlit as st

st.title('Hi amazing people')
st.header('Hello I am header')
st.subheader('And i am subheader')

st.text('This is the text')
st.markdown('#First header')
st.markdown('##Second header')
st.markdown('**This is a bold text**, *This is italic text*, and `this is a code`')

st.success('Congrulation! You have succesfully completed')
st.error('You have a error')
st.info('this is the information')
st.warning('Warining')

is_checked = st.checkbox('I agree to the term and conditioin')
if is_checked:
	st.write('You have agred to term and condition')
else:
	st.write('You havent agree the term and condition')

st.radio('Select your Gender',['Male','Female','Other'])

choosen_country = st.selectbox('Select your country',['Nepal', 'Usa','China','Russia'])
if choosen_country =='Nepal':
	st.write('You are from Nepal')
elif choosen_country =='Usa':
	st.write('You are from Usa')
elif choosen_country == 'China':
	st.write('You are from china')
elif choosen_country == 'Russia':
	st.write('You are from russia')

liked_game =st.multiselect('Select your games',['Cricket','Football','Volleyball'])
st.text('You have selected:'+','.join(liked_game))


def classify_iris(sepal_length,sepal_width,petal_length,petal_width):
	#logic to classify iris specifies based on input fratures
	return'serosa'#example output
sepal_length = st.number_input('enter length of sepal')
sepal_width = st.number_input('enter width of sepal')
petal_length = st.number_input('enter length of petal')
petal_width = st.number_input('enter width of petal')

btn = st.button('predict')

if btn:
	prediction = classify_iris(sepal_length,sepal_width,petal_length,petal_width)

	st.write('The prediction iris species is:',prediction)

from PIL import Image
img = Image.open('E:\IMG_2650.jpeg')
st.image(img,width=300)

	