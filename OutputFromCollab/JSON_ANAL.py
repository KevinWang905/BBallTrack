# Author: Kevin Wang
# Last Update: Feb 20, 2021

# Function: Parses JSON files for anatomic coordinate information extracted via OpenPose

# Outputs: 1 csv file


#################################################################################

import json
import pandas as pd
import numpy as np
import os




def extract_coords(framenum):
    frame_coord = [framenum]
    number_str = str(framenum)
    zfn = number_str.zfill(12)
    print('\nFrame: ' + str(framenum))


    with open('video_%s_keypoints.json' %zfn) as f:
        data = json.load(f)
    try:
	    #print(data['people'][0]['pose_keypoints_2d'])
	    full_data = data['people'][0]['pose_keypoints_2d']
	    for i in range (0, len(full_data)):
	        if i % 3 != 2:

	            frame_coord = frame_coord + [full_data[i]]
	    #print(frame_coord)
    except:
    	print(np.nan)
    	frame_coord = frame_coord + [np.nan]
    return frame_coord

coord_ = []
for i in range(0, 180):
	coord_ = coord_ + [extract_coords(i)]

coord_df = pd.DataFrame(coord_)
coord_df.columns = ['Frame', 'Head_X', 'Head_Y', 'Chest_X', 'Chest_Y', 'Shoulder_R_X', 'Shoulder_R_Y','Elbow_R_X', 'Elbow_R_Y',
					'Wrist_R_X', 'Wrist_R_Y','Shoulder_L_X', 'Shoulder_L_Y','Elbow_L_X', 'Elbow_L_Y',
					'Wrist_L_X', 'Wrist_L_Y','Groin_X', 'Groin_Y','Hip_R_X', 'Hip_R_Y', 'Knee_R_X', 'Knee_R_Y',
					'Ankle_R_X', 'Ankle_R_Y','Hip_L_X', 'Hip_L_Y','Knee_L_X', 'Knee_L_Y','Ankle_L_X', 'Ankle_L_Y',
					'Eye_R_X', 'Eye_R_Y','Eye_L_X', 'Eye_L_Y','Ear_R_X', 'Ear_R_Y','Ear_L_X', 'Ear_L_Y','Ses_L_X', 'Ses_L_Y',
					'Toes_L_X', 'Tose_L_Y','Heel_L_X', 'Heel_L_Y','Ses_R_X', 'Ses_R_Y','Toes_R_X', 'Tose_R_Y','Heel_R_X', 'Heel_R_Y']
coord_df.to_csv("coord_df.csv")

