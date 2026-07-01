# Steps to run inside the IBM Skills Network Cloud IDE

The Watson NLP `EmotionPredict` endpoint (`sn-watson-emotion.labs.skillsnetwork.site`) only resolves inside the Skills Network Cloud IDE lab session, so the steps below must be run there, not on your local machine.

1. Open the "Emotion Detector" lab in Skills Network Cloud IDE (Theia/Bash terminal).
2. Clone your repo into the lab environment:
   ```bash
   git clone https://github.com/NonomiyaIzumi/emotion-detector-flask.git
   cd emotion-detector-flask
   pip install -r requirements.txt
   ```

## Task 2 Activity 2 — import + raw output

```bash
python3
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector("I am so happy I am doing this")
```
Screenshot/copy the interpreter output. Save it as `submission_assets/task2_raw_output.txt`.

## Task 3 Activity 2 — formatted output

Same call as above, but since `emotion_detection.py` already returns the formatted dict (this repo already has Task 3's formatting applied), copy that output too.
Save it as `submission_assets/task3_formatted_output.txt`.

## Task 5 — unit tests

```bash
python3 -m unittest test_emotion_detection.py -v
```
All 1 test / 5 assertions should pass since the real Watson endpoint is reachable here. Save the terminal output as `submission_assets/task5_unittest_output.txt`.

## Task 6 Activity 2 — deployment screenshot

```bash
python3 server.py
```
Use the lab's "Launch Application" button (or the exposed port-5000 URL) to open the app in a browser, type a statement, click "Run Sentiment Analysis", and confirm a real result appears.
Take a screenshot and save it as `submission_assets/6b_deployment_test.png`.

## Task 7 Activity 3 — error handling screenshot

In the same running app, submit a blank input (empty text box) and click "Run Sentiment Analysis". Confirm the UI shows `Invalid text! Please try again!`.
Take a screenshot and save it as `submission_assets/7c_error_handling_interface.png`.

## After collecting these

Copy/download the 3 `.txt` files and 2 `.png` files back to this local project's `submission_assets/` folder, then tell me — I'll regenerate `Emotion_Detector_Submission.pdf` with everything filled in.
