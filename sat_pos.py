def sat_pos(trec, pc, sp3, r_apr): 
    """
    Computes the final satellite coordinates considering Earth's rotation.

    Args:
        trec (float): Reception time in seconds of the day.
        pc (float): Code pseudorange observation from the observation file (in meters).
        sp3 (numpy.ndarray or numpy.matrix): Matrix of satellite coordinates and clock corrections.
        r_apr (numpy.ndarray or list): Approximate receiver coordinates in ECEF [3x1] (in meters).

    Returns:
        tuple: A tuple containing:
            - result (list): Final satellite coordinates in ECEF [3x1] (in meters).
            - r_sat_apr (numpy.ndarray): Satellite coordinates at approximate reception time (in meters).
    """
    
    c = 299792458 # m/s - speed of light
    wE = 7.2921151467e-5 # Earth's rotation rate (WGS84) 
    
    clk = sp3[:, [0, 4]]  # Assuming sp3 is a numpy array or matrix
    tems = emist(trec, pc, clk)
    r_sat_apr = cal_sp3(tems, sp3)

    # Corrected satellite and receiver distance
    delta_t = np.sqrt((r_sat_apr[0] - r_apr[0])**2 + (r_sat_apr[1] - r_apr[1])**2 + (r_sat_apr[2] - r_apr[2])**2) / c

    # Angle of rotation of the earth - theta
    theta = wE * delta_t

    # Rotation matrix
    R3 = np.array([[np.cos(theta), np.sin(theta), 0],
                   [-np.sin(theta), np.cos(theta), 0],
                   [0, 0, 1]])

    # Final satellite coordinate (ECEF)
    r_sat_final = np.dot(R3, r_sat_apr)
    x = float(r_sat_final[0])
    y = float(r_sat_final[1])
    z = float(r_sat_final[2])
    
    result = [x, y, z]
    
    return result, r_sat_apr
