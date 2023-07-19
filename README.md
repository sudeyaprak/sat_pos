# sat_pos (trec, pc, sp3, r_apr)

**Function Description:**
The `sat_pos` function computes the final satellite coordinates in Earth-Centered, Earth-Fixed (ECEF) coordinates, considering the Earth's rotation due to its axial rotation. It takes into account the reception time, code pseudorange observation, satellite coordinates, and approximate receiver coordinates.

![image](https://github.com/sudeyaprak/sat_pos/assets/119863892/16c28dbe-4f01-4da4-b6e0-5fbdebfa92f2)

**Arguments:**
1. `trec` (float): The reception time in seconds of the day. It represents the time when the satellite signal was received by the receiver.
2. `pc` (float): The code pseudorange observation from the observation file in meters. Pseudorange is the estimated distance between the receiver and the satellite based on the time taken for the signal to travel between them.
3. `sp3` (numpy.ndarray or numpy.matrix): A matrix of satellite coordinates and clock corrections. It contains the satellite positions (x, y, z) and satellite clock corrections at various time tags. The matrix is assumed to have the time tags in the first column and satellite clock corrections in the fifth column.
4. `r_apr` (numpy.ndarray or list): Approximate receiver coordinates in ECEF [3x1] (in meters). These are the initial estimated coordinates of the receiver.

**Returns:**
The function returns a tuple containing two elements:
1. `result` (list): The final satellite coordinates in ECEF [3x1] (in meters) after considering the Earth's rotation. The coordinates are represented as `[x, y, z]`.
2. `r_sat_apr` (numpy.ndarray): The satellite coordinates at the approximate reception time (in meters) before considering the Earth's rotation.

**Function Logic:**
1. The function starts by defining the speed of light (`c`) and the Earth's rotation rate (`wE`) in appropriate units.
2. It extracts the satellite clock corrections from the `sp3` matrix by selecting the time tags in the first column and clock corrections in the fifth column, creating a new matrix `clk`.
3. The function then calculates the emission time of the satellite signal (`tems`) using the `emist` function. The `emist` function estimates the emission time based on the reception time (`trec`), pseudorange observation (`pc`), and satellite clock corrections (`clk`).
4. The satellite coordinates at the approximate reception time (`r_sat_apr`) are calculated by calling the `cal_sp3` function with `tems` and `sp3` as arguments. The `cal_sp3` function computes the satellite position based on the provided `sp3` matrix and the emission time (`tems`).
5. The corrected satellite and receiver distance (`delta_t`) are computed by calculating the Euclidean distance between the `r_sat_apr` and `r_apr` coordinates and dividing it by the speed of light (`c`).
6. The angle of rotation of the Earth (`theta`) due to its axial rotation is computed by multiplying the Earth's rotation rate (`wE`) with `delta_t`.
7. A 3x3 rotation matrix (`R3`) is constructed using the computed value of `theta`. This matrix represents the rotation of the Earth about the z-axis.
8. The final satellite coordinates (`r_sat_final`) are calculated by applying the rotation matrix (`R3`) to the satellite coordinates at the approximate reception time (`r_sat_apr`). This step accounts for the Earth's rotation.
9. The final satellite coordinates are extracted from `r_sat_final` and stored in a list called `result`.
10. The function returns a tuple containing `result` (the final satellite coordinates) and `r_sat_apr` (the satellite coordinates at the approximate reception time).

**Note:**
The function assumes that the `emist` and `cal_sp3` functions are correctly implemented and provide accurate results for estimating the emission time and satellite coordinates, respectively. Additionally, the function relies on accurate satellite clock corrections (`sp3`) and receiver coordinates (`r_apr`) for precise final satellite position calculations. It is essential to validate the inputs and ensure their accuracy to obtain reliable results.
