import torch
import torch.nn as nn
import streamlit as st
from PIL import Image
import torchvision.transforms as transforms

# Set page configuration
st.set_page_config(page_title="Cassava Leaf Disease Classification", layout="wide")

class LeNetCustomClassifier(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.model = nn.Sequential(                     # (3, 150, 150)
            nn.Conv2d(in_channels=3,
                      out_channels=6,
                      kernel_size=5,
                      padding='same'),                  # (6, 150, 150)
            nn.AvgPool2d(kernel_size=2, stride=2),      # (6, 75, 75)
            nn.ReLU(),
            nn.Conv2d(in_channels=6,
                      out_channels=16,
                      kernel_size=5),                   # (16, 71, 71)
            nn.AvgPool2d(kernel_size=2, stride=2),      # (16, 35, 35)
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(16 * 35 * 35, 120),
            nn.Linear(120, 84),
            nn.Linear(84, num_classes)
        )

    def forward(self, x):
        return self.model(x)


@st.cache_resource
def load_model(model_path, num_classes=5):
    lenet_model = LeNetCustomClassifier(num_classes)
    lenet_model.load_state_dict(torch.load(model_path, weights_only=True))
    lenet_model.eval()
    return lenet_model


def inference(image, model):
    idx2label = {
        0: 'cbb',
        1: 'cbsd',
        2: 'cgm',
        3: 'cmd',
        4: 'healthy',
    }
    w, h = image.size

    if w != h:
        crop = transforms.CenterCrop(min(w, h))
        image = crop(image)

    img_transform = transforms.Compose([
        transforms.Resize((150, 150)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.4479, 0.4965, 0.3222],
                             std=[0.2056, 0.2062, 0.1802]),
    ])
    img_new = img_transform(image)
    img_new = img_new.expand(1, 3, 150, 150)

    model.eval()
    with torch.no_grad():
        predictions = model(img_new)
    preds = nn.Softmax(dim=1)(predictions)
    p_max, yhat = torch.max(preds.data, 1)

    return p_max.item()*100, idx2label[yhat.item()]


def main():
    st.title('Cassava Leaf Disease Classification')
    st.markdown("### Model: LeNet\nDataset: Cassava Leaf Disease")

    st.sidebar.title("Options")
    option = st.sidebar.selectbox('Input Method', ('Upload Image File', 'Run Example Image'))

    if option == "Upload Image File":
        file = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        if file is not None:
            image = Image.open(file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
            with st.spinner('Classifying...'):
                pred, label = inference(image, model)
            st.success(f"The uploaded image is of the {label} with {pred:.2f}% probability.")
        else:
            st.warning("Please upload an image file.")

    elif option == "Run Example Image":
        image = Image.open('demo_cbsd.jpg')
        st.image(image, caption='Example Image', use_column_width=True)
        with st.spinner('Classifying...'):
            pred, label = inference(image, model)
        st.success(f"The image is of the {label} with {pred:.2f}% probability.")


if __name__ == '__main__':
    model = load_model('./model/rgb_lenet_model.pt')
    main()