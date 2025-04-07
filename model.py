import streamlit as st
import pickle
import numpy as np

# Function to load the model based on the selected disease
def load_model(disease):
    if disease == "Kidney Disease":
        return pickle.load(open("k_model.pkl", "rb"))
    elif disease == "Liver Disease":
        return pickle.load(open("l_model.pkl", "rb"))
    elif disease == "Parkinson's Disease":
        return pickle.load(open("p_model.pkl", "rb"))

# Function to get user input for each disease
def get_user_input(disease):
    inputs = {}

    if disease == "Kidney Disease":
        st.subheader("🩸 Enter Kidney Disease Features:")
        inputs['age'] = st.number_input("Age", min_value=0, max_value=100, value=50)
        inputs['bp'] = st.number_input("Blood Pressure", min_value=50, max_value=200, value=120)
        inputs['sg'] = st.number_input("Specific Gravity", min_value=1.0, max_value=1.05, value=1.02, step=0.01)
        inputs['al'] = st.number_input("Albumin", min_value=0, max_value=5, value=1)
        inputs['su'] = st.number_input("Sugar", min_value=0, max_value=5, value=0)

        # Encoding categorical values
        inputs['rbc'] = 1 if st.selectbox("Red Blood Cells", ["Normal", "Abnormal"]) == "Normal" else 0
        inputs['pc'] = 1 if st.selectbox("Pus Cells", ["Normal", "Abnormal"]) == "Normal" else 0
        inputs['pcc'] = 1 if st.selectbox("Pus Cell Clumps", ["Present", "Not Present"]) == "Present" else 0
        inputs['ba'] = 1 if st.selectbox("Bacteria", ["Present", "Not Present"]) == "Present" else 0
        inputs['htn'] = 1 if st.selectbox("Hypertension", ["Yes", "No"]) == "Yes" else 0
        inputs['dm'] = 1 if st.selectbox("Diabetes Mellitus", ["Yes", "No"]) == "Yes" else 0
        inputs['cad'] = 1 if st.selectbox("Coronary Artery Disease", ["Yes", "No"]) == "Yes" else 0
        inputs['appet'] = 1 if st.selectbox("Appetite", ["Good", "Poor"]) == "Poor" else 0
        inputs['pe'] = 1 if st.selectbox("Pedal Edema", ["Yes", "No"]) == "Yes" else 0
        inputs['ane'] = 1 if st.selectbox("Anemia", ["Yes", "No"]) == "Yes" else 0

        inputs['bgr'] = st.number_input("Blood Glucose Random", min_value=50, max_value=500, value=100)
        inputs['bu'] = st.number_input("Blood Urea", min_value=0, max_value=400, value=50)
        inputs['sc'] = st.number_input("Serum Creatinine", min_value=0.0, max_value=18.1, value=1.2)
        inputs['sod'] = st.number_input("Sodium", min_value=100, max_value=200, value=140)
        inputs['pot'] = st.number_input("Potassium", min_value=2.0, max_value=10.0, value=4.5)
        inputs['hemo'] = st.number_input("Hemoglobin", min_value=5.0, max_value=20.0, value=13.5)
        inputs['wc'] = st.number_input("White Blood Cell Count", min_value=2000, max_value=27000, value=8000)
        inputs['rc'] = st.number_input("Red Blood Cell Count", min_value=2.0, max_value=8.0, value=5.0)

        return np.array([[inputs['age'], inputs['bp'], inputs['sg'], inputs['al'], inputs['sc'],inputs['rbc'], 
                          inputs['pc'], inputs['pcc'], inputs['ba'], inputs['htn'], inputs['dm'], inputs['cad'], 
                          inputs['appet'], inputs['pe'], inputs['ane'], inputs['bgr'], inputs['bu'], inputs['sc'], 
                          inputs['sod'], inputs['pot'], inputs['hemo'], inputs['wc'], inputs['rc']]])

    elif disease == "Liver Disease":
        st.subheader("🫁 Enter Liver Disease Features:")
        inputs['age'] = st.number_input("Age", min_value=1, max_value=100, value=45)

        # Encoding categorical 'gender'
        inputs['gender'] = 1 if st.selectbox("Gender", ["Male", "Female"]) == "Male" else 0
        inputs['total_bilirubin'] = st.number_input("Total Bilirubin", min_value=0.0, max_value=50.0, value=1.0)
        inputs['alkaline_phosphotase'] = st.number_input("Alkaline Phosphotase", min_value=0, max_value=2200, value=100)
        inputs['alamine_aminotransferase'] = st.number_input("Alamine Aminotransferase", min_value=0, max_value=2000, value=50)
        inputs['albumin'] = st.number_input("Albumin", min_value=1.0, max_value=6.0, value=4.0)
        inputs['albumin_and_globulin_ratio'] = st.number_input("Albumin and Globulin Ratio", min_value=0.1, max_value=3.0, value=1.0, step=0.1)

        return np.array([[inputs['age'], inputs['gender'], inputs['total_bilirubin'],inputs['alkaline_phosphotase'], 
                          inputs['alamine_aminotransferase'], inputs['albumin'], inputs['albumin_and_globulin_ratio']]])

    elif disease == "Parkinson's Disease":
        st.subheader("🧠 Enter Parkinson's Disease Features:")
        inputs['mdvp_fo'] = st.number_input("MDVP:Fo(Hz)", min_value=50.0, max_value=300.0, value=150.0)
        inputs['mdvp_fhi'] = st.number_input("MDVP:Fhi(Hz)", min_value=50.0, max_value=600.0, value=200.0)
        inputs['mdvp_flo'] = st.number_input("MDVP:Flo(Hz)", min_value=50.0, max_value=240.0, value=100.0)
        inputs['mdvp_jitter'] = st.number_input("MDVP:Jitter(%)", min_value=0.0, max_value=1.0, value=0.01, step=0.01)
        inputs['mdvp_shimmer'] = st.number_input("MDVP:Shimmer", min_value=0.0, max_value=1.0, value=0.02, step=0.01)
        inputs['hnr'] = st.number_input("HNR", min_value=0.0, max_value=40.0, value=20.0)
        inputs['rpde'] = st.number_input("RPDE", min_value=0.0, max_value=1.0, value=0.5)
        inputs['dfa'] = st.number_input("DFA", min_value=0.0, max_value=2.0, value=0.7)
        inputs['spread1'] = st.number_input("Spread1", min_value=-10.0, max_value=10.0, value=-4.0)
        inputs['spread2'] = st.number_input("Spread2", min_value=0.0, max_value=1.0, value=0.2)
        inputs['d2'] = st.number_input("D2", min_value=0.0, max_value=4.0, value=2.0)

        return np.array([[inputs['mdvp_fo'], inputs['mdvp_fhi'], inputs['mdvp_flo'], inputs['mdvp_jitter'], 
                          inputs['mdvp_shimmer'], inputs['hnr'], inputs['rpde'], inputs['dfa'], inputs['spread1'], 
                          inputs['spread2'], inputs['d2']]])

# Main function
def main():
    st.title("🌟 AI-Powered Disease Prediction System")
    st.warning("⚠️ This is a prediction tool, not a medical diagnosis. Please consult a doctor for professional advice.")

    # Sidebar Navigation
    st.sidebar.title("🩺 Disease Prediction System")
    disease = st.sidebar.selectbox("🔍 Select a Disease", 
                                   ["Kidney Disease", "Liver Disease", "Parkinson's Disease"])

    model = load_model(disease)
    user_input = get_user_input(disease)

    if st.button("🔍 Predict"):
        prediction = model.predict(user_input)

        if prediction[0] == 1:
            st.markdown('<p class="positive">🚨 Positive Result: Check with a doctor immediately!</p>', unsafe_allow_html=True)
            st.markdown('<p class="advice">⚠️ It’s crucial to consult a healthcare professional to confirm the diagnosis and take timely action.</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="negative">✅ Negative Result: You seem fine!</p>', unsafe_allow_html=True)
            st.markdown('<p class="advice">👍 Keep up the good health, but regular check-ups are always recommended!</p>', unsafe_allow_html=True)

    st.markdown("---")
    st.info("📜 **Terms & Conditions:** This application is AI -Model only. Please consult a healthcare professional for actual diagnosis.")

if __name__ == "__main__":
    main()
