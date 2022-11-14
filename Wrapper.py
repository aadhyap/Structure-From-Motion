#choose 8 correspondances between two images (1 and another image)
import numpy as np
import cv2 as cv2
from EstimateFundamentalMatrix import EstimateFundamentalMatrix
from GetInlierRANSAC import GetInlierRANSAC
from EssentialMatrixFromFundamentalMatrix import EssentialMatrixFromFundamentalMatrix
from ExtractCameraPose import ExtractCameraPose
from LinearTriangulation import LinearTriangulation
from NonlinearTriangulation import NonlinearTriangulation
from DisambiguateCameraPose import DisambiguateCameraPose
from LinearPnP import LinearPnP
from PnPRANSAC import PnPRANSAC
from NonlinearPnP import NonlinearPnP





#read matching 1 txt file







'''
Params: takes in filename of the matching.txt file and the id of the pair it is trying to match to
#returns one list with the rgb values as key and a second with teh coordinates of the matching text 
file as key and the matches as value

'''

def FindMatchings(filename, id_):
    with open(filename) as f:
        lines = f.readlines()
        lengthLines = len(lines)
        matching_1 = {}
        for i in range(lengthLines):
            if( i != 0):
                points_data = {}
                data = lines[i]
                data = data.split()
        

        
                lenpoints = int(data[0])
                r = data[1]
                g = data[2]
                b = data[3]
               
                imgx = float(data[4])
                imgy = float(data[5])

                rgb = tuple([r, g, b, imgx, imgy])




                #data of other points start after data[5]
                twos = 0
                total = j = 6
                while j  < total + lenpoints  + 1:
                    ID = data[j]
                    if(ID == id_):
                        twos = twos + 1
                    img_u = float(data[j + 1])
                    img_v = float(data[j + 2])
                    j = j + 3
                    points_data[ID] = [img_u, img_v]


                matching_1[rgb] = points_data

    matchings = {}
    
    for keys in matching_1:
        if id_ in matching_1[keys]:

            currentimg = tuple([keys[3], keys[4]])
            matchings[currentimg] = matching_1[keys][id_]
    return matching_1, matchings







def TwoViews():
    matching_1, matchings= FindMatchings('./P3Data/matching1.txt',"2" )


    #Now choose 8 correspondances
    #img1 needs 8 and its corresponding image, (lets say 2)
    #FundamentalMatrix = EstimateFundamentalMatrix(matching_1)
    F = GetInlierRANSAC(matching_1, "2")
    #print("Final F ", F.getF())
    Essential = EssentialMatrixFromFundamentalMatrix(F.getF())
    K = Essential.getK() # instrinsic parameters
    #print("Essential Matrix ", Essential.getEssential())

    #Get camera poses
    CameraPoses = ExtractCameraPose(Essential.getEssential()).getCameraPoses()
    #print("Camera Poses ", CameraPoses)


    allworldpts = []
    for i in range(len(CameraPoses)):
        print("new Camera pose", CameraPoses[i])
        w= LinearTriangulation(K, CameraPoses[i], matching_1, "2")
        worldpoints = w.getWorldPoints()

        allworldpts.append(worldpoints)


    removeCameraPose = DisambiguateCameraPose(K, CameraPoses, allworldpts)
    bestCP, allpts = removeCameraPose.getbestCP()

    #print("best CP ", bestCP)
    #print("All World Points ", len(allpts))
    #print(worldpoints)

    nonlinear = NonlinearTriangulation(bestCP, allpts, K)
    optimized_worldX, imgToX= nonlinear.getWorld_pts()


    print("optimized world points ", optimized_worldX)
    return bestCP, imgToX, K



def get_N_images():
    

    CP, imgToX, K = TwoViews()

    print("===================================")
    print("starting to get n images")


    for i in range(3):

        print("Image " + str(i) + " ~~~~~~~~~~~~~~~~~~")


        iD = str(3 + i)

        print("image ID ", iD)
        matchings1, matching_2 = FindMatchings('./P3Data/matching2.txt',iD )
        pnp_ransac = PnPRANSAC(matching_2, imgToX, K)
        C, R, P = pnp_ransac.getPose()
        bestpts = pnp_ransac.getpts()
        pnp_non = NonlinearPnP(bestpts, C, R, P, K)
        C, R = pnp_non.getPose()

        print("NON LINEAR PNP NEW CAMERA RESULTS")
        print(C, R)

        w= LinearTriangulation(K, CP, matchings1, iD)
        worldpts = w.getWorldPoints()

        allpts = {}

        for pt in worldpts:


            world_pt = worldpts[pt]

            world_pt = world_pt / world_pt[3].reshape(-1,1)
            world_pt = world_pt[0][0:3]

        
            allpts[pt] = world_pt

  
        nonlinear = NonlinearTriangulation(CP, allpts, K)
        optimized_worldX, imgToWorld = nonlinear.getWorld_pts()

        print("non Linear Triangulation all world points of image ", iD, " ", optimized_worldX)



get_N_images()


       












#Now we have the the best Camera Pose, and Most Optimized Worldpoints
#So now we get the camera pose






