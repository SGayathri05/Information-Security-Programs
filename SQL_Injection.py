import streamlit as st
import hashlib
import sqlite3

conn = sqlite3.connect("nen.db")
c = conn.cursor()

def Hash(passwords):
    result1 = hashlib.md5(passwords.encode())
    return result1.hexdigest()

st.title("SQL Injection")

username = st.text_input("Enter your username: ")
password = st.text_input("Enter your password: ")
pass_en = Hash(password)

register = st.button("Register")
if register:
    c.execute("INSERT INTO stud (name, password) Values ('{}', '{}')".format(username,pass_en))

st.title("LOGIN")
username1 = st.text_input("Enter your username: ", key=1)
password1 = st.text_input("Enter your password: ", key=2)
pass_enc = Hash(password1)

login = st.button("Login")

if login:
    c.execute("SELECT * FROM sqli where username = '%s' and pass = '%s' and hack = '%s'"%(username1, password1, pass_enc))
    conn.commit()
    for i in c:
        st.write(i[0], i[1], i[2])
