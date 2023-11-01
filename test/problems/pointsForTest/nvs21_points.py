import numpy as np

test_points = np.array([[0.15, 47, 1, 0, -668.1443454],
                        [0.15, 3, 2, 2, 0.1261120837],
                        [0.15, 194, 3, 1, 0.1204441584],
                        [0.15, 20, 4, 2, 498.2205777],
                        [0.15, 69, 4, 0, -641.7735045],
                        [0.15, 9, 6, 2, 30.64523634],
                        [0.15, 55, 6, 2, 42740.9031882614],
                        [0.15, 56, 6, 0, -630.1001114],
                        [0.15, 85, 6, 2, 243819.614451662],
                        [0.15, 87, 6, 1, -0.05775216264],
                        [0.15, 72, 8, 2, 167363.850752093],
                        [0.15, 39, 13, 2, 23412.2669501776],
                        [0.15, 76, 13, 0, -561.6686275],
                        [0.15, 186, 13, 1, 0.1092045058],
                        [0.15, 196, 15, 1, 0.1232176685],
                        [0.15, 182, 16, 1, 0.1034940191],
                        [0.15, 96, 17, 2, 1124023.88653258],
                        [0.15, 186, 19, 0, -415.8745478],
                        [0.15, 192, 20, 0, -397.8718708],
                        [0.15, 7, 21, 2, 39.25121835],
                        [0.15, 18, 23, 2, 1879.57449575105],
                        [0.15, 70, 23, 2, 429894.296248501],
                        [0.15, 134, 23, 1, 0.02933023543],
                        [0.15, 109, 25, 0, -413.9923373],
                        [0.15, 47, 28, 1, -0.1534816391],
                        [0.15, 10, 29, 1, -0.2965255129],
                        [0.15, 26, 29, 0, -527.1284341],
                        [0.15, 140, 30, 0, -320.035213],
                        [0.15, 118, 31, 0, -338.2538048],
                        [0.15, 121, 31, 1, 0.007028168083],
                        [0.15, 27, 34, 0, -498.3308176],
                        [0.15, 95, 35, 1, -0.04150827824],
                        [0.15, 124, 36, 0, -274.1209659],
                        [0.15, 92, 37, 2, 2063453.66114363],
                        [0.15, 115, 37, 2, 5037728.66490144],
                        [0.15, 158, 37, 0, -209.9172117],
                        [0.15, 140, 38, 0, -225.3779365],
                        [0.15, 28, 41, 2, 19618.1327540185],
                        [0.15, 141, 41, 0, -188.1519744],
                        [0.15, 39, 42, 0, -412.7100841],
                        [0.15, 74, 45, 2, 1050463.77304565],
                        [0.15, 50, 46, 1, -0.1451387212],
                        [0.15, 25, 47, 0, -440],
                        [0.15, 149, 47, 1, 0.05375786614],
                        [0.15, 65, 48, 1, -0.1067501001],
                        [0.15, 43, 49, 2, 130410.208510086],
                        [0.15, 54, 49, 2, 324349.18146243],
                        [0.15, 68, 52, 1, -0.09962561155],
                        [0.15, 76, 52, 1, -0.08136113968],
                        [0.15, 35, 54, 1, -0.1898712153],
                        [0.15, 195, 54, 0, 79.06896236],
                        [0.15, 41, 55, 1, -0.1710080646],
                        [0.15, 1, 56, 1, -0.3802701665],
                        [0.15, 190, 61, 0, 165.8269739],
                        [0.15, 109, 62, 1, -0.01464866762],
                        [0.15, 9, 63, 1, -0.3028104996],
                        [0.15, 32, 63, 2, 51425.9294492028],
                        [0.15, 98, 63, 0, -51.33181899],
                        [0.15, 109, 63, 1, -0.01464866762],
                        [0.15, 58, 64, 1, -0.1240423759],
                        [0.15, 19, 66, 2, 6695.76227726211],
                        [0.15, 78, 66, 1, -0.07694737247],
                        [0.15, 127, 69, 0, 102.5905092],
                        [0.15, 36, 70, 1, -0.1866209992],
                        [0.15, 4, 73, 0, -529],
                        [0.15, 50, 73, 2, 355176.778993134],
                        [0.15, 34, 74, 2, 76981.9796028714],
                        [0.15, 52, 74, 0, -141.3784112],
                        [0.15, 193, 75, 0, 366.9332992],
                        [0.15, 16, 78, 0, -363],
                        [0.15, 8, 82, 0, -443.0689758],
                        [0.15, 73, 83, 0, 34.15231086],
                        [0.15, 18, 84, 0, -318.6181823],
                        [0.15, 45, 86, 1, -0.1591923789],
                        [0.15, 56, 86, 2, 658403.674866573],
                        [0.15, 193, 86, 0, 519.7501831],
                        [0.15, 22, 89, 0, -257.5529974],
                        [0.15, 113, 89, 0, 271.0829773],
                        [0.15, 4, 90, 0, -495],
                        [0.15, 190, 90, 0, 565.5643877],
                        [0.15, 38, 94, 1, -0.1802532723],
                        [0.15, 168, 94, 0, 543.3792513],
                        [0.15, 28, 97, 0, -161.7242457],
                        [0.15, 42, 97, 1, -0.168001992],
                        [0.15, 37, 99, 2, 144438.768793777],
                        [0.15, 45, 100, 1, -0.1591923789],
                        [0.15, 18, 105, 0, -229.5227279],
                        [0.15, 113, 110, 0, 494.3160394],
                        [0.15, 17, 116, 2, 7542.15340703808],
                        [0.15, 116, 119, 0, 606.6692241],
                        [0.15, 102, 124, 0, 577.3386124],
                        [0.15, 47, 137, 0, 264.2246803],
                        [0.15, 1, 139, 0, -536],
                        [0.15, 10, 140, 0, -232.2811276],
                        [0.15, 88, 140, 0, 638.3164128],
                        [0.15, 13, 143, 1, -0.2793575996],
                        [0.15, 197, 143, 0, 1332.1006452094],
                        [0.15, 165, 144, 0, 1174.71349132778],
                        [0.15, 16, 145, 0, -95],
                        [0.15, 18, 148, 1, -0.2546832327],
                        [0.15, 167, 148, 0, 1237.58150153137],
                        [0.15, 138, 151, 0, 1098.84835879508],
                        [0.15, 123, 153, 0, 1021.85208548064],
                        [0.15, 16, 158, 2, 8060.81037001393],
                        [0.15, 13, 162, 1, -0.2793575996],
                        [0.15, 134, 163, 0, 1211.86141515481],
                        [0.15, 171, 173, 0, 1587.26855169761],
                        [0.15, 195, 174, 0, 1754.7777676158],
                        [0.15, 166, 175, 0, 1579.7172771769],
                        [0.15, 40, 178, 0, 450.770847],
                        [0.15, 80, 180, 0, 934.9689438],
                        [0.15, 120, 180, 0, 1296.8012070186],
                        [0.15, 94, 181, 0, 1079.86010838471],
                        [0.15, 34, 182, 0, 386.2332449],
                        [0.15, 38, 183, 0, 453.0877625],
                        [0.15, 12, 184, 2, 2970.19179575474],
                        [0.15, 62, 188, 0, 805.3134803],
                        [0.15, 49, 190, 0, 655],
                        [0.15, 65, 193, 0, 881.0157454],
                        [0.15, 73, 197, 0, 1008.16873782755],
                        [0.15, 163, 199, 0, 1865.66192162594],
                        [0.125, 118, 61, 0, -12.37039004],
                        [0.125, 119, 30, 2, 4275236.69622038],
                        [0.125, 121, 4, 0, -631],
                        [0.175, 122, 29, 1, 0.04306060209],
                        [0.175, 124, 35, 1, 0.04683258795],
                        [0.125, 125, 16, 2, 2775946.54333],
                        [0.125, 127, 24, 0, -404.5337359],
                        [0.125, 128, 14, 1, -0.019],
                        [0.125, 129, 45, 2, 8855690.27651637],
                        [0.125, 130, 54, 1, -0.01588711259],
                        [0.125, 130, 41, 0, -207.5280757],
                        [0.125, 131, 53, 0, -68.38727346],
                        [0.175, 139, 56, 0, -14.76973714],
                        [0.175, 139, 52, 1, 0.07420381183],
                        [0.175, 139, 10, 0, -557.1017388],
                        [0.125, 142, 15, 0, -496.2543707],
                        [0.125, 143, 13, 0, -519.5426103],
                        [0.1125, 143, 12, 2, 3382966.63527561],
                        [0.1125, 144, 56, 2, 16233430.799768],
                        [0.125, 150, 48, 0, -87.12246173],
                        [0.125, 150, 42, 0, -160.607154],
                        [0.1125, 148, 2, 0, -650.6689499],
                        [0.1125, 148, 27, 0, -346.5308234],
                        [0.1125, 150, 36, 1, -0.008208081871],
                        [0.1125, 151, 32, 0, -281.7774167],
                        [0.1125, 151, 49, 2, 17174187.0185926],
                        [0.125, 160, 39, 0, -181.684685],
                        [0.175, 162, 48, 0, -64.05974105],
                        [0.125, 163, 21, 0, -406.889948],
                        [0.175, 164, 40, 1, 0.1167238094],
                        [0.10625, 159, 13, 0, -511.0762372],
                        [0.175, 169, 34, 0, -233],
                        [0.1125, 163, 25, 1, 0.009223072709],
                        [0.175, 171, 46, 0, -73.47194579],
                        [0.1875, 119, 57, 1, 0.05336109069],
                        [0.125, 174, 20, 0, -411.1818808],
                        [0.10625, 165, 28, 1, -0.0002966443889],
                        [0.1875, 120, 3, 1, 0.05534164903],
                        [0.1125, 168, 21, 1, 0.01574130239],
                        [0.125, 178, 12, 0, -514.9000312],
                        [0.125, 178, 19, 0, -421.5083828],
                        [0.1125, 170, 38, 1, 0.01832139211],
                        [0.10625, 167, 28, 0, -313.1602565],
                        [0.103125, 166, 1, 0, -662.1159013],
                        [0.1587608017, 118, 33, 1, 0.01382530654],
                        [0.158756117, 119, 2, 1, 0.01564902998],
                        [0.125, 184, 43, 1, 0.06058315233],
                        [0.125, 185, 43, 0, -90.13676812],
                        [0.1588279602, 121, 37, 0, -268],
                        [0.103125, 171, 2, 1, 0.0009330303751],
                        [0.10625, 173, 39, 0, -162.0350889],
                        [0.1125, 177, 23, 1, 0.02723424342],
                        [0.175, 187, 12, 1, 0.1530576894],
                        [0.1125, 178, 40, 0, -141.3334374],
                        [0.1015625, 172, 27, 0, -320.8983197],
                        [0.1331391658, 146, 15, 0, -493.7543104]])