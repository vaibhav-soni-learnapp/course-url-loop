import streamlit as st

def generate_image_urls(base_url, num_images):
    image_urls = []
    for i in range(1, num_images + 1):
        url = base_url + "+" + "(" + str(i) + ")" + ".jpg"
        image_urls.append(url)
    return image_urls

def main():
    st.title("Dynamic Image URLs")

    base_url = st.text_input("Enter the base URL:")
    num_images = st.slider("Number of images:", 1, 500, 20)

    if st.button("Generate URLs"):
        image_urls = generate_image_urls(base_url, num_images)
        st.write("Generated URLs:")
        st.write(image_urls)

if __name__ == "__main__":
    main()
