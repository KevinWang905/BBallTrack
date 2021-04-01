# Author: Kevin Wang
# Last Update: April 1, 2021

# Function: Parses JSON files for anatomic coordinate information extracted via OpenPose

# Outputs: 1 csv file


#################################################################################

import json
import pandas as pd
import numpy as np
import os

###################################################
# User Inputs
videoname = 'chris_1_'
videoframes = 41
###################################################

def extract_coords(framenum):
    frame_coord = [framenum]
    number_str = str(framenum)
    zfn = number_str.zfill(12)
    print('\nFrame: ' + str(framenum))

    vidname = videoname+str(zfn)


    with open('%s_keypoints.json' %vidname) as f:
        data = json.load(f)
    try:
	    #print(data['people'][0]['pose_keypoints_2d'])
	    full_data = data['people'][0]['pose_keypoints_2d']
	    hand_data = data['people'][0]['hand_right_keypoints_2d']
	    frame_data_body = []
	    frame_data_hand = []
	    frame_data_full = []
	    for i in range (0, len(full_data)):
	        if i % 3 != 2:
	        	frame_data_body = frame_data_body+[full_data[i]]
	    for i in range (0, len(hand_data)):
	        if i % 3 != 2:
	        	frame_data_hand = frame_data_hand+[hand_data[i]]
	            
	    #print(frame_coord)
	    frame_coord = frame_coord + frame_data_body + frame_data_hand
	    print(frame_coord)
    except:
    	print(np.nan)
    	frame_coord = frame_coord + [np.nan]
    return frame_coord

coord_ = []
for i in range(0, videoframes):
	coord_ = coord_ + [extract_coords(i)]

coord_df = pd.DataFrame(coord_)
coord_df.columns = ['Frame', 'Head_X', 'Head_Y', 'Chest_X', 'Chest_Y', 'Shoulder_R_X', 'Shoulder_R_Y','Elbow_R_X', 'Elbow_R_Y',
					'Wrist_R_X', 'Wrist_R_Y','Shoulder_L_X', 'Shoulder_L_Y','Elbow_L_X', 'Elbow_L_Y',
					'Wrist_L_X', 'Wrist_L_Y','Groin_X', 'Groin_Y','Hip_R_X', 'Hip_R_Y', 'Knee_R_X', 'Knee_R_Y',
					'Ankle_R_X', 'Ankle_R_Y','Hip_L_X', 'Hip_L_Y','Knee_L_X', 'Knee_L_Y','Ankle_L_X', 'Ankle_L_Y',
					'Eye_R_X', 'Eye_R_Y','Eye_L_X', 'Eye_L_Y','Ear_R_X', 'Ear_R_Y','Ear_L_X', 'Ear_L_Y','Ses_L_X', 'Ses_L_Y',
					'Toes_L_X', 'Tose_L_Y','Heel_L_X', 'Heel_L_Y','Ses_R_X', 'Ses_R_Y','Toes_R_X', 'Toes_R_Y','Heel_R_X', 'Heel_R_Y',
					'0_X','0_Y','1_X','1_Y','2_X','2_Y','3_X','3_Y','4_X','4_Y','5_X','5_Y','6_X','6_Y','7_X','7_Y','8_X','8_Y',
					'Mid_knuckle_X','Mid_knuckle_Y','10_X','10_Y','11_X','11_Y','Mid_fing_X','Mid_fing_Y',
					'13_X','13_Y','14_X','14_Y','15_X','15_Y','16_X','16_Y','17_X','17_Y','18_X','18_Y','19_X','19_Y','20_X','20_Y']
coord_df.to_csv("coord_df.csv")

