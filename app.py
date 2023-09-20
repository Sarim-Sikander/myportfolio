from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
icon = current_dir / "assets" / "favicon.ico"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sarim Sikander"
PAGE_ICON = ":wave:"
NAME = "Sarim Sikander"
DESCRIPTION = """
Data Scientist & Part-time Backend Developer, assisting enterprises by supporting data-driven decision-making and integrating them with websites.
"""
EMAIL = "sarimsikander24@gmail.com"
SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/cibean.7189",
    "LinkedIn": "https://linkedin.com/in/sarimsikandercs",
    "GitHub": "https://github.com/Sarim-Sikander",
    "Twitter": "https://twitter.com/SikSarim",
}
PROJECTS = {
    "🏆 Top Stories - Recommending stories based on user input": "https://github.com/Sarim-Sikander/Top-stories",
    "🏆 Quranic Hadees verifier - Verify quranic hadees based on Social media posts": "https://github.com/Sarim-Sikander/hadees",
    "🏆 Price Estimation - Using Vertex AI to estimate price": "https://github.com/Sarim-Sikander/GCP-Vertex-AI",
    "🏆 Social Media Application - Social media based on Islamic rules using Advanced Ml Algorithms": "https://github.com/Sarim-Sikander/FASTAPI",
    "🏆 Toxic Comments Classifier - Using advance transformers (Distil-BERT) to classify comments": "https://github.com/Sarim-Sikander/Toxic-comments-classification",
}

icon_pic = Image.open(icon)
st.set_page_config(page_title=PAGE_TITLE, page_icon=icon_pic)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

st.info('Open for new opportunities!', icon="📣", )

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
    
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 4 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python, SQL, Spark and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Have a Can-Do attitude with strong concepts of Machine learning
- ✔️ Always searching for more learning and growth oppotunities
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA, Java, Spark, DAX, Javascript, C++, Rust, Latex
- ⚡ Cloud Platforms: Amazon Web services, Google Cloud Platform
- 📊 Data Visulization: PowerBi, MS Excel, Plotly, Matplotlib, Seaborn, Tableau
- 🗄️ Frameworks: Flask, FastApi, Django, Express.js, Streamlit 
- 📚 Modeling: Logistic regression, linear regression, decition trees, Transformers, Random Forests, GPT, Timeseries models (ARIMA, SARIMA, SARIMX, GARCH), K-means, Ensemble trees
- 🗄️ Recommendation Systems: Collaborative, Content based, Hybrid
- 🗄️ Databases: Postgres, MongoDB, MySQL, Teradata
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Mentor | Kaggle**")
st.write("08/2023 - Present")
st.write(
    """
- ► Leading a team of mentees to get their projects done in given deadline
- ► Using advanced ML algorithms to perform appropriate tasks
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Scientist (Resourse Management) | Pakistan Telecommunication Limited**")
st.write("02/2023 - Present")
st.write(
    """
- ► Using business automation and integration tools to perform sheet automation to help better achieve KPI's
- ► Converting Excel sheets to get better understanding of Services and Sales KPI's and descreased MTTR to 22 hrs
- ► Creating monthly targets for overall PTCL workforce in all regions, sending inventories, automating processes, and help better achieve results by explaning to nontechnical stakeholders
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Forward Program | McKinsey & Companies**")
st.write("11/2022 - 02/2023")
st.write(
    """
- ► Develop innovative solutions for diverse clients' complex business challenges
- ► Accelerate professional growth through mentorship and training
- ► Contribute to impactful projects shaping industries worldwide
"""
)

st.write('\n')
st.write("🚧", "**Data Scientist | Turing**")
st.write("03/2022 - 09/2022")
st.write(
    """
- ► Mentoring ICs and other leads
- ► Building ETL pipelines, Creating dashboards with key business metrics and Creating metrics to drive business growth
- ► Troubleshooting business issues with data and Building data models to turn a mix of data from multiple sources into coherent entities
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
