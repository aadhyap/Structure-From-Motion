#choose 8 correspondances between two images (1 and another image)
import numpy as np
import cv2 as cv2
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from scipy.spatial.transform import Rotation 
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
from BuildVisibilityMatrix import BuildVisibilityMatrix
from BundleAdjustment import BundleAdjustment





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
    return bestCP, imgToX, K, optimized_worldX



def get_N_images():

    filenames = ['./P3Data/matching2.txt', './P3Data/matching2.txt', './P3Data/matching2.txt', './P3Data/matching5.txt']
    

    CP, imgToX, K, optimized_worldX = TwoViews()
    Cset = [CP]

    print("===================================")
    print("starting to get n images")


    all_worldpts = optimized_worldX
    n_cameras = []
    for i in range(3):

        print("Image " + str(i) + " ~~~~~~~~~~~~~~~~~~")


        iD = str(3 + i)

        print("image ID ", iD)
        print("i ", i)
        matchings1, matching_2 = FindMatchings(filenames[i],iD )
        pnp_ransac = PnPRANSAC(matching_2, imgToX, K)
        C, R, P = pnp_ransac.getPose()
        bestpts = pnp_ransac.getpts()
        pnp_non = NonlinearPnP(bestpts, C, R, P, K)
        C, R = pnp_non.getPose()
        Cset.append([C,R])
        n_cameras.append([C,R])

        print("NON LINEAR PNP NEW CAMERA RESULTS")
        print(C, R)

        w= LinearTriangulation(K, CP, matchings1, iD)
        worldpts = w.getWorldPoints()

        allpts = {}

        camera_indices = []
        i = 0
        for pt in worldpts:

    
            i = i+ 1



            world_pt = worldpts[pt]

            world_pt = world_pt / world_pt[3].reshape(-1,1)
            world_pt = world_pt[0][0:3]

        
            allpts[pt] = world_pt

  
        nonlinear = NonlinearTriangulation(CP, allpts, K)
        optimized_world, imgToWorld = nonlinear.getWorld_pts()

        print("non Linear Triangulation all world points of image ", iD, " ", optimized_world)


        
        all_worldpts = np.append(all_worldpts, optimized_world, axis = 0)

        n = 9 * n_cameras + 3 * n_points
        m = 2 * points_2d.shape[0]


        BuildVisibilityMatrix vis = BuildVisibilityMatrix(matchings1, matching_2, imgToWorld)
        vis.bundle_adjustment_sparsity()

        A = vis.bundle_adjustment_sparsity(n_cameras, all_worldpts, camera_indices, point_indices)

        BundleAdjustment bun  = BundleAdjustment(camera_params, points_3d, n_cameras, n_points, camera_indices, point_indices, points_2d)
        C, R, allworldpts = bun.getPose()







    print("ALL World Points")
    print(all_worldpts)

    X = all_worldpts
    x = X[:,0]
    y = X[:,1]
    z = X[:,2]

    print(len(x))
    
    # 2D plotting
    fig = plt.figure(figsize = (10, 10))
    plt.xlim(-20,  20)
    plt.ylim(-10,  20)
    plt.scatter(x, z, marker='.',linewidths=0.5, color = 'green')
    for i in range(0, len(Cset)):
        euler = Rotation.from_matrix(Cset[i][1])
        R1 =  euler.as_rotvec()
        R1 = np.rad2deg(R1)
        plt.plot(Cset[i][0][0],Cset[i][0][2], marker=(3, 0, int(R1[1])), markersize=3, linestyle='None')
        
    plt.savefig('2D.png')
    plt.show()
  







get_N_images()


       












#Now we have the the best Camera Pose, and Most Optimized Worldpoints
#So now we get the camera pose






