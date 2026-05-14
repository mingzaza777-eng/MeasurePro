import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="MeasurePro")

# ================= STATE =================
if "page" not in st.session_state:
    st.session_state.page = "cover"

if "inputs" not in st.session_state:
    st.session_state.inputs = [""]

if "v_main" not in st.session_state:
    st.session_state.v_main = random.randint(1, 9)
    st.session_state.v_decimal = random.randint(0, 9)

if "m_main" not in st.session_state:
    st.session_state.m_main = random.randint(0, 9)
    st.session_state.m_thimble = random.randint(0, 49)


def go(page):
    st.session_state.page = page


page = st.session_state.page

# ================= COVER PAGE =================
if page == "cover":

    st.markdown(
        "<h1 style='text-align:center; font-size:60px;'>MeasurePro</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center; font-size:18px;'>Smart Measurement Learning App</p>",
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("เริ่มใช้งาน 🚀"):
        st.session_state.page = "menu"
        st.rerun()


# ================= MENU =================
if page == "menu":

    st.title("MeasurePro")

    st.button("เรียนรู้เครื่องมือ", on_click=go, args=("learn",))
    st.button("ฝึกเวอร์เนียร์", on_click=go, args=("vernier",))
    st.button("ฝึกไมโครมิเตอร์", on_click=go, args=("micro",))
    st.button("คำนวณค่าเฉลี่ย", on_click=go, args=("calc",))
    st.button("ออก", on_click=go, args=("exit",))


# ================= LEARN (DETAILED VERSION) =================
elif page == "learn":

    st.title("การใช้เครื่องมือวัด")

    # ================= VERNIER =================
    st.subheader("เวอร์เนียร์คาลิปเปอร์")
    st.image("verni.png")

    st.write("""
**การใช้งานเวอร์เนียร์คาลิปเปอร์**

เวอร์เนียร์คาลิปเปอร์ใช้สำหรับวัดขนาดชิ้นงานที่ต้องการความละเอียดระดับมิลลิเมตรถึงทศนิยม

🔹 การวัดภายนอก (Outside Measurement)  
- ใช้ปากวัดใหญ่หนีบชิ้นงานด้านนอก  
- ต้องให้ปากวัดตั้งฉากกับชิ้นงานเพื่อความแม่นยำ  
- เหมาะสำหรับวัดความกว้าง ความหนา เส้นผ่านศูนย์กลางภายนอก  

🔹 การวัดภายใน (Inside Measurement)  
- ใช้ปากวัดเล็กสอดเข้าไปในรู  
- กางออกให้สัมผัสผิวด้านในของชิ้นงาน  
- ใช้วัดเส้นผ่านศูนย์กลางรูหรือช่องว่าง  

🔹 การวัดความลึก (Depth Measurement)  
- ใช้ก้านวัดด้านท้ายของเครื่องมือ  
- วางฐานให้แนบกับผิวชิ้นงาน  
- ใช้วัดความลึกของรูหรือร่องต่าง ๆ
""")

    st.divider()

    # ================= MICROMETER =================
    st.subheader("ไมโครมิเตอร์")
    st.image("mic.jpg")

    st.write("""
**การใช้งานไมโครมิเตอร์**

ไมโครมิเตอร์ใช้สำหรับวัดชิ้นงานที่ต้องการความละเอียดสูงมาก (0.01 mm)

🔹 การวัดชิ้นงานทรงกลม / ทรงกระบอก  
- วางชิ้นงานระหว่างแกนวัด (Spindle) และแกนรับ (Anvil)  
- หมุนแกนจนสัมผัสชิ้นงานพอดี  

🔹 การใช้ Ratchet Stop  
- หมุนจนเริ่มใกล้ชิ้นงาน  
- ใช้ Ratchet หมุนจนเกิดเสียงคลิก 2–3 ครั้ง  
- เพื่อให้แรงกดคงที่ ลดความคลาดเคลื่อน  

🔹 หลักการอ่านค่า  
- สเกลหลัก (Sleeve) แสดงค่ามิลลิเมตร  
- สเกลปลอกหมุน (Thimble) แสดงค่า 0.01 mm  
- นำค่าทั้งสองมารวมกันเพื่อหาค่าที่ถูกต้อง
""")

    st.button("⬅ กลับเมนู", on_click=go, args=("menu",))


# ================= VERNIER (FIXED CHECK ANSWER) =================
elif page == "vernier":

    st.title("ฝึกอ่านค่าเวอร์เนียร์")

    main = st.session_state.v_main
    decimal = st.session_state.v_decimal

    correct = round(main + decimal * 0.1, 2)

    fig, ax = plt.subplots(figsize=(9, 3))

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)

    # ================= MAIN SCALE =================
    for i in range(11):
        x = i

        ax.plot([x, x], [0.45, 0.95], color="black", linewidth=2)
        ax.text(x, 0.1, str(i), ha="center")

        if i < 10:
            ax.plot([x + 0.5, x + 0.5], [0.6, 0.95], color="gray", linewidth=1.5)

            for j in range(1, 5):
                ax.plot([x + j * 0.2, x + j * 0.2],
                        [0.7, 0.95],
                        color="lightgray",
                        linewidth=1)

    # ================= VERNIER SCALE =================
    start = main

    for i in range(10):
        x = start + i * 0.1
        ax.plot([x, x], [0.0, 0.4], color="blue", linewidth=1.5)
        ax.text(x, 0.42, str(i), ha="center", fontsize=8, color="blue")

    # ================= POINTER =================
    pointer = main + decimal * 0.1
    ax.axvline(pointer, color="red", linewidth=2)

    ax.axis("off")
    st.pyplot(fig)

    user = st.text_input("ตอบเป็น mm")

    if st.button("ตรวจคำตอบ"):
        try:
            if abs(float(user) - correct) < 0.01:
                st.success("ถูกต้อง!")
            else:
                st.error(f"ผิด! คำตอบที่ถูกคือ {correct} mm")
        except:
            st.warning("กรอกตัวเลข")

    if st.button("ข้อถัดไป"):
        st.session_state.v_main = random.randint(1, 9)
        st.session_state.v_decimal = random.randint(0, 9)
        st.rerun()

    st.button("⬅ กลับเมนู", on_click=go, args=("menu",))


# ================= MICRO (CLEAN FINAL FIXED) =================
elif page == "micro":

    st.title("ฝึกอ่านค่าไมโครมิเตอร์")

    main = st.session_state.m_main
    thimble = st.session_state.m_thimble

    correct = round(main + thimble * 0.01, 2)

    fig, ax = plt.subplots(figsize=(9, 3))

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)

    # ================= SLEEVE =================
    ax.plot([1, 7], [2, 2], color="black", linewidth=3)

    for i in range(11):
        x = 1 + i * 0.6
        ax.plot([x, x], [1.7, 2.3], color="black", linewidth=2)
        ax.text(x, 1.2, str(i), ha="center")

    pointer_x = 1 + main * 0.6
    ax.plot([pointer_x, pointer_x], [1.5, 2.5], color="red", linewidth=3)

    ax.text(0.5, 2.6, "SLEEVE", fontsize=10)

    # ================= THIMBLE =================
    ax.text(8.5, 3, "THIMBLE", fontsize=10)

    start_y = 0.5

    for i in range(0, 50, 5):
        y = start_y + (i / 50) * 2.5
        ax.plot([8, 9], [y, y], color="blue", linewidth=2)
        ax.text(9.2, y, str(i), fontsize=8, va="center")

    thimble_y = start_y + (thimble / 50) * 2.5
    ax.plot([8, 9], [thimble_y, thimble_y], color="red", linewidth=3)

    ax.axis("off")
    st.pyplot(fig)

    user = st.text_input("ตอบเป็น mm")

    if st.button("ตรวจคำตอบ"):
        try:
            if abs(float(user) - correct) < 0.01:
                st.success("ถูกต้อง!")
            else:
                st.error("ผิด! ลองใหม่อีกครั้ง")
        except:
            st.warning("กรอกตัวเลข")

    if st.button("ข้อถัดไป"):
        st.session_state.m_main = random.randint(0, 9)
        st.session_state.m_thimble = random.randint(0, 49)
        st.rerun()

    st.button("⬅ กลับเมนู", on_click=go, args=("menu",))


# ================= CALC =================
elif page == "calc":

    st.title("คำนวณค่าเฉลี่ย")

    for i in range(len(st.session_state.inputs)):
        st.session_state.inputs[i] = st.text_input(
            f"ค่าที่ {i+1}",
            value=st.session_state.inputs[i]
        )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("เพิ่มช่อง"):
            st.session_state.inputs.append("")
            st.rerun()

    with col2:
        if st.button("รีเซ็ต"):
            st.session_state.inputs = [""]
            st.rerun()

    if st.button("คำนวณ"):
        try:
            vals = [float(x) for x in st.session_state.inputs if x != ""]

            if len(vals) > 0:
                avg = sum(vals) / len(vals)
                st.success(f"ค่าเฉลี่ย = {avg:.2f}")

                fig, ax = plt.subplots()
                ax.plot(vals, marker="o")
                st.pyplot(fig)

            else:
                st.warning("ยังไม่มีข้อมูล")

        except:
            st.error("กรอกตัวเลขไม่ถูกต้อง")

    st.button("⬅ กลับเมนู", on_click=go, args=("menu",))


# ================= EXIT =================
elif page == "exit":
    st.write("ปิดได้เลย 👍")