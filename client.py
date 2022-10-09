import banana_dev as banana
import os
from dotenv import load_dotenv
from timeit import default_timer as timer

load_dotenv()

BANANA_DEV_CLIP_MODEL_KEY = os.environ.get('BANANA_DEV_CLIP_MODEL_KEY')
BANANA_DEV_API_KEY = os.environ.get('BANANA_DEV_API_KEY')

model_inputs = {
    "text": "banana",
    "imageURL":"https://demo-images-banana.s3.us-west-1.amazonaws.com/image1.jpg"
}

print( "API KEY", BANANA_DEV_API_KEY)
print( "MODEL KEY", BANANA_DEV_CLIP_MODEL_KEY)
# Run the model
start = timer()
out = banana.run(BANANA_DEV_API_KEY, BANANA_DEV_CLIP_MODEL_KEY, model_inputs)
end = timer()

print("Time taking to generate image", (end-start))

print(out)