import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Dictionary containing UI translations in multiple languages
languages = {
    "en": {
        "title": "Face Recognition Attendance System Software",
        "help": "Help Desk",
        "email": "Email",
        "phone": "Phone Number",
        "exit_confirm": "Do you want to exit the project?",
        "yes": "Yes",
        "no": "No",
        "student_details": "Student Details",
        "face_detector": "Face Detector",
        "attendance": "Attendance",
        "language": "Language",
        "chatbox": "Chat Box",
        "train_data": "Train Data",
        "photos": "Photos",
        "developer": "Developer",
        "exit": "Exit",
        "developer": "Developer Info",
        "team_admin": "Team Admin",
        "team_member": "Team Member",
        "NAME : Aditya Roy": "NAME : Aditya Roy",
        "NAME : Samaresh Debnath": "NAME : Samaresh Debnath",
        "NAME : Subhasis Mahato": "NAME : Subhasis Mahato",
        "NAME : Deepanjan Seth": "NAME : Deepanjan Seth",
        "DEPT : Information Technology": "DEPT : Information Technology",
        "Year : 1st Year": "Year : 1st Year",
        "College : University Institute of Technology,BU": "College : University Institute of Technology, BU",
        "status": "Status",
        "home": "Home",
        "train_data_set": "Train Data Set",
        "train": "Train",
        "help_desk": "Help Desk",
        "Train Data": "Train Data",
        "face_recognition": "Face Recognition",
        "exit": "Exit",
        "select_department": "Select Department",  # New entry
        "cse": "CSE",
        "it": "IT",
        "me": "ME",
        "ce": "CE",
        "ece": "ECE",
        "ee": "EE",
        "course": "Course",
        "select_course": "Select Course",
        "b.e": "B.E",
        "b.tech": "B.Tech",
        "m.e": "M.E",
        "m.tech": "M.Tech",
        "year": "Year",
        "select_year": "Select Year",
        "1st_year": "1st Year",
        "2nd_year": "2nd Year",
        "3rd_year": "3rd Year",
        "4th_year": "4th Year",
        "semester": "Semester",
        "select_semester": "Select Semester",
        "1st_semester": "1st Semester",
        "2nd_semester": "2nd Semester",
        "3rd_semester": "3rd Semester",
        "4th_semester": "4th Semester",
        "student_information": "Student Information",
        "student_id": "Student ID",
        "student_name": "Student Name",
        "class_division": "Class Division",
        "select_class_division": "Select Class Division",
        "roll_no": "Roll No",
        "gender": "Gender",
        "select_gender": "Select Gender",
        "male": "Male",
        "female": "Female",
        "other": "Other",
        "date_of_birth": "Date of Birth",
        "email": "Email",
        "phone_no": "Phone No",
        "address": "Address",
        "teacher_name": "Teacher Name",
        "take_photo_sample": "Take Photo Sample",
        "no_photo_sample": "No Photo Sample",
        "save": "Save",
        "update": "Update",
        "delete": "Delete",
        "reset": "Reset",
        "take_photo": "Take Photo",
        "update_photo": "Update Photo",
        "search_student_information": "Search Student Information",
        "search_by": "Search By",
        "select": "Select",
        "search": "Search",
        "show_all": "Show All",
    },
    "hi": {
        "title": "चेहरे की पहचान उपस्थिति प्रणाली सॉफ़्टवेयर",
        "help": "सहायता डेस्क",
        "email": "ईमेल",
        "phone": "फ़ोन नंबर",
        "exit_confirm": "क्या आप परियोजना से बाहर निकलना चाहते हैं?",
        "yes": "हाँ",
        "no": "नहीं",
        "student_details": "छात्र विवरण",
        "face_detector": "चेहरा पहचानकर्ता",
        "attendance": "उपस्थिति",
        "language": "भाषा",
        "chatbox": "चैट बॉक्स",
        "train_data": "डेटा प्रशिक्षण",
        "photos": "फ़ोटो",
        "developer": "डेवलपर",
        "exit": "बाहर जाएं",
        "developer": "डेवलपर जानकारी",
        "team_admin": "टीम प्रशासन",
        "team_member": "टीम सदस्य",
        "NAME : Aditya Roy": "नाम : आदित्य रॉय",
        "NAME : Samaresh Debnath": "नाम : समरेश देबनाथ",
        "NAME : Subhasis Mahato": "नाम : सुबासिस महतो",
        "NAME : Deepanjan Seth": "नाम : दीपांजन सेठ",
        "DEPT : Information Technology": "विभाग : सूचना प्रौद्योगिकी",
        "Year : 1st Year": "वर्ष : प्रथम वर्ष",
        "College : University Institute of Technology,BU": "कॉलेज : यूनिवर्सिटी इंस्टीट्यूट ऑफ टेक्नोलॉजी, बीयू",
        "status": "स्थिति",
        "train_data_set": "ट्रेन डेटा सेट",
        "home": "होम",
        "train": "प्रशिक्षण",
        "department": "विभाग",
        "help_desk": "मदद डेस्क",
        "face_recognition": "चेहरे की पहचान",
        "exit": "बाहर जाएं", 
        "select_department": "विभाग चुनें",  # New entry
        "cse": "सीएसई",
        "it": "आईटी",
        "me": "एमई",
        "ce": "सीई",
        "ece": "ईसीई",
        "ee": "ईई",
        "course": "पाठ्यक्रम",
        "select_course": "पाठ्यक्रम चुनें",
        "b.e": "बी.ई",
        "b.tech": "बी.टेक",
        "m.e": "एम.ई",
        "m.tech": "एम.टेक",
        "year": "वर्ष",
        "select_year": "वर्ष चुनें",
        "1st_year": "प्रथम वर्ष",
        "2nd_year": "द्वितीय वर्ष",
        "3rd_year": "तृतीय वर्ष",
        "4th_year": "चतुर्थ वर्ष",
        "semester": "सेमेस्टर",
        "select_semester": "सेमेस्टर चुनें",
        "1st_semester": "प्रथम सेमेस्टर",
        "2nd_semester": "द्वितीय सेमेस्टर",
        "3rd_semester": "तृतीय सेमेस्टर",
        "4th_semester": "चतुर्थ सेमेस्टर",
        "student_information": "छात्र जानकारी",
        "student_id": "छात्र आईडी",
        "student_name": "छात्र का नाम",
        "class_division": "कक्षा विभाजन",
        "select_class_division": "कक्षा विभाजन चुनें",
        "roll_no": "रोल नंबर",
        "gender": "लिंग",
        "select_gender": "लिंग चुनें",
        "male": "पुरुष",
        "female": "महिला",
        "other": "अन्य",
        "date_of_birth": "जन्म तिथि",
        "email": "ईमेल",
        "phone_no": "फोन नंबर",
        "address": "पता",
        "teacher_name": "शिक्षक का नाम",
        "take_photo_sample": "फोटो सैंपल लें",
        "no_photo_sample": "कोई फोटो सैंपल नहीं",
        "save": "सहेजें",
        "update": "अपडेट करें",
        "delete": "हटाएं",
        "reset": "रीसेट करें",
        "take_photo": "फोटो लें",
        "update_photo": "फोटो अपडेट करें",
        "search_student_information": "छात्र जानकारी खोजें",
        "search_by": "के द्वारा खोजें",
        "select": "चुनें",
        "search": "खोजें",
        "show_all": "सभी दिखाएं",  
        "student_management_system": "छात्र प्रबंधन प्रणाली", 
    },
    "bn": {
        "title": "মুখ শনাক্তকরণ উপস্থিতি সিস্টেম সফটওয়্যার",
        "help": "সহায়তা ডেস্ক",
        "email": "ইমেল",
        "phone": "ফোন নম্বর",
        "exit_confirm": "আপনি কি প্রকল্পটি ছেড়ে যেতে চান?",
        "yes": "হ্যাঁ",
        "no": "না",
        "student_details": "শিক্ষার্থী বিবরণ",
        "face_detector": "মুখ শনাক্তকারী",
        "attendance": "উপস্থিতি",
        "language": "ভাষা",
        "chatbox": "চ্যাট বক্স",
        "train_data": "ডেটা প্রশিক্ষণ",
        "photos": "ছবি",
        "developer": "ডেভেলপার",
        "department": "বিভাগ",
        "exit": "প্রস্থান করুন",
        "developer": "ডেভেলপার তথ্য",
        "team_admin": "টিম প্রশাসক",
        "team_member": "টিম সদস্য",
        "NAME : Aditya Roy": "নাম : আদিত্য রায়",
        "DEPT : Information Technology": "বিভাগ : তথ্য প্রযুক্তি",
        "Year : 1st Year": "বছর : প্রথম বছর",
        "College : University Institute of Technology,BU": "কলেজ : ইউনিভার্সিটি ইনস্টিটিউট অফ টেকনোলজি, বিএইউ",
        "status": "স্ট্যাটাস",
        "home": "হোম",
        "course": "কোর্স",
        "student_management_system": "ছাত্র ব্যবস্থাপনা সিস্টেম",
        "NAME : Samaresh Debnath": "নাম : সমরেশ দেবনাথ",
        "NAME : Subhasis Mahato": "নাম : সুবাসিস মহাতো",
        "NAME : Deepanjan Seth": "নাম : দীপাঞ্জন সেথ",
        "train_data_set": "ট্রেন ডেটা সেট",
        "train": "প্রশিক্ষণ",
        "help_desk": "সাহায্য ডেস্ক",
        "Train Data": "ট্রেন ডেটা",
        "face_recognition": "মুখ চিনাক্তকরণ",
        "exit": "বাহির",
        "select_department": "বিভাগ নির্বাচন করুন",  # New entry
        "cse": "সিএসই",
        "it": "আইটি",
        "me": "এমই",
        "ce": "সিই",
        "ece": "ইসিই",
        "ee": "ইই",
        "course": "কোর্স",
        "select_course": "কোর্স নির্বাচন করুন",
        "b.e": "বি.ই",
        "b.tech": "বি.টেক",
        "m.e": "এম.ই",
        "m.tech": "এম.টেক",
        "year": "বছর",
        "select_year": "বছর নির্বাচন করুন",
        "1st_year": "১ম বর্ষ",
        "2nd_year": "২য় বর্ষ",
        "3rd_year": "৩য় বর্ষ",
        "4th_year": "৪র্থ বর্ষ",
        "semester": "সেমিস্টার",
        "select_semester": "সেমিস্টার নির্বাচন করুন",
        "1st_semester": "১ম সেমিস্টার",
        "2nd_semester": "২য় সেমিস্টার",
        "3rd_semester": "৩য় সেমিস্টার",
        "4th_semester": "৪র্থ সেমিস্টার",
        "student_information": "ছাত্র তথ্য",
        "student_id": "ছাত্র আইডি",
        "student_name": "ছাত্রের নাম",
        "class_division": "ক্লাস বিভাগ",
        "select_class_division": "ক্লাস বিভাগ নির্বাচন করুন",
        "roll_no": "রোল নম্বর",
        "gender": "লিঙ্গ",
        "select_gender": "লিঙ্গ নির্বাচন করুন",
        "male": "পুরুষ",
        "female": "মহিলা",
        "other": "অন্যান্য",
        "date_of_birth": "জন্ম তারিখ",
        "email": "ইমেইল",
        "phone_no": "ফোন নম্বর",
        "address": "ঠিকানা",
        "teacher_name": "শিক্ষকের নাম",
        "take_photo_sample": "ছবি নমুনা নিন",
        "no_photo_sample": "কোনও ছবি নমুনা নয়",
        "save": "সংরক্ষণ করুন",
        "update": "আপডেট করুন",
        "delete": "মুছে ফেলুন",
        "reset": "রিসেট করুন",
        "take_photo": "ছবি তুলুন",
        "update_photo": "ছবি আপডেট করুন",
        "search_student_information": "ছাত্র তথ্য অনুসন্ধান করুন",
        "search_by": "দ্বারা অনুসন্ধান করুন",
        "select": "নির্বাচন করুন",
        "search": "অনুসন্ধান করুন",
        "show_all": "সব দেখান",
    },
    "ta": {
        "title": "முகம் அடையாளம் காணும் வருகை பதிவு மென்பொருள்",
        "help": "உதவி மேசை",
        "email": "மின்னஞ்சல்",
        "phone": "தொலைபேசி எண்",
        "exit_confirm": "திட்டத்திலிருந்து வெளியேற விரும்புகிறீர்களா?",
        "yes": "ஆம்",
        "no": "இல்லை",
        "student_details": "மாணவர் விவரங்கள்",
        "face_detector": "முகம் கண்டறியும் கருவி",
        "attendance": "வருகை பதிவு",
        "language": "மொழி",
        "chatbox": "அரட்டை பெட்டி",
        "train_data": "தரவை பயிற்று",
        "photos": "புகைப்படங்கள்",
        "developer": "டெவலப்பர்",
        "exit": "வெளியேறு",
        "developer": "டெவலப்பர் தகவல்",
        "team_admin": "அணி நிர்வாகி",
        "team_member": "அணி உறுப்பினர்",
        "NAME : Aditya Roy": "பெயர் : ஆதி ராய்",
        "DEPT : Information Technology": "துறை : தகவல் தொழில்நுட்பம்",
        "Year : 1st Year": "ஆண்டு : முதல் ஆண்டு",
        "College : University Institute of Technology,BU": "கல்லூரி : யூனிவர்சிட்டி இன்ஸ்டிட்யூட் ஆஃப் டெக்னாலஜி, பி.யூ",
        "status": "நிலை",
        "home": "முகப்பு",
        "NAME : Samaresh Debnath": "பெயர் : சமரேஷ் தேவநாத்",
        "NAME : Subhasis Mahato": "பெயர் : சுபாஸிஸ் மகாத்தோ",
        "NAME : Deepanjan Seth": "பெயர் : தீபஞ்சன் சேத்",
        "train_data_set": "பயிற்சி தரவுத்தொகுப்பு",
        "train": "பயிற்சி",
        "help_desk": "உதவி மையம்",
        "Train Data": "பயிற்சி தரவு",
        "face_recognition": "முகம் அடையாளம் காணல்",
        "exit": "வெளியேறு",    
        "course": "பாடநெறி",
        "select_course": "பாடநெறியை தேர்ந்தெடுக்கவும்",
        "b.e": "பி.இ",
        "b.tech": "பி.டெக்",
        "m.e": "எம்.இ",
        "m.tech": "எம்.டெக்",
        "year": "ஆண்டு",
        "select_year": "ஆண்டைத் தேர்ந்தெடுக்கவும்",
        "1st_year": "முதல் ஆண்டு",
        "2nd_year": "இரண்டாம் ஆண்டு",
        "3rd_year": "மூன்றாம் ஆண்டு",
        "4th_year": "நான்காம் ஆண்டு",
        "semester": "செமஸ்டர்",
        "select_semester": "செமஸ்டரை தேர்ந்தெடுக்கவும்",
        "1st Semester": "முதல் செமஸ்டர்",
        "2nd Semester": "இரண்டாம் செமஸ்டர்",
        "3rd Semester": "மூன்றாம் செமஸ்டர்",
        "4th Semester": "நான்காம் செமஸ்டர்",
        "student_information": "மாணவர் தகவல்",
        "student_id": "மாணவர் ஐடி",
        "student_name": "மாணவர் பெயர்",
        "class_division": "வகுப்பு பிரிவு",
        "select_class_division": "பிரிவை தேர்ந்தெடுக்கவும்",
        "roll_no": "உருட்டு எண்",
        "gender": "பாலினம்",
        "select_gender": "பாலினத்தை தேர்ந்தெடுக்கவும்",
        "male": "ஆண்",
        "female": "பெண்",
        "other": "மற்றவை",
        "date_of_birth": "பிறந்த தேதி",
        "email": "மின்னஞ்சல்",
        "phone_no": "தொலைபேசி எண்",
        "address": "முகவரி",
        "teacher_name": "ஆசிரியர் பெயர்",
        "take_photo_sample": "புகைப்பட மாதிரி எடுக்கவும்",
        "no_photo_sample": "புகைப்பட மாதிரி இல்லை",
        "save": "சேமிக்கவும்",
        "update": "புதுப்பிக்கவும்",
        "delete": "நீக்கவும்",
        "reset": "மீட்டமைக்கவும்",
        "take_photo": "புகைப்படம் எடுக்கவும்",
        "update_photo": "புகைப்படத்தை புதுப்பிக்கவும்",
        "search_student_information": "மாணவர் தகவலை தேடுங்கள்",
        "search_by": "இதனால் தேடு",
        "select": "தேர்ந்தெடுக்கவும்",
        "search": "தேடுங்கள்",
        "show_all": "அனைத்தையும் காண்பிக்கவும்", 
        "student_management_system": "மாணவர் மேலாண்மை அமைப்பு",
        "home": "முகப்பு",
        "current_course_information": "தற்போதைய பாடத்திட்ட தகவல்",
        "department": "துறை",
        "select_department": "துறையை தேர்ந்தெடுக்கவும்",
        "cse": "சி.எஸ்.இ",
        "it": "ஐ.டி",
        "me": "எம்.இ",
        "ce": "சி.இ",
        "ece": "ஈ.சி.இ",
        "ee": "ஈ.இ",   
    },
    "te": {
        "title": "ముఖం గుర్తింపు హాజరు సిస్టమ్ సాఫ్ట్‌వేర్",
        "help": "సహాయ డెస్క్",
        "email": "ఇమెయిల్",
        "phone": "ఫోన్ నంబర్",
        "exit_confirm": "మీరు ప్రాజెక్ట్‌ను వదలాలనుకుంటున్నారా?",
        "yes": "అవును",
        "no": "కాదు",
        "student_details": "విద్యార్థి వివరాలు",
        "face_detector": "ముఖం గుర్తింపు పరికరం",
        "attendance": "హాజరు",
        "language": "భాష",
        "chatbox": "చాట్ బాక్స్",
        "train_data": "డేటా శిక్షణ",
        "photos": "ఫోటోలు",
        "developer": "డెవలపర్",
        "exit": "బయటకు రండి",
        "developer": "డెవలపర్ సమాచారం",
        "team_admin": "టీం అడ్మిన్",
        "team_member": "టీం సభ్యుడు",
        "NAME : Aditya Roy": "పేరు : ఆదిత్య రాయ్",
        "DEPT : Information Technology": "విభాగం : సమాచారం సాంకేతికత",
        "Year : 1st Year": "సంవత్సరం : మొదటి సంవత్సరం",
        "College : University Institute of Technology,BU": "కాలేజ్ : యూనివర్సిటీ ఇన్స్టిట్యూట్ ఆఫ్ టెక్నాలజీ, బీయూ",
        "status": "స్థితి",
        "home": "హోమ్",
        "NAME : Samaresh Debnath": "పేరు : సమరేశ్ దేవనాథ్",
        "NAME : Subhasis Mahato": "పేరు : సుభాసిస్ మహతో",
        "NAME : Deepanjan Seth": "పేరు : దీపాంజన్ సేత్",
        "train_data_set": "ప్రశిక్షణ డేటా సెట్",
        "train": "ప్రశిక్షణ",
        "help_desk": "సహాయం డెస్క్",
        "Train Data": "ట్రైన్ డేటా",
        "face_recognition": "ముఖం గుర్తింపు",
        "exit": "బయటకి పో",
        "student_management_system": "విద్యార్థి నిర్వహణ వ్యవస్థ",
        "home": "హోమ్",
        "current_course_information": "ప్రస్తుత కోర్సు సమాచారం",
        "department": "శాఖ",
        "select_department": "శాఖను ఎంచుకోండి",
        "cse": "సిఎస్‌ఇ",
        "it": "ఐటి",
        "me": "ఎం.ఇ",
        "ce": "సిఇ",
        "ece": "ఇసిఇ",
        "ee": "ఈఈ",
        "course": "కోర్సు",
        "select_course": "కోర్సును ఎంచుకోండి",
        "b.e": "బి.ఇ",
        "b.tech": "బి.టెక్",
        "m.e": "ఎం.ఇ",
        "m.tech": "ఎం.టెక్",
        "year": "సంవత్సరం",
        "select_year": "సంవత్సరాన్ని ఎంచుకోండి",
        "1st_year": "మొదటి సంవత్సరం",
        "2nd_year": "రెండవ సంవత్సరం",
        "3rd_year": "మూడవ సంవత్సరం",
        "4th_year": "నాల్గవ సంవత్సరం",
        "semester": "సెమిస్టర్",
        "select_semester": "సెమిస్టర్ ఎంచుకోండి",
        "1st Semester": "మొదటి సెమిస్టర్",
        "2nd Semester": "రెండవ సెమిస్టర్",
        "3rd Semester": "మూడవ సెమిస్టర్",
        "4th Semester": "నాల్గవ సెమిస్టర్",
        "student_information": "విద్యార్థి సమాచారం",
        "student_id": "విద్యార్థి ఐడి",
        "student_name": "విద్యార్థి పేరు",
        "class_division": "తరగతి విభజన",
        "select_class_division": "విభజన ఎంచుకోండి",
        "roll_no": "రుల్ నంబర్",
        "gender": "లింగం",
        "select_gender": "లింగాన్ని ఎంచుకోండి",
        "male": "పురుషుడు",
        "female": "స్త్రీ",
        "other": "ఇతరులు",
        "date_of_birth": "పుట్టిన తేది",
        "email": "ఈమెయిల్",
        "phone_no": "ఫోన్ నంబర్",
        "address": "చిరునామా",
        "teacher_name": "గురువు పేరు",
        "take_photo_sample": "ఫోటో నమూనాను తీసుకోండి",
        "no_photo_sample": "ఫోటో నమూనా లేదు",
        "save": "సేవ్ చేయండి",
        "update": "నవీకరించండి",
        "delete": "తొలగించండి",
        "reset": "రీసెట్ చేయండి",
        "take_photo": "ఫోటో తీసుకోండి",
        "update_photo": "ఫోటో నవీకరించండి",
        "search_student_information": "విద్యార్థి సమాచారం శోధించండి",
        "search_by": "ద్వారా శోధించండి",
        "select": "ఎంచుకోండి",
        "search": "శోధించండి",
        "show_all": "అన్నీ చూపించండి",

    },
    "gu": {
        "title": "ચહેરા ઓળખ હાજરી સિસ્ટમ સોફ્ટવેર",
        "help": "સહાય ડેસ્ક",
        "email": "ઇમેઇલ",
        "phone": "ફોન નંબર",
        "exit_confirm": "શું તમે પ્રોજેક્ટમાંથી બહાર નીકળવા માંગો છો?",
        "yes": "હા",
        "no": "ના",
        "student_details": "વિદ્યાર્થી વિગતો",
        "face_detector": "ચહેરો શોધક",
        "attendance": "હાજરી",
        "language": "ભાષા",
        "chatbox": "ચેટ બોક્સ",
        "train_data": "ડેટા તાલીમ",
        "photos": "ફોટા",
        "developer": "ડેવલપર",
        "exit": "બહાર નીકળો",
        "developer": "ડેવલપર માહિતી",
        "team_admin": "ટીમ પ્રશાસક",
        "team_member": "ટીમ સભ્ય",
        "NAME : Aditya Roy": "નામ : આદિત્ય રોય",
        "DEPT : Information Technology": "વિભાગ : માહિતી ટેકનોલોજી",
        "Year : 1st Year": "વર્ષ : પ્રથમ વર્ષ",
        "College : University Institute of Technology,BU": "કોલેજ : યુનિવર્સિટી ઇન્સ્ટીટ્યૂટ ઓફ ટેકનોલોજી, બીયૂ",
        "status": "સ્થિતિ",
        "home": "ઘર",
        "NAME : Samaresh Debnath": "નામ : સમરેશ દેવનાથ",
        "NAME : Subhasis Mahato": "નામ : સુભાસિસ મહતો",
        "NAME : Deepanjan Seth": "નામ : દીપાંજન સેથ",
        "train_data_set": "પ્રશિક્ષણ ડેટા સેટ",
        "train": "પ્રશિક્ષણ",
        "help_desk": "મદદ ડેસ્ક",
        "Train Data": "પ્રશિક્ષણ ડેટા",
        "face_recognition": "મુખ ઓળખાણ",
        "exit": "બહાર જાઓ",
         "student_management_system": "વિદ્યાર્થી વ્યવસ્થાપન સિસ્ટમ",
        "home": "મુખ્ય પૃષ્ઠ",
        "current_course_information": "વર્તમાન કોર્સ માહિતી",
        "department": "વિભાગ",
        "select_department": "વિભાગ પસંદ કરો",
        "cse": "સીએસઈ",
        "it": "આઈટી",
        "me": "એમઈ",
        "ce": "સીઈ",
        "ece": "ઈસઈ",
        "ee": "ઈઈ",
        "course": "કોર્સ",
        "select_course": "કોર્સ પસંદ કરો",
        "b.e": "બી.ઈ",
        "b.tech": "બી.ટેક",
        "m.e": "એમ.ઈ",
        "m.tech": "એમ.ટેક",
        "year": "વર્ષ",
        "select_year": "વર્ષ પસંદ કરો",
        "1st_year": "પ્રથમ વર્ષ",
        "2nd_year": "બીજું વર્ષ",
        "3rd_year": "તૃતીય વર્ષ",
        "4th_year": "ચોથી વર્ષ",
        "semester": "સેમેસ્ટર",
        "select_semester": "સેમેસ્ટર પસંદ કરો",
        "1st Semester": "પ્રથમ સેમેસ્ટર",
        "2nd Semester": "બીજું સેમેસ્ટર",
        "3rd Semester": "તૃતીય સેમેસ્ટર",
        "4th Semester": "ચોથી સેમેસ્ટર",
        "student_information": "વિદ્યાર્થી માહિતી",
        "student_id": "વિદ્યાર્થી આઈડી",
        "student_name": "વિદ્યાર્થી નામ",
        "class_division": "વર્ગ વિભાજન",
        "select_class_division": "વિભાજન પસંદ કરો",
        "roll_no": "રોલ નંબર",
        "gender": "લિંગ",
        "select_gender": "લિંગ પસંદ કરો",
        "male": "પુરુષ",
        "female": "સ્ત્રી",
        "other": "અન્ય",
        "date_of_birth": "જન્મ તારીખ",
        "email": "ઇમેઇલ",
        "phone_no": "ફોન નંબર",
        "address": "સરનામું",
        "teacher_name": "શિક્ષકનું નામ",
        "take_photo_sample": "ફોટો નમૂનો લો",
        "no_photo_sample": "ફોટો નમૂનો નથી",
        "save": "સેવ કરો",
        "update": "અપડેટ કરો",
        "delete": "કાઢી નાંખો",
        "reset": "રીસેટ કરો",
        "take_photo": "ફોટો લો",
        "update_photo": "ફોટો અપડેટ કરો",
        "search_student_information": "વિદ્યાર્થી માહિતી શોધો",
        "search_by": "દ્વારા શોધો",
        "select": "પસંદ કરો",
        "search": "શોધો",
        "show_all": "બધું બતાવો",
    }
}

# Default language
current_language = "en"

def set_language(lang_code):
    """Set the current language for the application."""
    global current_language
    if lang_code in languages:
        current_language = lang_code
        logging.info(f"Language set to: {lang_code}")
    else:
        logging.warning(f"Unsupported language code attempted: {lang_code}")
        raise ValueError(f"Language code '{lang_code}' is not supported.")

def get_text(key):
    """Retrieve the text for the current language based on the key.
    Falls back to English if key not found in current language.
    """
    # Attempt to get the text from the current language
    text = languages.get(current_language, {}).get(key)

    # If the text is None, log a warning and fall back to English
    if text is None:
        logging.warning(f"Key '{key}' not found in language '{current_language}'. Falling back to English.")
        text = languages["en"].get(key, f"[{key}]")  # Fallback to English or return the key itself if not found

    return text
