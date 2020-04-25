DATASET_DIR = '../Data/dataset/'
AUDIO_DIR = '../Data/dataset/'

# The length of shortest wav
N_SAMPLES = 800
# MINIMUIN_LENGTH = 400

# Parameters for fbank features
NUM_PREVIOUS_FRAME = 9
#NUM_PREVIOUS_FRAME = 13
NUM_NEXT_FRAME = 23

NUM_FRAMES = NUM_PREVIOUS_FRAME + NUM_NEXT_FRAME
USE_LOGSCALE = True
USE_DELTA = False
USE_SCALE = True
USE_ENERGY = False
SAMPLE_RATE = 16000
TRUNCATE_SOUND_FIRST_SECONDS = 0.5
FILTER_BANK = 64

TDNN_FBANK_FILTER = 23
CMVN = 'cmvnw'
VAD = True
NORMALIZE = True

# Paramters for Spectrogram
NUM_FFT = 512
NUM_FRAMES_SPECT = 300

# Parameters for VAD
VAD_ENERGY_THRESHOLD = 5.5
VAD_ENERGY_MEAN_SCALE = 0.5
VAD_PROPORTION_THRESHOLD = 0.12
VAD_FRAMES_CONTEXT = 2

#
DNN_FILTER = [0.00754443, 0.01200533, 0.01642858, 0.01972508, 0.02147102,
              0.0226888, 0.02469071, 0.02506242, 0.02584714, 0.026544,
              0.02744689, 0.02778561, 0.0288272, 0.02941703, 0.02986392,
              0.02941785, 0.02964678, 0.02946718, 0.03002279, 0.02958207,
              0.02994801, 0.02939642, 0.02953483, 0.02839124, 0.02855285,
              0.02796266, 0.02814863, 0.02748642, 0.02801614, 0.02749056,
              0.02747193, 0.02631736, 0.02615773, 0.0255265, 0.0258321,
              0.02544096, 0.02596661, 0.02555359, 0.02552891, 0.02462734,
              0.0247531, 0.02457665, 0.02512659, 0.02495774, 0.02543424,
              0.02510019, 0.0251669, 0.0244995, 0.02457104, 0.02447885,
              0.02504115, 0.02461394, 0.02525825, 0.02497334, 0.02470482,
              0.02371456, 0.02343372, 0.02306277, 0.02339805, 0.02276554,
              0.02315823, 0.02268941, 0.02241172, 0.02143822, 0.02147482,
              0.02109371, 0.02139363, 0.02079251, 0.02117723, 0.0205691,
              0.02046507, 0.01975423, 0.01990366, 0.01977469, 0.02047094,
              0.0199114, 0.02047737, 0.02007335, 0.02003213, 0.01925786,
              0.019457, 0.019261, 0.019761, 0.01930143, 0.01955818,
              0.01895796, 0.01901542, 0.0180656, 0.0182367, 0.01800973,
              0.01860644, 0.01828756, 0.0189565, 0.01867137, 0.01885242,
              0.01791786, 0.01838151, 0.01811256, 0.01885726, 0.01862201,
              0.01964463, 0.01930191, 0.01989467, 0.01923947, 0.01988874,
              0.01977481, 0.02087282, 0.02053996, 0.02158896, 0.02121622,
              0.02174318, 0.02079145, 0.0215099, 0.02139695, 0.02233053,
              0.02206058, 0.02311639, 0.02285545, 0.0233136, 0.02231173,
              0.02337892, 0.02316566, 0.02410961, 0.02363132, 0.0246225,
              0.02399185, 0.02440539, 0.02356056, 0.02411388, 0.02374618,
              0.02446622, 0.02371911, 0.02471249, 0.02384905, 0.02423068,
              0.02286158, 0.02348385, 0.02281719, 0.02363081, 0.0226122,
              0.02335403, 0.02261329, 0.02296318, 0.02155136, 0.02207833,
              0.02116796, 0.02185807, 0.0204712, 0.02089286, 0.01970987,
              0.01964203, 0.01815534, 0.01857068, 0.01795201, 0.01873097,
              0.01793163, 0.01839271, 0.01749192, 0.01760474, 0.01468716,
              0.01088171]

# 2020 4 24 soft 4.37
VOX_FILTER = [0.00570303, 0.00939937, 0.01203585, 0.01391259, 0.01382084,
              0.01364415, 0.01416829, 0.01362097, 0.01296229, 0.01257852,
              0.01229255, 0.01188666, 0.01138058, 0.01086876, 0.01055123,
              0.01032323, 0.00985663, 0.00947784, 0.00923412, 0.00902301,
              0.0086822, 0.00832081, 0.00807913, 0.00793588, 0.00774215,
              0.00770259, 0.00763482, 0.00764003, 0.00761247, 0.00768839,
              0.00765249, 0.00763313, 0.00748619, 0.00743761, 0.00734098,
              0.00734422, 0.00720801, 0.00717585, 0.00707383, 0.00720071,
              0.00711014, 0.00723078, 0.00724596, 0.00745671, 0.0073872,
              0.00753253, 0.00749936, 0.00759182, 0.00742777, 0.00744372,
              0.00732293, 0.00734428, 0.00715304, 0.00707854, 0.00687955,
              0.00684789, 0.0066003, 0.0065191, 0.00639582, 0.00641725,
              0.00627491, 0.00627223, 0.00614685, 0.00619729, 0.00607931,
              0.00612942, 0.00605115, 0.00616204, 0.00606613, 0.00610238,
              0.00601645, 0.00609737, 0.005949, 0.00601728, 0.00592563,
              0.00602567, 0.00587893, 0.00590294, 0.00575652, 0.00581599,
              0.00566053, 0.00566695, 0.00554534, 0.0056292, 0.00545874,
              0.00545373, 0.00531324, 0.00532464, 0.00514361, 0.00514108,
              0.0050164, 0.0050615, 0.00492668, 0.004922, 0.00479529,
              0.00482669, 0.00468056, 0.00471658, 0.00463719, 0.0047175,
              0.00461473, 0.0046389, 0.00454612, 0.00462528, 0.00451879,
              0.00457309, 0.00450546, 0.0046014, 0.00450672, 0.00456469,
              0.00449741, 0.00458829, 0.00448197, 0.00454503, 0.00449609,
              0.00462914, 0.00453534, 0.00461707, 0.00453455, 0.0046176,
              0.0045107, 0.0045757, 0.00452146, 0.00461045, 0.00451514,
              0.00456493, 0.00446798, 0.00453265, 0.00443338, 0.00446365,
              0.00439844, 0.00445834, 0.0043308, 0.00434389, 0.00424731,
              0.00427338, 0.0041243, 0.00413044, 0.00402014, 0.00406023,
              0.00393848, 0.00393662, 0.00385043, 0.00388435, 0.00376469,
              0.00379182, 0.0037281, 0.00379813, 0.003692, 0.00370631,
              0.00363398, 0.00366177, 0.00352356, 0.00347584, 0.00337838,
              0.00342646, 0.00339417, 0.003411, 0.00353147, 0.00348524,
              0.00284462]

# mean_weight
# TIMIT_FIlTER = [0.00438871, 0.01160961, 0.00957214, 0.01141842, 0.01001372,
#                 0.01003338, 0.00932224, 0.00917608, 0.00769265, 0.00793429,
#                 0.00655623, 0.00723177, 0.00651865, 0.00641746, 0.00593072,
#                 0.00692516, 0.0062521, 0.00656339, 0.00585565, 0.00647662,
#                 0.00551753, 0.00578098, 0.0053743, 0.00613742, 0.00546302,
#                 0.00605668, 0.00547354, 0.0060053, 0.00521483, 0.00586652,
#                 0.0053714, 0.00593993, 0.00526677, 0.00576459, 0.00511302,
#                 0.00556865, 0.0049147, 0.00545784, 0.0049947, 0.00563289,
#                 0.00513415, 0.00573856, 0.00520307, 0.00579096, 0.00519562,
#                 0.00577502, 0.00528196, 0.00583518, 0.00539886, 0.00589751,
#                 0.00527434, 0.00575686, 0.0053225, 0.00560838, 0.0052121,
#                 0.00584799, 0.00545013, 0.00592394, 0.00546769, 0.00610077,
#                 0.00549983, 0.00599317, 0.005605, 0.00624946, 0.0058025,
#                 0.00640206, 0.00580106, 0.00640739, 0.00589833, 0.0062511,
#                 0.00573257, 0.00637377, 0.00604299, 0.0064972, 0.00593189,
#                 0.00647808, 0.00603195, 0.00629374, 0.00580848, 0.00644126,
#                 0.00609148, 0.0064778, 0.0058325, 0.00647128, 0.00583835,
#                 0.00614009, 0.00572108, 0.00642075, 0.00600638, 0.00635413,
#                 0.00572564, 0.00643374, 0.00588593, 0.00608729, 0.00566962,
#                 0.00626002, 0.00591399, 0.00637217, 0.00575651, 0.00624367,
#                 0.00572105, 0.0061001, 0.00571627, 0.00630855, 0.00588308,
#                 0.00644777, 0.00587655, 0.00656378, 0.00594684, 0.00628707,
#                 0.00591668, 0.00659803, 0.0062303, 0.00676784, 0.00605407,
#                 0.0067257, 0.00608058, 0.0065976, 0.00617009, 0.0068267,
#                 0.00654335, 0.00717557, 0.00646952, 0.00714041, 0.00646003,
#                 0.00702034, 0.00655731, 0.00710213, 0.00664681, 0.00714033,
#                 0.00646539, 0.00701774, 0.0064717, 0.00685962, 0.00653114,
#                 0.00703848, 0.00654586, 0.00698199, 0.0063195, 0.00677797,
#                 0.00628652, 0.00662829, 0.00633496, 0.00677041, 0.00621359,
#                 0.00677706, 0.00623519, 0.00651487, 0.00581428, 0.00598001,
#                 0.00562069, 0.0060354, 0.00554316, 0.00575794, 0.00506065,
#                 0.00522674, 0.00458464, 0.00532818, 0.00480734, 0.00446642,
#                 0.00266636]

# mean*var

# mean*var
# TIMIT_FIlTER = [2.77643060e-03, 1.98896174e-02, 3.42867883e-02,
#                 4.51870618e-02, 1.90287045e-02, 2.92933598e-02,
#                 1.86277036e-02, 1.69996561e-02, 8.86331312e-03,
#                 1.10660632e-02, 5.23648597e-03, 7.25722097e-03,
#                 6.05573526e-03, 7.36543701e-03, 4.50031598e-03,
#                 5.93682774e-03, 5.78684878e-03, 6.72088660e-03,
#                 6.02830285e-03, 6.24044236e-03, 5.71631979e-03,
#                 5.98614762e-03, 4.73157141e-03, 5.74332915e-03,
#                 5.03369319e-03, 4.95623078e-03, 4.66374780e-03,
#                 5.63057416e-03, 4.20044349e-03, 5.33054320e-03,
#                 3.80932097e-03, 4.95671362e-03, 3.74472644e-03,
#                 4.24244694e-03, 3.52848215e-03, 4.01947276e-03,
#                 3.40083888e-03, 4.39937774e-03, 3.31252515e-03,
#                 4.08231968e-03, 3.50945487e-03, 4.05944620e-03,
#                 3.72098973e-03, 4.45009662e-03, 3.83633327e-03,
#                 4.82810563e-03, 3.62344322e-03, 4.82946698e-03,
#                 3.96127306e-03, 4.35678983e-03, 3.77780618e-03,
#                 4.68471952e-03, 3.93933574e-03, 4.73766830e-03,
#                 3.89077878e-03, 4.89638441e-03, 4.20723951e-03,
#                 4.66283068e-03, 4.54409201e-03, 5.43961663e-03,
#                 4.61786763e-03, 5.73999666e-03, 4.68665269e-03,
#                 6.14184844e-03, 5.00949008e-03, 5.67663715e-03,
#                 5.11996302e-03, 6.03817993e-03, 4.82290427e-03,
#                 6.19803030e-03, 5.04806493e-03, 6.27445871e-03,
#                 5.19817199e-03, 5.81290406e-03, 5.33157695e-03,
#                 6.20467412e-03, 5.13523346e-03, 5.94020480e-03,
#                 5.11774981e-03, 6.39134760e-03, 5.57069154e-03,
#                 5.63769799e-03, 5.32310609e-03, 6.11908943e-03,
#                 5.57429707e-03, 6.15559740e-03, 5.13826538e-03,
#                 6.03561376e-03, 5.39338171e-03, 5.53374348e-03,
#                 5.28221106e-03, 5.62662925e-03, 5.16505301e-03,
#                 5.53848687e-03, 4.89586816e-03, 5.33022539e-03,
#                 5.12275675e-03, 5.18000222e-03, 5.22313559e-03,
#                 5.14394183e-03, 4.87753903e-03, 5.31029705e-03,
#                 4.85239835e-03, 5.20427379e-03, 5.12107655e-03,
#                 5.27451772e-03, 5.21348536e-03, 5.08431262e-03,
#                 5.17174247e-03, 5.71294151e-03, 4.92983845e-03,
#                 5.13292088e-03, 5.43107603e-03, 5.70531115e-03,
#                 5.48478938e-03, 5.34379406e-03, 5.45773281e-03,
#                 6.21192151e-03, 5.72607993e-03, 5.81929336e-03,
#                 6.21005322e-03, 6.62421846e-03, 6.48872460e-03,
#                 6.31716231e-03, 6.46044940e-03, 7.56665620e-03,
#                 6.66391035e-03, 6.68647691e-03, 6.90446647e-03,
#                 7.21501882e-03, 7.42602830e-03, 7.04122812e-03,
#                 6.99086300e-03, 7.52130021e-03, 7.08828744e-03,
#                 7.00755886e-03, 7.54466491e-03, 7.15606564e-03,
#                 6.86481160e-03, 6.42855192e-03, 6.37753335e-03,
#                 7.04692112e-03, 6.80428648e-03, 6.30332739e-03,
#                 5.94593403e-03, 5.82118985e-03, 6.20576354e-03,
#                 5.69333014e-03, 5.14761456e-03, 5.55510863e-03,
#                 4.05103578e-03, 4.31842729e-03, 4.12763804e-03,
#                 4.16651241e-03, 3.20842839e-03, 2.52618037e-03,
#                 1.89161734e-03, 2.05014781e-03, 1.95110484e-03,
#                 1.38583119e-03, 6.25800553e-05]

# var
TIMIT_FIlTER = [0.00385497, 0.01409909, 0.02044194, 0.02400406, 0.01274147,
                0.01762282, 0.01329654, 0.01250353, 0.00760603, 0.00893792,
                0.00562884, 0.00691985, 0.00592911, 0.00682357, 0.0051223,
                0.00628589, 0.00598721, 0.00662981, 0.00617779, 0.00644716,
                0.00596013, 0.00629679, 0.00535042, 0.00611746, 0.00550035,
                0.00557303, 0.00537693, 0.00605216, 0.00488729, 0.00587671,
                0.00467616, 0.00565372, 0.00459269, 0.00505737, 0.00450426,
                0.00494333, 0.0043191, 0.00522964, 0.0042799, 0.00495049,
                0.00438412, 0.00491352, 0.00460433, 0.00518662, 0.00461919,
                0.00552181, 0.0045252, 0.00550929, 0.00473413, 0.00514666,
                0.00471065, 0.00546784, 0.00476059, 0.00545187, 0.00475387,
                0.00557329, 0.00494034, 0.00537339, 0.00529525, 0.00604731,
                0.00525623, 0.00622191, 0.00543044, 0.00652253, 0.00557333,
                0.00614883, 0.00578026, 0.00648796, 0.0054595, 0.00659273,
                0.00572557, 0.0066274, 0.00574022, 0.00628397, 0.00592509,
                0.00659834, 0.00568892, 0.00636838, 0.00574542, 0.00670719,
                0.00599993, 0.00615498, 0.00591648, 0.00656457, 0.00602737,
                0.00654237, 0.00576812, 0.00650299, 0.00586128, 0.00605236,
                0.00589436, 0.00621064, 0.00570947, 0.00608731, 0.0056009,
                0.00597072, 0.00568442, 0.00582786, 0.00584172, 0.00581629,
                0.00542271, 0.00582412, 0.00550578, 0.00584896, 0.00561535,
                0.00580499, 0.00579486, 0.0057384, 0.00562342, 0.00613032,
                0.0055908, 0.00579379, 0.00584061, 0.00616005, 0.00603102,
                0.00596581, 0.00585685, 0.00643737, 0.00606006, 0.00616503,
                0.0063246, 0.00672406, 0.00672505, 0.00664977, 0.00651122,
                0.00735204, 0.00677516, 0.0068726, 0.00685444, 0.00710337,
                0.00725978, 0.00705254, 0.00678782, 0.00723298, 0.00690913,
                0.00688477, 0.00711287, 0.00696053, 0.00688649, 0.00668611,
                0.00644867, 0.00693465, 0.0067243, 0.00649216, 0.00611712,
                0.00615464, 0.00633753, 0.00605202, 0.0055625, 0.00600235,
                0.00484857, 0.00508374, 0.00472899, 0.00487364, 0.0040965,
                0.00346418, 0.00276751, 0.0029077, 0.00255249, 0.00198912,
                0.00029049]

# 2020 4 24
LIBRI_FILTER = [0.00704546, 0.00543752, 0.00785011, 0.0063976, 0.00812723,
                0.00618142, 0.00802173, 0.00618615, 0.00767452, 0.0057291,
                0.0071284, 0.00575854, 0.00787357, 0.00603028, 0.00810531,
                0.00616736, 0.00772087, 0.00599237, 0.00834553, 0.00658158,
                0.00783094, 0.00573386, 0.0074456, 0.00595703, 0.00736949,
                0.00548685, 0.00740053, 0.00612626, 0.00769291, 0.0056949,
                0.00724305, 0.0057307, 0.00731674, 0.00551271, 0.00721512,
                0.00589398, 0.0075366, 0.00562215, 0.00711141, 0.00562279,
                0.00724366, 0.00540575, 0.00700809, 0.00569686, 0.00744983,
                0.00566074, 0.0071555, 0.00558114, 0.00711885, 0.00545947,
                0.00715292, 0.00574997, 0.00745407, 0.00562065, 0.00706585,
                0.00551157, 0.00706268, 0.00541217, 0.006952, 0.00566279,
                0.00750916, 0.00563019, 0.00688875, 0.00539278, 0.00704609,
                0.00537139, 0.00697231, 0.00557542, 0.00716211, 0.00551102,
                0.00713285, 0.00560747, 0.00706011, 0.00527911, 0.00683334,
                0.00556237, 0.00725048, 0.00551789, 0.0068204, 0.00531218,
                0.00683559, 0.00520779, 0.00675734, 0.00551115, 0.00710459,
                0.00545066, 0.0067643, 0.00528851, 0.00665119, 0.00503373,
                0.0065056, 0.00528035, 0.00680203, 0.005214, 0.00649112,
                0.0051294, 0.00653575, 0.00499618, 0.0063938, 0.00522532,
                0.00675656, 0.00509456, 0.00627122, 0.00499575, 0.00648396,
                0.00509251, 0.00662391, 0.0054026, 0.0069453, 0.00537497,
                0.0067164, 0.00537297, 0.00700325, 0.00539775, 0.00682029,
                0.00563387, 0.00727441, 0.00562134, 0.00689839, 0.00549582,
                0.00719652, 0.00562228, 0.00698442, 0.00567715, 0.00739354,
                0.00578919, 0.00698804, 0.00542698, 0.00686931, 0.00535288,
                0.00680297, 0.00551015, 0.00704394, 0.00550754, 0.00665815,
                0.00523983, 0.00672577, 0.00526327, 0.00636751, 0.00514745,
                0.00671402, 0.00522509, 0.00629304, 0.00497595, 0.00636717,
                0.00503406, 0.00634701, 0.00522852, 0.00690434, 0.00534711,
                0.00632189, 0.00490145, 0.00569841, 0.00457853, 0.00616267,
                0.00525095, 0.00653267, 0.004737, 0.004293, 0.00313822,
                0.00316953]


# TIMIT_FIlTER = [0.00023661, 0.01669825, 0.02125655, 0.02627175, 0.01751978,
#                 0.02091466, 0.01601569, 0.01508592, 0.01005613, 0.01154809,
#                 0.00501273, 0.00709499, 0.00669917, 0.00819075, 0.00385591,
#                 0.0049142, 0.00560719, 0.00704817, 0.00608785, 0.00547906,
#                 0.00556113, 0.00545453, 0.00400463, 0.00511243, 0.00450075,
#                 0.003991, 0.00323734, 0.00452368, 0.00330588, 0.00429099,
#                 0.00241071, 0.00295584, 0.00204205, 0.00223633, 0.00126788,
#                 0.00162129, 0.00137238, 0.0021811, 0.00122526, 0.00174958,
#                 0.0016026, 0.00217564, 0.00218022, 0.00297162, 0.00273184,
#                 0.00339905, 0.0026015, 0.00352932, 0.00322493, 0.00314407,
#                 0.00233214, 0.00304625, 0.00295879, 0.00339754, 0.00292505,
#                 0.00360743, 0.003755, 0.00369849, 0.00373958, 0.00433877,
#                 0.00439785, 0.00507664, 0.00467313, 0.00523916, 0.00531578,
#                 0.00523321, 0.00491371, 0.00513935, 0.0048346, 0.00539471,
#                 0.0053772, 0.00593623, 0.00624347, 0.00592501, 0.00565248,
#                 0.00595077, 0.00608898, 0.0059869, 0.00564812, 0.00582707,
#                 0.00632508, 0.00601213, 0.00570106, 0.00581659, 0.0059829,
#                 0.00599994, 0.00574064, 0.00559464, 0.00603581, 0.00579266,
#                 0.00546322, 0.00548659, 0.00573457, 0.00576936, 0.00549532,
#                 0.00513439, 0.00560857, 0.00543168, 0.00498894, 0.00494378,
#                 0.00515174, 0.00564291, 0.00541211, 0.00495206, 0.00528614,
#                 0.00560756, 0.00553618, 0.00554504, 0.00552215, 0.00593071,
#                 0.00605203, 0.00582979, 0.0061642, 0.0063893, 0.0059803,
#                 0.00582385, 0.00613368, 0.00695021, 0.00729953, 0.00688198,
#                 0.00729623, 0.008301, 0.00835363, 0.00808782, 0.00781258,
#                 0.00879345, 0.00953409, 0.00860236, 0.00864163, 0.00972668,
#                 0.01001589, 0.00976134, 0.00942435, 0.01032801, 0.01045107,
#                 0.00999452, 0.00996147, 0.01058146, 0.01009149, 0.00976301,
#                 0.00882807, 0.00978413, 0.01081803, 0.01038582, 0.00894065,
#                 0.00899766, 0.00845226, 0.00926698, 0.00817182, 0.00765828,
#                 0.00768802, 0.00539208, 0.00614423, 0.00657554, 0.00587436,
#                 0.00346217, 0.0020781, 0.00061639, 0.00148055, 0.00293487,
#                 0.00092614]
