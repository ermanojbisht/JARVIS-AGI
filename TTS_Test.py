from ENGINE.TTS.ElevenLabs import ElevenLabsAPI

if __name__ == "__main__":
    api = ElevenLabsAPI()
    api.speak(text="""सुबह की धूप, पक्षियों का चहचहाना, हवा में ताज़गी - ये सब मिलकर एक ख़ूबसूरत दिन की शुरुआत करते हैं। हरी-भरी घास के मैदान, फूलों की सुगंध, और आसमान में तैरते बादल - ये दृश्य मन को प्रसन्न करते हैं और जीवन के प्रति आशा जगाते हैं।""", voice_name="glinda")
