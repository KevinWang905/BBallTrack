# Author(s): Kevin Wang
# Last Update: April 1, 2021

# Function: Parses output csv from JSON_ANAL.py for paramters from raw data
# Outputs: 1 csv file


#################################################################################

import pandas as pd
import math
from measurements import *

# import data and remove null rows
rawData = pd.read_csv('coord_df.csv')
rawData.dropna(axis = 0,inplace= True)
rawData.reset_index(inplace = True)

 
def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

def getDistance(a,b):
	distance = ((((b[0] - a[0] )**2) + ((b[1]-a[1])**2) )**0.5)
	return distance

def shoulder_flexion(frame):
	elbow_coords = (rawData.loc[frame,'Elbow_L_X'], rawData.loc[frame,'Elbow_L_Y'])
	shoulder_coords = (rawData.loc[frame,'Shoulder_L_X'], rawData.loc[frame,'Shoulder_L_Y'])
	groin_coords = (rawData.loc[frame,'Groin_X'], rawData.loc[frame,'Groin_Y'])
	angle = getAngle(elbow_coords, shoulder_coords, groin_coords)
	return 360 - angle if angle > 180 else angle

def elbow_flexion(frame):
	Wrist_coords = (rawData.loc[frame,'Wrist_L_X'], rawData.loc[frame,'Wrist_L_Y'])
	elbow_coords = (rawData.loc[frame,'Elbow_L_X'], rawData.loc[frame,'Elbow_L_Y'])
	shoulder_coords = (rawData.loc[frame,'Shoulder_L_X'], rawData.loc[frame,'Shoulder_L_Y'])
	angle = getAngle(Wrist_coords, elbow_coords, shoulder_coords)
	return 360 - angle if angle > 180 else angle

def knee_flexion(frame):
	ankle_coords = (rawData.loc[frame,'Ankle_L_X'], rawData.loc[frame,'Ankle_L_Y'])
	knee_coords = (rawData.loc[frame,'Knee_L_X'], rawData.loc[frame,'Knee_L_Y'])
	hip_coords = (rawData.loc[frame,'Hip_L_X'], rawData.loc[frame,'Hip_L_Y'])
	angle = getAngle(ankle_coords, knee_coords, hip_coords)
	return 360 - angle if angle > 180 else angle

def trunk_flexion(frame):
	chest_coords = (rawData.loc[frame,'Chest_X'], rawData.loc[frame,'Chest_Y'])
	groin_coords = (rawData.loc[frame,'Groin_X'], rawData.loc[frame,'Groin_Y'])
	knee_coords = (rawData.loc[frame,'Knee_L_X'], rawData.loc[frame,'Knee_L_Y'])
	angle = getAngle(chest_coords, groin_coords, knee_coords)
	return 360 - angle if angle > 180 else angle

def wrist_flexion(frame):
	elbow_coords = (rawData.loc[frame,'Elbow_L_X'], rawData.loc[frame,'Elbow_L_Y'])
	wrist_coords = (rawData.loc[frame,'Wrist_L_X'], rawData.loc[frame,'Wrist_L_Y'])
	knuckle_coords = (rawData.loc[frame,'Mid_knuckle_X'], rawData.loc[frame,'Mid_knuckle_Y'])
	angle = getAngle(elbow_coords, wrist_coords, knuckle_coords)
	return angle

def finger_flexion(frame):
	finger_coords = (rawData.loc[frame,'Mid_fing_X'], rawData.loc[frame,'Mid_fing_Y'])
	knuckle_coords = (rawData.loc[frame,'Mid_knuckle_X'], rawData.loc[frame,'Mid_knuckle_Y'])
	wrist_coords = (rawData.loc[frame,'Wrist_L_X'], rawData.loc[frame,'Wrist_L_Y'])
	angle = getAngle(finger_coords, knuckle_coords, wrist_coords)
	return angle

def finger_flexion(frame):
	finger_coords = (rawData.loc[frame,'Mid_fing_X'], rawData.loc[frame,'Mid_fing_Y'])
	knuckle_coords = (rawData.loc[frame,'Mid_knuckle_X'], rawData.loc[frame,'Mid_knuckle_Y'])
	wrist_coords = (rawData.loc[frame,'Wrist_L_X'], rawData.loc[frame,'Wrist_L_Y'])
	angle = getAngle(finger_coords, knuckle_coords, wrist_coords)
	return angle

def ball_shoulder(frame):
	ball_coords = (rawData.loc[frame,'Wrist_L_X'], rawData.loc[frame,'Wrist_L_Y'])
	shoulder_coords = (rawData.loc[frame,'Shoulder_L_X'], rawData.loc[frame,'Shoulder_L_Y'])
	distance = getDistance(ball_coords, shoulder_coords)
	return distance

def get_parameters():
	param_list = [] 
	for i in range(len(rawData)):
		param_list = param_list + [[i,shoulder_flexion(i),elbow_flexion(i),knee_flexion(i),trunk_flexion(i), wrist_flexion(i), finger_flexion(i), ball_shoulder(i), rawData.loc[i,'Wrist_L_Y']]]
	params = pd.DataFrame(param_list, columns = ['frame', 'shoulder_flexion', 'elbow_flexion', 'knee_flexion', 'trunk flexion', 'wrist_flexion', 'finger_flexion', 'ball_from_body','ball_height'])
	params.to_csv("params_df.csv")
	return 0

print(Shooters[DAME].height)
get_parameters()