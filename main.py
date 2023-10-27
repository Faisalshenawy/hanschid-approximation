import streamlit as st

# Title and Image
st.title("Dose Calculation Web App")
st.image("equation1.png", use_column_width=True)

# Create input fields for cell parameters
st.write("Enter the following cell parameters:")

# Select box for organ
organs = ["Left Kidney", "Right Kidney", "Liver","Lesion"]
selected_organ = st.selectbox("Select Organ", organs)

total_count = st.number_input("Total Count")
time_point_hours = st.number_input("Time Point in Hours")
time_per_projection = st.number_input("Time per Projection (seconds)")
num_images = st.number_input("Number of Images")
volume = st.number_input("Volume (ml)")
calibration_factor = st.number_input("Calibration Factor")

# Calculation logic (you need to implement this)
if st.button("Calculate Dose"):
    # Perform the calculation based on the entered values
    dose = 0.25 * (total_count * time_point_hours) / (time_per_projection * num_images * volume * calibration_factor)
    # Display the absorbed dose for the selected organ
    st.write(f"Absorbed Dose for {selected_organ} (Gy) = {dose:.2f} Gy")



# Reference text
st.markdown("Reference: Dose Mapping After Endoradiotherapy with 177Lu-DOTATATE/DOTATOC by a Single Measurement After 4 Days.https://jnm.snmjournals.org/content/59/1/75")
