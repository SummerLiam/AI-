import streamlit as st
from generator import create_character

st.title("🎮 AI像素角色生成器")

st.info("""
支持的关键词：

发色：金发、棕发、白发、黑发\n
眼睛：蓝眼、绿眼、棕眼\n
性别：男、女\n
衣服：红衣、蓝衣、绿衣、黑衣\n
""")

description = st.text_input(
    "请输入角色描述",
    "金发蓝眼女红衣"
)


if st.button("生成角色"):

    hair = (20,20,20)
    eyes = (0,100,255)
    clothes = (220,0,0)
    gender = "male"

    if "女" in description:
        gender = "female"

    if "金发" in description:
        hair = (255,215,0)

    elif "棕发" in description:
        hair = (139,69,19)

    elif "白发" in description:
        hair = (220,220,220)

    if "绿眼" in description:
        eyes = (0,255,0)

    elif "棕眼" in description:
        eyes = (120,70,20)

    if "蓝衣" in description:
        clothes = (0,0,255)

    elif "绿衣" in description:
        clothes = (0,180,0)

    elif "黑衣" in description:
        clothes = (30,30,30)

    img = create_character(
        hair,
        eyes,
        clothes,
        gender
    )

    st.image(img, width=256)
