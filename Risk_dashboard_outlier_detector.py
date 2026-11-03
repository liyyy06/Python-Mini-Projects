import numpy as np

a_return = 0.4
b_return = -0.7
c_return = 0.9
d_return = 0.5
e_return = -0.1

# return_asset = np.array([0.4, -0.7, 0.9, 0.5, -0.1])
n = 5

jumlah_data = n
print("Jumlah data: ", jumlah_data)
if jumlah_data < 2:
    print("Data terlalu sedikit untuk menghitung sample variance")
else:
    mean_ret = (a_return + b_return + c_return + d_return + e_return) / n
    # mean_ret = return_asset.mean()
    print("Rata-rata return aset: ", mean_ret)

    var_return = (1 / (n-1)) * ((a_return-mean_ret)**2 + (b_return-mean_ret)**2 + (c_return-mean_ret)**2 + (d_return-mean_ret)**2 + (e_return-mean_ret)**2)
    print("Variance: ", var_return)

    std_return = var_return**0.5
    #std_return = (((a_return-mean_ret)**2 + (b_return-mean_ret)**2 + (c_return-mean_ret)**2 + (d_return-mean_ret)**2 + (e_return-mean_ret)**2)/(n-1))**0.5
    # std_return = return_asset.std(ddof=1)
    print("Standard deviation: ", std_return*100, "%")
    if std_return == 1e-12:
        print("Semua data sama")
    else:
        az_score = (a_return - mean_ret) / std_return
        bz_score = (b_return - mean_ret) / std_return
        cz_score = (c_return - mean_ret) / std_return
        dz_score = (d_return - mean_ret) / std_return
        ez_score = (e_return - mean_ret) / std_return
        print("Z-score aset A: ", round(az_score, 2))
        print("Z-score aset B: ", round(bz_score, 2))
        print("Z-score aset C: ", round(cz_score, 2))
        print("Z-score aset D: ", round(dz_score, 2))
        print("Z-score aset E: ", round(ez_score, 2))

    # print("Z-score :", z_score)
        threshold = 2
        outlier_returns = []
        a_outlier = az_score > threshold or az_score < -threshold
        if a_outlier:
            outlier_returns.append(a_return)
        b_outlier = bz_score > threshold or bz_score < -threshold
        if b_outlier:
            outlier_returns.append(b_return)
        c_outlier = cz_score > threshold or cz_score < -threshold
        if c_outlier:
            outlier_returns.append(c_return)
        d_outlier = dz_score > threshold or dz_score < -threshold
        if d_outlier:
            outlier_returns.append(d_return)
        e_outlier = ez_score > threshold or ez_score < -threshold
        if e_outlier:
            outlier_returns.append(e_return)

    # outliers = [a_outlier, b_outlier, c_outlier, d_outlier, e_outlier]
    # outliers = np.abs(z_score) > 2 #absolute
        print("Outliers return: ", outlier_returns)
