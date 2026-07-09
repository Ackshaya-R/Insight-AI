import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* Hide Streamlit */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}


/* App Background */

.stApp{

background:
linear-gradient(
135deg,
#eef2ff 0%,
#dbeafe 50%,
#f8fafc 100%
);

}


/* Sidebar */

section[data-testid="stSidebar"]{

background:rgba(15,23,42,.95);

backdrop-filter:blur(18px);

border-right:1px solid rgba(255,255,255,.1);

}


/* Sidebar Text */

section[data-testid="stSidebar"] *{

color:white;

}


/* Buttons */

.stButton>button{

background:linear-gradient(
90deg,
#2563EB,
#7C3AED
);

color:white;

border:none;

border-radius:14px;

height:52px;

font-size:16px;

font-weight:700;

width:100%;

transition:.3s;

}

.stButton>button:hover{

transform:translateY(-2px);

box-shadow:0 10px 25px rgba(37,99,235,.35);

}


/* Metric Cards */

div[data-testid="stMetric"]{

background:rgba(255,255,255,.55);

backdrop-filter:blur(18px);

padding:18px;

border-radius:18px;

border:1px solid rgba(255,255,255,.25);

box-shadow:0 8px 20px rgba(0,0,0,.08);

}


/* Chat Messages */

.stChatMessage{

background:rgba(255,255,255,.45);

backdrop-filter:blur(20px);

border-radius:18px;

padding:18px;

margin-bottom:15px;

box-shadow:0 8px 20px rgba(0,0,0,.05);

}


/* File Uploader */

[data-testid="stFileUploader"]{

background:rgba(255,255,255,.55);

backdrop-filter:blur(20px);

padding:20px;

border-radius:18px;

border:1px solid rgba(255,255,255,.2);

}


/* Text Inputs */

.stTextInput input{

border-radius:15px;

background:white;

}


/* Chat Input */

[data-testid="stChatInput"]{

background:white;

border-radius:16px;

box-shadow:0 8px 18px rgba(0,0,0,.08);

}


/* Selectbox */

.stSelectbox{

background:white;

border-radius:15px;

}


/* Expander */

.streamlit-expanderHeader{

font-weight:bold;

}


/* Scrollbar */

::-webkit-scrollbar{

width:8px;

}

::-webkit-scrollbar-thumb{

background:#94A3B8;

border-radius:10px;

}


/* Titles */

h1{

font-size:42px;

font-weight:800;

}

h2{

font-size:34px;

font-weight:700;

}

h3{

font-size:26px;

font-weight:700;

}


/* Success */

div[data-baseweb="notification"]{

border-radius:15px;

}


/* Hover Animation */

div[data-testid="stMetric"]:hover{

transform:translateY(-3px);

transition:.3s;

}


/* Smooth Animation */

*{

transition:.25s;

}

</style>
""",
        unsafe_allow_html=True,
    )