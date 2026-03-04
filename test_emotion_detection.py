from EmotionDetection import emotion_detector

def test_emotions():

    result = emotion_detector("I am glad this happened")
    assert result['dominant_emotion'] == 'joy'
    print("Test 1 passed")

    result = emotion_detector("I am really mad about this")
    assert result['dominant_emotion'] == 'anger'
    print("Test 2 passed")

    result = emotion_detector("I feel disgusted just hearing about this")
    assert result['dominant_emotion'] == 'disgust'
    print("Test 3 passed")

    result = emotion_detector("I am so sad about this")
    assert result['dominant_emotion'] == 'sadness'
    print("Test 4 passed")

    result = emotion_detector("I am really afraid that this will happen")
    assert result['dominant_emotion'] == 'fear'
    print("Test 5 passed")


test_emotions()