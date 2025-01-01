import os
import replicate
import streamlit as st

# Set the Replicate API token
os.environ["REPLICATE_API_TOKEN"] = "r8_G2f177ag7U7mu7sPhxeXHGVqEwYWDJt4VVNUp"

# Streamlit app layout
st.title("Bald filter")
st.write("Enter a prompt to generate an image using AI.")

# Input field for prompt
prompt = st.text_input("Enter your prompt:", "")

# Generate button
if st.button("Generate Image"):
    if not prompt.strip():
        st.error("Please enter a valid prompt.")
    else:
        st.write("Generating image... Please wait.")
        try:
            # Call Replicate API
            output = replicate.run(
                "black-forest-labs/flux-schnell",
                input={
                    "prompt": prompt,
                    "go_fast": True,  # Default: enable fast generation
                    "megapixels": "1",  # Default: 1 megapixel
                    "num_outputs": 1,  # Default: 1 output
                    "aspect_ratio": "1:1",  # Default: 1:1 aspect ratio
                    "output_format": "webp",  # Default: webp format
                    "output_quality": 80,  # Default: 80 quality
                    "num_inference_steps": 4,  # Default: 4 inference steps
                },
            )

            # Debugging: Display the raw output
            st.write("Raw Output:", output)

            # Handle FileOutput object
            if isinstance(output, list) and len(output) > 0:
                file_output = output[0]
                st.write("FileOutput Object:", file_output)

                # Assuming the file_output has a URL or file path
                if hasattr(file_output, "url"):
                    st.image(file_output.url, caption="Generated Image", use_column_width=True)
                elif hasattr(file_output, "path"):
                    st.image(file_output.path, caption="Generated Image", use_column_width=True)
                else:
                    st.error("Unexpected output format. Unable to display the image.")
            else:
                st.error("Failed to generate an image. Please try again.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
