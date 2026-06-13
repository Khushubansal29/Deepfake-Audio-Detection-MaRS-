import os

from predict import predict_audio

test_fake_path = "../dataset/for-2sec/for-2seconds/testing/fake"
test_real_path = "../dataset/for-2sec/for-2seconds/testing/real"

print("FAKE FILES")
for file in os.listdir(test_fake_path)[:5]:
    path = os.path.join(test_fake_path, file)

    prediction = predict_audio(path)

    print(file, "->", prediction)

print("\nREAL FILES")
for file in os.listdir(test_real_path)[:5]:
    path = os.path.join(test_real_path, file)

    prediction = predict_audio(path)

    print(file, "->", prediction)