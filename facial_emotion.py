# import cv2
# from deepface import DeepFace
#
# def detect_emotion_from_webcam():
#     cap = cv2.VideoCapture(0)
#     print("📷 Starting webcam. Press 'q' to capture face.")
#
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to grab frame.")
#             break
#
#         cv2.imshow("Press 'q' to capture", frame)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()
#
#     try:
#         print("🔍 Analyzing emotion...")
#         result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
#         emotion = result[0]['dominant_emotion']
#         print(f"🧠 Detected Emotion: {emotion}")
#         return emotion
#     except Exception as e:
#         print("❌ Emotion detection failed:", e)
#         return None
