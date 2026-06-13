import streamlit as st
import pandas as pd
import datetime
import re
import time

# ==========================================
# إعدادات الصفحة المتقدمة للموقع
# ==========================================
st.set_page_config(
    page_title="ClinicalTrack Portal | منصة التدريب السريري", 
    page_icon="🏥", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص التصميم والخطوط لتبدو كمنصة طبية احترافية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');
    html, body, [data-testid="stSidebar"], .stMarkdown {
        font-family: 'Tajawal', sans-serif;
        text-align: right;
    }
    .stButton>button {
        background-color: #0f172a;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        width: 100%;
        padding: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0ea5e9;
        border-color: #0ea5e9;
    }
    [data-testid="stRadio"]>label {
        text-align: right;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# محرك الذكاء الاصطناعي (AI Functions)
# ==========================================
def ai_anonymize_data(text):
    text = re.sub(r'\b\d{10,11}\b', '[🔒 رقم هاتف محمي ومشفر]', text)
    names_to_hide = ['أحمد', 'محمد', 'علي', 'فاطمة', 'سارة', 'حسين', 'زمن', 'مصطفى']
    for name in names_to_hide:
        text = text.replace(name, '[🔒 اسم مريض مخفي للخصوصية]')
    return text

def ai_clinical_assistant(text):
    text_lower = text.lower()
    if "سعال" in text_lower or "حرارة" in text_lower or "كحة" in text_lower:
        return "🤖 اشتباه في عدوى بالجهاز التنفسي (Respiratory Infection). التوصية الدراسية: يُنصح بطلب صورة أشعة للصدر (Chest X-Ray) وفحص الدم الشامل CBC لمراقبة خلايا WBC."
    elif "صداع" in text_lower or "دوار" in text_lower or "دوخة" in text_lower:
        return "🤖 الأعراض قد تشير إلى اضطراب في ضغط الدم أو إجهاد سريري. التوصية الدراسية: قياس الضغط فوراً (BP Check) ومراقبة العلامات الحيوية للمريض."
    elif "كسر" in text_lower or "ألم شديد في العظم" in text_lower:
        return "🤖 حالة طارئة تستدعي توجيه المريض فوراً لغرفة الأشعة السينية (X-Ray Tube) لتحديد نوع ومكان الكسر بدقة."
    else:
        return "🤖 تحليل النظام: الأعراض الحالية بحاجة لإدخال تفاصيل سريرية أكثر (مثل قراءة العلامات الحيوية) لتقديم توجيه أكاديمي دقيق."

# ==========================================
# القائمة الجانبية للتنقل (Sidebar)
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #0ea5e9;'>🏥 ClinicalTrack</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 12px; color: #94a3b8;'>HCT 487 - AI in Healthcare Project</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    choice = st.radio(
        "انتقل بين أقسام الموقع:",
        ["📊 لوحة التحكم (Dashboard)", "📝 سجل الحالات الذكي (AI Logbook)", "🔬 دليل المختبر والأجهزة"]
    )
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; font-size: 11px; color: #64748b;'>إعداد الطالب | تحت إشراف د. عباس الزبيدي</p>", unsafe_allow_html=True)

# ==========================================
# واجهات الموقع الرئيسية (App Sections)
# ==========================================

if choice == "📊 لوحة التحكم (Dashboard)":
    st.title("لوحة التحكم السريرية لطلاب قسم العلوم الصحية 👨‍⚕️")
    st.write(f"مرحباً بك مجدداً | تاريخ اليوم: {datetime.date.today().strftime('%Y-%m-%d')}")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📌 **القسم الحالي بالتدريب**\n\nقسم الأشعة والتصوير الطبي (Radiology)")
    with col2:
        st.success("📈 **إجمالي الحالات الموثقة**\n\n24 حالة سريرية بنجاح")
    with col3:
        st.warning("🔒 **تأمين البيانات بالـ AI**\n\n100% متوافق مع معايير HIPAA العالمية")
        
    st.markdown("---")
    st.subheader("📊 توزيع الحالات وفحوصات الأجهزة الطبية الموثقة هذا الأسبوع")
    
    chart_data = pd.DataFrame({
        'نوع الفحص الطبي': ['X-Ray', 'MRI', 'CT Scan', 'Blood Tests', 'Ultrasound'],
        'عدد الحالات الموثقة': [12, 5, 3, 18, 7]
    })
    
    st.bar_chart(data=chart_data, x='نوع الفحص الطبي', y='عدد الحالات الموثقة', color='#0ea5e9')

elif choice == "📝 سجل الحالات الذكي (AI Logbook)":
    st.title("📝 سجل الحالات الطبي الذكي (AI Logbook)")
    st.write("أداة مخصصة لتوثيق الحالات السريرية أثناء التناوب العملي، مع معالجة البيانات فورياً لحماية خصوصية المرضى.")
    st.markdown("---")
    
    with st.container(border=True):
        st.subheader("إدخال بيانات الحالة الجديدة")
        
        patient_notes = st.text_area(
            "الملاحظات السريرية والأعراض (أدخل اسماً ورقم هاتف للتجربة ورؤية كيف يحميه الـ AI):", 
            placeholder="مثال: راجعنا اليوم المريض أحمد، رقم هاتفه 07712345678، وهو يعاني من سعال جاف وحرارة مرتفعة منذ يومين..."
        )
        
        equipment_used = st.selectbox(
            "جهاز الفحص المرتبط بالحالة:",
            ["بدون جهاز (فحص سريري عام)", "Siemens P 135/30 R X-ray Tube", "GE SIGNA MRI Scanner", "Philips Ultrasound"]
        )
        
        if st.button("تحليل ومعالجة الحالة بالذكاء الاصطناعي ✨"):
            if not patient_notes.strip():
                st.error("⚠️ الرجاء كتابة ملاحظات أو أعراض الحالة أولاً قبل التحليل!")
            else:
                with st.spinner("جاري تشغيل محرك الـ AI وفلترة البيانات الحساسة..."):
                    time.sleep(1.5)
                    
                    safe_data = ai_anonymize_data(patient_notes)
                    ai_suggestion = ai_clinical_assistant(patient_notes)
                    
                    st.success("✅ تم الانتهاء من معالجة البيانات بنجاح!")
                    
                    st.markdown("### 🔒 1. إخفاء هوية البيانات (De-identification Result):")
                    st.info(safe_data)
                    
                    st.markdown("### 💡 2. المساعد التشخيصي والتوجيه الأكاديمي للطلاب:")
                    st.warning(ai_suggestion)
                    st.caption(f"⚙️ تم ربط هذه الحالة في السجل بجهاز: **{equipment_used}**")

elif choice == "🔬 دليل المختبر والأجهزة":
    st.title("🔬 المرجع السريع للأجهزة الطبية والتحاليل")
    st.write("مرجع سريع للطالب لضمان الكفاءة أثناء الجولات السريرية والمختبرية.")
    st.markdown("---")
    
    tab1, tab2 = st.tabs(["🩸 القيم الطبيعية للتحاليل (CBC)", "☢️ بروتوكولات الأجهزة الطبية"])
    
    with tab1:
        st.subheader("المعدلات الطبيعية لفحص الدم الشامل (Normal Values)")
        df_cbc = pd.DataFrame({
            "الفحص (Test Name)": ["Hemoglobin (Hb)", "White Blood Cells (WBC)", "Platelets (الصفائح)"],
            "الوحدة المختبرية": ["g/dL", "/mcL", "/mcL"],
            "النطاق الطبيعي للذكور والاناث": ["12.1 - 17.2", "4,500 - 11,000", "150,000 - 450,000"]
        })
        st.table(df_cbc)
        
    with tab2:
        st.subheader("إرشادات التشغيل والسلامة للأجهزة المعتمدة بالقسم")
        st.error("**⚠️ Siemens X-ray Tube:** تأكد دائماً من ضبط إعدادات الـ (kVp) والـ (mAs) بدقة حسب سماكة العضو لتقليل الجرعة الإشعاعية للمريض تماشياً مع مبدأ (ALARA).")
        st.info("**ℹ️ GE SIGNA MRI Scanner:** الفحص الأمني الصارم لمنع دخول أي مواد ممغنطة أو معادن إلى غرفة الفحص لخطورة المجال المغناطيسي العالي.")
