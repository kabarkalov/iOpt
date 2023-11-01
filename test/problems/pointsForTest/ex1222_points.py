import numpy as np

test_points = np.array([[0.600390625, -1.612171592, 0, 0, 0.1197640363],
                        [0.600390625, -1.612171592, 1, 0, 0.1197640363],
                        [0.999609375, -1.613368408, 1, 0, -0.6113033381],
                        [0.999609375, -1.613368408, 1, 1, 0.4866315918],
                        [0.200390625, -1.612171592, 0, 0, 0.6117808905],
                        [0.200390625, -1.612171592, 1, 0, 0.6117808905],
                        [0.999609375, -1.613368408, 0, 0, -0.6113033381],
                        [0.999609375, -1.613368408, 0, 1, -0.6133684082],
                        [0.999609375, -1.613368408, 0, 2, 0.999609375],
                        [0.799609375, -1.919753408, 0, 0, 0.09834623397],
                        [0.800390625, -1.305786592, 0, 0, -0.5170441128],
                        [0.800390625, -1.305786592, 0, 1, -0.3057865918],
                        [0.800390625, -1.305786592, 0, 2, 0.800390625],
                        [0.600390625, -1.305786592, 0, 0, -0.1866209637],
                        [0.600390625, -1.305786592, 0, 1, -0.3057865918],
                        [0.600390625, -1.305786592, 0, 2, 0.600390625],
                        [0.800390625, -2.224941592, 0, 0, 0.4021108872],
                        [0.700390625, -1.458979092, 0, 0, -0.1903863365],
                        [0.700390625, -1.458979092, 0, 1, -0.4589790918],
                        [0.700390625, -1.458979092, 0, 2, 0.700390625],
                        [0.400390625, -1.918556592, 0, 0, 0.69667663],
                        [0.400390625, -1.918556592, 1, 0, 0.69667663],
                        [0.443359375, -1.220812627, 1, 0, -0.0547143073],
                        [0.443359375, -1.220812627, 1, 1, 0.879187373],
                        [0.443359375, -1.220812627, 0, 0, -0.0547143073],
                        [0.443359375, -1.220812627, 0, 1, -0.220812627],
                        [0.443359375, -1.220812627, 0, 2, 0.443359375],
                        [0.293359375, -1.230387158, 0, 0, 0.1325309517],
                        [0.550390625, -1.449404561, 0, 0, 0.02978258041],
                        [0.378515625, -1.032912451, 0, 0, -0.1625291107],
                        [0.378515625, -1.032912451, 0, 1, -0.03291245117],
                        [0.378515625, -1.032912451, 0, 2, 0.378515625],
                        [0.271484375, -1.067620127, 0, 0, -0.006481240783],
                        [0.271484375, -1.067620127, 0, 1, -0.06762012695],
                        [0.271484375, -1.067620127, 0, 2, 0.271484375],
                        [0.214453125, -1.164562256, 0, 0, 0.1500041794],
                        [0.204296875, -1.077194658, 0, 0, 0.0728885384],
                        [0.462109375, -1.505654932, 0, 0, 0.2059862457],
                        [0.799609375, -1.919753408, 1, 0, 0.09834623397],
                        [0.800390625, -2.224941592, 1, 0, 0.4021108872],
                        [0.800390625, -1.305786592, 1, 0, -0.5170441128],
                        [0.800390625, -1.305786592, 1, 1, 0.7942134082],
                        [0.900390625, -2.071749092, 1, 0, 0.05720960852],
                        [0.999609375, -2.072945908, 1, 0, -0.1517258381],
                        [0.999609375, -2.072945908, 1, 1, 0.0270540918],
                        [0.950390625, -1.995152842, 1, 0, -0.1226742895],
                        [0.950390625, -1.995152842, 1, 1, 0.1048471582],
                        [0.949609375, -2.149542158, 1, 0, 0.03336893323],
                        [0.900390625, -2.071749092, 0, 0, 0.05720960852],
                        [0.999609375, -2.072945908, 0, 0, -0.1517258381],
                        [0.999609375, -2.072945908, 0, 1, -1.072945908],
                        [0.999609375, -2.072945908, 0, 2, 0.999609375],
                        [0.237109375, -1.024534736, 0, 0, -0.01327178839],
                        [0.237109375, -1.024534736, 0, 1, -0.02453473633],
                        [0.237109375, -1.024534736, 0, 2, 0.237109375],
                        [0.950390625, -2.224941592, 1, 0, 0.1071144605],
                        [0.949609375, -2.072945908, 1, 0, -0.04322731677],
                        [0.949609375, -2.072945908, 1, 1, 0.0270540918],
                        [0.205859375, -1.032912451, 0, 0, 0.02703587646],
                        [0.400390625, -2.224941592, 0, 0, 1.00306163],
                        [0.400390625, -2.224941592, 1, 0, 1.00306163],
                        [0.216015625, -1.000598408, 0, 0, -0.01554615434],
                        [0.216015625, -1.000598408, 0, 1, -0.0005984082031],
                        [0.216015625, -1.000598408, 0, 2, 0.216015625],
                        [0.450390625, -1.332116553, 0, 0, 0.04758946564],
                        [0.516015625, -1.369217861, 0, 0, -0.002433826188],
                        [0.516015625, -1.369217861, 0, 1, -0.3692178613],
                        [0.516015625, -1.369217861, 0, 2, 0.516015625],
                        [0.924609375, -2.111244033, 1, 0, 0.04731931132],
                        [0.202734375, -1.005385674, 0, 0, 0.002647557015],
                        [0.578515625, -1.032912451, 0, 0, -0.4272031698],
                        [0.578515625, -1.032912451, 0, 1, -0.03291245117],
                        [0.578515625, -1.032912451, 0, 2, 0.578515625],
                        [0.621484375, -2.054993662, 0, 0, 0.5307712673],
                        [0.658984375, -2.027466885, 1, 0, 0.4450009082],
                        [0.544921875, -1.578660732, 0, 0, 0.1667811202],
                        [0.975390625, -2.186643467, 1, 0, 0.01520328644],
                        [0.999609375, -2.187840283, 1, 0, -0.03683146314],
                        [0.999609375, -2.187840283, 1, 1, -0.0878402832],
                        [0.999609375, -2.187840283, 1, 2, -0.200390625],
                        [0.999609375, -2.187840283, 1, 3, -3.634152568],
                        [0.987109375, -2.206989346, 1, 0, 0.009952915631],
                        [0.987890625, -2.167494404, 1, 0, -0.03125913114],
                        [0.987890625, -2.167494404, 1, 1, -0.0674944043],
                        [0.987890625, -2.167494404, 1, 2, -0.212109375],
                        [0.987890625, -2.167494404, 1, 3, -3.592458393],
                        [0.987109375, -2.187840283, 1, 0, -0.009196146869],
                        [0.987109375, -2.187840283, 1, 1, -0.0878402832],
                        [0.987109375, -2.187840283, 1, 2, -0.212890625],
                        [0.987109375, -2.187840283, 1, 3, -3.589661069],
                        [0.414453125, -1.430255498, 0, 0, 0.1910714652],
                        [0.803515625, -2.017892354, 0, 0, 0.1893563932],
                        [0.803515625, -2.017892354, 1, 0, 0.1893563932],
                        [0.390234375, -1.317754756, 0, 0, 0.1082217071],
                        [0.226171875, -1.40631917, 0, 0, 0.3798018039],
                        [0.987890625, -2.224941592, 1, 0, 0.02618805636],
                        [0.975390625, -2.167494404, 1, 0, -0.003945776061],
                        [0.975390625, -2.167494404, 1, 1, -0.0674944043],
                        [0.975390625, -2.167494404, 1, 2, -0.224609375],
                        [0.975390625, -2.167494404, 1, 3, -3.547428843],
                        [0.924609375, -2.072945908, 1, 0, 0.009021186317],
                        [0.884765625, -1.923343857, 1, 0, -0.05996308607],
                        [0.884765625, -1.923343857, 1, 1, 0.1766561426],
                        [0.884765625, -1.923343857, 0, 0, -0.05996308607],
                        [0.884765625, -1.923343857, 0, 1, -0.9233438574],
                        [0.884765625, -1.923343857, 0, 2, 0.884765625],
                        [0.555078125, -1.51283583, 0, 0, 0.08654375108],
                        [0.713671875, -1.997546475, 1, 0, 0.3261292985],
                        [0.994140625, -2.173478486, 1, 0, -0.03906029272],
                        [0.994140625, -2.173478486, 1, 1, -0.07347848633],
                        [0.994140625, -2.173478486, 1, 2, -0.205859375],
                        [0.994140625, -2.173478486, 1, 3, -3.614756837],
                        [0.989453125, -2.184249834, 1, 0, -0.01794193928],
                        [0.989453125, -2.184249834, 1, 1, -0.08424983398],
                        [0.989453125, -2.184249834, 1, 2, -0.210546875],
                        [0.989453125, -2.184249834, 1, 3, -3.59804633],
                        [0.980859375, -2.197414814, 1, 0, 0.01406704046],
                        [0.371484375, -1.478128154, 0, 0, 0.2910625596],
                        [0.588671875, -1.570283018, 0, 0, 0.09526253675],
                        [0.917578125, -2.175872119, 1, 0, 0.1264084687],
                        [0.995703125, -2.20220208, 1, 0, -0.01379649307],
                        [0.995703125, -2.20220208, 1, 1, -0.1022020801],
                        [0.995703125, -2.20220208, 1, 2, -0.204296875],
                        [0.995703125, -2.20220208, 1, 3, -3.620309379],
                        [0.995703125, -2.195021182, 1, 0, -0.02097739151],
                        [0.995703125, -2.195021182, 1, 1, -0.09502118164],
                        [0.995703125, -2.195021182, 1, 2, -0.204296875],
                        [0.995703125, -2.195021182, 1, 3, -3.620309379]])