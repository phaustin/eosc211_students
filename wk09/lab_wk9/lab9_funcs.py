import numpy as np
from matplotlib import pyplot as plt

def get_data_dict(filename):
    """
    Takes in "filename" (csv file) and outputs a dictionary containing
    keys:

         "lats"  - lattitude of each point
         "lons"  - longitude of each point
         "u_vel" - eastward velocity component
         "v_vel" - northward velocity component
    """
    the_file = np.genfromtxt(filename, delimiter=",")

    # extract variables from the csv
    # (namespaces are a honking great idea)
    var_dict = {
        "lats": the_file[:, 1],
        "lons": the_file[:, 2],
        "u_vel": the_file[:, 3],
        "v_vel": the_file[:, 4],
    }
    # extra information we dont need right now
    # "u_dev":the_file[:,5],
    # "v_dev":the_file[:,6]}
    return var_dict


def move_to_grid(lats, lons, u_vel, v_vel):
    """

    function to create 2D numpy arrays out of FORTRAN formatted csv data

    function to create 2D arrays out of FORTRAN formatted csv data.  
    Assumes user wants a 1 deg by 1 deg grid.

    in:
    csv file with columns 15000., lon, lat, u_vel, v_vel, u_dev, v_dev

    (dev is the standard deviation of each velocity measurement, 15000.
    is an artifact from FORTRAN formatting)

    out:
    1D arrays: lat_0, lon_0
    2D arrays: u, v
    """
    # set up grids
    # initializing with NaNs also automatically deals with points where there is
    # no data (eg. on land) because those locations will simply contain NaNs

    lon_0 = np.arange(-179, 180)
    lat_0 = np.arange(-89, 89)
    
    lon_0 = np.arange(-179, 181)
    lat_0 = np.arange(-89, 90)   # CJ modified to 90 so goes -89 to 89
    
    nlat = len(lat_0)            # CJ added these two lines to reduce hardwiring.
    nlon = len(lon_0)
    
    u = np.full([nlat, nlon], np.nan)
    v = np.full([nlat, nlon], np.nan)

    # Loop through all points in .csv file.
    #
    # For each, calculate the row/col indices
    # from the lat/longs.  Lats get converted
    # into row indices 'i', and longs into column
    # indices 'j'. Since we have a 1 degree spacing
    # we just have to add the right offset
    # to make this work - for example, for latitudes
    # latitude of -89 goes to row 0,
    # latitude of -88 goes to row 1, etc.
    #
    # Then write the
    # corresponding U/V data for that lat/long
    # into the right place (i.e. index (i,j) )
    # in the U/V matrices
    for k in range(len(lats)):      # CJ changed from len(lats0) <-- was a bug
        i = int(lons[k]) + 78  # row index
        j = int(lats[k]) + 179  # column index
        u[i, j] = u_vel[k]
        v[i, j] = v_vel[k]

    return lon_0, lat_0, u, v


def mean2d(in_map, winlen):
    """
    Takes a 2D running mean of an input np array

    in:  winlen -- window length
         in_map -- numpy array on which to perform the running mean.

    assumes in_map is a world map, and wraps longitude[-1] around to [0]

    out: out_map -- the filtered map
    """

    def do_mean(in_map, winlen):
        # initialize output array and internal variables
        out_map = np.empty_like(in_map)
        out_map[:] = np.nan
        nrows, ncols = in_map.shape
        wn = int((winlen - 1) // 2)

        # loop through every point (i, j) in the grid:
        # (ignore edges for now)
        for i in range(wn, nrows - wn):
            for j in range(wn, ncols - wn):
                # don't filter points containing nan (ie land, edge of map)
                if not np.isfinite(in_map[i, j]):
                    out_map[i, j] = np.nan
                else:
                    # create the window
                    imin = i - wn
                    imax = i + wn + 1
                    jmin = j - wn
                    jmax = j + wn + 1

                    the_window = in_map[imin:imax, jmin:jmax]
                    # use nanmean to take the mean, ignoring nan values
                    out_map[i, j] = np.nanmean(the_window)

        return out_map

    # check for odd winlen
    winlen = int(winlen)
    if winlen % 2 == 0:
        winlen += 1

    return do_mean(in_map, winlen)


def mask_nth(in_map, n):
    """
    Decimates a 2d array with all values using every n-th
    value, and setting all empty grid cells to NaNs.
    in:
        in_map: 2d numpy array
        n: desired spacing of points

    out:
        masked_map: 2d numpy array with mask applied
    """
    masked_map = np.empty_like(in_map)
    masked_map[:] = np.nan
    masked_map[::n, ::n] = in_map[::n, ::n]
    return masked_map


def get_magnitudes(u, v):
    """
    takes in velocity components 'u' (int or float, array-like containing int or float)
    and 'v' (int or float, array-like containing int or float) and returns velocity magnitude

    m = (u^2 + v^2) ^ 0.5

    """
    return (u ** 2 + v ** 2) ** 0.5


def do_plot(lats, lons, m_filt, u_masked, v_masked):
    """
    Generates a plot of an input velocity field
    """
    fig, ax = plt.subplots(figsize=(10, 7))
    vals=ax.contourf(lons, lats, m_filt, cmap="BuGn")
    cbar=fig.colorbar(vals)
    label=cbar.set_label("speed (m/s)",rotation=270, labelpad=15)
    ax.quiver(lons, lats, u_masked, v_masked, pivot="middle", scale=15)
    ax.set_title("Summertime Surface Ocean Currents")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    fig.savefig("example.png")
    return None



def select_region(lons=None, lats=None, u_vel=None, v_vel = None,
                  lon_slice=slice(0,360),lat_slice=slice(0,179)):
    """
    Write your select region
    """
    lats=lats[lat_slice]
    lons = lons[lon_slice]
    u_vel=u_vel[lat_slice,lon_slice]
    v_vel = v_vel[lat_slice,lon_slice]
    return lons, lats, u_vel,v_vel
