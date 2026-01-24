import numpy as np

# Input Parameters
# ----------

dim = 1024 # image dimension (resolution)
xmin, xmax = 0, dim
ymin, ymax = 0, dim
n_scales = 2500 # total number of scales
n_iter = 30 # iterations for centroid computation
force = 1 # calculate anew?
seed = 1 # random seed

np.random.seed(seed)

def main():
    print("Hello from Scalator!")


if __name__ == "__main__":
    main()
