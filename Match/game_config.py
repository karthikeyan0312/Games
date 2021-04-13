import os

IMAGE_SIZE=128
SCREEN_SIZE=512
NUM_TILES_SIDE=4
NUM_TILES_TOTAL=16
MARGIN=4

ASSET_DIR=  r'E:\my python\game\New folder\assests'
ASSET_FILES=[x for x in os.listdir(ASSET_DIR) if x[-3:].lower()=='png']
try:
    assert len(ASSET_FILES)==8

except AssertionError:
    print(" we have problem")
    raise