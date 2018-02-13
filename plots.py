import matplotlib.pyplot as plt

num_cars_list = [0, 0, 128, 184, 227, 272, 306, 339, 372, 405, 441, 476, 515, 562, 593, 614, 640, 672, 706, 731, 756, 790, 814, 847, 901, 949, 1000, 1074, 1210, 1360, 1570, 1902, 2143, 2348, 2600, 2934, 3103, 3441, 3582, 3642, 3762, 3892, 3939, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000]
num_cars_list += [0, 0, 136, 179, 230, 271, 318, 346, 377, 420, 449, 483, 534, 568, 618, 655, 689, 725, 752, 795, 837, 870, 935, 999, 1059, 1132, 1296, 1473, 1786, 2121, 2547, 2860, 2975, 3072, 3310, 3600, 3789, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000]
num_cars_list += [0, 0, 114, 150, 203, 246, 286, 324, 369, 403, 439, 470, 506, 535, 574, 613, 648, 682, 718, 752, 814, 854, 890, 931, 1006, 1105, 1281, 1473, 1748, 2004, 2301, 2606, 3102, 3136, 3158, 3261, 3481, 3819, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000]
num_charge_list = []
time = list(range(53))*3

a = [0, 327,462, 578, 676, 775, 901, 1045, 1272, 1660]
a += [0, 346, 456, 573, 676, 775, 884, 998, 117, 1373]
a += [0, 329, 430, 531, 631, 712, 832, 960, 1146, 1457]
a_time = list(range(10))*3

orig_x = "Number of Iterations"
orig_y = "Number of Car Owners"

# held start time at probability of .1
const_start_ratio = [1, .323, .4465, .309]
const_start_didnt_get = [0, 371, 541, 344]
const_start_futs = [.9, .7, .5, .3]

const_start_x = "Probability of Future Station Placement"
const_start_rat_y = "Proportion of Individuals with an Electric Car"
const_start_didnt_get_y = "Number of Individuals Desiring an Electric Car Without One"

# held prob of future time at probability .3
const_fut_ratio = [.43375, .4016, .36425, .38375, .42075]
const_fut_didnt_get = [813, 720, 634, 532, 626]
const_fut_starts = [.01, .05, .1, .2, .3]

const_fut_x = "Probability of Initial Station Placement"

fig = plt.figure()
cars = fig.add_subplot(111)
cars.scatter(a_time, a)

cars.set_xlabel(orig_x).set_fontsize(20)
cars.set_ylabel(orig_y).set_fontsize(20)

plt.show()
