import streamlit as st

st.title("Simplified Dosimetry For Peptide Receptor Radionuclide Therapy (PRRT) Using 177Lu-DOTATATE/DOTATOC ")


st.image("equation1.png", use_column_width=True)

# Create input fields for cell parameters on the main page
st.write("Enter the following cell parameters:")
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

    # Display the result
    st.write(f"Dose (Gy) = {dose:.2f} Gy")

# Optionally, provide some instructions to the user
st.markdown("Enter the cell parameters above, then click 'Calculate Dose' to get the result.")



# Reference text
st.markdown("Reference: Dose Mapping After Endoradiotherapy with 177Lu-DOTATATE/DOTATOC by a Single Measurement After 4 Days.https://jnm.snmjournals.org/content/59/1/75")