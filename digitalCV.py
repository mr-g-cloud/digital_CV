# --- IMPORTS ---
from pathlib import Path
import streamlit as st
from PIL import Image
from datetime import date

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "GZ_CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic2.png"
linkedIn_icon = current_dir / "assets" / "linkedin_icon.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Gurdon Zoltán"
PAGE_ICON = Image.open(current_dir / "assets" / "favicon.ico")
DESCRIPTION = """Szoftvertesztelő/Tesztelés vezető"""
SUMMARY = """
Határidő orientált tesztelő vagyok közel 6 éves tapasztalattal, többnyire manuális tesztelés területén, 
viszont minimálisan foglalkoztam automatizálással is.\nKülönösen szeretem a technikai jellegű feladatokat.\n
Agilis és nem agilis projekten is részt vettem.\n
Könnyen teremtek kapcsolatot az emberekkel, jól kijövök a fejlesztő és manager kollégákkal is. Higgadt és türelmes 
embernek tartom magam, szeretem az "egyenes beszédet".\n
"""

# --- Contact info ----
NAME = "Gurdon Zoltán"
EMAIL = "zoltan.gurdon@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/zolt%C3%A1n-gurdon-a504a9103/"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title("Digitális önéletrajz")

# --- LOAD ASSETS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
linkedIn_icon = Image.open(linkedIn_icon)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)

    col3, mid, col4 = st.columns([1, 1, 20])

    with col3:
        st.image(linkedIn_icon, width=20)
    with col4:
        for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            col4.write(f"[{platform}]({link})")

    st.write("✉", EMAIL)
    st.write("További elérhetőségeimet a letölthető önéletrajzomban találja.")

# --- ITERATED SOCIAL LINKS ---
# st.write("#")
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#    cols[index].write(f"[{platform}]({link})")

# Download CV
st.write("#")
st.download_button(
    label="📄 Önéletrajz letöltése",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream",
)

# --- SUMMARY ---
with st.expander("Magamról", True):
    st.write(SUMMARY)

# --- EXPERIENCE & QUALIFICATIONS ---


# --- SKILLS ----
st.write("#")
with st.expander("Tapasztalatok", True):
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        st.write(
            """
        - ► Manuális szoftvertesztelés: Tesztek írása, karbantartása, verifikációk/validációk tervezése/végrehajtása
        - ► Adatbázis ismeretek: Oracle SQL
        - ► Programozási ismeretek: C, VBA, Python, C#, JAVA, Matlab
        - ► MS Office ismeret: Excel, World, PowerPoint
        """
        )
    with col2:
        st.write(
            """
        - ►️ Jó Csapatjátékos
        - ► A projekt és üzleti igények/elvárások szem előtt tartása
        - ►️ Kritikus gondolkodás
        - ►️ Oktatásban több éves tapsztalat
        - ►️ Hatékony munkavégzés
        - ►️ Agilis projekt tapasztalat
        - ►️ Demók tartása az ügyfelek számára
        """
        )
    with col3:
        st.write(
            """
        - ► Jegykezelő eszköz: Jira
        - ► Tesztmenedzsment eszközök: Jira Xray, TestRail (Cloud verzió)
        - ► Verziókezelő eszköz: SVN 
        - ► Programozási eszközök: PyCharm, Visual Studio, NetBeans
        - ► API: Postman
        """
        )

# --- WORK HISTORY ---
st.write("#")
with st.expander("Szakmai tapasztalatok", True):
    st.write("---")

    # --- JOB 1
    st.write("**Szoftvertesztelő/Tesztvezető | Szintézis-Net KFT.**")
    st.write("2022.01 - Jelenleg is")
    st.write("""
        - Web alapú pénzügyi alkalmazás front-end és back-end funkcióinak manuálus tesztelése, 
        tesztelés támogatása, tesztelés nyomonkövetése, dokumentálása, felülvizsgálatok elvégzése. 
        A projekt célja komplex Excel táblázatok kiváltása, mellyel a kockázatkezelési osztály napi munkáját segítjük.\n 
        - Tesztelési feladataim közé tartozik az adattárházból való adatok betöltésének, ütemezett feladatok megfelelő 
        lefutásának és a társrendszerek felé küldött üzenetek ellenőrzése, SQL scriptek írása, mock teszt adatok 
        előállításához script írása.\n
    """)
    # --- JOB 2
    st.write("#")
    st.write("---")
    st.write("**Szoftvertesztelő/Projekt koordinátor | Szintézis-Net KFT.**")
    st.write("2019.06 - 2021.12")
    st.write("""
        - Többnyire desktop alapú, francia kórházi alkalmazások (5 fő és 4 mellék alkalmazás) manuális és automatizált 
        tesztelése.\n 
        - Mint szoftvertesztelő a napi munkám közé tartozott az üzleti követelmények megértése, azokból 
        integrációs, regressziós valamint verifikációs és validációs tesztek írása, futtatása, manuális tesztek átírása
        automatikus python scriptekké. VBA scriptek írása mellyel a Traceability matrix-hoz fűződő feladatokat 
        automatizáltam mellyel heti több órát spóroltam meg mint az itthoni, mint a kinti csapatnak.
         A V&V-t megelőző és közben történő fáziskban aktív részvétel mind tervezési mind futtatási fázisban.\n
        - Projekt koordinátorként feladataim az ügyféllel való folyamatos kapcsolattartás, a magyar csapat (5 fő) 
        munkájának felügyelete, támogatása, problémák kezelése, reportok készítése. 
    """)
    # --- JOB 3
    st.write("#")
    st.write("---")
    st.write("**Szoftverfejlesztő | Szintézis-Net KFT.**")
    st.write("2017.06 - 2019.06")
    st.write("""
        - Többnyire desktop alapú, francia kórházi alkalmazásokhoz (5 fő és 4 mellék alkalmazás) tartozó funkciók
        fejlesztése. Üzleti követelmények alapján a hozzájuk tartozó analízisek készítése, felülvizsgálata, adatbázisok 
        szükség esetén történő módosítása, alkalmazásban lévő nyelvi fordítások kivitelezése.
    """)

    # --- JOB 4
    st.write("#")
    st.write("---")
    st.write("**Informatika és programozás óradó tanár | Bolyai János Technikum Mosonmagyaróvár.**")
    st.write("2016.02 - 2017.06")
    st.write("""
            - Szakközép iskolás diákoknak az informatika alapjait valamint a programozás alapjait tanítottam.
        """)

    # --- JOB 5
    st.write("#")
    st.write("---")
    st.write("**Smr Automotive Mirror Technology Hungary Bt.**")
    st.write("2014.06 – 2014.12")
    st.write("""
                - VBA makrók tervezése és írása a beszerzési osztály zárolt raktárban történő alkatrész mozgások
                nyomonkövetésére.
            """)

# --- Certificates ---
st.write("#")
with st.expander("Megszerzett tanúsítványok", True):
    st.write("---")

    # --- Certificate 1
    st.write("🏆 2020: ISTQB - CTFL - [link](http://scr.istqb.org/?name=&number=H20111315%2FCTFL&orderBy=relevancy"
             "&orderDirection=&dateStart=&dateEnd=&expiryStart=&expiryEnd=&certificationBody=&examProvider"
             "=&certificationLevel=&country=)")
    # --- Certificate 2
    st.write("🏆 2014: SAP ABAP Webdynpro fejlesztői tanúsítvány (MTC-S)")
    st.write("🏆 2014: SAP ABAP fejlesztői tanúsítvány (MTC-S)")

# --- Educations ---
st.write("#")
with st.expander("Tanulmányok", True):
    st.write("---")

    # --- School 1
    st.write("2009 - 2016: Széchényi István Egyetem Mérnök Informatika szak, BSC")
    # --- School 2
    st.write("2006 - 2000: Reguly Antal Szakképző Iskola Zirc Felnőtt képzés (nappali) – Érettségi bizonyítvány")
    st.write("2002 - 2006: Reguly Antal Szakképző Iskola Zirc Élelmiszer- és vegyiáru kereskedő – "
             "Szakmunkás-bizonyítvány")

# Languages
st.write("#")
with st.expander("Nyelvtudás", True):
    st.write("---")
    st.write("Angol: Társalgási szint")

# --- Hobbies ---
st.write("#")
with st.expander("Hobbi", True):
    st.write("---")
    st.write("🍖 Autentikus BBQ sütés")
    st.write("🎸 Gitározás")
    st.write("🎾 Teniszezés")

# gilub link -> https://github.com/mr-g-cloud/digital_CV.git

# --- Last modified date time ---
st.write("#")
today = date.today()
st.write("Utolsó módosítás: ", today)
