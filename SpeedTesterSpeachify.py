from ENGINE.TTS.speechify import Async_Speechify_Speechify_SpeechGenerator, Speechify_SpeechGenerator, speak
import time

async_generator = Async_Speechify_Speechify_SpeechGenerator()
partial_async_generator = Speechify_SpeechGenerator()


# text = 'सूरज की किरणें धीरे-धीरे  पेड़ों के पत्तों के बीच से झाँक रही थीं'
# text = '''सूरज की किरणें धीरे-धीरे  पेड़ों के पत्तों के बीच से झाँक रही थीं। हवा में ताज़ी खुशबू तैर रही थी, जैसे ज़मीन से उठी हो।  पक्षियों के चहचहाने से सन्नाटा टूट गया था, और  जंगल जीवन के साथ गूंज उठा था।  एक छोटा सा खरगोश पेड़ के नीचे से निकला, अपनी छोटी सी नाक हवा में घुमाते हुए,  और कुछ ही पलों में  घने  पेड़ों में  गायब हो गया।'''
text = "Thank you for watching! I hope you found this video informative and helpful. If you did, please give it a thumbs up and consider subscribing to my channel for more videos like this."
# speak(text)
for i in range(10):
    start = time.time()
    async_generator.speak(text)
    print(f"\033[92m\nAsync Audio Generator response time: {time.time() - start:.2f} seconds\033[0m") # Green

    start = time.time()
    partial_async_generator.speak(text)
    print(f"\033[94mSession Audio Generator response time: {time.time() - start:.2f} seconds\033[0m") # Blue

    start = time.time()
    speak(text)
    print(f"\033[93mNormal Audio Generator response time: {time.time() - start:.2f} seconds\033[0m") # Yellow
